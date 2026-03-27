# Deep Dive Elements Reference

Implementation patterns for the three interactive elements unique to Deep Dive Mode. These complement the standard elements in `interactive-elements.md`. Use the same design tokens from `design-system.md`.

## Table of Contents
1. [Package Anatomy Card](#package-anatomy-card)
2. [Data Pipeline Tracer](#data-pipeline-tracer)
3. [Git Diff Overlay](#git-diff-overlay)

---

## Package Anatomy Card

An expandable card that X-rays a single package/module/script. Collapsed state shows the one-liner purpose and I/O summary. Expanded state reveals: function list, call graph, dependencies, and data shapes.

**When to use**: Every core package identified in Phase 1 gets one of these. They replace paragraphs like "this file handles X and contains functions for Y."

### HTML

```html
<div class="pkg-card animate-in" data-pkg="pipeline_runner">
  <!-- Collapsed header (always visible) -->
  <button class="pkg-header" onclick="togglePkg(this)">
    <div class="pkg-icon" style="background: var(--color-actor-1)">📦</div>
    <div class="pkg-info">
      <h3 class="pkg-name">pipeline_runner.py</h3>
      <p class="pkg-purpose">Orchestrates the full CER generation pipeline from input to final report</p>
    </div>
    <div class="pkg-io-summary">
      <span class="pkg-io-in">IN: config dict, chapter list</span>
      <span class="pkg-io-out">OUT: formatted CER document</span>
    </div>
    <span class="pkg-toggle">▼</span>
  </button>

  <!-- Expanded body (hidden by default) -->
  <div class="pkg-body">
    <!-- Function list -->
    <div class="pkg-section">
      <h4 class="pkg-section-title">Core functions</h4>
      <div class="pkg-functions">
        <div class="pkg-fn" onclick="highlightFn('run_pipeline')">
          <code class="pkg-fn-name">run_pipeline(config)</code>
          <span class="pkg-fn-desc">Main entry point — calls each stage in sequence</span>
          <div class="pkg-fn-io">
            <span class="pkg-fn-in">→ config: dict with chapter_ids, model_name, output_path</span>
            <span class="pkg-fn-out">← CompletedReport object</span>
          </div>
        </div>
        <div class="pkg-fn" onclick="highlightFn('process_chapter')">
          <code class="pkg-fn-name">process_chapter(chapter_id, context)</code>
          <span class="pkg-fn-desc">Processes one chapter: fetch → compare → generate</span>
          <div class="pkg-fn-io">
            <span class="pkg-fn-in">→ chapter_id: str, context: PipelineContext</span>
            <span class="pkg-fn-out">← ChapterResult with diff_table, narrative, score</span>
          </div>
        </div>
        <div class="pkg-fn" onclick="highlightFn('post_process')">
          <code class="pkg-fn-name">post_process(raw_output, rules)</code>
          <span class="pkg-fn-desc">Applies formatting rules and validation to LLM output</span>
          <div class="pkg-fn-io">
            <span class="pkg-fn-in">→ raw_output: str (LLM response), rules: list[Rule]</span>
            <span class="pkg-fn-out">← CleanedOutput with warnings list</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Dependencies -->
    <div class="pkg-section">
      <h4 class="pkg-section-title">Depends on</h4>
      <div class="pkg-deps">
        <span class="pkg-dep" onclick="scrollToPkg('llm_client')">llm_client</span>
        <span class="pkg-dep" onclick="scrollToPkg('data_loader')">data_loader</span>
        <span class="pkg-dep" onclick="scrollToPkg('formatter')">formatter</span>
      </div>
    </div>

    <!-- Data shape preview -->
    <div class="pkg-section">
      <h4 class="pkg-section-title">Data shape at output</h4>
      <pre class="pkg-data-shape"><code>{
  "chapter_id": "ch04",
  "diff_table": [["field", "old_value", "new_value", "status"], ...],
  "narrative": "Based on the comparison, the following changes...",
  "confidence_score": 0.92,
  "warnings": ["table_mismatch_row_3"]
}</code></pre>
    </div>
  </div>
</div>
```

### CSS

```css
.pkg-card {
  border-radius: var(--radius-md);
  overflow: hidden;
  margin: var(--space-6) 0;
  border: 1px solid var(--color-border-light);
  transition: border-color var(--duration-normal);
}
.pkg-card:hover { border-color: var(--color-border); }

.pkg-header {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  padding: var(--space-4) var(--space-5);
  background: var(--color-bg-surface);
  border: none;
  cursor: pointer;
  width: 100%;
  text-align: left;
}
.pkg-icon {
  width: 36px; height: 36px; border-radius: var(--radius-sm);
  display: flex; align-items: center; justify-content: center;
  font-size: 1rem; flex-shrink: 0;
  background: var(--color-bg-alt);
}
.pkg-name {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  font-weight: 600;
  color: var(--color-text);
  margin: 0;
}
.pkg-purpose {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  margin: var(--space-1) 0 0;
}
.pkg-io-summary {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
  margin-left: auto;
  text-align: right;
}
.pkg-io-in, .pkg-io-out {
  font-size: var(--text-xs);
  font-family: var(--font-mono);
  padding: 2px 8px;
  border-radius: var(--radius-full);
}
.pkg-io-in {
  background: var(--color-bg-alt);
  color: var(--color-text-secondary);
}
.pkg-io-out {
  background: var(--color-bg-alt);
  color: var(--color-text-secondary);
}
.pkg-toggle {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  transition: transform var(--duration-fast);
}
.pkg-card.open .pkg-toggle { transform: rotate(180deg); }

.pkg-body {
  max-height: 0;
  overflow: hidden;
  transition: max-height var(--duration-slow) var(--ease-out);
  background: var(--color-bg-alt);
  border-top: 1px solid var(--color-border-light);
}
.pkg-card.open .pkg-body {
  max-height: 2000px;
}
.pkg-section {
  padding: var(--space-4) var(--space-5);
  border-bottom: 1px solid var(--color-border-light);
}
.pkg-section:last-child { border-bottom: none; }
.pkg-section-title {
  font-size: var(--text-xs);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--color-text-muted);
  margin: 0 0 var(--space-3);
  font-family: var(--font-mono);
  font-weight: 500;
}

.pkg-fn {
  padding: var(--space-3) var(--space-4);
  margin-bottom: var(--space-2);
  background: var(--color-bg-surface);
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: border-color var(--duration-fast);
  border-left: 2px solid transparent;
}
.pkg-fn:hover { border-left-color: var(--color-accent); }
.pkg-fn-name {
  font-size: var(--text-sm);
  color: var(--color-text);
  font-weight: 500;
}
.pkg-fn-desc {
  display: block;
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  margin-top: var(--space-1);
}
.pkg-fn-io {
  display: none;
  flex-direction: column;
  gap: var(--space-1);
  margin-top: var(--space-2);
  font-family: var(--font-mono);
  font-size: var(--text-xs);
}
.pkg-fn:hover .pkg-fn-io { display: flex; }
.pkg-fn-in { color: var(--color-text-secondary); }
.pkg-fn-in::before { content: "→ "; }
.pkg-fn-out { color: var(--color-text-secondary); }
.pkg-fn-out::before { content: "← "; }

.pkg-deps {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}
.pkg-dep {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  padding: 4px 12px;
  background: var(--color-bg-surface);
  color: var(--color-text-secondary);
  border: 1px solid var(--color-border-light);
  border-radius: var(--radius-full);
  cursor: pointer;
  transition: all var(--duration-fast);
}
.pkg-dep:hover { border-color: var(--color-accent); color: var(--color-accent); }

.pkg-data-shape {
  background: var(--color-bg-code);
  color: #CDD6F4;
  padding: var(--space-4);
  border-radius: var(--radius-sm);
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  overflow-x: hidden;
  white-space: pre-wrap;
  word-break: break-word;
}

@media (max-width: 768px) {
  .pkg-header { flex-wrap: wrap; }
  .pkg-io-summary { margin-left: 0; text-align: left; width: 100%; margin-top: var(--space-2); flex-direction: row; gap: var(--space-2); }
}
```

### JS

```javascript
window.togglePkg = function(btn) {
  const card = btn.closest('.pkg-card');
  card.classList.toggle('open');
};

window.scrollToPkg = function(pkgName) {
  const target = document.querySelector(`[data-pkg="${pkgName}"]`);
  if (target) {
    target.scrollIntoView({ behavior: 'smooth', block: 'center' });
    target.classList.add('open');
    target.style.boxShadow = '0 0 0 3px ' + getComputedStyle(document.documentElement).getPropertyValue('--color-accent');
    setTimeout(() => { target.style.boxShadow = ''; }, 2000);
  }
};
```

### Rules
- Every Package Anatomy Card MUST have the I/O summary visible in collapsed state — the user should see input/output without expanding
- Function list must show I/O on hover, not just function names
- Dependencies must be clickable links to other Package Anatomy Cards
- Data shape preview uses the dark code block style and shows a REAL example from the codebase (not a schema)
- Keep the function list to 3-6 most important functions — don't list every helper and utility

---

## Data Pipeline Tracer

An animated, step-by-step visualization of data flowing through a processing pipeline. Each stage is a clickable node. Clicking a stage reveals the data shape at that point — what the data looks like BEFORE and AFTER the transformation.

**When to use**: Any multi-step data processing pipeline. Especially important for pipelines with post-processing layers, where the user needs to understand "the data was X here, then became Y after this function."

### HTML

```html
<div class="pipeline-tracer animate-in">
  <div class="pipeline-header">
    <h3>Data pipeline: CER chapter processing</h3>
    <button class="pipeline-play-btn" onclick="playPipeline(this)">▶ Animate</button>
  </div>

  <div class="pipeline-stages">
    <!-- Stage 1 -->
    <div class="pipeline-stage" data-stage="1" onclick="inspectStage(this)">
      <div class="stage-node" style="--stage-color: var(--color-actor-1)">
        <span class="stage-num">1</span>
      </div>
      <div class="stage-label">Raw input</div>
      <div class="stage-desc">Chapter text + reference data</div>
    </div>

    <div class="pipeline-arrow">→</div>

    <!-- Stage 2 -->
    <div class="pipeline-stage" data-stage="2" onclick="inspectStage(this)">
      <div class="stage-node" style="--stage-color: var(--color-actor-2)">
        <span class="stage-num">2</span>
      </div>
      <div class="stage-label">LLM call</div>
      <div class="stage-desc">Send to model, get raw response</div>
    </div>

    <div class="pipeline-arrow">→</div>

    <!-- Stage 3 -->
    <div class="pipeline-stage" data-stage="3" onclick="inspectStage(this)">
      <div class="stage-node" style="--stage-color: var(--color-actor-3)">
        <span class="stage-num">3</span>
      </div>
      <div class="stage-label">Post-process 1</div>
      <div class="stage-desc">Extract table from response</div>
    </div>

    <div class="pipeline-arrow">→</div>

    <!-- Stage 4 -->
    <div class="pipeline-stage" data-stage="4" onclick="inspectStage(this)">
      <div class="stage-node" style="--stage-color: var(--color-actor-4)">
        <span class="stage-num">4</span>
      </div>
      <div class="stage-label">Post-process 2</div>
      <div class="stage-desc">Validate + format table</div>
    </div>

    <div class="pipeline-arrow">→</div>

    <!-- Stage 5 -->
    <div class="pipeline-stage" data-stage="5" onclick="inspectStage(this)">
      <div class="stage-node" style="--stage-color: var(--color-actor-5)">
        <span class="stage-num">5</span>
      </div>
      <div class="stage-label">Final output</div>
      <div class="stage-desc">Merged into CER document</div>
    </div>
  </div>

  <!-- Inspection panel (shows on stage click) -->
  <div class="pipeline-inspector" id="pipeline-inspector">
    <div class="inspector-tabs">
      <button class="inspector-tab active" onclick="switchTab(this, 'before')">Data IN</button>
      <button class="inspector-tab" onclick="switchTab(this, 'after')">Data OUT</button>
      <button class="inspector-tab" onclick="switchTab(this, 'code')">Code</button>
    </div>
    <div class="inspector-content" id="inspector-before">
      <pre><code><!-- populated by JS --></code></pre>
    </div>
    <div class="inspector-content" id="inspector-after" style="display:none">
      <pre><code><!-- populated by JS --></code></pre>
    </div>
    <div class="inspector-content" id="inspector-code" style="display:none">
      <pre><code><!-- populated by JS --></code></pre>
    </div>
  </div>
</div>
```

### CSS

```css
.pipeline-tracer {
  margin: var(--space-8) 0;
  padding: var(--space-6);
  background: var(--color-bg-surface);
  border-radius: var(--radius-md);
  border: 1px solid var(--color-border-light);
}
.pipeline-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-6);
}
.pipeline-header h3 {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  font-weight: 600;
  margin: 0;
}
.pipeline-play-btn {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  padding: 6px 16px;
  border: 1px solid var(--color-border);
  color: var(--color-text-secondary);
  background: transparent;
  border-radius: var(--radius-full);
  cursor: pointer;
  transition: all var(--duration-fast);
}
.pipeline-play-btn:hover { border-color: var(--color-text); color: var(--color-text); }

.pipeline-stages {
  display: flex;
  align-items: flex-start;
  gap: 0;
  overflow-x: auto;
  padding-bottom: var(--space-4);
}
.pipeline-stage {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-width: 100px;
  cursor: pointer;
  padding: var(--space-2);
  border-radius: var(--radius-sm);
  transition: background var(--duration-fast);
}
.pipeline-stage:hover { background: var(--color-bg-hover); }
.pipeline-stage.active {
  background: var(--color-accent-light);
}
.pipeline-stage.animated {
  animation: stagePulse 0.5s var(--ease-out);
}
@keyframes stagePulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.1); }
  100% { transform: scale(1); }
}

.stage-node {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--color-text);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform var(--duration-fast);
}
.pipeline-stage:hover .stage-node {
  transform: scale(1.08);
}
.pipeline-stage.active .stage-node {
  background: var(--color-accent);
}
.stage-num {
  color: white;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: var(--text-base);
}
.stage-label {
  font-size: var(--text-sm);
  font-weight: 600;
  margin-top: var(--space-2);
  text-align: center;
}
.stage-desc {
  font-size: var(--text-xs);
  color: var(--color-text-muted);
  text-align: center;
  max-width: 120px;
}

.pipeline-arrow {
  color: var(--color-text-muted);
  font-size: var(--text-lg);
  margin-top: 12px;
  flex-shrink: 0;
}

.pipeline-inspector {
  margin-top: var(--space-6);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  overflow: hidden;
  display: none; /* shown by JS */
}
.pipeline-inspector.open { display: block; }

.inspector-tabs {
  display: flex;
  border-bottom: 1px solid var(--color-border-light);
  background: var(--color-bg-alt);
}
.inspector-tab {
  flex: 1;
  padding: var(--space-3);
  border: none;
  background: transparent;
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--color-text-muted);
  cursor: pointer;
  border-bottom: 2px solid transparent;
  transition: all var(--duration-fast);
}
.inspector-tab:hover { color: var(--color-text-secondary); }
.inspector-tab.active {
  color: var(--color-text);
  border-bottom-color: var(--color-text);
  font-weight: 500;
}
.inspector-content {
  background: var(--color-bg-code);
  padding: var(--space-4);
  max-height: 240px;
  overflow-y: auto;
}
.inspector-content pre {
  margin: 0;
  color: #CDD6F4;
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  white-space: pre-wrap;
  word-break: break-word;
}

@media (max-width: 768px) {
  .pipeline-stages { flex-wrap: wrap; justify-content: center; }
  .pipeline-arrow { transform: rotate(90deg); margin: var(--space-1) 0; }
}
```

### JS

```javascript
// Stage data — populated during build with REAL data from the codebase
const stageData = {
  1: {
    before: 'N/A (this is the entry point)',
    after: '{\n  "chapter_id": "ch04",\n  "ref_text": "Clinical data from 2019...",\n  "prev_cer": "Previous report section 4.2..."\n}',
    code: 'def load_chapter(chapter_id):\n    ref = fetch_reference(chapter_id)\n    prev = load_previous_cer(chapter_id)\n    return {"chapter_id": chapter_id, "ref_text": ref, "prev_cer": prev}'
  },
  2: {
    before: '(same as Stage 1 output)',
    after: '"Based on the clinical evidence provided, the following changes\\nare noted in Table 4.2:\\n| Field | Old | New | Status |\\n| --- | --- | --- |..."',
    code: 'def call_llm(context):\n    prompt = build_prompt(context)\n    response = client.chat(model="gpt-4", messages=[...])\n    return response.content'
  },
  // ... populate for each stage
};

window.inspectStage = function(el) {
  document.querySelectorAll('.pipeline-stage').forEach(s => s.classList.remove('active'));
  el.classList.add('active');

  const stage = el.dataset.stage;
  const data = stageData[stage];
  const inspector = document.getElementById('pipeline-inspector');
  inspector.classList.add('open');

  document.querySelector('#inspector-before code').textContent = data.before;
  document.querySelector('#inspector-after code').textContent = data.after;
  document.querySelector('#inspector-code code').textContent = data.code;

  // Reset to "Data IN" tab
  document.querySelectorAll('.inspector-tab').forEach(t => t.classList.remove('active'));
  document.querySelector('.inspector-tab').classList.add('active');
  document.getElementById('inspector-before').style.display = '';
  document.getElementById('inspector-after').style.display = 'none';
  document.getElementById('inspector-code').style.display = 'none';
};

window.switchTab = function(btn, tab) {
  document.querySelectorAll('.inspector-tab').forEach(t => t.classList.remove('active'));
  btn.classList.add('active');
  document.getElementById('inspector-before').style.display = tab === 'before' ? '' : 'none';
  document.getElementById('inspector-after').style.display = tab === 'after' ? '' : 'none';
  document.getElementById('inspector-code').style.display = tab === 'code' ? '' : 'none';
};

window.playPipeline = function(btn) {
  const stages = document.querySelectorAll('.pipeline-stage');
  btn.disabled = true;
  btn.textContent = '⏳ Playing...';
  let i = 0;
  const interval = setInterval(() => {
    if (i > 0) stages[i-1].classList.remove('animated');
    if (i >= stages.length) {
      clearInterval(interval);
      btn.disabled = false;
      btn.textContent = '▶ Replay';
      return;
    }
    stages[i].classList.add('animated');
    inspectStage(stages[i]);
    i++;
  }, 800);
};
```

### Rules
- The `stageData` object MUST be populated with REAL data from the codebase — not placeholder Lorem Ipsum
- "Data IN" shows the actual data shape entering this stage (JSON, CSV columns, string format)
- "Data OUT" shows the actual data shape leaving this stage
- "Code" shows the actual function that performs this transformation (5-10 lines, original code)
- Every post-processing step gets its own stage — don't collapse "validate + format + clean" into one node. The whole point is seeing each transformation layer
- The animation should light up nodes left-to-right with 800ms delay between each
- Stage count should be 3-8. Fewer than 3 means you're collapsing too much; more than 8 means you need to group sub-stages

---

## Git Diff Overlay

A visual layer that highlights which parts of the architecture changed between two commits or versions. Applied ON TOP OF the architecture diagram or module collaboration map from Module 1.

**When to use**: When the user asks "what changed" or when the codebase has recent git history worth explaining. This is NOT a standalone element — it's an overlay that augments the existing architecture view.

### HTML

```html
<div class="diff-overlay-container animate-in">
  <div class="diff-header">
    <h3>What changed</h3>
    <div class="diff-commits">
      <span class="diff-commit old">abc1234</span>
      <span class="diff-arrow">→</span>
      <span class="diff-commit new">def5678</span>
    </div>
    <label class="diff-toggle">
      <input type="checkbox" checked onchange="toggleDiffOverlay(this.checked)">
      Show changes
    </label>
  </div>

  <!-- Architecture diagram with diff highlights -->
  <div class="diff-architecture">
    <!-- Re-use the architecture diagram structure from interactive-elements.md -->
    <!-- Add .diff-changed class to modified nodes -->
    <!-- Add .diff-added class to new nodes -->
    <!-- Add .diff-removed class to deleted nodes -->
    <!-- Add .diff-affected-path class to data flow arrows that pass through changed nodes -->
  </div>

  <!-- Change summary cards -->
  <div class="diff-summary">
    <div class="diff-card changed">
      <div class="diff-card-icon">✏️</div>
      <div class="diff-card-info">
        <strong>llm_client.py</strong>
        <p>Updated model call — added retry logic, changed response parsing</p>
        <span class="diff-impact">Affects: chapter processing pipeline, output format</span>
      </div>
    </div>
    <div class="diff-card changed">
      <div class="diff-card-icon">✏️</div>
      <div class="diff-card-info">
        <strong>post_processor.py</strong>
        <p>Removed table validation step — output now passes through directly</p>
        <span class="diff-impact">Affects: final CER format, QA gate</span>
      </div>
    </div>
    <div class="diff-card added">
      <div class="diff-card-icon">✨</div>
      <div class="diff-card-info">
        <strong>csv_exporter.py</strong>
        <p>New file — exports intermediate LLM results as CSV for AB testing</p>
        <span class="diff-impact">New capability: direct intermediate output access</span>
      </div>
    </div>
  </div>
</div>
```

### CSS

```css
.diff-overlay-container {
  margin: var(--space-8) 0;
}
.diff-header {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  margin-bottom: var(--space-6);
  flex-wrap: wrap;
}
.diff-header h3 {
  font-family: var(--font-display);
  font-size: var(--text-xl);
  margin: 0;
}
.diff-commits {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-family: var(--font-mono);
  font-size: var(--text-xs);
}
.diff-commit {
  padding: 4px 10px;
  border-radius: var(--radius-full);
}
.diff-commit.old { background: var(--color-error-light); color: var(--color-error); }
.diff-commit.new { background: var(--color-success-light); color: var(--color-success); }
.diff-arrow { color: var(--color-text-muted); }

.diff-toggle {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-sm);
  cursor: pointer;
  color: var(--color-text-secondary);
}

/* Diff highlight states — applied to architecture diagram nodes */
.diff-changed {
  animation: diffPulse 2s ease-in-out infinite;
  outline: 1.5px solid var(--color-text);
  outline-offset: 3px;
}
.diff-added {
  animation: diffPulse 2s ease-in-out infinite;
  outline: 1.5px dashed var(--color-success);
  outline-offset: 3px;
}
.diff-removed {
  opacity: 0.3;
  text-decoration: line-through;
}
.diff-affected-path {
  stroke: var(--color-text) !important;
  stroke-width: 2px !important;
  stroke-dasharray: 6 4;
  animation: dashFlow 1s linear infinite;
}
@keyframes diffPulse {
  0%, 100% { outline-offset: 3px; }
  50% { outline-offset: 5px; }
}
@keyframes dashFlow {
  to { stroke-dashoffset: -10; }
}

/* Change summary cards */
.diff-summary {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  margin-top: var(--space-6);
}
.diff-card {
  display: flex;
  align-items: flex-start;
  gap: var(--space-3);
  padding: var(--space-4);
  border-radius: var(--radius-sm);
  border-left: 2px solid transparent;
  background: var(--color-bg-alt);
}
.diff-card.changed {
  border-left-color: var(--color-text);
}
.diff-card.added {
  border-left-color: var(--color-success);
}
.diff-card.removed {
  border-left-color: var(--color-error);
}
.diff-card-icon { font-size: 1.2rem; flex-shrink: 0; margin-top: 2px; }
.diff-card-info strong {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
}
.diff-card-info p {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  margin: var(--space-1) 0;
}
.diff-impact {
  font-size: var(--text-xs);
  font-family: var(--font-mono);
  color: var(--color-text-muted);
  font-style: italic;
}

@media (max-width: 768px) {
  .diff-header { flex-direction: column; align-items: flex-start; }
  .diff-toggle { margin-left: 0; }
}
```

### JS

```javascript
window.toggleDiffOverlay = function(show) {
  document.querySelectorAll('.diff-changed, .diff-added, .diff-removed').forEach(el => {
    el.style.display = show ? '' : 'none';
    if (!show) {
      el.classList.remove('diff-changed', 'diff-added', 'diff-removed');
      el.dataset.diffClass && el.classList.add(el.dataset.diffClass);
    }
  });
  document.querySelectorAll('.diff-affected-path').forEach(el => {
    el.style.visibility = show ? 'visible' : 'hidden';
  });
};
```

### Rules
- The diff overlay is NOT a standalone module — it augments the architecture diagram that should already exist in the course
- Every changed file MUST have an "Affects:" line explaining the downstream impact — don't just list what changed, explain what it MEANS
- Use the three visual states consistently: solid outline = changed, dashed outline = added, dimmed + strikethrough = removed
- The animated dashed path (diff-affected-path) should trace the data flow through changed nodes — this is the "impact path"
- Change summary cards should be ordered by impact severity, not alphabetically
- If `git diff` output is available, extract the actual line counts and show them: "+42 / -18 lines"
- The toggle lets the user see the architecture with and without the diff — this comparison is where the "aha" moment happens

### How to extract git diff data during Phase 1

```bash
# Get recent commits
git log --oneline -10

# Get changed files between two commits
git diff --stat <old_commit> <new_commit>

# Get detailed diff for a specific file
git diff <old_commit> <new_commit> -- path/to/file.py

# Get just function-level changes (Python)
git diff <old_commit> <new_commit> -- '*.py' | grep -E '^[+-].*def '
```

Map the changed files to your module collaboration graph. For each changed file:
1. Which module/package does it belong to?
2. Which functions within it were modified?
3. What data flows through this file?
4. What downstream modules consume this file's output?

This mapping is what turns a raw git diff into an actionable understanding of "what broke and why."

---

## Advanced Visualization Patterns

These visualization types use D3.js loaded via CDN. They are more powerful than the basic flow diagrams and should be used when the data warrants them. The rule is: **effective, not flashy**. Every visualization must answer a specific question the learner has.

### When to Use Each Pattern

| Pattern | Best For | NOT For |
|---|---|---|
| Force-directed graph | Module dependency map, import relationships, "who calls who" | Sequential pipelines, hierarchical data |
| Sankey diagram | Data flow volume, pipeline stages with branching/merging | Simple linear A→B→C flows (use Pipeline Tracer instead) |
| Chord diagram | Mutual dependencies, cross-module call frequency matrix | One-directional flows, hierarchical data |
| Collapsible tree | File trees, JSON/YAML schema, class inheritance | Circular dependencies, data flow |
| Mini data table | CSV column profiles, config file summaries | Large datasets (show sample only) |

### CDN Loading Pattern

All D3 visualizations in the course use the same loading pattern. Include once at the bottom of the HTML:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js"></script>
```

### Force-Directed Dependency Graph

**Purpose**: Show which modules/files depend on which others. Nodes are files, edges are import/call relationships. The physics simulation naturally clusters tightly-coupled modules together — this is the "aha" moment.

**Data format:**
```javascript
const graphData = {
  nodes: [
    { id: "pipeline_runner.py", group: "core", fileType: "py" },
    { id: "llm_client.py", group: "core", fileType: "py" },
    { id: "config.yaml", group: "config", fileType: "yaml" },
    { id: "formatter.py", group: "utils", fileType: "py" }
  ],
  links: [
    { source: "pipeline_runner.py", target: "llm_client.py", type: "imports" },
    { source: "pipeline_runner.py", target: "config.yaml", type: "reads" },
    { source: "pipeline_runner.py", target: "formatter.py", type: "imports" }
  ]
};
```

**Styling rules:**
- Node size: 8px default, 12px for files with 3+ connections
- Node color: use file-type dot colors from design-system.md (`--ft-python`, `--ft-json`, etc.)
- Edge color: `var(--color-border)` for normal imports, `var(--color-accent)` for the primary data flow path
- Edge style: solid for imports, dashed for config reads
- On hover: highlight all connected edges and dim everything else
- On click: `sendPrompt('Explain [filename] in detail')` or jump to that file's Package Anatomy Card
- Labels: filename only (no path), 12px, positioned to avoid overlap
- Keep the simulation gentle: `forceCharge(-120)`, `forceLink().distance(80)`

### Sankey Data Flow Diagram

**Purpose**: Show how data flows through the system with volume. Left side is input sources, right side is output destinations, middle bands show transformation stages. Band width represents relative data volume or importance.

**When to use instead of Pipeline Tracer**: When the flow branches or merges (e.g., multiple input files converge into one processor, or one processor fans out to multiple outputs). Pipeline Tracer is for linear flows; Sankey is for complex flows.

**Data format:**
```javascript
const sankeyData = {
  nodes: [
    { name: "Raw chapters (input)" },
    { name: "LLM processor" },
    { name: "Table extractor" },
    { name: "Validator" },
    { name: "CER document (output)" },
    { name: "CSV export (output)" }
  ],
  links: [
    { source: 0, target: 1, value: 10 },
    { source: 1, target: 2, value: 8 },
    { source: 1, target: 3, value: 2 },
    { source: 2, target: 4, value: 6 },
    { source: 2, target: 5, value: 2 },
    { source: 3, target: 4, value: 2 }
  ]
};
```

**Styling rules:**
- Node rectangles: 20px wide, height proportional to flow volume
- Node color: `var(--color-text)` (near-black) — the bands carry the color, not the nodes
- Band color: accent blue at 25% opacity for the primary flow, `var(--color-border)` at 15% for secondary flows
- Band on hover: raise opacity to 60% and show a tooltip with the data shape at that stage
- Labels: 13px, positioned outside the node rectangles
- Load via: `https://cdnjs.cloudflare.com/ajax/libs/d3-sankey/0.12.3/d3-sankey.min.js`

### Collapsible Tree (for JSON/YAML/file structure)

**Purpose**: Let the learner explore a hierarchical structure by expanding and collapsing nodes. Superior to a flat code block for JSON schemas, YAML configs, and file trees.

**Styling rules:**
- Use the file-type dot colors for leaf nodes
- Folders/objects get a subtle triangle toggle (▶ / ▼)
- Expand the first two levels by default, collapse deeper levels
- On hover: show a tooltip with the field's purpose (populated from Phase 1 analysis)
- Values (strings, numbers) shown in mono font, keys in regular font
- CSS-only implementation preferred (no D3 needed) — use `<details>` / `<summary>` with custom styling
- Max visible depth without scrolling: 3 levels. Deeper nesting collapses automatically

### Mini Data Table (for CSV/tabular data)

**Purpose**: Give a quick profile of a CSV or data file — column names, types, sample values, and which code consumes it.

**Structure:**
```html
<div class="data-profile">
  <table class="data-table">
    <thead>
      <tr>
        <th>Column</th>
        <th>Type</th>
        <th>Sample</th>
        <th>Notes</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>chapter_id</code></td>
        <td><span class="type-badge str">str</span></td>
        <td>"ch04"</td>
        <td>Primary key, referenced by pipeline_runner.py</td>
      </tr>
      <!-- more rows -->
    </tbody>
  </table>
</div>
```

**Styling rules:**
- Table: full width, 1px border-bottom on rows, no outer border
- Header: `var(--color-text-tertiary)`, uppercase, 11px mono, letter-spacing 0.08em
- Type badges: tiny pills (font-size 10px, padding 2px 6px, border-radius full)
  - `str` → blue-gray, `int` → green, `float` → amber, `bool` → purple, `date` → teal
- Sample values: mono font, truncated at 30 chars with `...`
- Notes column: regular font, `var(--color-text-secondary)`
- Show max 8 rows. If more columns exist, add a "and N more columns" footer
- Below the table: a one-liner like "Consumed by: `pipeline_runner.py` → `process_chapter()`"

### Rules for All Advanced Visualizations

1. **Always provide a text fallback.** Below every D3 visualization, include a brief text summary of what the diagram shows. Screen readers and users who can't interact with the diagram should still get the key insight.
2. **Responsive handling**: On mobile (< 768px), replace force-directed graphs with a simple indented list. Replace Sankey with a numbered step list. D3 layouts don't work well on small screens.
3. **Loading**: D3 scripts load from CDN. Include a tiny CSS spinner placeholder that disappears when the visualization renders. Never show a blank space while loading.
4. **Interaction budget**: Each visualization gets at most 2 interaction types (e.g., hover + click, or drag + click). More than that creates confusion. Pick the two that answer the learner's most likely questions.
5. **Color budget**: Max 3 colors per visualization (excluding grays). Use the file-type dot colors from design-system.md for file nodes, and accent blue for highlighted paths. Everything else is gray/black.

