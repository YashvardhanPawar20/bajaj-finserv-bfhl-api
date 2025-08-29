"""
Unit tests for BFHL logic functions.
"""

import pytest
from app.logic import (
    is_integer_str,
    is_alpha_str,
    get_parity,
    extract_alphabetic_chars,
    process_bfhl_data
)


class TestClassificationFunctions:
    """Test basic classification helper functions."""
    
    def test_is_integer_str(self):
        """Test integer string validation."""
        # Valid integers
        assert is_integer_str("123") == True
        assert is_integer_str("0") == True
        assert is_integer_str("1") == True
        assert is_integer_str("334") == True
        assert is_integer_str("92") == True
        
        # Invalid integers
        assert is_integer_str("") == False
        assert is_integer_str("a") == False
        assert is_integer_str("1a") == False
        assert is_integer_str("a1") == False
        assert is_integer_str("3.14") == False
        assert is_integer_str("+123") == False
        assert is_integer_str("-123") == False
        assert is_integer_str("12.0") == False
        assert is_integer_str("abc") == False
        assert is_integer_str("$") == False
        assert is_integer_str("&") == False
    
    def test_is_alpha_str(self):
        """Test alphabetic string validation."""
        # Valid alphabetic strings
        assert is_alpha_str("a") == True
        assert is_alpha_str("A") == True
        assert is_alpha_str("abc") == True
        assert is_alpha_str("ABC") == True
        assert is_alpha_str("AbC") == True
        assert is_alpha_str("R") == True
        assert is_alpha_str("ABcD") == True
        assert is_alpha_str("DOE") == True
        
        # Invalid alphabetic strings
        assert is_alpha_str("") == False
        assert is_alpha_str("1") == False
        assert is_alpha_str("a1") == False
        assert is_alpha_str("1a") == False
        assert is_alpha_str("abc123") == False
        assert is_alpha_str("$") == False
        assert is_alpha_str("&") == False
        assert is_alpha_str("-") == False
        assert is_alpha_str("*") == False
        assert is_alpha_str("3.14") == False
    
    def test_get_parity(self):
        """Test parity determination."""
        # Even numbers
        assert get_parity(0) == "even"
        assert get_parity(2) == "even"
        assert get_parity(4) == "even"
        assert get_parity(92) == "even"
        assert get_parity(334) == "even"
        
        # Odd numbers
        assert get_parity(1) == "odd"
        assert get_parity(3) == "odd"
        assert get_parity(5) == "odd"
        assert get_parity(7) == "odd"


class TestConcatStringAlgorithm:
    """Test the concat_string algorithm with provided examples."""
    
    def test_example_a_concat(self):
        """Test Example A: ["a","1","334","4","R","$"] -> "Ra" """
        data = ["a", "1", "334", "4", "R", "$"]
        result = extract_alphabetic_chars(data)
        assert result == "Ra", f"Expected 'Ra', got '{result}'"
    
    def test_example_b_concat(self):
        """Test Example B: ["2","a","y","4","&","-","*","5","92","b"] -> "ByA" """
        data = ["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"]
        result = extract_alphabetic_chars(data)
        assert result == "ByA", f"Expected 'ByA', got '{result}'"
    
    def test_example_c_concat(self):
        """Test Example C: ["A","ABcD","DOE"] -> "EoDdCbAa" """
        data = ["A", "ABcD", "DOE"]
        result = extract_alphabetic_chars(data)
        assert result == "EoDdCbAa", f"Expected 'EoDdCbAa', got '{result}'"
    
    def test_empty_data_concat(self):
        """Test empty data returns empty string."""
        result = extract_alphabetic_chars([])
        assert result == ""
    
    def test_no_alphabets_concat(self):
        """Test data with no alphabetic characters."""
        data = ["1", "2", "$", "&"]
        result = extract_alphabetic_chars(data)
        assert result == ""


class TestFullProcessing:
    """Test complete data processing with provided examples."""
    
    def test_example_a_full(self):
        """Test full processing for Example A."""
        data = ["a", "1", "334", "4", "R", "$"]
        result = process_bfhl_data(data)
        
        assert result["odd_numbers"] == ["1"]
        assert result["even_numbers"] == ["334", "4"]
        assert result["alphabets"] == ["A", "R"]
        assert result["special_characters"] == ["$"]
        assert result["sum"] == "339"
        assert result["concat_string"] == "Ra"
    
    def test_example_b_full(self):
        """Test full processing for Example B."""
        data = ["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"]
        result = process_bfhl_data(data)
        
        assert result["odd_numbers"] == ["5"]
        assert result["even_numbers"] == ["2", "4", "92"]
        assert result["alphabets"] == ["A", "Y", "B"]
        assert result["special_characters"] == ["&", "-", "*"]
        assert result["sum"] == "103"
        assert result["concat_string"] == "ByA"
    
    def test_example_c_full(self):
        """Test full processing for Example C."""
        data = ["A", "ABcD", "DOE"]
        result = process_bfhl_data(data)
        
        assert result["odd_numbers"] == []
        assert result["even_numbers"] == []
        assert result["alphabets"] == ["A", "ABCD", "DOE"]
        assert result["special_characters"] == []
        assert result["sum"] == "0"
        assert result["concat_string"] == "EoDdCbAa"
    
    def test_empty_data_full(self):
        """Test processing empty data."""
        data = []
        result = process_bfhl_data(data)
        
        assert result["odd_numbers"] == []
        assert result["even_numbers"] == []
        assert result["alphabets"] == []
        assert result["special_characters"] == []
        assert result["sum"] == "0"
        assert result["concat_string"] == ""
    
    def test_mixed_data_full(self):
        """Test processing mixed complex data."""
        data = ["123", "abc", "12a", "", "0", "XYZ", "!@#", "999"]
        result = process_bfhl_data(data)
        
        assert result["odd_numbers"] == ["123", "999"]
        assert result["even_numbers"] == ["0"]
        assert result["alphabets"] == ["ABC", "XYZ"]
        assert result["special_characters"] == ["12a", "", "!@#"]
        assert result["sum"] == "1122"  # 123 + 0 + 999
    
    def test_large_numbers(self):
        """Test processing large numbers."""
        data = ["999999999", "1000000000"]
        result = process_bfhl_data(data)
        
        assert result["odd_numbers"] == ["999999999"]
        assert result["even_numbers"] == ["1000000000"]
        assert result["sum"] == "1999999999"


if __name__ == "__main__":
    pytest.main([__file__])
