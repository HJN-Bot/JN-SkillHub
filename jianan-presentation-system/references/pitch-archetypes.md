# Pitch Archetypes — High-Persuasion Building Blocks

This is the v2 expansion that lifts Jianan's presentation system from "internal proposal deck" to "general-purpose persuasion engine." It captures three reusable archetypes drawn from YC pitch coaching, Apple keynote choreography, and Stripe Press / a16z Memo patterns:

1. **Cold Open** — the first 30 seconds that decides whether the audience leans in
2. **Wow Moment** — the single, undeniable proof point the entire deck is built around
3. **Why Us / Why Now** — the unfair-advantage argument that converts interest into commitment

Each archetype includes structure, trigger conditions, generic worked examples, and explicit failure modes. Project-specific worked examples (e.g., R·Agent) live in `objection-handling.md` and the user's CHANGELOG, not here — this file stays domain-neutral so it transfers to future projects.

---

## Archetype 1: Cold Open

### Why this exists

The first 30 seconds determine attention allocation for the next 20 minutes. A presentation that opens with "Hi, I'm X from team Y, today I'll cover three things" has already lost the room. v1's three-signal validation (policy / industry / internal) is excellent for **internal stakeholders who already know you** but underperforms for **external audiences, investors, and cross-org listeners.**

Cold Open replaces or precedes the v1 Phase-1 opener depending on audience.

### The four originals

#### 1.1 Painful Status Quo

**When to use**: Internal PoC graduation, cross-department rollout, any audience that has personally felt the pain you're solving.

**Structure**:
```
[Specific moment + specific person + specific time]
        ↓
[The frequency] (how often this hellish moment repeats)
        ↓
[Implicit question: "what if this didn't have to happen?"]
```

**Generic example**:
> "Last Wednesday at 11pm, our compliance team was still cross-checking version 47 of a single document. This happened 200 times last year."

**Why it works**: Audiences who've lived the pain instantly recognize themselves. The specificity ("11pm", "version 47", "200 times") is non-negotiable — generalities ("we work hard on documents") evoke nothing.

**Failure modes**:
- Using rounded numbers (~50 times → fake; 47 times → real)
- Anonymizing the moment ("a team member" → "Sarah from RA")
- Skipping straight to the solution before pain has landed

---

#### 1.2 Inevitable Future

**When to use**: Investor pitch, external speaking, executive audiences who need to feel they're betting on a wave, not a feature.

**Structure**:
```
[Bold prediction with timeframe]
        ↓
[Re-frame the question: it's not WHETHER, it's WHO]
        ↓
[Implicit positioning: we are the WHO]
```

**Generic example**:
> "Within five years, every regulatory submission in this industry will be drafted by AI and reviewed by humans. The question isn't whether — it's who builds the workflow first."

**Why it works**: Forces the audience into a binary stance. They can no longer ask "is this real?" They have to ask "are we early or late?"

**Failure modes**:
- Hedging ("we think maybe...") destroys the entire effect
- Picking a timeframe that's too long (10+ years) makes it abstract
- No second beat — Inevitable Future without "who" reframing is just a TED talk opener

---

#### 1.3 Counterintuitive Insight

**When to use**: Executive persuasion, industry talks, situations where you need to **shift the audience's mental model** before showing the product.

**Structure**:
```
[Set up the conventional wisdom everyone holds]
        ↓
[Reveal why it's wrong, with credibility marker]
        ↓
[State the better mental model — short]
```

**Generic example**:
> "Every team building LLM automation chases 100% accuracy. We spent three months learning that's the wrong target. The real moat isn't accuracy — it's structured failure modes."

**Why it works**: Audiences come in with priors. If you confirm priors, they nod and forget. If you violate priors with credibility, they update their model — and now they're paying attention because they have something to learn.

