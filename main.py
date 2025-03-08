import logging
from app import app, logger

if __name__ == "__main__":
    logger.info("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True)