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

2. Create a virtual environment:
A virtual environment helps isolate the dependencies for this project. Create one with the following command:

```bash
python -m venv venv
```

3. Activate the virtual environment:
Activate the virtual environment depending on your operating system:

- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. Install Dependencies :
Once your virtual environment is activated, install the necessary packages by running:

```bash
pip install -r requirements.txt
```

5. Set up the database:
Set up the database by running the following migration command:
```bash
python manage.py migrate
```

6. Create a superuser:
To access the Django admin panel, create a superuser account:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up a username, email, and password.

7. Run the development server:
Start the Django development server:

```bash
python manage.py runserver
```
You can now access the application in your browser at `http://localhost:8000`.

## Troubleshooting

- If you encounter any package installation issues, make sure your pip is up to date:
```bash
pip install --upgrade pip
```


- If you get a "No module named 'django'" error, ensure you've activated your virtual environment and installed the requirements.

- For database-related issues, try:
```bash
python manage.py makemigrations
python manage.py migrate
```


- If you're having trouble with static files, run:
```bash
python manage.py collectstatic
```


- For any other issues, please check the Django documentation or open an issue in this repository.

## Running Tests

To run the tests, use the following command:
```bash
python manage.py test
```


## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.