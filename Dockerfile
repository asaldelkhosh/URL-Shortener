# Start from the latest golang base image
FROM golang:alpine AS builder

# Set the Current Working Directory inside the container
WORKDIR /app

# Installing Git for alpine
RUN apk add --no-cache git

# Copy the source from the current directory to the Working Directory inside the container
COPY . .

# Build the Go app
WORKDIR /app/cmd/blue-sky

RUN go build -o /blue-sky

FROM alpine:latest

WORKDIR /app/

COPY --from=builder /blue-sky.

ENTRYPOINT ["./blue-sky"]