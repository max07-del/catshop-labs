FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

RUN useradd --system app && mkdir /data && chown app /data
USER app

EXPOSE 8080
CMD ["python", "app.py"]