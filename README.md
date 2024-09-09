# Travel Booking System

Welcome to the **Travel Booking System**, a Django-based application that allows users to filter and book various travel options easily.

This guide will walk you through setting up the project, running it locally, and troubleshooting common issues.

## Table of Contents
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Troubleshooting](#troubleshooting)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- Browse and filter travel options by destination, price, and availability.
- User-friendly booking interface.
- Admin panel for managing users, bookings, and travel listings.
- Secure login and registration for users.
- Integration with payment gateways (future version).

---

## Setup Instructions

### Prerequisites
Before setting up the project, make sure you have the following installed:
- Python (version 3.8 or higher)
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/travel-booking.git 
cd travel-booking
```

### Step 2: Create a Virtual Environment
A virtual environment helps isolate the dependencies for this project. Create one with the following command:

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment
Activate the virtual environment depending on your operating system:

- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

### Step 4: Install Dependencies
Once your virtual environment is activated, install the necessary packages by running:

```bash
pip install -r requirements.txt
```

### Step 5: Set Up the Database
First, open the `travel_booking/settings.py` file and locate the `DATABASES` configuration. Replace the `PASSWORD` field with your actual MySQL server password:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travel_booking_db',
        'USER': 'travel_user',
        'PASSWORD': 'YOUR_MYSQL_PASSWORD_HERE',  # Replace with your actual MySQL password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

After updating the password, set up the database by running the following migration command:
```bash
python manage.py migrate
```

### Step 6: Create a Superuser
To access the Django admin panel, create a superuser account:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up a username, email, and password.

### Step 7: Run the Development Server
Start the Django development server:

```bash
python manage.py runserver
```
You can now access the application in your browser at `http://localhost:8000`.

To access the admin dashboard, navigate to `http://localhost:8000/admin` and log in using the superuser credentials you created in Step 6.

## Troubleshooting

Here are some common issues you may encounter, along with their solutions:

- **Issue**: Packages not installing properly.

 - **Solution**: Ensure that your version of pip is up to date:
    ```bash
    pip install --upgrade pip
    ```

- **Issue**: Error: "No module named 'django'"

 - **Solution**: Make sure you have activated the virtual environment and installed the project dependencies.

- **Issue**: Database issues such as missing tables.

 - **Solution**: Run the following commands to fix database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

- **Issue**: Static files not loading properly.

 - **Solution**: Collect static files by running:
    ```bash
    python manage.py collectstatic
    ```

If you're still having trouble, consult the official [Django documentation](https://docs.djangoproject.com/en/5.1/) or open an issue in this repository.

## Running Tests

To ensure everything is functioning correctly, run the test suite with:
```bash
python manage.py test
```
This will execute the automated tests to verify the integrity of the system.