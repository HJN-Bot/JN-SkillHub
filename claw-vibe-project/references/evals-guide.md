# Evals 复用指南

## 设计思路

项目级 evals 是**可复用的验证资产**，不是一次性测试。
每次 AI 做了修改，evals 帮你验证「没有破坏已有逻辑」。

---

## Eval 条目 JSON 格式

```json
{
  "id": "eval-auth-001",
  "version": "1.0",
  "description": "用户登录成功，返回有效 token",
  "tags": ["auth", "happy-path", "p0"],
  "priority": "p0",
  "input": {
    "scenario": "用户提交正确的用户名和密码",
    "context": "用户已注册，账号未被锁定",
    "mock_data": { "username": "test@example.com", "password": "correct" }
  },
  "expected": {
    "assertions": [
      { "type": "contains_field", "field": "token" },
      { "type": "status_code", "value": 200 },
      { "type": "not_contains", "value": "error" }
    ],
    "notes": "token 格式为 JWT，有效期 24h"
  },
  "last_run": "2026-03-20",
  "status": "passing",
  "linked_harness": "harness/interfaces/auth.ts"
}
```

---

## 优先级分层

| 优先级 | 触发时机 | 运行范围 |
|--------|---------|---------|
| **P0** | 每次 session 结束 | `evals/core/smoke.json` |
| **P1** | 修改 harness/ 后 | `evals/core/regression.json` |
| **P2** | 每周漂移检测时 | 全量 |
| **P3** | 按需手动触发 | 特定功能模块 |

---

## 跑 Eval 的 Prompt

```
请跑 evals/core/smoke.json 中的所有测试用例：
1. 对每个 eval，根据 input.scenario 执行相应逻辑
2. 检查输出是否满足所有 assertions
3. 输出 pass/fail 表格
4. 如有 fail，说明原因和建议修复方向
5. 更新每个条目的 last_run 日期和 status
```

---

## Eval 与 Harness 的关系

- `linked_harness` 字段指向对应的接口定义
- 如果 harness 接口改了，相关 eval 必须同步更新
- CHANGELOG 中 `[HARNESS CHANGE]` 条目应触发 P1 eval 重跑

---

## 跨项目复用

常用 eval 模板可以沉淀到 `evals/shared/` 目录：

```
evals/
├── shared/               # 跨项目通用模板（可复制到新项目）
│   ├── api-basics.json   # REST API 基础测试模板
│   └── auth-flow.json    # 认证流程测试模板
├── core/                 # 本项目核心 eval
└── features/             # 功能模块 eval
```

新项目初始化时，从 `shared/` 复制相关模板，修改为项目具体内容。
