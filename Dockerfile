FROM python:3.8

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/scraper.py /

CMD [ "python", "./scraper.py" ]