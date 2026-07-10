"""SQLite 连接管理。

每个请求通过 :func:`get_conn` 拿到一个独立的、启用行工厂的连接,
用于上下文管理器中自动 commit/rollback/close。
"""

import os
import sqlite3
from contextlib import contextmanager

# 数据库文件放在 backend 目录下,与 app 包同级。
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "personal_os.db")


def get_conn() -> sqlite3.Connection:
    """返回一个启用 Row 工厂的 SQLite 连接。

    Row 工厂让结果行可以像字典一样按列名取值,
    方便后面转成 JSON 返回。
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@contextmanager
def transaction():
    """事务上下文管理器:进入拿连接,正常退出提交,异常回滚。

    用法::

        with transaction() as conn:
            conn.execute("INSERT INTO weight ...")
    """
    conn = get_conn()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
