# FastAPI Verification Address App

This repository contains a FastAPI application for Verification Address App using a trained model. The application is containerized using Docker and can be easily built and deployed.

## Contents

- [Architecture](#architecture)
- [Usage](#usage)
  - [Building the Docker Image](#building-the-docker-image)
  - [Testing the Solution](#testing-the-solution)
  - [Verifying the Results](#verifying-the-results)
- [Datasets and Source Links](#datasets-and-source-links)
- [Contributing](#contributing)
- [Contact](#Contact)
- [Feedback](#Feedback)

## Architecture

The repository includes the following components:

- **Model Architecture Code**: The architecture of the sentiment analysis model is defined in the file `model_architecture.py`.
- **Server App Code**: The FastAPI application code is provided in the file `main.py`.
- **Docker Compose Configuration**: The `docker-compose.yml` file defines the services required to build and run the application in a Docker container.
- **Dockerfile**: The `Dockerfile` contains instructions for building the Docker image. Ensure that you have all necessary dependencies listed in `requirements.txt`.

## Usage

### Building the Docker Image

To build the Docker image, run the following command in the terminal:

```bash
docker-compose up --build
```
To Build the Docker container:

```
docker build -t add-nlp .
```

```
docker run -p 8000:8000 add-nlp
```
    
This command builds the image based on the provided Dockerfile and docker-compose.yml configuration.

### Testing the Solution
Once the Docker image is built, the FastAPI application will be accessible at http://localhost:8000/predict/. To test the solution:

Ensure the Docker containers are running.
Use your preferred tool (e.g., curl, Postman, or a web browser) to send POST requests to http://localhost:8000/predict/ with JSON payloads containing the text data you want to classify.

### Verifying the Results
To verify the results:
Compare the predictions from the FastAPI application with the expected outcomes.

## Datasets and Source Links
Dataset: The Address verification model is trained on the Cairo dataset that is collected from here API.


## Contributing

Contributions to this project are welcome! If you have ideas for improvements or bug fixes, please create an issue or submit a pull request.

## Contact

[<img alt="alt_text" width="30px" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Whatsapp2_colored_svg-512.png" />](https://wa.me/+201006491306)
&nbsp;&nbsp;
[<img alt="alt_text" width="30px" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-512.png" />](https://www.linkedin.com/in/bassem-ahmed-ahmed/)
&nbsp;&nbsp;
[<img alt="alt_text" width="30px" src="https://cdn4.iconfinder.com/data/icons/social-media-logos-6/512/112-gmail_email_mail-256.png" />](mailto:bassemahmed.am@gmail.com)
&nbsp;&nbsp;
[<img alt="alt_text" width="30px" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Facebook2_colored_svg-512.png" />](https://www.facebook.com/bassem.ahmed.7712/)


## Feedback

Can you please provide me with feedback on how I can improve myself and any ideas to improve the model, I am eager to receive any advice that can help me develop my skills.

&nbsp;&nbsp;
**Wish you a nice day :)**
