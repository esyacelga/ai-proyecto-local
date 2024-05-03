from pydantic import BaseModel

class SalaryPredictionRequest(BaseModel):
    YearsExperience: float


class SalaryPredictionResponse(BaseModel):
    Salary: float
