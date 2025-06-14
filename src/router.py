from fastapi import APIRouter, HTTPException, status, Request, Depends
from src.crud import create_book, get_books, delete_books, get_book
from src.database import SessionDep
from src.schemas import BookCreate, Book

router = APIRouter(tags=["Books"])

@router.post("/create_book", response_model=BookCreate)
async def create_new_book(book_in: BookCreate):
    return await create_book(book_in)


@router.get("/get_books", response_model=list[Book])
async def get_all_books(session: SessionDep):
    return await get_books(session)


@router.get("/get_book/{book_id}", response_model=Book)
async def get_one_book(book_id: int) -> Book | None:
    result = await get_book(book_id)
    if result is not None:
        return result
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@router.get("/delete_books")
async def delete_all_books():
    return await delete_books()