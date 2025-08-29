# BFHL REST API

A production-ready REST API implementation for the VIT "Full Stack Question Paper - BFHL" specification. Built with FastAPI, Python 3.11+, and designed for easy deployment.

## Features

- **FastAPI** framework with automatic OpenAPI documentation
- **Type-safe** with Pydantic models and comprehensive type hints
- **CORS enabled** for cross-origin requests
- **Structured logging** for debugging and monitoring
- **Comprehensive test coverage** with pytest
- **Production-ready** with proper error handling
- **Single-pass processing** for optimal performance O(n)

## API Specification

### Endpoint
- **Method**: POST
- **Route**: `/bfhl`
- **Content-Type**: `application/json`

### Request Body
```json
{
  "data": ["<strings that may be numbers/alphabets/specials>", ...]
}
```

### Response Body
```json
{
  "is_success": true,
  "user_id": "yash_kumar_17091999",
  "email": "yash@example.com", 
  "roll_number": "22BCE0000",
  "odd_numbers": ["1", "5"],
  "even_numbers": ["2", "4"],
  "alphabets": ["A", "B"],
  "special_characters": ["$", "&"],
  "sum": "12",
  "concat_string": "Ba"
}
```

## Local Development

### Prerequisites
- Python 3.11 or higher
- pip package manager

### Setup & Installation

1. **Clone and navigate to project directory**:
```bash
cd /path/to/bajaj_finserve
```

2. **Create virtual environment** (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run the server**:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Testing

**Run all tests**:
```bash
pytest
```

**Run tests with coverage**:
```bash
pytest --cov=app tests/
```

**Run specific test**:
```bash
pytest tests/test_logic.py::TestFullProcessing::test_example_a_full -v
```

### API Documentation

Once the server is running, visit:
- **Interactive docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Usage Examples

### Example 1: Basic Request
```bash
curl -X POST "http://localhost:8000/bfhl" \
  -H "Content-Type: application/json" \
  -d '{"data": ["a","1","334","4","R","$"]}'
```

**Expected Response**:
```json
{
  "is_success": true,
  "user_id": "yash_kumar_17091999",
  "email": "yash@example.com",
  "roll_number": "22BCE0000",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

### Example 2: Complex Data
```bash
curl -X POST "http://localhost:8000/bfhl" \
  -H "Content-Type: application/json" \
  -d '{"data": ["2","a","y","4","&","-","*","5","92","b"]}'
```

**Expected Response**:
```json
{
  "is_success": true,
  "user_id": "yash_kumar_17091999",
  "email": "yash@example.com", 
  "roll_number": "22BCE0000",
  "odd_numbers": ["5"],
  "even_numbers": ["2", "4", "92"],
  "alphabets": ["A", "Y", "B"],
  "special_characters": ["&", "-", "*"],
  "sum": "103",
  "concat_string": "ByA"
}
```

### Example 3: Alphabets Only
```bash
curl -X POST "http://localhost:8000/bfhl" \
  -H "Content-Type: application/json" \
  -d '{"data": ["A","ABcD","DOE"]}'
```

## Deployment

### Vercel (Recommended)

1. **Install Vercel CLI**:
```bash
npm i -g vercel
```

2. **Deploy**:
```bash
vercel --prod
```

The `vercel.json` configuration is included for automatic deployment.

### Railway

1. **Install Railway CLI**:
```bash
npm i -g @railway/cli
```

2. **Deploy**:
```bash
railway login
railway init
railway up
```

The `Procfile` is included for Railway deployment.

### Render

1. **Connect your GitHub repository** to Render
2. **Use the following settings**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Environment**: Python 3.11

### Docker (Alternative)

```bash
# Build image
docker build -t bfhl-api .

# Run container
docker run -p 8000:8000 bfhl-api
```

## Configuration

Update the following constants in `app/main.py` with your actual values:

```python
FULL_NAME_LOWERCASE = "your_name"      # e.g., "john_doe"  
DOB_DDMMYYYY = "ddmmyyyy"              # e.g., "17091999"
EMAIL_ID = "your.email@example.com"    # e.g., "john@xyz.com"
ROLL_NUMBER = "YOUR_ROLL_NUMBER"       # e.g., "ABCD123"
```

## Project Structure

```
bajaj_finserve/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── models.py        # Pydantic schemas
│   └── logic.py         # Core processing logic
├── tests/
│   ├── __init__.py
│   └── test_logic.py    # Unit tests
├── requirements.txt     # Python dependencies
├── vercel.json         # Vercel deployment config
├── Procfile           # Railway/Heroku deployment config
├── Dockerfile         # Docker configuration
└── README.md          # This file
```

## Performance Notes

- **O(n) single-pass processing** for optimal performance
- **Streaming approach** to handle large input arrays efficiently
- **Memory-efficient** character extraction and processing
- **Proper error handling** with structured responses

## License

This project is created for educational purposes as per VIT Full Stack Question Paper specifications.

## Support

For issues and questions, please check the test cases in `tests/test_logic.py` which cover all specification examples and edge cases.
