ARG BUILD_FROM=ghcr.io/hassio-addons/base:14.0.1
FROM $BUILD_FROM

WORKDIR /app

COPY . ./

# Install Python, pip and dependencies
RUN apk add --no-cache python3 py3-pip && pip3 install -r requirements.txt

CMD [ "/run.sh" ]