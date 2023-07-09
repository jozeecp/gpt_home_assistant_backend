ARG BUILD_FROM=ghcr.io/hassio-addons/base:14.0.1
FROM $BUILD_FROM

WORKDIR /app

COPY . ./

# Install dependencies
RUN pip install -r requirements.txt

CMD [ "/run.sh" ]