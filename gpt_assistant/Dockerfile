ARG BUILD_FROM=arm32v7/alpine:3.18.2
FROM $BUILD_FROM

WORKDIR /app

COPY . ./

# Install Python, pip and dependencies
RUN apk add --no-cache python3 py3-pip && pip3 install -r requirements.txt

CMD [ "/run.sh" ]