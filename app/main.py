"""
FastAPI application for BFHL REST API.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
from typing import Dict, Any

from .models import BFHLRequest, BFHLResponse
from .logic import process_bfhl_data

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="BFHL API",
    description="REST API for VIT Full Stack Question Paper - BFHL",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Constants - Replace these with actual values
FULL_NAME_LOWERCASE = "yash_kumar"
DOB_DDMMYYYY = "17091999"
EMAIL_ID = "yash@example.com"
ROLL_NUMBER = "22BCE0000"

USER_ID = f"{FULL_NAME_LOWERCASE}_{DOB_DDMMYYYY}"


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Global exception handler to ensure we always return proper JSON."""
    logger.error(f"Unhandled exception: {exc}")
    
    error_response = BFHLResponse(
        is_success=False,
        user_id=USER_ID,
        email=EMAIL_ID,
        roll_number=ROLL_NUMBER,
        odd_numbers=[],
        even_numbers=[],
        alphabets=[],
        special_characters=[],
        sum="0",
        concat_string=""
    )
    
    return JSONResponse(
        status_code=200,
        content=error_response.model_dump()
    )


@app.post("/bfhl", response_model=BFHLResponse)
async def bfhl_endpoint(request: BFHLRequest) -> BFHLResponse:
    """
    Process BFHL data according to specification.
    
    Args:
        request: BFHLRequest containing data array
        
    Returns:
        BFHLResponse with processed data
    """
    try:
        logger.info(f"Processing BFHL request with {len(request.data)} items")
        
        # Process the data using our logic module
        result = process_bfhl_data(request.data)
        
        # Build response
        response = BFHLResponse(
            is_success=True,
            user_id=USER_ID,
            email=EMAIL_ID,
            roll_number=ROLL_NUMBER,
            odd_numbers=result["odd_numbers"],
            even_numbers=result["even_numbers"],
            alphabets=result["alphabets"],
            special_characters=result["special_characters"],
            sum=result["sum"],
            concat_string=result["concat_string"]
        )
        
        logger.info("Successfully processed BFHL request")
        return response
        
    except Exception as e:
        logger.error(f"Error processing BFHL request: {e}")
        
        # Return error response with proper structure
        return BFHLResponse(
            is_success=False,
            user_id=USER_ID,
            email=EMAIL_ID,
            roll_number=ROLL_NUMBER,
            odd_numbers=[],
            even_numbers=[],
            alphabets=[],
            special_characters=[],
            sum="0",
            concat_string=""
        )


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
