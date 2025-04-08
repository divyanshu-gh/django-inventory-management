
# Django Inventory Management

This is a simple **Inventory Management System** built with **Django**. It allows users to manage their inventory, track stock levels, and view inventory details in a clean, user-friendly interface. The app supports basic CRUD operations (Create, Read, Update, Delete) for inventory items.

## Features

- **Add New Items**: Add items with details like name, category, price, and quantity.
- **View Inventory**: View a list of all inventory items with key details.
- **Edit Items**: Update inventory details like price, stock quantity, and category.
- **Delete Items**: Remove items from the inventory.
- **Low Stock Alerts**: Highlight items with low stock levels.
- **Simple UI**: Built with **Bootstrap** for a responsive, easy-to-use interface.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap)
- **Database**: SQLite (default), can be changed to PostgreSQL or MySQL
- **Hosting (optional)**: Can be deployed using platforms like **Heroku**, **AWS**, etc.

## Setup Instructions

### Prerequisites

Make sure you have the following installed:

- **Python** (version 3.8+)
- **Django** (can be installed via `pip install django`)
- **SQLite** (default database, no additional setup needed)

### Clone the Repository

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/divyanshu-gh/django-inventory-management.git
cd django-inventory-management
```

### Install Dependencies

Create a virtual environment (recommended) and install the required packages:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Set Up Database

Run the following commands to set up the database and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser (Optional)

If you want to access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your superuser.

### Run the Development Server

To run the app locally, use the following command:

```bash
python manage.py runserver
```

Open your browser and navigate to **http://127.0.0.1:8000/** to see the app in action.

### Access Django Admin Panel (Optional)

To access the Django admin panel, visit **http://127.0.0.1:8000/admin/** and log in with the superuser credentials you created earlier.

## Project Structure

```
django-inventory-management/
│
├── inventory/                # App for managing inventory
│   ├── migrations/           # Database migrations
│   ├── admin.py              # Register models for admin interface
│   ├── apps.py               # App configuration
│   ├── models.py             # Inventory item models
│   ├── views.py              # Views for CRUD operations
│   ├── urls.py               # URL routing for inventory app
│   ├── templates/            # HTML templates
│   └── forms.py              # Forms for adding/editing items
│
├── django_inventory_management/        # Project configuration
│   ├── __init__.py           # Package initialization
│   ├── settings.py           # Django settings
│   ├── urls.py               # Project URL routing
│   └── wsgi.py               # WSGI application
│
└── manage.py                 # Django management script
```

## Contributing

Feel free to fork this repository and submit pull requests for any features, bug fixes, or improvements.

### Issues

If you encounter any issues, feel free to create a GitHub issue in the repository.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
