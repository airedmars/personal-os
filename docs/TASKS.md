# Tasks — 任务追踪

> 本文件追踪 Personal OS 的所有任务。任务编号 `Task-XXX`。
> 状态：📋 Pending（待办）/ 🚧 In Progress（进行中）/ ✅ Done（完成）

---

## 任务状态总览

| 编号 | 名称 | 状态 | 目标版本 |
|------|------|------|----------|
| Task-001 | 项目文档体系 | ✅ Done | v0.0.1 |
| Task-002 | Weight API CRUD 完善 | 📋 Pending | v0.0.2 |
| Task-003 | Body 模块统计与导出 | 📋 Pending | v0.0.2 |

---

## 当前任务

（暂无进行中任务）

---

## 已完成任务

### Task-001 — 项目文档体系 (Project Documentation Foundation) ✅
- **完成日期：** 2026-07-10
- **目标：** 建立 docs 文档体系，让未来 AI/开发者快速理解项目。
- **交付物：** PROJECT / ROADMAP / CHANGELOG / CLAUDE / DATABASE / API / TASKS
- **说明：** 文档已创建，待用户执行 Git commit 后正式归档。

---

## 推荐下一步任务

### Task-002 — Weight API CRUD 完善
- **理由：** v0.0.1 仅完成 `POST /api/weight`，缺少查询、修改、删除，无法形成最小闭环。
- **范围：**
  - [ ] `GET /api/weight`（支持时间范围、limit）
  - [ ] `GET /api/weight/{id}`
  - [ ] `PUT /api/weight/{id}`
  - [ ] `DELETE /api/weight/{id}`
  - [ ] 对应单元测试
- **目标版本：** v0.0.2

### Task-003 — Body 模块统计与导出
- **理由：** 数据需要可导出、可统计才算"数据优先"。
- **范围：**
  - [ ] 体重均值/趋势统计接口
  - [ ] CSV 导出
  - [ ] CSV 导入
- **目标版本：** v0.0.2

---

## 任务规范

新增任务时：
1. 分配下一个编号（如 Task-004）。
2. 在「任务状态总览」表格登记。
3. 在下方添加任务详情（目标、范围、约束、目标版本）。
4. 完成后更新 [CHANGELOG.md](./CHANGELOG.md)。
