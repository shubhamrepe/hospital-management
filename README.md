# Hospital Management Project

## Introduction

The Hospital Management Project is a Django web application that streamlines hospital operations, including patient management, appointments, and medical records.

## Features

- Patient registration and management
- Doctor and staff management
- Appointment scheduling and management
- Medical records and reports management
- Billing and payment management
- User authentication and authorization
- Dashboard for insights

## Installation

1. Clone the repository:
    ```shell
    git clone https://github.com/shubhamrepe/hospital-management.git
    ```

2. Create and activate a virtual environment:
    ```shell
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```shell
    pip install -r requirements.txt
    ```
4. Apply database migrations:
    ```shell
    python manage.py migrate
    ```
5. Create a superuser:
    ```shell
    python manage.py createsuperuser
    ```


## Usage

To start the server, run:
```shell
python manage.py runserver
