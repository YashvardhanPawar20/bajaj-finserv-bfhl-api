#!/usr/bin/env python3
"""
BFHL API Tester Script
Test the deployed API from anywhere with Python
"""

import requests
import json

# API endpoint
API_URL = "https://bajaj-finserv-bfhl-api.vercel.app/bfhl"

# Test cases from specification
test_cases = [
    {
        "name": "Example A",
        "data": ["a", "1", "334", "4", "R", "$"],
        "expected_concat": "Ra",
        "expected_sum": "339"
    },
    {
        "name": "Example B", 
        "data": ["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"],
        "expected_concat": "ByA",
        "expected_sum": "103"
    },
    {
        "name": "Example C",
        "data": ["A", "ABcD", "DOE"],
        "expected_concat": "EoDdCbAa",
        "expected_sum": "0"
    }
]

def test_api(data):
    """Test the API with given data"""
    try:
        response = requests.post(
            API_URL,
            json={"data": data},
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        return response.status_code, response.json()
    except Exception as e:
        return None, str(e)

def main():
    print("🔥 BFHL API Tester")
    print(f"🌐 Testing: {API_URL}")
    print("=" * 60)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📋 Test {i}: {test_case['name']}")
        print(f"Input: {test_case['data']}")
        
        status_code, result = test_api(test_case['data'])
        
        if status_code == 200:
            print("✅ Status: SUCCESS")
            print(f"📤 concat_string: {result.get('concat_string')}")
            print(f"🔢 sum: {result.get('sum')}")
            
            # Verify expected results
            if result.get('concat_string') == test_case['expected_concat']:
                print("✅ concat_string matches expected")
            else:
                print(f"❌ concat_string mismatch. Expected: {test_case['expected_concat']}")
                
            if result.get('sum') == test_case['expected_sum']:
                print("✅ sum matches expected")
            else:
                print(f"❌ sum mismatch. Expected: {test_case['expected_sum']}")
                
            print(f"📊 Full Response: {json.dumps(result, indent=2)}")
        else:
            print(f"❌ Status: FAILED ({status_code})")
            print(f"Error: {result}")
    
    print("\n" + "=" * 60)
    print("🎉 Testing Complete!")

if __name__ == "__main__":
    main()
