FROM node:18.16.1-alpine AS build

WORKDIR /src

COPY package*.json ./

#npm ci works similarly to npm i, but skips the expensive dependency resolution step, and instead just installs the exact dependencies specified in your package-lock.json file. It’s basically a faster npm i for use in CI environments.

RUN npm ci

COPY webui/ ./

# Run some formatting tests on the code

RUN npm run lint ./webui.js

# Get rid of any development dependency
RUN npm prune --production


# FROM node:18.16.1-alpine

# WORKDIR /project

# RUN npm run build

FROM node:18.16.1-alpine 

WORKDIR /project

COPY package.json ./

COPY --from=build /src/node_modules ./node_modules

COPY webui/ ./

USER node

CMD [ "npm", "--srvname=redis", "start" ]