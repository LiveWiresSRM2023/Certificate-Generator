#
import firebase_admin
from firebase_admin import credentials, firestore, storage

# Initialize the Firebase app
# cred = credentials.Certificate('..//serviceKey.json')
cred = credentials.Certificate('C:\\Users\\Dev\\Desktop\\Certificate_gen_v1.3.9\\Certificate-Generator\\CG_PRO\\generator_engine\\serviceKey.json')

firebase_app = firebase_admin.initialize_app(cred, {
    'storageBucket': 'certificate-generator-bd0ba.appspot.com'
})

# Get a Firestore client
db = firestore.client()

# Get a Storage bucket client
bucket = storage.bucket()

# Expose the initialized resources
__all__ = ['firebase_app', 'db', 'bucket']
