from app.models import merchants
from app.database import database

async def create_merchant(data):
    query = merchants.insert().values(**data)
    return await database.execute(query)

async def get_merchants():
    query = merchants.select()
    return await database.fetch_all(query)

async def get_merchant_by_id(merchant_id: int):
    query = merchants.select().where(merchants.c.id == merchant_id)
    return await database.fetch_one(query)