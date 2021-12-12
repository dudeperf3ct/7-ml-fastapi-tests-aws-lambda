# Sentiment Classification

In this project, we will deploy a sentiment analyser model using fastapi on AWS lambda using continuous delivery and publishing this container to a container registry that anyone can consume.

- Containerizing different components of projects
- Writing tests and testing individual modules
- Using [trunk](https://docs.trunk.io/) for automatic code checking, formatting and liniting
- Adding a Github actions for registring and publishing containzerized fastapi app to github container registry
- Deploying fastapi app as a lambda function on AWS

## Run

### Locally

- Sentiment Model

```bash
cd sentiment
docker build -t sentiment .
cd ..
docker run --rm -it -v $(pwd):/app sentiment bash
python3 sentiment/model.py
pytest --cov test/test_sentiment_model.py
```

- Fastapi

> Note: To run `pytest` replace `requirements.txt` with `requirements-dev.txt` in `Dockerfile`

```bash
docker build -t sentiment .
docker run --rm -it -v $(pwd):/app -p 8000:8000 sentiment bash
uvicorn app:app --host=0.0.0.0
pytest --cov test/test_fastapi.py
```