**Failure modes**:
- Inventing a fake conventional wisdom ("everyone thinks..." when they don't) — audience smells it
- Insight that's actually obvious dressed up as counterintuitive
- Forgetting the credibility marker ("we spent three months learning..." or "after running 47 evals...")

---

#### 1.4 Loaded Question

**When to use**: Universal fallback. Works in nearly all settings, especially when you don't yet know the audience well.

**Structure**:
```
[Hypothetical that contains a hidden absurdity]
        ↓
[Hand the design problem to the audience]
        ↓
[Audience now mentally engaged — they're solving WITH you]
```

**Generic example**:
> "If I told you 70% of the work in regulatory documentation is reformatting the same paragraph eight different ways — how would you redesign that workflow?"

**Why it works**: Activates the audience's problem-solving brain. They can't passively listen anymore — they're already drafting a solution in their head, which means they're invested in seeing yours.

**Failure modes**:
- Question is too easy (audience answers it before you finish — embarrassing)
- Question is too abstract ("how would you redesign healthcare?")
- Forgetting to actually answer it later in the deck — the question must be paid off

---

### Cold Open discipline (applies to all four)

**DO**:
- Keep the first sentence ≤12 words (short breath = focus)
- Land the first concrete number within 90 seconds
- Hold off on self-introduction until **after** the hook lands (YC's classic move)
- Treat the Cold Open as a single slide — minimal text, no logo, no agenda

**DON'T**:
- Open with "Hi, I'm X" or "Today I'll talk about..."
- Open with thanks or acknowledgements (move those to the close)
- Open with the agenda slide (kills momentum instantly)
- Use more than one Cold Open archetype — combining them dilutes both

---

## Archetype 2: Wow Moment

### Why this exists

v1 distributed proof across Phase 3 (Demo, slides 9-12) and Phase 4 (Numbers, slides 13-14). This is **teaching structure**, not **persuasion structure**. The audience walks away informed but not gripped.

Apple keynotes, Tesla unveilings, and YC demo days all converge on the same insight: **compress the strongest evidence into a single, undeniable moment**, then let the rest of the deck explain how it's possible.

### The three-act structure

```
┌─────────────────────────────────────────┐
│ ACT 1: SETUP                            │
│ One sentence anchoring the conventional │
│ baseline. Make the audience feel the    │
│ "before" state in their bones.          │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ ACT 2: REVEAL                           │
│ Show the result. Not the method, not    │
│ the architecture — just the result.     │
│ Visually: side-by-side or before/after. │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ ACT 3: PAUSE                            │
│ 5–10 seconds of silence while the       │
│ result sits on screen. NO explanation.  │
│ This is where the room changes.         │
└─────────────────────────────────────────┘
```

### Slide composition for the Wow Moment

**One slide. No bullets. No logo. No title bar.**

```
┌────────────────────────────────┬────────────────────────────────┐
│                                │                                │
│  [BEFORE screenshot or image]  │   [AFTER screenshot or image]  │
│  with timestamp / metric       │   with timestamp / metric      │
│                                │                                │
└────────────────────────────────┴────────────────────────────────┘
                                
              [ONE LINE OF TEXT IN THE CENTER]
              Format: "Same X. Y → Z."
              e.g., "Same task. 8 hours → 4 minutes."
```

That center sentence is the only text on the slide. It's the t-shirt the audience walks away wearing.

### Oral script for the Wow Moment

```markdown
[SETUP — 1 sentence, ~10 seconds]
"This kind of cross-document comparison takes our team eight hours per project."

[REVEAL — click to reveal side-by-side]
"Here's the same task, run by the system."

[PAUSE 5-10s — DO NOT EXPLAIN]
[SCRIPT INSTRUCTION: count silently to 8 before next word. Resist the urge to fill.]

[BRIDGE — only after pause completes]
"Let me show you how this works."
```

The pause is the hardest discipline. Most presenters fill silence within 2 seconds — that kills the Wow.

### Wow Moment placement in the deck

The Wow Moment **anchors the deck**. Everything before it builds tension; everything after it explains the magic.

| Beat | Role relative to Wow |
|---|---|
| Hook (Beat 1) | Sets up why anyone should care |
| Insight (Beat 2) | Shifts the mental model so the Wow lands harder |
| **Wow Moment (early in Beat 3)** | **Gravitational center of the deck** |
| Rest of Beat 3 | "Here's how we did it" — slow-motion replay |
| Beat 4 | "Here's why we can keep doing it" |
| Beat 5 | "Here's what we need from you" |

### Failure modes

- **Explaining during Reveal**: "And as you can see, our novel transformer architecture leverages..." — kills the moment instantly. Architecture goes in the next slide.
- **Multiple Wow Moments**: Two Wows = zero Wows. Pick the strongest, demote the others to supporting evidence.
- **Wow Moment without Setup**: If the audience doesn't feel the "before," the "after" is just a number.
- **Generic before/after**: Stock images, fake screenshots, rounded numbers. Real artifacts only.
- **No pause**: The presenter talks through the reveal. The slide changes before the moment lands.

### Choosing the right Wow Moment

A useful sanity check: imagine the audience texting one friend after the talk. What's the one sentence they'd send? If it's not the line on your Wow Moment slide, the Wow Moment is wrong.

---

## Archetype 3: Why Us / Why Now

### Why this exists

v1 Phase 5 (Scalability) demonstrates "we can extend this." But it doesn't answer the harder question every investor and senior decision-maker silently asks: **"Why can't someone else do this faster or cheaper than you?"**

YC pitch memos call this the **Unfair Advantage** section. It's not bragging — it's de-risking. The audience needs to believe that backing you locks in something competitors can't easily replicate.

### The three-column matrix

The cleanest format is a comparison table that makes the unfair advantage visually obvious:

```
┌──────────────────────────────────┬──────────────┬──────────────┬──────────────┐
│ CAPABILITY                       │ COMPETITOR A │ COMPETITOR B │ US           │
├──────────────────────────────────┼──────────────┼──────────────┼──────────────┤
│ [Capability 1 — technical]       │      ✓       │      ✗       │      ✓       │
│ [Capability 2 — domain]          │      ✗       │      ✓       │      ✓       │
│ [Capability 3 — bridging both]   │      ✗       │      ✗       │      ✓       │
│ Time-to-replicate                │  6 months    │   2 years    │   0 (now)    │
└──────────────────────────────────┴──────────────┴──────────────┴──────────────┘
```

**Key design rules**:
- The "Us" column should be the **only** column with all checkmarks
- The bottom row converts the qualitative advantage into time/cost units — this is what makes it land with executives
- Pick competitors honestly — including a strong competitor that beats you on one axis builds credibility for your wins on others
- Capabilities are listed so that the third one is the genuinely rare combination

### Why "Why Now" pairs with "Why Us"

A great "Why Us" can still fail if "Why Now" is missing. Audiences ask: "If you've had this advantage all along, why is now the moment?"

Three patterns for Why Now:

| Pattern | Form | Example phrasing |
|---|---|---|
| **Capability unlock** | A new technology / model / regulation just made this possible | "GPT-4-class models crossed the threshold for [X] in late 2024." |
| **Demand surge** | The market just started asking for it | "Three customers asked us for this in the last quarter — none asked last year." |
| **Closing window** | If we don't act now, the option disappears | "Once a competitor sets the standard, switching costs lock everyone else out for 5+ years." |

The strongest pitches **chain** Why Us with Why Now: "Only we can do this (Why Us), and the window is closing (Why Now), therefore: act."

### Slide composition for Why Us / Why Now

This is typically **two slides, not one**:

- **Slide A — Why Us matrix**: the three-column comparison table above. Header: "Why this team."
- **Slide B — Why Now**: a single timeline or trend line showing the inflection point. Header: "Why this moment."

Both slides keep the v1 visual style: orange/teal palette, 18pt section headers, ≥12pt body, evidence on the right side.

### Failure modes

- **Generic capabilities**: "We have great engineers." Every team says this. Specificity is what sells.
- **Cherry-picked competitors**: Comparing yourself to a strawman damages credibility more than the win helps.
- **No "Why Now"**: Audience walks away thinking "interesting team, I'll watch them" instead of "I need to commit now."
- **Why Us as ego**: This section is about **structural advantage**, not about how smart your team is. Focus on what competitors **structurally cannot** match within the relevant time horizon.

---

## How the three archetypes compose

A complete high-persuasion deck threads all three:

```
COLD OPEN  →  [audience leans in]
   ↓
INSIGHT    →  [mental model updated]
   ↓
WOW MOMENT →  [proof becomes undeniable]
   ↓
WHY US     →  [advantage becomes structural]
   ↓
WHY NOW    →  [urgency becomes binding]
   ↓
ASK        →  [decision becomes natural]
```

Each archetype is independently powerful, but the compounding effect comes from sequencing. Skipping any one of the three creates a predictable failure pattern:

| Skipped | Failure pattern |
|---|---|
| Cold Open | Audience never tunes in; rest of deck talks past them |
| Wow Moment | Audience is informed but not moved; "interesting, will think about it" |
| Why Us / Why Now | Audience is moved but not committing; "let's reconvene next quarter" |

When in doubt: **the Wow Moment is the most important. If you only have time to add one archetype to a v1-style deck, add the Wow Moment.**

---

## Quick reference: which archetype for which scenario

| Scenario | Cold Open | Wow Moment | Why Us / Why Now |
|---|---|---|---|
| Internal PoC graduation | Painful Status Quo | Required | Light (1 slide) |
| Cross-department rollout | Painful Status Quo | Required | Required (replication framing) |
| HQ technical team alignment | Counterintuitive Insight | Required | Required (complementarity framing) |
| Senior leadership / budget ask | Counterintuitive Insight or Loaded Question | Required | Required (full matrix) |
| External investor pitch | Inevitable Future | Required | Required (full matrix + Why Now) |
| Industry conference talk | Counterintuitive Insight | Optional | Light (credibility, not selling) |
| Product launch / press event | Inevitable Future | Required (centerpiece) | Why Now only |

---

## Integration with v1 6-Phase

For internal scenarios where v1's 6-Phase still applies, the archetypes are **inserted**, not **replacing**:

```
[Cold Open]                        ← NEW (1 slide)
   ↓
Phase 1: Strategic Urgency         ← v1 retained
   ↓
[Insight slide]                    ← NEW (1 slide, optional)
   ↓
Phase 2: Capability Demonstration  ← v1 retained
   ↓
[Wow Moment]                       ← NEW (1 slide, REQUIRED)
   ↓
Phase 3: Live Product Demo         ← v1 retained, reframed as "slow-motion of the Wow"
   ↓
Phase 4: Impact Quantification     ← v1 retained
   ↓
[Why Us / Why Now]                 ← NEW (2 slides)
   ↓
Phase 5: Scalability & Roadmap     ← v1 retained
   ↓
Phase 6: Call to Action            ← v1 retained
```

For external/investor scenarios, the 5-Beat structure (see `content-logic.md`) takes over and the 6-Phase collapses into Beats 3-4.
