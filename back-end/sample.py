


#################MongoDB######################


from flask import Flask, request, jsonify
from pymongo import MongoClient
from gridfs import GridFS
from pdf2image import convert_from_bytes
import hashlib



# MongoDB configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['pdf_database']
fs = GridFS(db)

# Function to calculate the MD5 hash of a file's content
def calculate_hash(content):
    md5 = hashlib.md5()
    md5.update(content)
    return md5.hexdigest()

# Route for uploading PDF files for a specific customer
# @app.route('/upload/<customer_id>', methods=['POST'])
@app.route('/upload', methods=['POST'])

def upload_pdf(customer_id):
    try:
        # Check if customer collection exists, create it if not
        customer_collection = db[customer_id]
        
        # Check for duplicates by calculating the hash of the uploaded file's content
        pdf_file = request.files['file']
        pdf_content = pdf_file.read()
        pdf_hash = calculate_hash(pdf_content)
        
        if customer_collection.find_one({'hash': pdf_hash}):
            return jsonify({'message': 'Duplicate PDF file detected'}), 409
        
        # Insert the PDF file into GridFS
        file_id = fs.put(pdf_content, filename=pdf_file.filename)
        
        # Insert metadata into customer's collection
        metadata = {
            'filename': pdf_file.filename,
            'hash': pdf_hash,
            'file_id': file_id
        }
        customer_collection.insert_one(metadata)
        
        return jsonify({'message': 'PDF file uploaded successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
########################################MOngo db##############################







