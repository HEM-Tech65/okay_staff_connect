# Okay Staff Connect

A Django-based staff portal application for managing staff connections and registrations.

## Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd okay_staff_connect
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```
   python manage.py migrate
   ```

5. (Optional) Create a superuser for admin access:
   ```
   python manage.py createsuperuser
   ```

## Running the Application

1. Ensure the virtual environment is activated.

2. Start the development server:
   ```
   python manage.py runserver
   ```

3. Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/` (if superuser created)
- Register new staff members through the portal interface
- View dashboard and manage staff connections

## Project Structure

- `core/`: Main Django project settings
- `portal/`: Staff portal app with models, views, and templates
- `db.sqlite3`: SQLite database file
- `manage.py`: Django management script

## Troubleshooting

- If you encounter database errors, try deleting `db.sqlite3` and running `python manage.py migrate` again.
- Ensure all dependencies are installed and virtual environment is activated.
- For production deployment, refer to Django's deployment documentation.