---
name: grill-me
description: Invoke before designing or coding any non-trivial feature. Forces the AI to interview you relentlessly, walking down every branch of the design tree until shared understanding is reached. Use when you say "grill me", "challenge my idea", or before writing a PRD.
---

# Grill Me — Design Tree Interview

**3 sentences:**

> Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one by one. Finally, if a question can be answered by exploring the codebase, explore the codebase instead.

## What it does

Forces a structured design interview before any code is written. Each decision node (e.g. "advanced search vs text box") spawns child questions (filters, sorting methods, UX states, edge cases). Walk ALL branches before committing to implementation.

## When to use

- Before writing any PRD or spec
- When you say "grill me", "tear this apart", "what am I missing"
- Before starting a feature that spans >1 file
- When resuming a project after a gap

## What to expect

- 10-50 questions depending on scope
- 5-45 minute sessions for complex features
- Codebase exploration instead of guesswork when answers exist in code
- A shared mental model between you and the AI before any code is written

## Design Tree concept

From Frederick P. Brooks, *The Design of Design*. Design is not linear — it's a tree. Every decision creates new branches. Walk them all before you commit. An undecided branch = guaranteed future rework.

## Example

User: "I want to add a document panel to my article writer."
AI explores codebase → asks 16 questions:
1. Where does the document live?
2. What's the UI layout?
3. Which modes get the document panel?
4. Document lifecycle?
5. What does the right document tool look like?
6. Edit tool shape?
7-16: edge cases, state transitions, error handling, mobile behavior...

Only then does the AI produce a plan.
