from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class ImagePair(BaseModel):
    """
    Represents a pair of images: the original and the compliant edited version.
    """
    compliance_id: str
    original_url: HttpUrl
    edited_url: HttpUrl

class Property(BaseModel):
    """
    Represents a property listing which contains multiple image pairs.
    """
    id: int
    address: str
    image_pairs: List[ImagePair] = []
    description: Optional[str] = None
