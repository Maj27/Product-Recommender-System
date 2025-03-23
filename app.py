# app.py
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
from helper import get_recommendations
import os

app = FastAPI(title="Product Recommendation API")


class RecommendationRequest(BaseModel):
    product_index: int

@app.get("/", response_class=HTMLResponse)
def read_root():
    """
    Root endpoint that provides a welcome message and instructions on how to use the API.
    """
    html_content = """
    <html>
        <head>
            <title>Welcome to the Product Recommendation API</title>
        </head>
        <body>
            <h1>Welcome to the Product Recommendation API!</h1>
            <p>To get product recommendations, please use the <code>/recommendations</code> endpoint.</p>
            <p>For example, you can use Postman or <code>curl</code> to send a POST request:</p>
            <pre><code>curl -X POST "http://0.0.0.0:8000/recommendations" -H "Content-Type: application/json" -d '{"product_index": 49002}'</code></pre>
            <p>Replace <code>49002</code> with the product index for which you want recommendations. An example product is:</p>
            <ul>
                <li><code>49002</code>: تيشيرت ليفربول الاساسي</li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
    
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
