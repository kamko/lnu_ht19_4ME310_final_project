FROM node:12.14.0-buster-slim AS builder

WORKDIR /app

COPY . .

RUN npm install && npm run build:prod

FROM nginx:1.17.6

COPY --from=builder /app/dist/ /usr/share/nginx/html/
