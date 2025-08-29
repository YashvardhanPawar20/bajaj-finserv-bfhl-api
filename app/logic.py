"""
Core logic for processing BFHL data according to specification.
"""

from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


def is_integer_str(s: str) -> bool:
    """
    Check if string represents a valid base-10 integer.
    
    Args:
        s: String to check
        
    Returns:
        True if string is a valid integer (digits only), False otherwise
    """
    if not s:
        return False
    
    # Only digits 0-9 allowed (no leading +/- signs)
    return s.isdigit()


def is_alpha_str(s: str) -> bool:
    """
    Check if string contains only alphabetic characters.
    
    Args:
        s: String to check
        
    Returns:
        True if string contains only letters A-Z or a-z, False otherwise
    """
    if not s:
        return False
    
    return s.isalpha()


def get_parity(n: int) -> str:
    """
    Determine if number is even or odd.
    
    Args:
        n: Integer to check
        
    Returns:
        "even" or "odd"
    """
    return "even" if n % 2 == 0 else "odd"


def extract_alphabetic_chars(data: List[str]) -> str:
    """
    Extract all alphabetic characters from input data, reverse order,
    and apply alternating case starting with uppercase.
    
    Args:
        data: List of input strings
        
    Returns:
        Processed string with alternating case
    """
    # Extract all alphabetic characters maintaining order
    chars = []
    for item in data:
        for char in item:
            if char.isalpha():
                chars.append(char)
    
    # Reverse the character sequence
    chars_reversed = chars[::-1]
    
    # Apply alternating case starting with uppercase at index 0
    result = ""
    for i, char in enumerate(chars_reversed):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    
    return result


def process_bfhl_data(data: List[str]) -> Dict[str, Any]:
    """
    Process BFHL data according to specification.
    
    Args:
        data: List of input strings
        
    Returns:
        Dictionary with processed results
    """
    logger.info(f"Processing {len(data)} data items")
    
    # Initialize result containers
    odd_numbers = []
    even_numbers = []
    alphabets = []
    special_characters = []
    numeric_sum = 0
    
    # Process each item in single pass
    for item in data:
        if is_integer_str(item):
            # Valid integer - classify by parity and add to sum
            num = int(item)
            numeric_sum += num
            
            if get_parity(num) == "even":
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
                
        elif is_alpha_str(item):
            # Pure alphabetic string - convert to uppercase
            alphabets.append(item.upper())
            
        else:
            # Special character, mixed string, or other
            special_characters.append(item)
    
    # Generate concatenated string with alternating case
    concat_string = extract_alphabetic_chars(data)
    
    result = {
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(numeric_sum),
        "concat_string": concat_string
    }
    
    logger.info(f"Processed data: {len(odd_numbers)} odd, {len(even_numbers)} even, "
               f"{len(alphabets)} alphabets, {len(special_characters)} special, "
               f"sum={numeric_sum}, concat='{concat_string}'")
    
    return result
