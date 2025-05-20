from pydantic import BaseModel, ConfigDict

class BookBase(BaseModel):
    title: str
    description: str | None = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    model_config = ConfigDict(from_attributes=True)
    id: int