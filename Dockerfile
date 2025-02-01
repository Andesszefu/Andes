FROM python:3.10

WORKDIR /app

COPY . .  # Kopiuje wszystkie pliki do kontenera

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot.py"]
