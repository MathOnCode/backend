from fastapi import APIRouter
from python_modules.formResponse import rootForm_Response
from python_modules.formVerification import rootForm_Verification
from python_modules.formSchemas import FormModel

router = APIRouter()

@router.post("/request", status_code= 200)
async def root(payload: FormModel):
        if rootForm_Verification(payload):
            return rootForm_Response(payload)