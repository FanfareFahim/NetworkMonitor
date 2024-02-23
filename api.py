from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError

app = FastAPI()

class InputData(BaseModel):
    macAddress: str
    dateTime: str

@app.post("/process_data")
def process_data(data: InputData):
    try:
        # This will raise a ValidationError if the data is invalid
        data_dict = data.dict()
    except ValidationError as e:
        # Log the validation error for debugging
        print(f"Validation Error: {e}")
        raise HTTPException(status_code=422, detail="Validation Error")

    mac_address = data_dict["macAddress"]
    datetime_value = data_dict["dateTime"]

    # Your existing processing logic here...

    # Return a response
    return {mac_address, datetime_value}
