# Personal OS - Backend

最小可运行版本(MVP),仅实现体重记录的写入与查询闭环。

## 技术栈

- Python + FastAPI
- SQLite(本地文件 `personal_os.db`,自动生成)
- 原生 `sqlite3`,不使用 ORM

## 目录结构

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI 入口,启动时建表
│   ├── api/
│   │   ├── __init__.py
│   │   └── body.py      # /body/weight 接口
│   └── db/
│       ├── __init__.py
│       ├── database.py  # 连接管理 + 事务上下文
│       └── init_db.py   # 建表脚本
├── requirements.txt
└── personal_os.db       # 运行后自动生成
```

## 安装与运行

```bash
cd backend
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux
pip install -r requirements.txt

uvicorn app.main:app --reload
```

## API

### 添加体重

```
POST /body/weight?value=77.2
```

```json
{ "success": true, "value": 77.2 }
```

### 获取体重列表

```
GET /body/weight
```

```json
{
  "success": true,
  "data": [
    { "id": 1, "value": 77.2, "date": "2026-07-04 10:00:00" }
  ]
}
```

## 数据结构

表 `weight`:

| 字段  | 类型    | 说明                |
| ----- | ------- | ------------------- |
| id    | integer | 主键,自增          |
| value | float   | 体重(kg)          |
| date  | text    | 记录时间字符串      |
