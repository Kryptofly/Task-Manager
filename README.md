# TaskManager

TaskManager is a simple Python-based web application using Django that allows users to create, read, update, and delete tasks.

## Features

- Create new tasks.
- View all tasks.
- Edit existing tasks.
- Delete tasks.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/TaskManager.git
    cd TaskManager
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the application:
    ```bash
    python manage.py runserver
    ```

6. Open your web browser and go to `http://127.0.0.1:8000`.

## License

This project is licensed under the MIT License.
