# Personal OS — 项目总览 (Project Overview)

> 个人长期管理系统：用数据驱动的方式管理身体、工作、投资与知识。

## 项目简介 (What is Personal OS)

Personal OS 是一套面向个人的长期管理软件。它的核心理念是把个人的**身体状态、工作任务、投资分析和知识积累**统一到一个自托管、数据自有、长期可维护的系统中。

AI 在本系统中**只作为分析工具**，不作为数据存储的替代品，也不接管决策。数据永远优先，AI 仅提供洞察。

## 核心目标 (Core Goals)

帮助个人管理四个维度：

| 模块 | 英文 | 说明 |
|------|------|------|
| 身体 | Body | 体重、运动、睡眠、健康指标追踪 |
| 工作 | Work | 任务、项目、时间管理 |
| 投资 | Investment | 投资组合分析、收益追踪 |
| 知识 | Knowledge | 笔记、学习记录、知识库 |

## 技术栈 (Tech Stack)

| 层级 | 技术 | 说明 |
|------|------|------|
| 前端 | Vue 3 | SPA，组件化 |
| 后端 | FastAPI | Python 异步 Web 框架 |
| 数据库 | SQLite | 单文件，零配置，长期可靠 |
| 语言 | Python 3.12 | 后端语言 |

**为什么选 SQLite？** 单文件、无服务、跨平台、可被多种工具直接读取，最适合个人长期项目。详见 [DATABASE.md](./DATABASE.md)。

## 开发原则 (Development Principles)

1. **保持简单 (Keep it simple)** — 能用单表就不用多表，能用一个文件就不拆模块。
2. **长期维护 (Long-term maintainable)** — 优先选择 10 年后仍可运行、可读、可迁移的方案。
3. **不过度设计 (No over-engineering)** — 不为想象中的需求提前构建复杂系统。
4. **数据优先 (Data first)** — 数据是核心资产，AI 只是分析工具。
5. **AI 只作为分析工具 (AI as analysis only)** — 不让 AI 持久化持有或替代数据。

## 当前版本 (Current Version)

**v0.0.1** — 项目基础搭建阶段 (Foundation)

详见 [CHANGELOG.md](./CHANGELOG.md) 与 [ROADMAP.md](./ROADMAP.md)。

## 项目结构 (Project Structure)

```
personal-os/
├── README.md
├── docs/                  # 项目文档（本目录）
│   ├── PROJECT.md         # 项目总览
│   ├── ROADMAP.md         # 版本路线图
│   ├── CHANGELOG.md       # 变更记录
│   ├── CLAUDE.md          # AI 协作指南（未来 Claude 必读）
│   ├── DATABASE.md        # 数据库设计
│   ├── API.md             # API 文档
│   └── TASKS.md           # 任务追踪
└── backend/               # FastAPI 后端
```

## 相关文档 (Related Docs)

- [ROADMAP.md](./ROADMAP.md) — 版本路线图
- [CHANGELOG.md](./CHANGELOG.md) — 变更记录
- [CLAUDE.md](./CLAUDE.md) — AI 协作指南（未来 Claude 必读）
- [DATABASE.md](./DATABASE.md) — 数据库设计
- [API.md](./API.md) — API 文档
- [TASKS.md](./TASKS.md) — 任务追踪

## 仓库 (Repository)

- GitHub: https://github.com/airedmars/personal-os
- 默认分支: `main`
