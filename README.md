📁 Django FileManager App
A web-based file and folder management system built with Django, enabling users to create, organize, and manage files and directories through an intuitive interface.

🚀 Features
User authentication and authorization

Create, edit, and delete folders and files

Nested folder structure with parent-child relationships

File upload with size restrictions (10MB to 50MB)

Display file extensions and enable file previews/downloads

Responsive design for various devices

Dockerized setup for easy deployment
Stack Overflow
+1
Django Project
+1

🛠 Installation
Prerequisites
Python 3.8+

Poetry for dependency management

Docker and Docker Compose (optional, for containerized setup)

Clone the Repository
bash
Copy
Edit
git clone https://github.com/hosssein21/Django-FileManager-App.git
cd Django-FileManager-App
Using Poetry
bash
Copy
Edit
poetry install
poetry shell
Apply Migrations
bash
Copy
Edit
python manage.py migrate
Create Superuser
bash
Copy
Edit
python manage.py createsuperuser
Run the Development Server
bash
Copy
Edit
python manage.py runserver
Access the Application
Open your browser and navigate to http://127.0.0.1:8000/.

🐳 Docker Setup (Optional)
Ensure Docker and Docker Compose are installed.

bash
Copy
Edit
docker-compose up --build
The application will be available at http://localhost:8000/.

📂 Project Structure
plaintext
Copy
Edit
├── core/                 # Django project settings
├── dashboard/            # Main app for file and folder management
├── templates/            # HTML templates
├── static/               # Static files (CSS, JS)
├── media/                # Uploaded media files
├── dockerfiles/          # Docker-related configurations
├── docker-compose.yml    # Docker Compose configuration
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
⚙️ Configuration
Ensure the following settings are configured in core/settings.py:

python
Copy
Edit
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
Add 'dashboard' to the INSTALLED_APPS list.

🧪 Running Tests
To run the test suite:

bash
Copy
Edit
python manage.py test
📸 Screenshots
Include screenshots of the application's main features here.

🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

📬 Contact
For questions or suggestions, please open an issue on the GitHub repository.
