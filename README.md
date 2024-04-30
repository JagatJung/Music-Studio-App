# Artist Records Admin Panel

This project is a simple admin panel designed to manage records of artists and their song collections. It provides basic CRUD (Create, Read, Update, Delete) functionalities for managing users, artists, and songs.

## Table of Contents

- [Technical Stack](#technical-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Technical Stack

- **Language:** Python
- **Framework:** Django
- **Frontend:** HTML, CSS (Tailwind CSS), JavaScript
- **Database:** MySQL (Relational Database)
- **ORM:** Raw SQL queries
- **API:** Django Views (Not RESTful)
- **UI Components:** DataTables

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/JagatJung/Music-Studio-App
    cd artist-records-admin-panel
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:

    - Ensure MySQL is installed and running.
    - Create a new database.
    - Configure the database settings in `settings.py`.

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

## Usage

1. Run the development server:

    ```bash
    python manage.py runserver
    ```

2. Navigate to `http://localhost:8000` in your web browser.

3. Register as a new admin user or log in with existing credentials.

## Features

- **User Management:**
    - List user records with pagination.
    - Create, update, and delete user records.

- **Artist Management:**
    - List artist records with pagination.
    - Create, update, and delete artist records.
    - Import and export artist records as CSV.
    - Manage songs associated with each artist:
        - List songs with pagination.
        - Create, update, and delete song records.

- **Authentication:**
    - Login screen for admin users with registration option.
    - Redirects to dashboard after successful login.


## Contributing

Contributions are welcome! Please feel free to open a pull request or create an issue for any bugs or feature requests.

## License

This project is licensed under the [MIT License](LICENSE).


