import os
import json
import logging

def load_secrets():
    """
    Loads generic secrets from a JSON string provided via the 
    TRENDYTRACKER_SECRETS environment variable.
    """
    secrets_json = os.getenv("TRENDYTRACKER_SECRETS")
    if secrets_json:
        try:
            secrets = json.loads(secrets_json)
            for k, v in secrets.items():
                os.environ[k] = str(v)
            logging.info("Successfully loaded secrets from TRENDYTRACKER_SECRETS JSON.")
        except json.JSONDecodeError as e:
            logging.error(f"Failed to parse TRENDYTRACKER_SECRETS JSON payload: {e}")

# Automatically load secrets as soon as this module is imported.
load_secrets()
