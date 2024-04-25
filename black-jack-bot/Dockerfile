FROM amazonlinux

WORKDIR /app

COPY requirements.txt .

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r requirements.txt

COPY . .

CMD [".venv/bin/python", "main.py"]