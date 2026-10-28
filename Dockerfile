FROM python:3.11-slim
WORKDIR /app
RUN pip install flask
COPY app.py /app
COPY . .
CMD ["python" , "app.py"]
