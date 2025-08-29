from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ✅ Your details (replace with your own)
FULL_NAME = "john_doe"
DOB = "17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

# ✅ Request body schema
class InputData(BaseModel):
    data: List[str]

# ✅ Alternating caps reverse function
def alternating_caps_reverse(s: str) -> str:
    result = ""
    toggle = True
    for ch in reversed(s):
        result += ch.upper() if toggle else ch.lower()
        toggle = not toggle
    return result

# ✅ POST /bfhl route
@app.post("/bfhl")
def process_data(input_data: InputData):
    try:
        data = input_data.data
        odd, even, alphabets, special = [], [], [], []
        total = 0
        alpha_concat = ""

        for item in data:
            if item.isdigit():  # number
                num = int(item)
                total += num
                (even if num % 2 == 0 else odd).append(item)
            elif item.isalpha():  # alphabets
                alphabets.append(item.upper())
                alpha_concat += item
            else:  # special characters
                special.append(item)

        return {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd,
            "even_numbers": even,
            "alphabets": alphabets,
            "special_characters": special,
            "sum": str(total),
            "concat_string": alternating_caps_reverse(alpha_concat)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
