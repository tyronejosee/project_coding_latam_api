# Coding Latam API

The JSON used as the database is located in [`app/data/db.py`](https://github.com/tyronejosee/project_coding_latam_api/blob/main/app/data/db.py)

## Requirements

- Python 3.8+

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone git@github.com:tyronejosee/project_coding_latam_api.git
```

### Virtual Environment Setup

It is recommended to create a virtual environment to isolate all the project dependencies:

```bash
# Linux
python3 -m venv env

# Windows
python -m venv env
```

Activate the virtual environment:

```bash
# Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Installing Dependencies

You can install the dependencies using `pip` or `Poetry`.

#### pip

```bash
pip install -r requirements.txt
```

#### Poetry

```bash
poetry install
```

## Running the Application

To run the application in development mode, use:

```bash
uvicorn app.main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

### API Documentation

Once the application is running, you can access the interactive documentation at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- Redoc: `http://127.0.0.1:8000/redoc`

## Deploy

### Example with Railway

Log in or sign up at [railway.app](https://railway.app/).

Select New on your dashboard and Deploy from GitHub repo:

![Example-01](/app/static/images/examples/01.png)

Configure and grant permission to the specific repositories for deployment:

![Example-02](/app/static/images/examples/02.png)
![Example-03](/app/static/images/examples/03.png)

Go to the Settings tab of the instance.

![Example-04](/app/static/images/examples/04.png)

Add the command `pip install -r requirements.txt` in the `Custom Build Command` field:

![Example-05](/app/static/images/examples/05.png)

Add the command `uvicorn app.main:app --host 0.0.0.0 --port $PORT` in the `Custom Start Command` field:

![Example-06](/app/static/images/examples/06.png)

After completing the Railway process, click on `Generate Domain` within `Settings`:

![Example-07](/app/static/images/examples/07.png)

And your API will be deployed successfully. 🎉🎉

![Example-08](/app/static/images/examples/08.png)
