FROM public.ecr.aws/lambda/python:3.8

COPY . ./

RUN pip3 install -r requirements-aws.txt

CMD [ "app.handler"]