# 4 类输入的处理规范

每次 Jianan 抛出一个想沉淀的内容时，先识别类型，再用对应的 fragment 模板。

## 识别决策树

```
Jianan 抛出一段内容
        │
        ▼
   是「别人说的话」或「书里读到的话」？
        ├─ 是 → quote
        └─ 否 ▼
   是「我意识到我不懂的事」？
        ├─ 是 → gap
        └─ 否 ▼
   是「我做过 / 在做的实验或调研」？
        ├─ 是 → research
        └─ 否 ▼
   是「一段对话的精华」？
        ├─ 是 → dialogue
        └─ 否 → 默认按 quote 处理（最宽松类别）
```

## 命名规范

`fragments/<type>/<YYYY-MM-DD>_<slug>.md`

- `slug` 是 3-5 个英文单词，用连字符
- 例：`fragments/quotes/2026-05-07_machine-learning-needs-human-teaching.md`
- 例：`fragments/research/2026-04-03_anchor-verify-three-tier-fallback.md`

## frontmatter 必填字段

所有 fragment 都必须有：
- `type`
- `date`
- `status`（raw / refined / integrated）
- `related_chapters`（可以为空数组 `[]`）

## status 流转

```
raw → refined → integrated
 │       │            │
 │       │            └─ 已编入某章，不再是独立 fragment
 │       └─ 已经过润色，结构清晰
 └─ 刚记下来的原始素材
```

## 反模式

- ❌ 一个 fragment 同时是 quote 又是 research（合不下就拆成两个）
- ❌ slug 用中文（编译可能出问题，统一用英文）
- ❌ 不写 related_chapters（"暂时不知道编入哪章"也要写 `[]`，方便后续搜索）
