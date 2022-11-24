FROM python:3
WORKDIR /app
COPY webapp/requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
WORKDIR ./webapp
CMD ["python", "app.py"]
