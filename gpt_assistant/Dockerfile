ARG BUILD_FROM=arm64v8/alpine:3.18.2
FROM $BUILD_FROM

WORKDIR /app

COPY . ./

# Install Python, pip, rust, cargo and dependencies
RUN apk add --no-cache python3 py3-pip rust cargo && pip3 install -r requirements.txt

CMD [ "/run.sh" ]
