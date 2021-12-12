# Sentiment Classification

In this project, we will deploy a sentiment analyser model using fastapi on AWS lambda using continuous delivery and publishing this container to a container registry that anyone can consume.

Following all best practices such as containerizing different components of projects, writing tests and testing individual modules, github actions for registring and publishing to github container registry.

## Run

### Locally

- Sentiment Model

```bash
cd sentiment
docker build -t sentiment .
cd ..
docker run --rm -it -v $(pwd):/app sentiment bash
cd sentiment
python3 model.py
cd ..
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
