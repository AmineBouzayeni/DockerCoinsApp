FROM node:18.16.1-alpine AS build


WORKDIR /src

COPY --chown=node:node package*.json webui/ ./

# Run: -npm ci works similarly to npm i, but skips the expensive dependency resolution step, and instead just installs the exact dependencies specified in your package-lock.json file. It’s basically a faster npm i for use in CI environments.
#      - lint to do some formatting tests 

RUN npm ci && \
    npm run lint ./webui.js

# Get rid of any development dependency
RUN npm prune --production


FROM node:18.16.1-alpine

WORKDIR /project

COPY --chown=node:node package.json webui/ ./

COPY --chown=node:node --from=build /src/node_modules ./node_modules

USER node

CMD [ "npm", "--srvname=redis", "start" ]