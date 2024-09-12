from pydantic import BaseModel


class ApiBaseModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True
