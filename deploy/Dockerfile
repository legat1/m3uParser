FROM python:3.7

# Create app directory
RUN mkdir -p /opt/m3u_parser
WORKDIR /opt/m3u_parser

# Bundle app source
COPY app .

#Install python additional packages
RUN pip3 install -r requirements.txt

EXPOSE 1785
CMD gunicorn -b :1785 app:app

