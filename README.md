# Product Recommendation API
This repository contains a content-based product recommendation system that leverages textual features—specifically, product names—to generate personalized recommendations. The application is built using FastAPI, and the project is containerized using Docker for easy deployment. The repository includes helper scripts for preprocessing and feature extraction, as well as utility functions for tokenization/normalization.

## Files
- Salla Product Recommender System.ipynb

Notebook with all work rationale and steps
  
- app.py
  
The main API application file. It defines the API endpoints (e.g., /recommendations) and contains the logic to retrieve product recommendations based on input product indices.

- helper.py
  
Contains helper functions used throughout the project, such as functions for text preprocessing, feature extraction, or similarity calculations.

- locutfile.py
  
Provides additional utility function to perform stess test

- Dockerfile
  
Contains the instructions for containerizing the application. It installs all necessary dependencies, copies the project files, and starts the API server.

- requirements.txt
  
Lists all required Python packages with pinned versions to ensure reproducibility. 

## Getting Started
- Clone the Repository
  ```bash
  git clone https://github.com/Maj27/Product-Recommender-System.git
   cd Product-Recommender-System ```
   
- Install Dependencies
  
Install the required packages locally using:

``` bash pip install -r requirements.txt ```


- Running the Application Locally

Start the API by running:


python app.py
The API will be accessible at http://0.0.0.0:8000.

- Testing the API
You can test the /recommendations endpoint using a tool like curl or Postman. For example, send a POST request with the following JSON payload:


The API will return a list of recommended products.

- Docker Deployment
  
The application is containerized using Docker. To build and run the Docker image, follow these steps:

- Build the Docker Image:


 ``` bash docker build -t product-recommendation-api . ```


- Run the Docker Container:


``` bash docker run -p 8000:8000 product-recommendation-api ```

Your API will then be accessible at http://localhost:8000.

## Deployment Options
For a more permanent online deployment, consider using cloud platforms like AWS, Render, or Heroku. These services allow you to deploy your Docker container with minimal infrastructure management. For example, AWS Elastic Beanstalk or Render provide guides for containerized deployments.

## Limitations & Future Work
- Data Volume:
Due to memory constraints, only a subset of the available data may be used, which could limit the recommendation coverage.

- Feature Extraction:
The system currently uses TF-IDF for textual feature extraction. More advanced methods, such as Word2Vec or FastText, could capture deeper semantic relationships.

- Model Complexity:
A simple cosine similarity-based approach is used for recommendations. Future improvements could involve more sophisticated neural network models.

- Feature Scope:
The system only utilizes textual features (product names). Incorporating additional features like user interactions and metadata could enhance recommendation accuracy.
