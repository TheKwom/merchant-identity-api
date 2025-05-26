import random
from app import crud

async def enrich_merchant_data(merchant):
    risk_score = random.randint(0, 100)
    high_risk = risk_score > 70

    updated_data = {
        "risk_score": risk_score,
        "high_risk": high_risk
    }

    await crud.update_merchant(merchant_id=merchant["id"], data=updated_data)

    print(f"Enriched merchant {merchant['name']} with risk score {risk_score} and high risk {high_risk}")
