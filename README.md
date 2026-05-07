# Patient Health Management System - FastAPI

## 📌 Project Overview

This is a **learning-focused** REST API project built with FastAPI for managing patient health information. The application demonstrates core concepts of modern API development including data validation, BMI calculations, health assessments, and persistent data storage using JSON.

**⚠️ Note:** This project is designed **for learning purposes only** and should not be used in production environments for managing actual patient data.

---

## ✨ Features

- **Patient Data Management**: Create, read, update, and retrieve patient information
- **BMI Calculation**: Automatically calculates Body Mass Index based on height and weight
- **Health Verdict**: Provides health status classification (Underweight, Normal weight, Overweight, Obese) based on BMI
- **Data Validation**: Robust input validation using Pydantic models
- **Persistent Storage**: Data is stored in a JSON file for persistence across sessions
- **Interactive API Documentation**: Auto-generated Swagger UI and ReDoc documentation
- **Type Hints**: Full type annotation support for better code clarity

---

## 🛠️ Technology Stack

- **FastAPI** - Modern Python web framework for building APIs
- **Pydantic** - Data validation and serialization library
- **Python 3.x** - Programming language
- **JSON** - Data persistence format

---

## 📁 Project Structure

```
FAST API/
├── main.py              # Main FastAPI application with all endpoints
├── patients.json        # JSON file storing patient data
├── .venv/              # Virtual environment (if created locally)
└── README.md           # This file
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone or Navigate to the Project**
   ```bash
   cd "FAST API"
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**
   
   **Windows:**
   ```bash
   .venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source .venv/bin/activate
   ```

4. **Install Required Dependencies**
   ```bash
   pip install fastapi uvicorn
   ```

---

## 📖 Running the Application

1. **Start the Development Server**
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the Application**
   - **API Base URL**: http://127.0.0.1:8000
   - **Swagger UI (Interactive Docs)**: http://127.0.0.1:8000/docs
   - **ReDoc (API Documentation)**: http://127.0.0.1:8000/redoc

---

## 🔌 API Endpoints

### 1. **Home Endpoint**
- **URL**: `GET /`
- **Description**: Welcome message
- **Response**:
  ```json
  {
    "message": "Welcome to the home page!"
  }
  ```

### 2. **Hello Endpoint**
- **URL**: `GET /hello`
- **Description**: Simple hello message
- **Response**:
  ```json
  {
    "message": "Hello, World!"
  }
  ```

### 3. **View All Patients**
- **URL**: `GET /view`
- **Description**: Retrieve all patient records with calculated BMI and health verdict
- **Response**:
  ```json
  {
    "patients": {
      "P001": {
        "name": "Maryam Naseem",
        "age": 28,
        "gender": "female",
        "height": 1.65,
        "weight": 90.0,
        "bmi": 33.06,
        "verdict": "Obese"
      }
    }
  }
  ```

---

## 📊 Patient Data Model

### Patient Object
```json
{
  "id": "P001",
  "name": "Maryam Naseem",
  "age": 28,
  "gender": "female",
  "height": 1.65,
  "weight": 90.0,
  "bmi": 33.06,
  "verdict": "Obese"
}
```

### Field Descriptions
| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| id | string | Unique patient identifier | Required (e.g., "P001") |
| name | string | Patient's full name | Required |
| age | integer | Patient's age in years | Required (1-109) |
| gender | string | Patient's gender | Required ("male", "female", "other") |
| height | float | Height in meters | Required (> 0) |
| weight | float | Weight in kilograms | Required (> 0) |
| bmi | float | Body Mass Index | Calculated automatically |
| verdict | string | Health classification | Calculated automatically |

### BMI Categories
- **Underweight**: BMI < 18.5
- **Normal weight**: 18.5 ≤ BMI < 25
- **Overweight**: 25 ≤ BMI < 30
- **Obese**: BMI ≥ 30

---

## 📚 Learning Concepts Covered

This project demonstrates the following concepts:

1. **FastAPI Basics**
   - Creating GET endpoints
   - Path and query parameters
   - Request/response handling

2. **Pydantic Models**
   - Data validation with Field constraints
   - Type hints and annotations
   - Computed fields for derived data

3. **JSON File Handling**
   - Reading and writing JSON files
   - Data persistence

4. **API Documentation**
   - Auto-generated Swagger UI
   - Proper docstrings and examples

5. **Data Validation**
   - Input constraints (greater than, less than)
   - Literal types for enumeration
   - Optional fields in update models

---

## 💡 Code Examples

### Example 1: Load Patient Data
```python
data = load_data()
print(data)  # Returns dictionary of all patients
```

### Example 2: Access Computed Fields
When a Patient object is created, BMI and verdict are automatically calculated:
```python
patient = Patient(
    id="P010",
    name="John Doe",
    age=25,
    gender="male",
    height=1.80,
    weight=75
)
print(f"BMI: {patient.bmi}")      # Output: 23.15
print(f"Verdict: {patient.verdict}")  # Output: Normal weight
```

---

## 🔒 Data Storage

Patient data is persisted in `patients.json` file. The file structure is:

```json
{
  "P001": { patient object },
  "P002": { patient object },
  ...
}
```

---

## 📝 Future Enhancements (Learning Ideas)

- Add CREATE endpoint to add new patients
- Add UPDATE endpoint to modify patient information
- Add DELETE endpoint to remove patient records
- Implement database (SQLite, PostgreSQL) instead of JSON
- Add authentication and authorization
- Add search and filtering capabilities
- Implement logging and error handling
- Add unit and integration tests
- Deploy to cloud platforms (AWS, Heroku, etc.)

---

## ⚠️ Important Notes

🔴 **For Learning Only**: This project is created purely for educational purposes. It should **NOT** be used in production for:
- Storing actual patient health records
- Clinical decision-making
- HIPAA or any healthcare compliance requirements
- Any real-world medical applications

For production healthcare applications, you would need:
- Proper database systems
- Data encryption
- Authentication and authorization layers
- Compliance with healthcare regulations (HIPAA, GDPR, etc.)
- Professional security audits

---

## 📖 Resources for Learning

- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [REST API Best Practices](https://restfulapi.net/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

---

## 📄 License

This project is created for educational purposes. Feel free to use it for learning and modification.

---

## 👤 Author

Created as a learning project to understand FastAPI and REST API development.

---

## 🤝 Contributing

Since this is a learning project, feel free to:
- Modify the code to experiment with new features
- Add more endpoints and functionality
- Improve data validation
- Enhance error handling

---

**Happy Learning! 🎓**
