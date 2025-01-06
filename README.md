Django-based application that imports [Central Park Squirrel Census data](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/data) and allows for additions, updates, and views of squirrel data. 

Utilized sqlite3, Leaflet.js, html, css, bootstrap, and others via a Ubuntu VM on Google Cloud Platform.

[Check it out 🐿️](https://squirrel-tracker-7adff3577835.herokuapp.com/)

# SquirrelTracker

This guide will help you set up the project, run the app locally, and manage the database.

## Prerequisites

- Python 3.10 or above
- pip

## Setup Instructions

### 1. Create and Activate a Virtual Environment

Start by creating a virtual environment to manage dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:
- **On macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```
- **On Windows**:
  ```bash
  .\venv\Scripts\activate
  ```

### 2. Install Dependencies

Install the required packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Set Up the Database

Run the following commands to create and set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

**Check for Existing Migrations**:
   Ensure migration files exist in the `tracker/migrations/` directory. If they do not, create them using:
   ```bash
   python manage.py makemigrations tracker
   ```

### 4. Load Squirrel Data

Import squirrel data from the provided CSV file:

```bash
python manage.py import_squirrel_data tracker/data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv
```

### 5. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

By default, the app will be available at `http://127.0.0.1:8000/`.

## App Pages

The following pages are available:

- **Home Page**: `http://127.0.0.1:8000/`
- **Map**: `http://127.0.0.1:8000/map.html`
- **Sightings**: `http://127.0.0.1:8000/sightings.html`
- **Add Sighting**: `http://127.0.0.1:8000/sightings/add`
- **Statistics**: `http://127.0.0.1:8000/stats.html`

## Static Files

During development, Django serves static files automatically. If they don't load, ensure your `STATICFILES_DIRS` and `STATIC_URL` settings in `settings.py` are correct.

To collect static files for deployment, run:

```bash
python manage.py collectstatic
```

## Troubleshooting

- **Pages Not Displaying Correctly**: Check for template errors or misconfigurations in `urls.py` and `views.py`.
- **Verify Database**: Use the Django shell to inspect data:
  
  ```bash
  python manage.py shell
  ```