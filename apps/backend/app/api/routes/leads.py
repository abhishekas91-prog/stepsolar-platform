from fastapi import APIRouter
router=APIRouter(prefix="/api")
@router.post("/leads")
async def leads(payload:dict): return {"success":True,"data":payload}
