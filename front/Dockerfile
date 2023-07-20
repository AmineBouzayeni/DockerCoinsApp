FROM node:18.16.1-alpine

WORKDIR /project

COPY front/package*.json .

RUN npm install

COPY front/webui/ .

CMD [ "npm", "--srvname=redis" "start" ]