"""
Pydantic models for BFHL API request/response schemas.
"""

from pydantic import BaseModel, Field, validator
from typing import List, Any


class BFHLRequest(BaseModel):
    """Request model for BFHL endpoint."""
    
    data: List[str] = Field(..., description="Array of strings to process")
    
    @validator('data')
    def validate_data(cls, v):
        """Ensure data is a list."""
        if not isinstance(v, list):
            raise ValueError('data must be a list')
        return v


class BFHLResponse(BaseModel):
    """Response model for BFHL endpoint."""
    
    is_success: bool = Field(..., description="Whether the request was successful")
    user_id: str = Field(..., description="User ID in format full_name_ddmmyyyy")
    email: str = Field(..., description="Email address")
    roll_number: str = Field(..., description="College roll number")
    odd_numbers: List[str] = Field(..., description="Odd numbers as strings")
    even_numbers: List[str] = Field(..., description="Even numbers as strings")
    alphabets: List[str] = Field(..., description="Alphabetic strings in uppercase")
    special_characters: List[str] = Field(..., description="Special characters and mixed strings")
    sum: str = Field(..., description="Sum of all numeric values as string")
    concat_string: str = Field(..., description="Concatenated alphabetic characters with alternating case")
