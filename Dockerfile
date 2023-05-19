FROM python:3.7-alpine
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
COPY . .
EXPOSE 5001
CMD ["python", "app.py"]