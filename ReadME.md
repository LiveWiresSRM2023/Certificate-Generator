### Certificate Generator

Certificate Generator is a web application built using Flask for generating and managing event participation certificates. It includes features for user sign-up, sign-in, certificate generation, and Firebase integration for storing certificate templates.

## Folder Structure

The project folder structure is organized as follows:

Certificate-Generator/
│
├── CG_PRO/
│ ├── generator_engine/
│ │ ├── app.py
│ │ ├── demo.py
│ │ ├── fb_access.py
│ │ ├── fonts/
│ │ │ └── MontserratBold-p781R.otf
│ │ └── serviceKey.json
│ ├── static/
│ │ ├── css/
│ │ │ └── style.css
│ │ └── js/
│ │ └── script.js
│ ├── templates/
│ │ ├── admin.html
│ │ ├── errormessage.html
│ │ ├── index.html
│ │ ├── otp.html
│ │ ├── otpsuccess.html
│ │ ├── signin.html
│ │ ├── signup.html
│ │ └── successmessage.html
│ └── database.db
├── .env
├── README.md
└── requirements.txt

## Folder Descriptions:

    CG_PRO/: Main project directory.

    --> generator_engine/: Contains backend logic and Firebase integration.
    --> app.py: Flask application setup and routes.
    --> demo.py: Module for certificate generation logic.
    --> fb_access.py: Firebase access setup.
    --> fonts/: Directory for custom fonts used in certificates.
    --> serviceKey.json: Firebase service key for authentication.
    --> static/: Static assets (CSS, JS) used in the web application.
    --> templates/: HTML templates used to render web pages.
    --> database.db: SQLite database file for storing user and event data.
    --> .env: Configuration file for environment variables (e.g., Firebase credentials).

    --> README.md: This file, providing an overview of the project.

## Features:

    --> User Management: Sign-up, sign-in, and user dashboard functionality.
    --> Certificate Generation: Dynamically generates certificates based on event and participant data.
    --> Firebase Integration: Stores certificate templates and manages file uploads.
    --> SQLite Database: Stores user data and event information.
