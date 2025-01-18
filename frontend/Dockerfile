FROM node:12-slim

ENV NODE_PATH=/srv/app/node_modules
WORKDIR /srv/app
COPY yarn.lock package.json ./

RUN set -ex; \
    yarn install --no-cache --frozen-lockfile; \

COPY . /srv/app

EXPOSE 3000
EXPOSE 35729

CMD ["yarn", "run", "start"]