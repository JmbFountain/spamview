FROM node:latest
RUN apt-get install -y git
RUN git clone https://github.com/carbon-app/carbon /carbon
RUN cd carbon
RUN npm i -g carbon-now-cli
RUN yarn
COPY ./run.sh /run.sh
CMD ["bash", "/run.sh"]
