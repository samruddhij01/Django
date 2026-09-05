# Talent Register App

A Django-based web application for managing talent/user records. Users can register, log in, view and update their information, and delete their profile — all through a simple, secure interface.

## Features

- **User Registration** – New users can create an account by providing their details.
- **Login** – Registered users can securely log in using their credentials.
- **Logout** – Users can safely log out of their session.
- **Update Information** – Logged-in users can edit and update their profile details.
- **Delete Information** – Users can delete their profile/record when no longer needed.

## Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite3
- **Frontend:** HTML, CSS (Django Templates)

## Project Structure

```
Django/
├── myapp/         # Main application logic
├── mypro/         # Project configuration
├── db.sqlite3     # SQLite database
├── manage.py      # Django management script
└── .gitattributes
```

## Getting Started

### Prerequisites

- Python 3.x installed
- pip (Python package manager)

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/samruddhij01/Django.git
   cd Django
   ```

2. Install dependencies
   ```bash
   pip install django
   ```

3. Apply migrations
   ```bash
   python manage.py migrate
   ```

4. Run the development server
   ```bash
   python manage.py runserver
   ```

5. Open your browser and go to
   ```
   http://127.0.0.1:8000/
   ```

## Usage

1. **Register** a new account from the registration page.
2. **Login** with your registered credentials.
3. View and **update** your saved information anytime.
4. **Delete** your record if you wish to remove it.
5. **Logout** securely when done.

## Future Improvements

- Add password reset/forgot password functionality
- Add email verification during registration
- Improve UI with better styling (Bootstrap/Tailwind)
- Add search and filter for talent records

## Author

**Samruddhi Jadhav**

## License

This project is open source and available for personal and educational use.
