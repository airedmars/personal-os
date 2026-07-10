"""建表脚本:幂等创建 weight 表。

可在命令行直接运行 ``python -m app.db.init_db`` 手动建表;
应用启动时 lifespan 也会调用 :func:`init_db` 自动建表。
"""

from app.db.database import transaction


def init_db() -> None:
    """创建 weight 表(如已存在则跳过)。"""
    with transaction() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS weight (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                value FLOAT NOT NULL,
                date  TEXT    NOT NULL
            )
            """
        )


if __name__ == "__main__":
    init_db()
    print("数据库初始化完成。")
