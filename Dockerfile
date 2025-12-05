FROM python:3.9-slim
WORKDIR /app

# 1. Copy requirements FIRST
COPY requirements.txt .

# 2. Install dependencies SECOND
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy app code THIRD
COPY . .

CMD ["python", "app.py"]