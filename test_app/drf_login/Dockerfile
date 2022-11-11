FROM python:latest
WORKDIR /code

COPY requirements.txt .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "uvicorn", "drf_login.asgi:application", "--host", "0.0.0.0", "--port", "7777"]