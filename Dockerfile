FROM python:3.13

WORKDIR /client

COPY ./requirements.txt /client/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /client/requirements.txt

COPY ./app /client/app

ENV GRADIO_SERVER_NAME="0.0.0.0"

EXPOSE 7860

CMD ["python", "app/main.py"]
