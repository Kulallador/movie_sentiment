FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN python3 -m nltk.downloader wordnet
# RUN unzip /root/nltk_data/corpora/wordnet.zip -d /root/nltk_data/corpora/

ENTRYPOINT ["python"]
CMD ["backend/manage.py", "runserver", "0.0.0.0:8000"]