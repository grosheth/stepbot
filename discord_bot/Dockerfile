FROM python:3.11-rc-buster
WORKDIR /bot
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"] 
