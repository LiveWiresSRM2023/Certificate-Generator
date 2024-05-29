from firebase_admin import credentials, firestore, storage
import firebase_admin
from PIL import Image
import requests
from io import BytesIO

# Initialize Firebase using the service account key JSON file
cred = credentials.Certificate("Certificate-Generator\CG_PRO\serviceKey.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'certificate-generator-bd0ba.appspot.com' #your storage bucket url
})
db = firestore.client()
bucket = storage.bucket()

def retrieve_and_open_image(cultural_name, event_name):
    try:
        # Get the document from Firestore
        cultural_ref = db.collection(cultural_name)
        doc_ref = cultural_ref.document(event_name)
        doc = doc_ref.get()

        if doc.exists:
            image_url = doc.to_dict().get('image')
            if not image_url:
                raise Exception("Image URL not found in document.")
            print(f"Image URL retrieved: {image_url}")

            # Download the image using the URL
            response = requests.get(image_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            image_data = BytesIO(response.content)

            # Open the image using PIL
            image = Image.open(image_data)
            return image
        else:
            raise Exception("Document not found.")
    except Exception as e:
        print("Error retrieving and opening image:", e)
        return None

# Example usage
cultural_name = 'TechUtsav'
event_name = 'Quiz'
image = retrieve_and_open_image(cultural_name, event_name)
if image:
    image.show()  # This will display the image
