FROM python:3.11-rc-buster
WORKDIR /bot
COPY . .
RUN apt-get update && apt-get install ffmpeg -y
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "discord_bot/main.py"]
