# PDF-LLM Backend

🚀 AI-Powered Document Processor: A FastAPI-based backend that processes PDFs, extracts text using OCR, summarizes content via LLMs, and serves clean, cloud-ready APIs.

## Features

- 📄 PDF upload and validation
- 📊 Text extraction from PDF documents
- 🔍 Document retrieval with pagination
- 🤖 AI-powered document summarization using Gemini 2.0
- ❓ Question answering based on document content
- 🔒 JWT authentication for protected endpoints
- ☁️ S3 integration for document storage
- 📦 MongoDB for document metadata and extracted text

## Architecture

The application follows a modular architecture:
- FastAPI for RESTful API endpoints
- MongoDB for document storage and retrieval
- AWS S3 for PDF file storage
- Google's Gemini LLM for AI-powered text processing
- JWT for secure authentication

## Prerequisites

- Python 3.10+
- MongoDB
- AWS S3 account
- Google AI Platform account (for Gemini API access)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pdf-llm-backend.git
cd pdf-llm-backend
```

2. Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root with the following variables:

```
# MongoDB Configuration
MONGO_URI=mongodb://localhost:27017/
MONGO_DB_NAME=pdf_llm_db

# AWS S3 Configuration
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_REGION=us-east-1
S3_BUCKET_NAME=your-bucket-name

# JWT Configuration
JWT_SECRET_KEY=your-secret-key-keep-this-safe
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60

# Google AI Platform (Gemini)
GEMINI_API_KEY=your_gemini_api_key
```

## Starting the Server

### Local Development
```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

### AWS Lambda Deployment

The application is also deployed as a serverless application on AWS Lambda via Amazon ECR. You can access the API through the API Gateway:

```
https://api-gateway-id.execute-api.region.amazonaws.com/stage
```

Test the deployed APIs using this endpoint without setting up a local environment.

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Document Management
- `POST /upload`: Upload PDF document
- `GET /documents/{doc_id}`: Retrieve a specific document
- `GET /documents?page=1&limit=10`: List documents with pagination

### LLM Processing
- `POST /summarize/{doc_id}`: Generate a 2-sentence summary of document (JWT protected)
- `POST /query/{doc_id}/{question}`: Get answer to a question based on document content

### Authentication
- `POST /generate-token`: Generate JWT token for authentication

## Usage Examples

### Upload a PDF document
```bash
curl -X POST http://localhost:8000/upload -F "file=@/path/to/document.pdf"
```

### Get document summary (requires authentication)
```bash
# First generate a token
TOKEN=$(curl -s -X POST http://localhost:8000/generate-token | jq -r .access_token)

# Use token to access protected endpoint
curl -X POST http://localhost:8000/summarize/60c72b2b5e8e5f5a8c9d1c5a \
  -H "Authorization: Bearer $TOKEN"
```

### Query document content
```bash
curl -X POST "http://localhost:8000/query/60c72b2b5e8e5f5a8c9d1c5a/What%20is%20the%20main%20topic%3F"
```

## Demo Video

[Watch the full demo video](https://youtu.be/your-video-id)

## Assumptions

- Used mock PDFs from `./samples/sample_invoices/`
- PDFs are text-based and not scanned documents
- All PDFs are reasonably sized (under 10MB)
- MongoDB and S3 credentials are properly configured
- For demos, the system uses a simplified authentication system

## Testing

The project includes comprehensive tests written with pytest:

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src tests/ --cov-report=term-missing
```

Test data is located in the `tests/fixtures` directory.

## Project Structure

```
pdf-llm-backend/
├── src/
│   ├── comms/              # API communication layer
│   ├── configs/            # Configuration settings
│   ├── services/           # Core services
│   │   ├── llm_service.py  # LLM integration
│   │   ├── mongodb.py      # Database service
│   │   ├── pdf_extractor.py# PDF processing
│   │   └── s3_service.py   # S3 storage service
│   └── utils/              # Utility functions
├── tests/                  # Test suite
├── samples/                # Sample PDFs for testing
├── .env                    # Environment variables
├── requirements.txt        # Dependencies
└── README.md               # This file
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributors

- [Your Name](https://github.com/yourusername) - Initial work

## Acknowledgments

- FastAPI for the excellent framework
- Google Gemini for the powerful LLM capabilities
