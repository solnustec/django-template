# @solnustec/django-template

First, you need to change the project name in the following files:

- `sonar-project.properties`
- `infrastructure/compose.yml`
- `local.yml`
- `README.md`

## Requirements

You need to install the following dependencies.

1. [Python](https://www.python.org/): the min version required is `3.10`

2. [Docker](https://docker.com): recommended in the latest version

3. [Git](https://git-scm.com/): recommended in the latest version

## Set-up

- Run `docker compose -f local.yml build` in the root directory. This going to install all
  the required packages.
- Run `docker compose -f local.yml up` to start the server on port `8080`
- Enjoy! 😊

If using the project's internal database, ensure PostgreSQL is up and running using Docker Compose:  

`docker compose -f infrastructure/compose.yml up -d`

If using an external database, this step is not necessary. Ensure the external database credentials are correctly configured in the `.env` file.




To configure the project, you must create an .env file by copying the provided `back.env` template:

```sh
cp back.env .env
```
Then, update the .env file with the following environment variables:

| Environment Variable          | Description                                                | Default Value           | Required |
| ----------------------------- | ---------------------------------------------------------- | ----------------------- | -------- |
| `DJANGO_SETTINGS_MODULE`      | Django settings module to load                            | `config.settings.local` | Yes      |
| `DATABASE_HOST`               | Database host                                             | `host.docker.internal`  | Yes      |
| `DATABASE_PORT`               | Database port                                             | `5454`                  | Yes      |
| `DATABASE_NAME`               | Name of the PostgreSQL database                           | `django-template-db`    | Yes      |
| `DATABASE_USER`               | Database username                                        | `postgres`              | Yes      |
| `DATABASE_PASSWORD`           | Database password                                        | `123456`                | Yes      |

## Running Tests & Code Formatting

Common commands for development tasks are available in the `Makefile`. To run them, use:

```sh
make <command>
```

### **Setup Commands**
These commands help manage Django's database migrations.

- `make migrations` → Create Django migrations.
- `make migrate` → Apply migrations.

### **Testing & Linting**
Commands for running tests and ensuring code quality.

- `make run-tests` → Run tests using `pytest` with database reuse.
- `make lint` → Format code using `black` and `isort`.
- `make lint-check` → Check code formatting without modifying files. Also runs `flake8` for linting.

### **Pre-Push Checks**
Ensure code quality and fix issues before pushing changes.

- `make pre-push-fix` → Auto-fix backend issues using predefined scripts.
- `make pre-push` → Run validation checks before pushing to GitHub.

