FROM amazonlinux

WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r requirements.txt

COPY main.py .
COPY blackjack.py .

CMD [".venv/bin/python", "main.py"]