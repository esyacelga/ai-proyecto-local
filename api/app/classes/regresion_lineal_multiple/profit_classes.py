from pydantic import BaseModel


class ProfitRequest(BaseModel):
    State_NewYork: int    
    State_Florida: int
    R_D_Spend: float
    Administration: float
    Marketing_Spend: float
    
    

class ProfitResponse(BaseModel):
    Profit: float
