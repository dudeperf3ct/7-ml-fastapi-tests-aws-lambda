# Sentiment Classification

In this project, we will deploy a sentiment analyser model using fastapi on AWS lambda using SAM with continuous delivery and publishing this container to a container registry that anyone can consume.

- Containerizing different components of projects
- Writing tests and testing individual modules using `pytest`
- Using [trunk](https://docs.trunk.io/) for automatic code checking, formatting and liniting
- Adding a Github actions for registring and publishing containzerized fastapi app to Github Container Registry
- Using the published package and deploy SAM

## Run

### Locally

- Sentiment Model

```bash
cd sentiment
docker build -t sentiment -f Dockerfile.t .
cd ..
docker run --rm -it -v $(pwd):/app sentiment bash
python3 sentiment/model.py
pytest --cov tests/test_sentiment_model.py
```

- Fastapi

> Note: To run `pytest` replace `requirements-fastapi.txt` with `requirements-dev.txt` in `Dockerfile`

```bash
docker build -t sentiment -f Dockerfile.fastapi .
docker run --rm -it -v $(pwd):/app -p 8000:8000 sentiment bash
uvicorn main:app --host=0.0.0.0
pytest --cov tests/test_fastapi.py
```

- AWS Lamda and SAM [Not working yet!]

Prerequisties: Install and configure aws cli, Install sam cli. [Guide](https://vinaykachare.medium.com/serverless-api-with-aws-sam-fastapi-3f4d9510d6b6)

Once the github actions runs successfully, our lambda function is packaged and published on Github Container Registry. To build your serverless application use `sam build` with option of [Building a .zip file archive](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-build.html) using container image from Github Container Registry.

```bash
sam build --use-container --build-image ghcr.io/dudeperf3ct/fastapi-distilbert:latest
sam local invoke  # test locally before deploying
sam deploy --guided # deploy
```

- Exercises

1. Another approach would be to write a github action to publish the package at AWS ECR and the deploy by following steps above.
2. Yet another approach would be to directly build a SAM application using `Dockerfile` only whtithout registring any containers.
3. A different approach would be just using python files that would require changing `template.yaml` file accordingly.
