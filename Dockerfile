FROM python:3.9

WORKDIR /app

RUN apt-get -y update && \
    apt-get install -y libgl1-mesa-glx && \
    apt-get clean

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["/bin/bash", "-c", "(uvicorn main:app --host 0.0.0.0 --port 8000 --reload)"]
