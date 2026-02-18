## Description

This project demonstrates a FastAPI application that performs file uploads to AWS S3 using boto3. It is built with modern Python features and leverages FastAPI for its high performance and automatic interactive documentation.

## Technology Stack

- **Backend Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **ASGI Server:** [Uvicorn](https://uvicorn.dev/)
- **AWS SDK:** [boto3](https://docs.aws.amazon.com/boto3/latest/)

## Installation and Setup

### Prerequisites

- Python 3.8+
- `pip` or [Poetry](https://python-poetry.org/) for dependency management

### Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    cd your-repo-name
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    .\\venv\\Scripts\\activate
    # On macOS/Linux
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run the Application

### Locally

Start the development server with Uvicorn:

```bash
uvicorn main:app --reload
```

Navigate to the [Docs](http://127.0.0.1:8000/docs) to access the interactive documentation
