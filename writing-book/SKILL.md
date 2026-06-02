---
name: writing-book
description: >
  Jianan 的持续积累式写书系统。把日常对话中沉淀的好观点、知识缺口、研究实践、
  对话精华，按主题（书）持续累积为 fragments，编排为 chapters，最终编译为 Epub。
  当 Jianan 提到「启动新书」「记下这个观点」「这块我不懂」「整理这次研究」
  「这段对话有价值」「编入第 X 章」「编译成 Epub」「现在书的状态」「写书」
  时，必须触发此 skill。第一本种子书是《CER 方法论》。
---

# Writing Book — 持续积累式写书系统

## 设计哲学

这个系统不是用来"一口气写完一本书"的，而是用来**让每次对话都成为某本书的素材**的。

核心原则：

1. **主题作容器**：每本书是一个独立 vault（`books/<book-id>/`）
2. **Fragment 优先**：先存 fragment，再编排 chapter
3. **教学输出方式可切换**：First Principles / Case-First / Dialogue 三种模式
4. **Epub 是终态**：所有积累最终用 `compile.py` 一键编译
5. **每章可独立完成度**：不要求全书一致进度

---

## 当用户说「启动新书《XXX》」

执行：

1. 读取 `assets/templates/BOOK.md`
2. 询问：书的核心命题（一句话）/ 目标读者 / 教导模式默认值
3. 在 `books/<book-id>/` 下创建：
   - `BOOK.md`（元数据 + TOC）
   - `chapters/`（章节正文）
   - `fragments/{quotes,gaps,research,dialogues}/`（4 类原料）
   - `CHANGELOG.md`（追加每次操作记录）
4. 在 `BOOK.md` 写入第一条 INIT 记录

---

## 4 类输入的差异化路由

每次 Jianan 抛出一个想沉淀的内容，先判断是哪类，再写到对应位置。

### 类型 1：好观点 / 听到的金句（Quotes）

**触发词**：「记下这个观点」「这句话很有意思」「这段值得记」

**落点**：`books/<book-id>/fragments/quotes/<YYYY-MM-DD>_<slug>.md`

**模板字段**：
```markdown
---
type: quote
date: YYYY-MM-DD
source: 谁说的 / 哪本书 / 哪次对话
related_chapters: [ch01, ch03]
status: raw | refined | integrated
---

# <观点的一句话浓缩>

## 原话 / 原始上下文
> （一句到一段）

## 我的批注
- 为什么这个观点击中我了
- 它和我已有的 X 想法的关系
- 它修正/挑战了我什么

## 后续动作
- [ ] 编入哪一章的哪一节
```

### 类型 2：知识框架缺口（Gaps）

**触发词**：「这块我不懂」「需要补这个」「我对 X 还不清楚」

**落点**：`books/<book-id>/fragments/gaps/<YYYY-MM-DD>_<slug>.md`

**模板字段**：
```markdown
---
type: gap
date: YYYY-MM-DD
priority: high | medium | low
status: identified | researching | filled
related_chapters: [ch02]
---

# <缺口的一句话描述>

## 我现在对它的理解（坦诚地）
（写下你目前已知的，包括猜测和不确定）

## 我不懂的是
- 具体问题 1
- 具体问题 2

## 补这个缺口需要做什么
- [ ] 读 X
- [ ] 问 Y
- [ ] 实验 Z

## 缺口被填上后要更新哪一章
```

### 类型 3：Research 实践（Research）

**触发词**：「整理这次研究」「记录这次实验」「沉淀这个方法」

**落点**：`books/<book-id>/fragments/research/<YYYY-MM-DD>_<slug>.md`

**模板字段**：
```markdown
---
type: research
date: YYYY-MM-DD
domain: technical | methodology | political | other
status: raw | analyzed | integrated
---

# <研究主题>

## 论点（Thesis）
（这次研究最终得出的核心结论，一句话）

## 证据（Evidence）
- 实验 / 案例 / 数据 1
- 实验 / 案例 / 数据 2

## 反例与边界（Counter）
- 在什么情况下这个结论不成立
- 我故意去找的反对意见

## 复用形式
- 公式化 / 步骤化的版本（让别人也能用）
```

### 类型 4：对话沉淀（Dialogues）

**触发词**：「这段对话有价值」「把这次讨论存下来」

**落点**：`books/<book-id>/fragments/dialogues/<YYYY-MM-DD>_<slug>.md`

**模板字段**：
```markdown
---
type: dialogue
date: YYYY-MM-DD
participants: [Jianan, Claude / 同事姓名]
status: raw | distilled | integrated
related_chapters: [ch04]
---

# <对话主题>

## 触发问题
（这次对话因为什么开始的）

## 关键交锋（提取问答骨架）
**Q1: ...**
A1: ...

**Q2: ...**
A2: ...

## 结晶
（这段对话最终留下的、值得带走的东西）
```

---

## 3 种教导输出方式（Teaching Modes）

每章可以指定一种主导的教导模式（在 `chapter.md` 的 frontmatter 里）。

### 模式 A：First Principles（从最底层概念建起）

