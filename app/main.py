from fastapi import FastAPI, BackgroundTasks
from app import database, crud
from pydantic import BaseModel
from app.enrichment import enrich_merchant_data

app = FastAPI(title="Merchant Identity API")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def root():
    return {"message": "Merchant Identity API is running"}


class MerchantCreate(BaseModel):
    name: str
    website: str
    address: str

@app.post("/merchants")
async def create_merchant_api(merchant: MerchantCreate, background_tasks: BackgroundTasks):
    merchant_data = merchant.dict()
    merchant_data.update({"verified_identity": False, "risk_score": 0, "high_risk": False})
    merchant_id = await crud.create_merchant(merchant_data)
    
    # Add merchant id to the dict so enrichment knows it
    merchant_data["id"] = merchant_id
    
    background_tasks.add_task(enrich_merchant_data, merchant_data)

    return {"id": merchant_id, **merchant_data}

@app.get("/merchants")
async def list_merchants():
    return await crud.get_merchants()

@app.get("/merchants/{merchant_id}")
async def get_merchant(merchant_id: int):
    merchant = await crud.get_merchant_by_id(merchant_id)
    if merchant:
        return merchant
    return {"error": "Merchant not found"}