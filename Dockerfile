FROM python:3.10

WORKDIR /app

COPY requirements.txt .  # Najpierw kopiujemy plik zależności
RUN pip install --no-cache-dir -r requirements.txt

COPY . .  # Dopiero potem kopiujemy resztę plików

CMD ["python", "bot.py"]
