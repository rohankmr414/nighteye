# build env
FROM node:16-alpine as build

COPY . /project

WORKDIR /project

ENV API_URL=${API_URL}

ENV API_PORT=${API_PORT}

RUN npm ci

RUN npm run build

# production env
FROM nginx:stable-alpine

COPY --from=build /project/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]