# Django ToDo Application

A simple ToDo web application built with Django. This app allows users to create, view, update, and delete tasks.

## Features

- Add new tasks
- List existing tasks
- Mark tasks as completed
- Delete tasks

## Requirements

- Python 3.x
- Django 5.x
- `python-dotenv` (for managing environment variables)

## Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/rohann-xd/todo-django.git
    cd todo-django
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    ```

    - **On Windows**:

      ```bash
      venv\Scripts\activate
      ```

    - **On macOS/Linux**:

      ```bash
      source venv/bin/activate
      ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file** in the root directory and add the following:

    ```bash
    SECRET_KEY='your-django-secret-key'
    DEBUG=True
    ```

    Replace `'your-django-secret-key'` with a secure key. You can generate a secret key using Django’s `django.core.management.utils.get_random_secret_key()` method.

5. **Apply database migrations**:

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser** (admin) to access the Django admin interface:

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

8. **Access the application** at `http://127.0.0.1:8000/`.

9. **Access the admin interface** at `http://127.0.0.1:8000/admin/` using the superuser credentials you created.

## Usage

- **Homepage**: View the list of tasks and manage them.
- **Admin Interface**: Use the Django admin dashboard to manage tasks and users.

## Contributing

1. **Fork the repository**.
2. **Create a new branch** for your changes.
3. **Make your changes** and test them.
4. **Submit a pull request** with a description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Django - A high-level Python web framework.
- Python - Programming language used for this project.
