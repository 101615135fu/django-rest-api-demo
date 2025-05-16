FROM python:3.10-slim

WORKDIR /app

COPY . .

# 安装系统依赖 + Python 依赖
RUN apt-get update && \
    apt-get install -y gcc build-essential && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
