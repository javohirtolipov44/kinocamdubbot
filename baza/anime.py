import aiosqlite
from baza.connect import DB_NAME

async def create_anime_table():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS anime (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                k_id TEXT,
                title TEXT,
                episod TEXT,
                hesh TEXT,
                message_id TEXT
            )
        """)
        await db.commit()

async def get_anime_by_hesh(hesh: str):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT k_id, message_id FROM anime WHERE hesh = ?",
            (hesh,)
        )
        return await cursor.fetchone()
        
async def get_anime_by_title(title):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            "SELECT k_id, message_id FROM anime WHERE title = ?",
            (title,)
        )
        return await cursor.fetchall()

async def add_anime(chanel_id, m_id, title, hesh):
    qism = 0
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO anime (k_id, title, episod, hesh, message_id) VALUES (?, ?, ?, ?, ?)",
            (chanel_id, title, qism, hesh, m_id)
        )
        await db.commit()