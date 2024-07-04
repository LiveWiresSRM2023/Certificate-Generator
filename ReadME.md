### Certificate Generator

Certificate Generator is a web application built using Flask for generating and managing event participation certificates. It includes features for user sign-up, sign-in, certificate generation, and Firebase integration for storing certificate templates.

## Folder Structure

The project folder structure is organized as follows:

Certificate-Generator/


    
    ├── app.py
    
    ├── demo.py
    
    ├── fb_access.py
    
    ├── fonts/
    
        └── MontserratBold-p781R.otf
        
    ├── static/
    
    ├── css/
    
        │ └── admin.css
        
        │ └── index.css
    
        │ └── login.css
        
        │ └── user_dashboard.css
        
    ├── templates/
    
        ├── admin.html
        
        ├── errormessage.html
        
        ├── index.html
        
        ├── otp.html
        
        ├── otpsuccess.html
        
        ├── signin.html
        
        ├── signup.html
        
        └── successmessage.html
    
        
    └── database.db
    
    ├── README.md
    
    └── requirements.txt


## Folder Descriptions:


    --> app.py: Flask application setup and routes.
    --> demo.py: Module for certificate generation logic.
    --> fb_access.py: Firebase access setup.
    --> fonts/: Directory for custom fonts used in certificates.
    --> static/: Static assets (CSS) used in the web application.
    --> templates/: HTML templates used to render web pages.
    --> database.db: SQLite database file for storing user and event data.
    --> README.md: This file, providing an overview of the project.

## Features:

    --> User Management: Sign-up, sign-in, and user dashboard functionality.
    --> Certificate Generation: Dynamically generates certificates based on event and participant data.
    --> Firebase Integration: Stores certificate templates and manages file uploads.
    --> SQLite Database: Stores user data and event information





