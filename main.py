from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

class DataRequest(BaseModel):
    data: List[Union[str, int]]

class DataResponse(BaseModel):
    is_success: bool
    user_id: str
    email: str
    roll_number: str
    numbers: List[str]
    alphabets: List[str]
    highest_alphabet: List[str]

@app.post("/bfhl", response_model=DataResponse)
async def process_data(request: DataRequest):
    data = request.data
    numbers = [str(item) for item in data if isinstance(item, int) or (isinstance(item, str) and item.isdigit())]
    alphabets = [item for item in data if isinstance(item, str) and item.isalpha()]
    highest_alphabet = [max(alphabets, key=str.lower)] if alphabets else []

    response = DataResponse(
        is_success=True,
        user_id="john_doe_17091999",
        email="john@xyz.com",
        roll_number="ABCD123",
        numbers=numbers,
        alphabets=alphabets,
        highest_alphabet=highest_alphabet
    )
    return response

@app.get("/bfhl")
async def get_operation_code():
    return {"operation_code": 1}
