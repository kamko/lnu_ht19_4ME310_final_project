FROM node:12.14.0-buster-slim AS builder

WORKDIR /app

COPY . .

RUN npm install && npm run build:prod

FROM garwan/spa-server:0.2.2

COPY --from=builder /app/dist/ /www/
