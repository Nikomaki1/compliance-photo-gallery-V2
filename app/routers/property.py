from fastapi import APIRouter
from app.models.schemas import ImagePair

router = APIRouter(
    prefix="/properties",
    tags=["properties"]
)

@router.post("/{property_id}/upload-pair")
async def upload_image_pair(property_id: str, image_pair: ImagePair):
    """
    Upload an original and edited image pair for a specific property.
    Validates input using the ImagePair schema and returns the compliance_id.
    """
    # In a real app, you might save this to a database or associate it with the property_id
    return {"compliance_id": image_pair.compliance_id}
