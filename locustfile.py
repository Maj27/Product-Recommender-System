from locust import HttpUser, task, between

class RecommendationUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def get_recommendations(self):
        # Simulate a request with a random product index, e.g., 0 to len(df)-1
        self.client.post("/recommendations", json={"product_index": 5})

# To run: locust -f locustfile.py --host=http://localhost:8000
