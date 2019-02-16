
import os
# DEBUG has to be to False in a production enrironment for security reasons
DEBUG = True
print('environ:', os.environ)
CONSUMER_KEY = os.environ.get('CONSUMER_KEY', '')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET', '')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', '')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET', '')
if not ACCESS_TOKEN_SECRET:
    raise ValueError("No secret key set for Flask application")
APP_DIR  = os.path.dirname(__file__)
LOG_PATH = os.path.join(APP_DIR, 'twitter.log')