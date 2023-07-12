#!/usr/bin/with-contenv bashio

# start app with gunicorn

# Set the necessary environment variables
export FLASK_APP=app
export FLASK_ENV=production

# Start the Flask app with Unicorn
gunicorn app:app