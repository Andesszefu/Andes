FROM python:3.10

WORKDIR /app

# Skopiuj pliki wymagane do działania
COPY bot.py .
COPY requirements.txt .

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Uruchom bota
CMD ["python", "bot.py"]
