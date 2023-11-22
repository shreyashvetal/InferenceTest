# Django E-commerce Project

This is a simple e-commerce system developed using Django. It includes features such as product listings, categories, user registration, authentication, and more.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your machine:

- Python (3.x recommended)
- Django
- Virtual environment (optional but recommended)

### Installing

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser (admin):

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

The project should now be running at http://127.0.0.1:8000/.

## Usage

- Visit the admin panel at http://127.0.0.1:8000/admin/ to manage products, categories, and other entities.
- Access the main application at http://127.0.0.1:8000/store/ to view and interact with the e-commerce system.
