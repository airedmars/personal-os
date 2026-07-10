"""Personal OS 后端入口。

启动时自动建表,然后挂载业务路由。
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import body
from app.db.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用启动:确保数据库与表已就绪。"""
    init_db()
    yield


app = FastAPI(title="Personal OS", version="0.1.0", lifespan=lifespan)
app.include_router(body.router)


@app.get("/")
def root() -> dict:
    """健康检查。"""
    return {"success": True, "service": "Personal OS"}
