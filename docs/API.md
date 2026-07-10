# API — 接口文档

> 后端：**FastAPI**
> 所有接口前缀：`/api`
> 数据格式：JSON
> 时间格式：ISO 8601 (UTC)

## 通用约定

### Base URL
```
http://localhost:8000/api
```

### 响应格式

**成功：**
```json
{ "data": "<结果>" }
```

**错误：**
```json
{ "detail": "<错误信息>" }
```

### 时间
- 输入 / 输出统一 ISO 8601 UTC，如 `2026-07-10T07:00:00Z`。

### 自动文档
FastAPI 自带交互式文档：
- Swagger UI：`http://localhost:8000/docs`
- ReDoc：`http://localhost:8000/redoc`

---

## Body 模块 — Weight API

### `POST /api/weight` ✅
记录一次体重测量。

**请求体：**
```json
{
  "weight": 72.5,
  "recorded_at": "2026-07-10T07:00:00Z",
  "note": "早晨空腹"
}
```

**响应 (201)：**
```json
{
  "data": {
    "id": 1,
    "weight": 72.5,
    "recorded_at": "2026-07-10T07:00:00Z",
    "note": "早晨空腹",
    "created_at": "2026-07-10T07:01:00Z"
  }
}
```

### `GET /api/weight` 🚧 (规划中)
获取体重记录列表，支持时间范围过滤。

**查询参数：**
| 参数 | 类型 | 说明 |
|------|------|------|
| `from` | ISO 8601 | 起始时间 |
| `to` | ISO 8601 | 结束时间 |
| `limit` | int | 返回条数 |

---

## 待实现接口 (Planned)

| 模块 | 端点 | 目标版本 |
|------|------|----------|
| Body | `GET /api/weight` | v0.0.2 |
| Body | `GET /api/weight/{id}` | v0.0.2 |
| Body | `PUT /api/weight/{id}` | v0.0.2 |
| Body | `DELETE /api/weight/{id}` | v0.0.2 |
| Body | `GET /api/weight/stats` | v0.0.2 |
| Work | `GET/POST /api/tasks` | v0.2.0 |
| Invest | `GET/POST /api/holdings` | v0.3.0 |
| Knowledge | `GET/POST /api/notes` | v0.4.0 |
