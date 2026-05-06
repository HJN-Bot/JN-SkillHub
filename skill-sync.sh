#!/bin/bash
# skill-sync: update a skill from clipboard or file, then push to all platforms
#
# Usage:
#   skill-sync <skill-name>           # read new SKILL.md from clipboard
#   skill-sync <skill-name> <file>    # read new SKILL.md from file
#   skill-sync --list                 # list all available skills

SKILLHUB=~/Documents/JN-SkillHub
OPENCLAW_SKILLS=~/.openclaw/workspace/skills

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'

if [ "$1" = "--list" ]; then
  echo "Available skills:"
  ls "$SKILLHUB" | grep -v "\.md$" | grep -v "^\." | grep -v "\.sh$" | sort
  exit 0
fi

if [ -z "$1" ]; then
  echo -e "${RED}Usage:${NC} skill-sync <skill-name> [file]"
  echo -e "       skill-sync --list"
  exit 1
fi

SKILL_NAME="$1"
SKILL_DIR="$SKILLHUB/$SKILL_NAME"

if [ ! -d "$SKILL_DIR" ]; then
  echo -e "${RED}Error:${NC} skill '$SKILL_NAME' not found in JN-SkillHub"
  echo "Run 'skill-sync --list' to see available skills"
  exit 1
fi

# Get new content: from file arg or clipboard
if [ -n "$2" ]; then
  if [ ! -f "$2" ]; then
    echo -e "${RED}Error:${NC} file '$2' not found"
    exit 1
  fi
  NEW_CONTENT=$(cat "$2")
  SOURCE="file: $2"
else
  NEW_CONTENT=$(pbpaste)
  SOURCE="clipboard"
fi

if [ -z "$NEW_CONTENT" ]; then
  echo -e "${RED}Error:${NC} no content found in $SOURCE"
  exit 1
fi

# Validate it looks like a SKILL.md (has frontmatter)
if ! echo "$NEW_CONTENT" | grep -q "^---"; then
  echo -e "${YELLOW}Warning:${NC} content doesn't look like a SKILL.md (no frontmatter '---')"
  read -p "Continue anyway? [y/N] " confirm
  [ "$confirm" != "y" ] && exit 1
fi

# Show diff before overwriting
echo -e "${YELLOW}=== Diff for $SKILL_NAME ===${NC}"
diff <(cat "$SKILL_DIR/SKILL.md" 2>/dev/null) <(echo "$NEW_CONTENT") | head -40
echo ""

read -p "Apply changes? [Y/n] " confirm
[ "$confirm" = "n" ] && echo "Aborted." && exit 0

# Write to JN-SkillHub
echo "$NEW_CONTENT" > "$SKILL_DIR/SKILL.md"
echo -e "${GREEN}✓${NC} Updated $SKILL_DIR/SKILL.md"

# Sync to OpenClaw if skill exists there
if [ -d "$OPENCLAW_SKILLS/$SKILL_NAME" ]; then
  cp "$SKILL_DIR/SKILL.md" "$OPENCLAW_SKILLS/$SKILL_NAME/SKILL.md"
  echo -e "${GREEN}✓${NC} Synced to OpenClaw"
else
  echo -e "${YELLOW}~${NC} Skill not in OpenClaw workspace, skipping"
fi

# Codex and Claude auto-update via symlinks (no action needed)
echo -e "${GREEN}✓${NC} Codex & Claude auto-updated (symlinks)"

# Git commit and push
cd "$SKILLHUB"
git add "$SKILL_NAME/SKILL.md"
git commit -m "update skill: $SKILL_NAME"
git push origin main

echo ""
echo -e "${GREEN}Done.${NC} $SKILL_NAME synced to all platforms."
