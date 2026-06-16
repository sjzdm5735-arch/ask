# Agent Skill Lifecycle Kit (ask)

Agent Skill Lifecycle Kit 是一个面向 AI Agent 维护者的开源工具框架，帮助团队把**Skill/提示词/工作流/维护 SOP** 从临时经验沉淀为可持续维护的资产。

## Why

大多数 AI Agent 项目都会遇到相同问题：
- Skill 越积越多，但质量不一致
- 重复工作流没有沉淀
- 反复踩坑但缺少 Pitfall 结构
- 维护负担增长快，治理能力增长慢
- 团队无法区分“能用”与“可维护”

这个项目要解决的不是“能不能调用 Skill”，而是：

**如何让 Skill 体系可维护、可演进、可审计。**

## Features

- Skill 骨架生成
- Skill 质量检查（frontmatter / 触发条件 / 步骤 / Pitfall / 验证）
- Pitfall 沉淀机制
- 复用型 SOP 模板
- 维护者检查清单
- 适配 Hermes / OpenClaw / 通用 Agent 工作流

## Install

```bash
git clone https://github.com/chenguagua/ask.git
cd ask
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
```

## Quick start

```bash
ask init
ask new my-skill
ask check my-skill
ask export my-skill
```

## Who is this for

- Open source Agent maintainers
- Prompt / Skill / Workflow engineers
- 使用 Hermes、OpenClaw、Claude Code、Codex 等系统的团队
- 需要把个人经验产品化的维护者

## License

MIT
