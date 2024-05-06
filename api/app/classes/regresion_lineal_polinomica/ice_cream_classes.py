from pydantic import BaseModel


class IceCreamRequest(BaseModel):
    temperature: float      
    
    

class IceCreamResponse(BaseModel):
    units_ice_cream: float
