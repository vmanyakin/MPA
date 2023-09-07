FROM python:3.11.5

WORKDIR /app/MPA

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip && pip install -r requirements.txt
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y ffmpeg

COPY ./ ./

ENTRYPOINT ["python3","-m" ,"src.main"]