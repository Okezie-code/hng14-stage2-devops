# --------- BUILD STAGE ---------
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .


# --------- FINAL STAGE ---------
FROM node:18-alpine

WORKDIR /app

RUN adduser -D appuser

COPY --from=builder /app /app

USER appuser

EXPOSE 3000

HEALTHCHECK CMD wget -qO- http://localhost:3000 || exit 1

CMD ["npm", "start"]
