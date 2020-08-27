FROM python:3.8

ADD src/scraper.py /

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

CMD [ "python", "./scraper.py" ]