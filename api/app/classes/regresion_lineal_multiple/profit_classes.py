from pydantic import BaseModel


class ProfitRequest(BaseModel):
    nueva_york: int    
    Florida: int
    R_D_Spend: float
    Administration: float
    Marketing_Spend: float
    
    

class ProfitResponse(BaseModel):
    Profit: float
