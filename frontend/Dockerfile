FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package.json .
RUN npm install

# Copy app code
COPY . .

# Create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Expose port
EXPOSE 3000

# Healthcheck
HEALTHCHECK CMD wget --spider http://localhost:3000 || exit 1

# Start app
CMD ["node", "app.js"]
