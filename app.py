# app.py
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import uvicorn
from helper import get_recommendations


app = FastAPI(title="Product Recommendation API")


class RecommendationRequest(BaseModel):
    product_index: int

@app.post("/recommendations")
def recommend_products(request: RecommendationRequest):
    try:
        recommendations = get_recommendations(request.product_index)
        return recommendations.to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