**适用**：方法论章节、原理性内容
**结构**：
```
1. 起点：一个最简单的事实 / 直觉
2. 推导：从这个事实出发，加上一两个原则，推出更复杂的结论
3. 验证：用一个具体例子验证推导
4. 拓展：这个结论还能解释哪些现象
5. 收口：把这个推导链浓缩成一句口诀 / 公式
```

**示例触发**："用 First Principles 重写第 3 章"

### 模式 B：Case-First（先讲具体案例再抽象）

**适用**：经验沉淀章节、实战教学内容
**结构**：
```
1. 现场：把读者拉到一个具体场景里（最好是真实发生的）
2. 困境：这个场景里我们当时遇到了什么问题
3. 错误尝试：我们先试了什么，为什么不行
4. 转折：什么让我们想到了真正的解法
5. 抽象：从这个具体案例抽象出可复用的原则
6. 反例：这个原则在什么情况下也会失效
```

**示例触发**："用 Case-First 写第 0 章"

### 模式 C：Dialogue（保留对话张力）

**适用**：争议性话题、需要展示思考过程的章节
**结构**：
```
1. 开场：抛出一个有争议的问题
2. 对话推进：A 说... B 说... A 反驳... B 修正...
3. 关键转折：某个反例 / 类比让对话进入新阶段
4. 共识：能达成的部分
5. 悬置：刻意保留的开放问题
```

**示例触发**："用 Dialogue 写第 5 章"

---

## Fragment → Chapter 编排流程

当 Jianan 说「**把片段编入第 X 章**」或「**写第 X 章**」：

1. 读取 `BOOK.md` 的 TOC，确认第 X 章的主题和教导模式
2. 扫描 `fragments/` 下所有 `related_chapters` 包含 ch0X 的片段
3. 按教导模式的结构，把 fragments 重组进章节
4. 每个被编入的 fragment，把 frontmatter 的 `status` 改为 `integrated`
5. 章节写入 `chapters/ch0X-<slug>.md`
6. 更新 `BOOK.md` 的 TOC 中该章的完成度
7. 在 `CHANGELOG.md` 追加 INTEGRATE 条目

---

## 「现在书的状态」命令

输出格式：

```
=== 《<书名>》当前状态 ===

进度：
  Ch 0  [██████████] 100%  - 引子：CER 方法论的来路
  Ch 1  [██████░░░░]  60%  - Pipeline 工程纪律
  Ch 2  [███░░░░░░░]  30%  - Anchor Verify 三级降级
  ...

待处理 fragments：
  quotes: 12 条（其中 8 条 raw / 4 条 refined）
  gaps: 5 条（其中 2 条 high priority）
  research: 7 条
  dialogues: 3 条

下一步建议：
  - Ch 2 缺一个具体案例 → 把 fragments/research/2026-04-03_anchor-verify.md 编入
  - Gap "L4 是否需要" 已经 high priority 1 周，建议本周补
```

---

## 「编译成 Epub」命令

执行 `scripts/compile.py`，参数为书的目录。

**编译流程**：
1. 读取 `BOOK.md` 解析元数据和 TOC
2. 按 TOC 顺序读取 `chapters/ch0X-*.md`
3. Markdown → HTML（用 `markdown` 库 + `fenced_code` + `tables` + `footnotes` + `toc` 扩展）
4. 套用 `assets/styles/tech-book.css`
5. 调用 `ebooklib` 组装 Epub
6. 输出到 `books/<book-id>/dist/<book-id>-<YYYYMMDD>.epub`
7. 同时输出一份 `dist/preview.html`（单文件 HTML 预览）

**严格规则**：
- 章节中的代码块自动加 `<pre class="mono">` 样式
- 引用块（`>`）转成带左边竖线的 `<blockquote>`
- 表格保留为 HTML `<table>`，不简化
- 所有图片必须在 `books/<book-id>/assets/images/` 下，路径相对引用

---

## 目录结构

```
books/
└── cer-methodology/
    ├── BOOK.md                    # 元数据 + TOC + 进度
    ├── CHANGELOG.md               # 操作日志
    ├── chapters/
    │   ├── ch00-introduction.md
    │   ├── ch01-pipeline-discipline.md
    │   └── ...
    ├── fragments/
    │   ├── quotes/
    │   ├── gaps/
    │   ├── research/
    │   └── dialogues/
    ├── assets/
    │   └── images/
    └── dist/
        ├── cer-methodology-20260507.epub
        └── preview.html
```

---

## 与其他 skill 的协作

- **claw-vibe-project**：写书 vault 也有 PROJECT.md / CHANGELOG.md 风格的元数据，沿用相同的"四文档分工"哲学
- **jianan-presentation-system**：演讲场景包的内容会成为《说服力演讲》一书的章节
- **frontend-design**：Epub 预览的 HTML 样式参考其设计原则

---

## 失败模式（要避免的反模式）

1. ❌ **fragment 越积越多但永远不编入章节** → 每次会话结束前问一句"有 fragment 可以现在编入哪章吗？"
2. ❌ **多本书同时进行，每本都进度 10%** → 始终只有一本"主推书"，其他书只接收 fragment 不主动编排
3. ❌ **追求 Epub 完美再编译** → 每周自动编译一次给 Jianan 看进度，Epub 是过程，不是终点
4. ❌ **fragment 写得像最终章节那么完整** → fragment 就是粗糙的素材，越快记下越好，编排时再打磨
