FROM python:latest

WORKDIR /home/pi/server/cryptobot

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./bot.py"]

