FROM python:3.10
COPY bot.py /app/bot.py
WORKDIR /app
CMD ["python", "bot.py"]
