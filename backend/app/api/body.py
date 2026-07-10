"""身体数据相关接口。

当前 MVP 只做体重的写入与查询。
"""

from datetime import datetime

from fastapi import APIRouter, Query

from app.db.database import transaction

router = APIRouter(prefix="/body", tags=["body"])


@router.post("/weight")
def add_weight(value: float = Query(..., description="体重(kg)")) -> dict:
    """添加一条体重记录,返回写入的值。"""
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with transaction() as conn:
        conn.execute(
            "INSERT INTO weight (value, date) VALUES (?, ?)",
            (value, date_str),
        )

    return {"success": True, "value": value}


@router.get("/weight")
def list_weight() -> dict:
    """返回全部体重记录(按 id 倒序,最新的在前)。"""
    with transaction() as conn:
        rows = conn.execute(
            "SELECT id, value, date FROM weight ORDER BY id DESC"
        ).fetchall()

    data = [{"id": row["id"], "value": row["value"], "date": row["date"]} for row in rows]
    return {"success": True, "data": data}
