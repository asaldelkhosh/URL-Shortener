FROM python.3.10-alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3000

CMD python main.py