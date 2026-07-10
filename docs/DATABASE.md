# Database — 数据库设计

> 数据库：**SQLite**（单文件存储）
> 原则：单库、少表、字段清晰、可长期迁移。

## 设计原则

1. **一个 `.db` 文件** — 不分库，模块用表名前缀区分（如 `body_weight`）。
2. **时间用 ISO 8601 UTC** — 存储为 `TEXT`，查询时转本地时区展示。
3. **主键** — 默认 `INTEGER PRIMARY KEY AUTOINCREMENT`。
4. **schema 变更走迁移** — 不手动改库，保留向后兼容。
5. **数据可导出** — 关键数据支持 CSV 导出，避免被系统锁定。

## 表命名约定

```
<module>_<entity>
```

| 模块前缀 | 示例 |
|----------|------|
| `body_` | body_weight, body_sleep |
| `work_` | work_task, work_project |
| `invest_` | invest_holding, invest_trade |
| `knowledge_` | knowledge_note, knowledge_tag |

---

## 当前表（v0.0.1）

### `body_weight` — 体重记录 ✅

身体模块的核心表，记录每次体重测量。

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | INTEGER PK | 自增主键 |
| `weight` | REAL | 体重 (kg) |
| `recorded_at` | TEXT | 测量时间 (ISO 8601 UTC) |
| `note` | TEXT | 备注（可选） |
| `created_at` | TEXT | 记录创建时间 |

**建表语句（参考）：**
```sql
CREATE TABLE body_weight (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    weight      REAL    NOT NULL,
    recorded_at TEXT    NOT NULL,
    note        TEXT,
    created_at  TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
);
```

**示例数据：**

| id | weight | recorded_at | note |
|----|--------|-------------|------|
| 1 | 72.5 | 2026-07-10T07:00:00Z | 早晨空腹 |

---

## 规划表 (Planned)

### Body 模块
- `body_sleep` — 睡眠记录
- `body_exercise` — 运动记录

### Work 模块
- `work_task` — 任务
- `work_project` — 项目

### Investment 模块
- `invest_holding` — 持仓
- `invest_trade` — 交易流水

### Knowledge 模块
- `knowledge_note` — 笔记
- `knowledge_tag` — 标签

---

## 迁移策略

- 每次表结构变更编写迁移脚本，存放于 `backend/migrations/`。
- 迁移脚本顺序执行，记录版本号。
- 不破坏旧数据；新增字段给默认值。

## 备份

- SQLite 单文件可直接复制备份。
- 建议定期导出 CSV 作为离线副本。
