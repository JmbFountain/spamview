FROM debian:latest
RUN apt-get update -y
RUN apt-get install python3 python3-pip tar wget -y
COPY ./requirements.txt /requirements.txt
COPY ./install_gecko_drivers /install_gecko_drivers
RUN pip3 install -r /requirements.txt
RUN bash /install_gecko_drivers
ENV FLASK_APP="/app/app.py"
CMD ["flask", "run"]
