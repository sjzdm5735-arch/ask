# Agent Skill Lifecycle Kit (ask)

Agent Skill Lifecycle Kit 是一个面向 AI Agent 维护者的开源工具框架，帮助团队把 **Skill、提示词、工作流、维护 SOP** 从临时经验沉淀为可持续维护的资产。

https://github.com/sjzdm5735-arch/ask

---

## Why this project exists

大多数 Agent 项目都会遇到同样的问题：

- Skill 越积越多，但质量不一致
- 反复踩坑，却没有结构化的 Pitfall 沉淀
- 重复工作流没有变成可复用资产
- 维护负担增长快，治理能力增长慢
- “能跑”和“可维护”不是一回事

这个项目要解决的不是“能不能调用 Skill”，而是：

**如何让 Skill 体系可维护、可演进、可审计。**

---

## Who this is for

这个项目适合以下人群：

- AI Agent 开源项目维护者
- Prompt / Skill / Workflow 工程师
- 使用 Hermes、OpenClaw、Claude Code、Codex 等系统的团队
- 需要把个人经验产品化、组织化的维护者
- 需要在长期项目里管理可复用知识资产的人

---

## Core ideas

### 1. Skills should be maintainable assets
Skill 不应该是临时提示词，而应该是：
- 有触发条件
- 有标准步骤
- 有 Pitfall
- 有验证方式
- 有版本演进

### 2. Maintenance burden is a first-class problem
很多 Agent 项目不是能力不够，而是：
- 治理不够
- 结构不够
- 复用不够
- 审计不够

### 3. Workflows should survive beyond chat
真正有价值的不是一次对话，而是：
- 可复用流程
- 可检查模板
- 可传承经验
- 可长期维护的资产

---

## Features

- Skill 骨架生成
- Skill 质量检查
- Pitfall 沉淀机制
- 复用型 SOP 模板
- 维护者检查清单
- 适配 Hermes / OpenClaw / 通用 Agent 工作流
- 本地 CLI 工具

---

## Install

```bash
git clone https://github.com/sjzdm5735-arch/ask.git
cd ask
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

---

## Quick start

```bash
ask init
ask new my-skill
ask check my-skill
ask export my-skill
```

---

## Example

```bash
ask new taobao-keyword-review
ask check taobao-keyword-review
ask export taobao-keyword-review
```

This creates a structured skill scaffold, checks its completeness, and exports a summary.

---

## Why it matters for the Agent ecosystem

随着 Agent 从“单次提示”走向“长期运行系统”，真正的瓶颈正在转移：

- 从“模型能不能做”
- 转向“系统能不能持续维护”

这个项目聚焦的是后面这一层：
**Agent 维护工程。**

---

## Roadmap

### v0.1
- Skill scaffold
- Skill check
- Skill export
- Basic CLI

### v0.2
- richer quality rules
- Pitfall library
- templates
- better Hermes/OpenClaw adapters

### v0.3
- batch checks
- export reports
- contributor workflows
- maintenance dashboard ideas

---

## Contributing

欢迎贡献，尤其是：

- 更好的 Skill 质量规则
- 更实用的维护模板
- Agent 平台适配器（Hermes / OpenClaw / Codex / Claude Code）
- CLI 体验优化
- 真实维护者工作流文档

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

[MIT](LICENSE)
