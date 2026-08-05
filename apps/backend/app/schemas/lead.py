from pydantic import BaseModel
class LeadCreate(BaseModel):
 full_name:str
 contact_number:str
