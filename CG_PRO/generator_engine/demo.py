import os
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from dotenv import load_dotenv
import json

# Load environment variables from the .env file
load_dotenv()

# Use environment variables for sensitive data and configurations
FONT_FILE_PATH = os.getenv('FONT_FILE_PATH')
SERVICE_KEY_PATH = os.getenv('SERVICE_KEY_JSON')
service_key_json = json.loads(SERVICE_KEY_PATH)

# Ensure environment variables are loaded
if not FONT_FILE_PATH:
    raise EnvironmentError("FONT_FILE_PATH is not set in the environment variables.")
if not SERVICE_KEY_PATH:
    raise EnvironmentError("SERVICE_KEY_PATH is not set in the environment variables.")

from fb_access import db

class RetrieveTemplate:
    def __init__(self):
        pass

    def url(self, c_name, e_name):
        try:
            # Get the document from Firestore
            cultural_ref = db.collection(c_name)
            doc_ref = cultural_ref.document(e_name)
            doc = doc_ref.get()

            if doc.exists:
                image_url = doc.to_dict().get('image')
                if not image_url:
                    raise Exception("Image URL not found in document.")
                print(f"Image URL retrieved: {image_url}")
                return image_url
            else:
                raise Exception("Document not found.")
        except Exception as e:
            print("Error retrieving image URL:", e)
            return None

class gen_engine:
    def __init__(self, font_path=None):
        if font_path is None:
            font_path = FONT_FILE_PATH
        self.font_path = font_path
        self.font_size = 61
        self.font_color = "#023047"

        # Check if the font file exists
        if not os.path.exists(self.font_path):
            raise FileNotFoundError(f"The font file {self.font_path} does not exist.")

        self.font = ImageFont.truetype(self.font_path, self.font_size)

    def generate(self, names, cultural_names, event_names):
        certificates = []  # Create an empty list to store certificates in memory (buffer)

        for i in range(min(len(names), len(cultural_names), len(event_names))):
            try:
                # Retrieve template URL
                rt = RetrieveTemplate()
                template_url = rt.url(cultural_names[i].lower(), event_names[i].lower())

                if not template_url:
                    raise ValueError("Template URL is None")

                # Fetch the template image from the URL
                response = requests.get(template_url)
                response.raise_for_status()  # Check if request was successful

                # Load the image
                template = Image.open(BytesIO(response.content))

                # Draw text on the image
                draw = ImageDraw.Draw(template)
                width, height = template.size
                text_length = draw.textlength(names[i], font=self.font)
                start_x = (width - text_length) // 2
                draw.text((start_x, (height - 251) // 2), names[i], fill=self.font_color, font=self.font)

                # Create a BytesIO object to store the certificate image in memory
                buffer = BytesIO()
                template.save(buffer, format=template.format)

                # Append the certificate image data to the certificates list
                certificates.append(buffer.getvalue())

                # Clear the buffer for memory efficiency
                buffer.seek(0)
                buffer.truncate()

                print(f"{names[i]}'s certificate is generated in memory!")
            except Exception as e:
                print(f"Error generating certificate for {names[i]}: {e}")

        return certificates  # Return the list of certificate image data

if __name__ == "__main__":
    # Example usage
    names = ["Alice", "Bob"]
    cultural_names = ["CultureA", "CultureB"]
    event_names = ["EventA", "EventB"]

    try:
        engine = gen_engine()
        certificates = engine.generate(names, cultural_names, event_names)
        # Further processing of certificates
    except Exception as e:
        print(f"An error occurred: {e}")
