
from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore, storage
import os
import tempfile

# Initialize Flask app
app = Flask(__name__)

# Initialize Firebase using the service account key JSON file
try:
    cred = credentials.Certificate("Certificate-Generator\CG_PRO\serviceKey.json")
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'certificate-generator-bd0ba.appspot.com'
    })
    db = firestore.client()
    bucket = storage.bucket()
    print("Firebase initialized successfully.")
except Exception as e:
    print("Error initializing Firebase:", e)

@app.route('/')
def working_admin():
    return render_template('working_admin.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        cultural_name = request.form['culturalName']
        event_name = request.form['eventName']
        file = request.files['file']

        print(f"Received file: {file.filename} for cultural name: {cultural_name} and event name: {event_name}")

        # Check if collection exists for cultural name
        cultural_ref = db.collection(cultural_name)

        # Create a temporary file to upload
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            file.save(temp_file.name)
            temp_file.close()  # Ensure the file is closed before uploading
            print(f"Temporary file saved at: {temp_file.name}")

            # Create a unique filename for the image
            file_name = f"{cultural_name}_{event_name}.png"
            blob = bucket.blob(file_name)
            print(f"Uploading file to blob: {file_name}")
            blob.upload_from_filename(temp_file.name)

            # Make the blob publicly accessible
            blob.make_public()
            print(f"File uploaded successfully. Public URL: {blob.public_url}")

            # Get URL of the uploaded file
            file_url = blob.public_url

            # Set data for the document
            doc_data = {
                'image': file_url
            }

            # Add document to the collection with the event name as the document ID
            doc_ref = cultural_ref.document(event_name)
            doc_ref.set(doc_data)
            print(f"Document created in Firestore for event: {event_name}")

            # Delete the temporary file after uploading
            os.remove(temp_file.name)
            print(f"Temporary file deleted: {temp_file.name}")

        return redirect(url_for('working_admin'))

    except Exception as e:
        print("Error during upload:", e)
        return f"An error occurred during upload: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
