# FastAPI Sentiment Analysis App

This repository contains a FastAPI application for sentiment analysis using a pre-trained model. The application is containerized using Docker and can be easily built and deployed.

## Contents

- [Architecture](#architecture)
- [Usage](#usage)
  - [Building the Docker Image](#building-the-docker-image)
  - [Testing the Solution](#testing-the-solution)
  - [Verifying the Results](#verifying-the-results)
- [Datasets and Source Links](#datasets-and-source-links)

## Architecture

The repository includes the following components:

- **Model Architecture Code**: The architecture of the sentiment analysis model is defined in the file `model_architecture.py`.
- **Server App Code**: The FastAPI application code is provided in the file `filename.py`. Please replace `filename` with the actual name of your file.
- **Docker Compose Configuration**: The `docker-compose.yml` file defines the services required to build and run the application in a Docker container.
- **Dockerfile**: The `Dockerfile` contains instructions for building the Docker image. Ensure that you have all necessary dependencies listed in `requirements.txt`.

## Usage

### Building the Docker Image

To build the Docker image, run the following command in the terminal:

```bash
docker-compose up --build
```
This command builds the image based on the provided Dockerfile and docker-compose.yml configuration.

## Testing the Solution
Once the Docker image is built, the FastAPI application will be accessible at http://localhost:8000/predict/. To test the solution:

Ensure the Docker containers are running.
Use your preferred tool (e.g., curl, Postman, or a web browser) to send POST requests to http://localhost:8000/predict/ with JSON payloads containing the text data you want to classify.
## Verifying the Results
To verify the results:

Compare the predictions from the FastAPI application with expected outcomes.
Use the provided test script (test_script.py) to automate the testing process.
##  Datasets and Source Links
IMDb Dataset: The sentiment analysis model is trained on the IMDb dataset.
Dataset Link: IMDb Dataset
Additional Information
For any issues or improvements, please open an issue or pull request. Your contributions are welcome!
