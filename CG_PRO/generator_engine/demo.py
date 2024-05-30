

import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import os
from firebase_admin import credentials, firestore, storage
import firebase_admin
from PIL import Image
import requests
from io import BytesIO
import sys
sys.path.append(os.path.abspath('C:\\Users\\Dev\\Desktop\\CG_PRO_V1.4\\Certificate-Generator\\CG_PRO\\'))
from generator_engine.fb_access import db





class retrive_template:
    def __init__(self):
        pass

    
    def url(self,cultural_name, event_name):
        
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
                return image_url
            else:
                raise Exception("Document not found.")
        except Exception as e:
            print("Error retrieving and opening image:", e)
            return None
    



 












class gen_engine:
    def __init__(self, font_path="..//CG_PRO//generator_engine//fonts//GreatVibes-Regular.ttf"):
        self.font_path = font_path
        self.font_size = 180
        self.font_color = "#FFFFFF"

        # Check if the font file exists
        if not os.path.exists(self.font_path):
            raise FileNotFoundError(f"The font file {self.font_path} does not exist.")

        self.font = ImageFont.truetype(self.font_path, self.font_size)

    def generate(self, names=['Devan'],cultural_name='TechUtsav',event_name='Quiz', output_dir='../CG_PRO/generator_engine/certif_img'):
        rt=retrive_template()
        cultural_name = 'TechUtsav'
        event_name = 'Quiz'
        template_url=rt.url(cultural_name,event_name)

        # df = pd.DataFrame(names)

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        

        def generate_certificate(name):
            try:
                # Fetch the template image from the URL
                response = requests.get(template_url)
                response.raise_for_status()  # Check if the request was successful
                template = Image.open(BytesIO(response.content))

                draw = ImageDraw.Draw(template)
                width, height = template.size
                length = self.font.getlength(name)
                start_x = (width - length) // 2
                draw.text((start_x, (height - 250) // 2), name, fill=self.font_color, font=self.font)

                # Construct the output path
                output_path = os.path.join(output_dir, f'{name}.png')
                template.save(output_path)

                print(f"{name}'s certificate is generated at {output_path}!")
                return "Completed"
            except Exception as e:
                print(f"Error generating certificate for {name}: {e}")
                return f"Error: {e}"

        # Generate certificates for all names in the DataFrame
        for name in names:
            generate_certificate(name)

        print("All certificates have been generated.")


    # def initialize_firebase(self):
        # try:
        #         cred = credentials.Certificate("..//CG_PRO//serviceKey.json")
                
        #         firebase_admin.initialize_app(cred, {'storageBucket': 'certificate-generator-bd0ba.appspot.com'})
        #         db = firestore.client()
        #         bucket = storage.bucket()
        #         print("Firebase initialized successfully.")
        #         return db, bucket
        # except Exception as e:
        #     print("Error initializing Firebase:", e)
        #     return None, None



# Usage example

# cultural_name = 'TechUtsav'
# event_name = 'Quiz'

# rt=retrieving.retrive_template()
# img,img_url=rt.url(cultural_name,event_name)

# engine = gen_engine()
# engine.generate()


# engine = retrive_template()
# db,bucket=engine.initialize_firebase()
# print(db)
# print('\n')
# print(bucket)



























# # Initialize Firebase using the service account key JSON file
# if not firebase_admin._apps:
#     cred = credentials.Certificate("..\\CG_PRO\\serviceKey.json")
#     firebase_admin.initialize_app(cred, {
#         'storageBucket': 'certificate-generator-bd0ba.appspot.com' #your storage bucket url
#     })
#     db = firestore.client()
#     bucket = storage.bucket()




    # def initialize_firebase(self):
    #     try:
    #             cred = credentials.Certificate("..//CG_PRO//serviceKey.json")
                
    #             firebase_admin.initialize_app(cred, {'storageBucket': 'certificate-generator-bd0ba.appspot.com'})
    #             db = firestore.client()
    #             bucket = storage.bucket()
    #             self.db=db
    #             self.bucket=bucket
    #             print("Firebase initialized successfully.")
    #             # return db, bucket
    #     except Exception as e:
    #         print("Error initializing Firebase:", e)
    #         return None, None
    # def retrive_db_bucket_FB(self):
    #     return self.db,self.bucket
        # return None, None