FROM python:3.10-alpine

WORKDIR /sai/src/exam8

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./

CMD ["python", "main.py"]
