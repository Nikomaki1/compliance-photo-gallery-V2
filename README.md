# Compliance Photo Gallery V2

A modern FastAPI application for managing compliance-related photography, providing a robust backend API for photo uploads, galleries, and compliance tracking.

## 🚀 Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Package Manager**: [uv](https://github.com/astral-sh/uv)
- **Language**: Python 3.12+
- **Server**: Uvicorn

## 🛠️ Getting Started

### Prerequisites

- [Python](https://www.python.org/) (3.12 or higher)
- [uv](https://github.com/astral-sh/uv) (recommended for dependency management)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Nikomaki1/compliance-photo-gallery-V2.git
   cd compliance-photo-gallery-V2
   ```

2. **Set up the environment**:
   Using `uv`:
   ```bash
   python -m uv venv
   python -m uv sync
   ```

### Running the Application

Start the development server with hot-reload:

```bash
python -m uv run uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## 📖 API Documentation

FastAPI automatically generates interactive documentation for the API:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📂 Project Structure

```text
compliance-photo-gallery-V2/
├── app/
│   └── main.py          # Application entry point & routes
├── .gitignore           # Git ignore rules
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock              # Locked dependencies
└── README.md            # Project documentation
```

## 📝 License

This project is licensed under the MIT License.
