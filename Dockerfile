FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV SECRET_KEY="key"
# RUN python backend/manage.py runserver
# CD backend/

# ENTRYPOINT ["python"]
# CMD ["backend/manage.py", "runserver"]