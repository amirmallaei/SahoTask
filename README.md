
# Django Project with Docker

This project is a simple Django application running inside Docker, including user authentication (login/logout), tracking user activities, and creating posts.

## Features

- User authentication (Login/Logout)
- Track user activities (Login, Logout, Post creation)
- Dockerized Django application

## Requirements

- Docker
- Docker Compose

## Setting Up the Project

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git git@github.com:amirmallaei/SahoTask.git
cd SahoTask
```

### 2. Build and Start Docker Containers

Build the Docker images and start the containers using `docker-compose`:

```bash
docker-compose up --build
```

This command will build the Docker images if necessary and start the containers.

### 3. Create Superuser

To create a superuser (admin user) for the Django admin interface, run the following command:

```bash
docker-compose exec app python manage.py createsuperuser
```

Follow the prompts to create the superuser.

### 4. Access the Application

Once the containers are up, you can access the Django application in your browser:

- **Application**: [http://127.0.0.1:8081](http://127.0.0.1:8081)
- **Admin Panel**: [http://127.0.0.1:8081/admin](http://127.0.0.1:8081/admin) (login with the superuser credentials you created)

## Authentication

### Login and Logout

1. **Login URL**: [http://127.0.0.1:8081/accounts/login/](http://127.0.0.1:8081/accounts/login/)
2. **Logout URL**: [http://127.0.0.1:8081/accounts/logout/](http://127.0.0.1:8081/accounts/logout/)

You can log in and log out using the default Django authentication views, or use the superuser credentials for accessing the admin panel.

### View User Activities

Once logged in, you can view the last 10 activities performed by the logged-in user. The activities include login, logout, and post creation actions.

- **User Activities**: [http://127.0.0.1:8081/tracking/activity/](http://127.0.0.1:8081/tracking/activity/)

This page will show the last 10 user activities, including actions like `login`, `logout`, and `create_post`.

## Running the Project Without Docker

If you prefer to run the project locally without Docker, follow these steps:

1. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

2. **Run the Development Server**:

```bash
python manage.py runserver
```

Then access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).

3. **Create Superuser**:

```bash
python manage.py createsuperuser
```

4. **Migrate Database**:

If you haven't done so already, run migrations to set up the database:

```bash
python manage.py migrate
```

### Access the Admin Panel

Once you have created the superuser, access the admin panel at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and log in using the superuser credentials.

## Logs

To view logs for the Django application running inside Docker, you can use the following command:

```bash
docker-compose logs app
```

This will display the logs of the `app` container. You can use `-f` to follow the logs in real time:

```bash
docker-compose logs -f app
```

This is useful for debugging and monitoring the app's output.

## Stopping the Project

To stop the Docker containers, use:

```bash
docker-compose down
```

This will stop and remove the containers.

