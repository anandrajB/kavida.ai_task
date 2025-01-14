from typing import Any, Dict, List, Optional, Union
from fastapi import FastAPI, HTTPException, Request 
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
app = FastAPI(
    title="Kavida.ai Task",
    version="1.0.0",
)


origins = [
    "*",
]



class ValidateRequestSchema(BaseModel):
    data: Union[Dict[str, Any], List[Any]] = Field(
        ...,
        example={
            "user": {
                "name": "John Doe",
                "age": 30,
                "address": {"city": "New York", "zip": "10001"}
            },
            "order": {
                "id": "12345",
                "items": [
                    {"name": "Laptop", "price": 1000},
                    {"name": "Mouse", "price": 20}
                ]
            }
        }
    )
    optional_fields: Optional[List[str]] = Field(
        default=None,
        example=["user.age"]
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get():
    return JSONResponse({"message": "Hello World"})

def validate_json(
    data: Union[Dict, List], 
    optional_fields: Optional[List[str]] = None
) -> Dict[str, Any]:
    optional_fields = optional_fields if optional_fields is not None else []

    def check_nulls(obj, path='', invalid_fields=None):
        if invalid_fields is None:
            invalid_fields = []
        
        if isinstance(obj, dict):
            for key, value in obj.items():
                field_path = f"{path}.{key}" if path else key
                if value is None and field_path not in optional_fields:
                    invalid_fields.append(field_path)
                elif isinstance(value, (dict, list)):
                    check_nulls(value, field_path, invalid_fields)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                check_nulls(item, f"{path}[{index}]", invalid_fields)
        
        return invalid_fields

    invalid_fields = check_nulls(data)
    
    if invalid_fields:
        return {"status": "error", "invalid_fields": invalid_fields}
    return {"status": "success"}

@app.post("/validate/")
async def validate_incoming_json(request: ValidateRequestSchema):
    try:
        body = await request.json()
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid JSON format , kindly retry with corrct format") from e
    optional_fields = request.query_params.getlist("optional_fields")
    result = validate_json(body, optional_fields=optional_fields)
    return result