# app.py
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import uvicorn
from helper import get_recommendations
import os

app = FastAPI(title="Product Recommendation API")


class RecommendationRequest(BaseModel):
    product_index: int

@app.get("/")
def read_root():
    """
    Root endpoint that provides a welcome message and instructions on how to use the API.
    """
    welcome_message = (
        "Welcome to the Product Recommendation API!\n\n"
        "To get product recommendations, please use the `/recommendations` endpoint.\n\n"
        "For example, you can use Postman or curl to send a POST request:\n\n"
        "```\n"
        "curl -X POST \"http://0.0.0.0:8000/recommendations\" -H \"Content-Type: application/json\" -d '{\"product_index\": 49002}'\n"
        "```\n\n"
        "Replace `49002` with the product index for which you want recommendations. "
        "An example product is:\n\n"
        "- `10`: مسكره حواجب \n"
    )
    return {"message": welcome_message}
    
@app.post("/recommendations")
def recommend_products(request: RecommendationRequest):
    try:
        recommendations = get_recommendations(request.product_index)
        return recommendations.to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
