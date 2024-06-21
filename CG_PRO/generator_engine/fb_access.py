import os
from dotenv import load_dotenv
from firebase_admin import credentials, firestore, storage, initialize_app

load_dotenv()

# get the service key  from the environ variables

service_key_path = os.getenv("SERVICE_KEY_PATH")
if not service_key_path:
    raise EnvironmentError("SERVICE KEY PATH IS NOT SENT IN THE ENVIRONMENT VARIABLE IN FB ACCESS")

# Initialize the Firebase app
cred = credentials.Certificate(service_key_path)

firebase_app = initialize_app(cred, {
    'storageBucket': 'certificate-generator-bd0ba.appspot.com'
})

# Get a Firestore client
db = firestore.client()

# Get a Storage bucket client
bucket = storage.bucket()

# Expose the initialized resources
__all__ = ['firebase_app', 'db', 'bucket']
