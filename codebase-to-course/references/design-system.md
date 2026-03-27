# Design System Reference — Apple Minimal

A black-and-white-first design system inspired by Apple's product pages. The course must look beautiful in pure grayscale. Color is punctuation — used sparingly and only where it earns its place (interactive affordances, file-type indicators, data flow accents).

## Table of Contents
1. [Color Palette](#color-palette)
2. [Typography](#typography)
3. [Spacing & Layout](#spacing--layout)
4. [Shadows & Depth](#shadows--depth)
5. [Animations & Transitions](#animations--transitions)
6. [Navigation & Progress](#navigation--progress)
7. [Module Structure](#module-structure)
8. [Responsive Breakpoints](#responsive-breakpoints)
9. [Scrollbar & Background](#scrollbar--background)
10. [File-Type Color Dots](#file-type-color-dots)

---

## Color Palette

```css
:root {
  /* --- BACKGROUNDS (refined neutral — NOT dead white) --- */
  --color-bg:             #FAFAF8;       /* warm ivory — primary modules, never pure #FFF */
  --color-bg-alt:         #F3F3F1;       /* soft warm gray — alternating modules */
  --color-bg-code:        #1C1C1E;       /* near-black for code blocks */
  --color-bg-surface:     #FCFCFA;       /* card surfaces — barely warm off-white */
  --color-bg-hover:       #EDEDEB;       /* hover state — slight warm tint */

  /* --- TEXT (Apple text hierarchy) --- */
  --color-text:           #1D1D1F;       /* primary text — near black */
  --color-text-secondary: #6E6E73;       /* secondary text — Apple gray */
  --color-text-tertiary:  #86868B;       /* tertiary — captions, timestamps */
  --color-text-muted:     #AEAEB2;       /* muted — decorative numbers, dividers */
  --color-text-inverse:   #F5F5F7;       /* text on dark backgrounds */

  /* --- BORDERS (minimal, near-invisible) --- */
  --color-border:         #D2D2D7;       /* standard border */
  --color-border-light:   #E8E8ED;       /* subtle dividers */
  --color-border-strong:  #C7C7CC;       /* emphasized borders */

  /* --- ACCENT (Apple blue — ONE color only) ---
     Used EXCLUSIVELY for: links, active nav states, buttons, toggles,
     interactive affordances. NEVER for backgrounds or section fills. */
  --color-accent:         #0071E3;       /* Apple blue */
  --color-accent-hover:   #0077ED;       /* slightly brighter on hover */
  --color-accent-light:   #E1F0FF;       /* very faint blue tint — selected states only */

  /* --- SEMANTIC (restrained — used only in quizzes & status) --- */
  --color-success:        #34C759;       /* Apple green */
  --color-success-light:  #E8FAF0;
  --color-error:          #FF3B30;       /* Apple red */
  --color-error-light:    #FFF0EF;
  --color-warning:        #FF9500;       /* Apple orange — git diff changed */
  --color-warning-light:  #FFF8EB;

  /* --- ACTOR COLORS (for data flow diagrams & group chat) ---
     Muted tones that don't fight the B&W baseline.
     Used only inside diagrams, flow animations, and chat bubbles. */
  --color-actor-1:        #1D1D1F;       /* near-black (default/primary) */
  --color-actor-2:        #0071E3;       /* blue (same as accent) */
  --color-actor-3:        #6E6E73;       /* gray */
  --color-actor-4:        #AC8E68;       /* warm muted gold */
  --color-actor-5:        #30B0C7;       /* muted teal */
}
```

**Rules:**
- Even-numbered modules use `--color-bg` (white), odd-numbered use `--color-bg-alt` (#F5F5F7)
- NO colored section backgrounds. The rhythm comes from white ↔ light gray alternation
- Color appears ONLY in: accent links/buttons, file-type dots, diagram actor lines, quiz feedback, and git diff indicators
- All other UI is black, white, and gray
- Actor colors for diagrams should be distinguishable but never saturated — they sit quietly on the page

---

## Typography

```css
:root {
  /* --- FONTS ---
     System stack for body (matches Apple's own sites).
     Mono for code — JetBrains Mono for clarity.
     NO decorative display fonts. Hierarchy via weight + size only. */
  --font-body:  -apple-system, 'SF Pro Display', 'Helvetica Neue', 'Inter', system-ui, sans-serif;
  --font-mono:  'SF Mono', 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;

  /* --- TYPE SCALE (1.25 ratio, Apple-inspired sizes) --- */
  --text-xs:    0.75rem;     /* 12px — mono labels, badges */
  --text-sm:    0.875rem;    /* 14px — secondary text, code */
  --text-base:  1.0625rem;   /* 17px — body text (Apple's standard) */
  --text-lg:    1.25rem;     /* 20px — lead paragraphs */
  --text-xl:    1.5rem;      /* 24px — screen headings */
  --text-2xl:   1.75rem;     /* 28px — sub-module titles */
  --text-3xl:   2.5rem;      /* 40px — module titles */
  --text-4xl:   3.5rem;      /* 56px — hero text (rare) */
  --text-5xl:   4.5rem;      /* 72px — module numbers (decorative) */

  /* --- LINE HEIGHTS --- */
  --leading-tight:    1.1;   /* module numbers, hero text */
  --leading-heading:  1.2;   /* headings */
  --leading-normal:   1.5;   /* body text */
  --leading-relaxed:  1.65;  /* long-form reading */

  /* --- FONT WEIGHTS --- */
  --weight-light:   300;     /* decorative module numbers ONLY */
  --weight-regular: 400;     /* body text */
  --weight-medium:  500;     /* sub-headings, labels */
  --weight-semibold:600;     /* section headers */
  --weight-bold:    700;     /* module titles, emphasis */
}
```

**Google Fonts link (only JetBrains Mono — system fonts handle the rest):**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

**Hierarchy rules:**
- Module numbers: `--text-5xl` (72px), weight 300 (light), `--color-text-muted` — architectural, barely there
- Module titles: `--text-3xl` (40px), weight 700, `--color-text` — the loudest element on each page
- Screen headings: `--text-xl` or `--text-2xl`, weight 600, `--color-text`
- Body text: `--text-base` (17px), weight 400, `--leading-normal`, `--color-text`
- Secondary text: `--text-sm`, weight 400, `--color-text-secondary`
- Code: `--text-sm`, `--font-mono`, weight 400
- Labels/badges: `--text-xs`, `--font-mono`, uppercase, letter-spacing 0.08em, `--color-text-tertiary`

---

## Spacing & Layout

```css
:root {
  --space-1:  0.25rem;    /* 4px */
  --space-2:  0.5rem;     /* 8px */
  --space-3:  0.75rem;    /* 12px */
  --space-4:  1rem;       /* 16px */
  --space-5:  1.25rem;    /* 20px */
  --space-6:  1.5rem;     /* 24px */
  --space-8:  2rem;       /* 32px */
  --space-10: 2.5rem;     /* 40px */
  --space-12: 3rem;       /* 48px */
  --space-16: 4rem;       /* 64px */
  --space-20: 5rem;       /* 80px */
  --space-24: 6rem;       /* 96px */

  --content-width:      720px;    /* tighter than typical — editorial feel */
  --content-width-wide: 960px;    /* for side-by-side code translations */
  --nav-height:         48px;
  --radius-sm:  6px;
  --radius-md:  10px;
  --radius-lg:  14px;
  --radius-full: 9999px;
}
```

**Module layout:**
```css
.module {
  min-height: 100dvh;
  scroll-snap-align: start;
  padding: var(--space-20) var(--space-6);
  padding-top: calc(var(--nav-height) + var(--space-16));
}
.module-content {
  max-width: var(--content-width);
  margin: 0 auto;
}
```

---

## Shadows & Depth

Apple prefers borders over shadows. When shadows are needed, they're barely perceptible.

```css
:root {
  --shadow-sm:   0 1px 2px rgba(0, 0, 0, 0.04);
  --shadow-md:   0 2px 8px rgba(0, 0, 0, 0.06);
  --shadow-lg:   0 4px 16px rgba(0, 0, 0, 0.08);
  --shadow-card: 0 0 0 1px var(--color-border-light);  /* prefer border over shadow */
}
```

**Rules:**
- Default to `--shadow-card` (1px border) for cards. Reserve actual shadows for elevated elements (inspector panel, tooltips)
- Never use colored shadows
- Never use `box-shadow` with spread > 0

---

## Animations & Transitions

```css
:root {
  --ease-apple:   cubic-bezier(0.25, 0.1, 0.25, 1);   /* Apple's standard ease */
  --ease-out:     cubic-bezier(0.16, 1, 0.3, 1);
  --ease-spring:  cubic-bezier(0.34, 1.56, 0.64, 1);   /* slight overshoot for toggles */
  --duration-fast:    150ms;
  --duration-normal:  300ms;
  --duration-slow:    500ms;
  --duration-reveal:  600ms;
  --stagger-delay:    80ms;     /* faster stagger than original — feels snappier */
}
```

**Scroll-triggered reveal (Apple fade-up):**
```css
.animate-in {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity var(--duration-reveal) var(--ease-apple),
              transform var(--duration-reveal) var(--ease-apple);
}
.animate-in.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Stagger children — tighter delay for Apple snap */
.stagger-children > .animate-in {
  transition-delay: calc(var(--stagger-index, 0) * var(--stagger-delay));
}
```

**JS setup:**
```javascript
// Stagger index assignment
document.querySelectorAll('.stagger-children').forEach(parent => {
  Array.from(parent.children).forEach((child, i) => {
    child.style.setProperty('--stagger-index', i);
  });
});

// Intersection Observer
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { rootMargin: '0px 0px -15% 0px', threshold: 0.1 });

document.querySelectorAll('.animate-in').forEach(el => observer.observe(el));
```

---

## Navigation & Progress

Apple-style frosted glass navigation.

**HTML:**
```html
<nav class="nav">
  <div class="progress-bar" role="progressbar" aria-valuenow="0"></div>
  <div class="nav-inner">
    <span class="nav-title">Course Title</span>
    <div class="nav-dots">
      <button class="nav-dot" data-target="module-1" data-tooltip="Module 1"
              role="tab" aria-label="Module 1"></button>
    </div>
  </div>
</nav>
```

**CSS:**
```css
.nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  background: rgba(250, 250, 248, 0.72);   /* warm ivory at 72% opacity */
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  border-bottom: 0.5px solid var(--color-border-light);
  height: var(--nav-height);
}
.nav-inner {
  max-width: var(--content-width-wide);
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  padding: 0 var(--space-6);
}
.nav-title {
  font-size: var(--text-sm);
  font-weight: var(--weight-semibold);
  color: var(--color-text);
  letter-spacing: -0.01em;
}
.progress-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 2px;
  background: var(--color-accent);
  transition: width 100ms linear;
}
```

**Nav dot states:**
- Default: 6px circle, `background: var(--color-border)`, no border
- Current: `background: var(--color-accent)`, slightly larger (8px)
- Visited: `background: var(--color-text-muted)`

**JS (same as original):**
```javascript
function updateProgressBar() {
  const scrollTop = window.scrollY;
  const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
  const progress = (scrollTop / scrollHeight) * 100;
  progressBar.style.width = progress + '%';
}
window.addEventListener('scroll', () => {
  requestAnimationFrame(updateProgressBar);
}, { passive: true });
```

**Keyboard navigation (same as original):**
```javascript
document.addEventListener('keydown', (e) => {
  if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;
  if (e.key === 'ArrowDown' || e.key === 'ArrowRight') { nextModule(); e.preventDefault(); }
  if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') { prevModule(); e.preventDefault(); }
});
```

---

## Module Structure

**HTML template:**
```html
<section class="module" id="module-N" style="background: var(--color-bg or --color-bg-alt)">
  <div class="module-content">
    <header class="module-header animate-in">
      <span class="module-number">0N</span>
      <h1 class="module-title">Module Title</h1>
      <p class="module-subtitle">One-line description</p>
    </header>

    <div class="module-body">
      <section class="screen animate-in">
        <h2 class="screen-heading">Screen Title</h2>
        <p>Content...</p>
      </section>
    </div>
  </div>
</section>
```

**Module number styling:**
```css
.module-number {
  display: block;
  font-size: var(--text-5xl);        /* 72px */
  font-weight: var(--weight-light);  /* 300 — thin, architectural */
  color: var(--color-text-muted);    /* barely there */
  line-height: var(--leading-tight);
  margin-bottom: var(--space-4);
  letter-spacing: -0.04em;
}
.module-title {
  font-size: var(--text-3xl);
  font-weight: var(--weight-bold);
  color: var(--color-text);
  line-height: var(--leading-heading);
  letter-spacing: -0.02em;
  margin: 0;
}
.module-subtitle {
  font-size: var(--text-lg);
  color: var(--color-text-secondary);
  margin: var(--space-2) 0 0;
  font-weight: var(--weight-regular);
}
```

---

## Responsive Breakpoints

```css
@media (max-width: 768px) {
  :root {
    --text-3xl: 2rem;
    --text-4xl: 2.5rem;
    --text-5xl: 3.5rem;
  }
  .translation-block { grid-template-columns: 1fr; }
  .pipeline-stages { flex-wrap: wrap; justify-content: center; }
}

@media (max-width: 480px) {
  :root {
    --text-3xl: 1.75rem;
    --text-4xl: 2rem;
    --text-5xl: 2.5rem;
  }
  .module { padding: var(--space-12) var(--space-4); }
  .flow-steps { flex-direction: column; }
  .flow-arrow { transform: rotate(90deg); }
}
```

---

## Scrollbar & Background

```css
/* Minimal scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
  background: var(--color-border);
  border-radius: var(--radius-full);
}

/* NO background gradients or patterns — pure flat warm ivory */
body {
  background: var(--color-bg);
  color: var(--color-text);
  font-family: var(--font-body);
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

html {
  scroll-snap-type: y proximity;
  scroll-behavior: smooth;
}
```

---

## File-Type Color Dots

The ONLY place file-type colors appear in the course. Used in file trees and package anatomy cards — a small 6px dot before the filename, color-coded by type.

```css
:root {
  --ft-python:  #3572A5;    /* muted blue */
  --ft-js:      #E8D44D;    /* yellow-gold */
  --ft-ts:      #3178C6;    /* TypeScript blue */
  --ft-html:    #E44D26;    /* HTML orange */
  --ft-css:     #663399;    /* CSS purple */
  --ft-json:    #6E6E73;    /* gray — data/config */
  --ft-yaml:    #6E6E73;    /* gray — same as json */
  --ft-csv:     #34C759;    /* green — tabular data */
  --ft-md:      #1D1D1F;    /* near-black — documentation */
  --ft-sql:     #CC6600;    /* amber — database */
  --ft-sh:      #89E051;    /* light green — automation */
  --ft-env:     #AEAEB2;    /* muted — secrets/config */
}

.ft-dot {
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  margin-right: 6px;
  vertical-align: middle;
}
.ft-dot-py   { background: var(--ft-python); }
.ft-dot-js   { background: var(--ft-js); }
.ft-dot-ts   { background: var(--ft-ts); }
.ft-dot-html { background: var(--ft-html); }
.ft-dot-css  { background: var(--ft-css); }
.ft-dot-json { background: var(--ft-json); }
.ft-dot-yaml { background: var(--ft-yaml); }
.ft-dot-csv  { background: var(--ft-csv); }
.ft-dot-md   { background: var(--ft-md); }
.ft-dot-sql  { background: var(--ft-sql); }
.ft-dot-sh   { background: var(--ft-sh); }
.ft-dot-env  { background: var(--ft-env); }
```

**Usage in file trees:**
```html
<div class="ft-file">
  <span class="ft-dot ft-dot-py"></span>
  <span class="ft-name">pipeline_runner.py</span>
  <span class="ft-desc">Orchestrates the CER generation pipeline</span>
</div>
```

---

## Code Block Globals

```css
pre, code {
  white-space: pre-wrap;
  word-break: break-word;
  overflow-x: hidden;
}
pre::-webkit-scrollbar,
.translation-code::-webkit-scrollbar {
  display: none;
}
```

---

## Syntax Highlighting (restrained — no neon)

For code blocks on the dark `--color-bg-code` (#1D1D1F) background. Colors are muted and harmonious — no rainbow, no neon green.

```css
.code-keyword  { color: #FF7B72; }   /* soft coral — if, else, return, def */
.code-string   { color: #A5D6FF; }   /* ice blue — "strings" */
.code-function { color: #D2A8FF; }   /* soft lavender — function names */
.code-comment  { color: #6E6E73; }   /* gray — // comments */
.code-number   { color: #79C0FF; }   /* light blue — numbers */
.code-property { color: #FFA657; }   /* muted amber — object keys, dict keys */
.code-operator { color: #C9D1D9; }   /* light gray — =, =>, +, etc. */
.code-tag      { color: #7EE787; }   /* soft green — HTML tags */
.code-attr     { color: #D2A8FF; }   /* lavender — HTML attributes */
.code-value    { color: #A5D6FF; }   /* ice blue — attribute values */
.code-type     { color: #FF7B72; }   /* coral — type annotations */
.code-builtin  { color: #FFA657; }   /* amber — built-in functions */
```

**Rules:**
- Max 5-6 distinct syntax colors in any code block. The overall feel should be "quiet dark mode" not "carnival"
- Comments in gray are deliberately hard to read — they're secondary information
- Keywords and function names carry the visual weight
- Strings and values are cool-toned (blue family) — they recede behind the structure
