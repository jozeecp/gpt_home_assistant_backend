import libs.utils as utils
from flask import Flask, jsonify, request
from functions.v1.requests.post.handler import handler as requests_post_handler

app = Flask(__name__)

logger = utils.get_logger(__name__, level="DEBUG")


@app.route("/api/v1/health", methods=["GET"])
def health():
    """Health check endpoint"""
    return jsonify({"status": "OK"}), 200


@app.route("/api/v1/requests", methods=["POST"])
def requests():
    """Requests endpoint"""

    # Call the handler function
    try:
        response = requests_post_handler(request)
    except Exception as e:
        logger.error(e)
        response = {"statusCode": 500, "body": {"error": str(e)}}

    return jsonify(response), response["statusCode"]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
