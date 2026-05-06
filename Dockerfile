FROM python:3.11-slim

WORKDIR /

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./app

ENV PYTHONPATH=/
CMD ["python", "-m", "app.main"]