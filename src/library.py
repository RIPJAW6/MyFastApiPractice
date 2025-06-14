from fastapi import Request, Depends, APIRouter, Form, Body
from requests import session

from src.crud import delete_books, get_book, get_books, delete_book, create_book
from src.database import SessionDep
from src.schemas import BookCreate
from src.templates import templates

router = APIRouter(tags=["Library"], prefix="/library")

@router.get("/", name="home")
async def homepage(request: Request, books=Depends(get_books)):
    return templates.TemplateResponse(
        request=request,
        name="homepage.html",
        context={"books": books})


@router.get("/get_one_book/{book_id}", name="book")
async def get_one_book(request: Request, book=Depends(get_book)):
    return templates.TemplateResponse(
        request=request,
        name="one_book.html",
        context={"book": book})


@router.get("/add_book")
async def add_book(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="add_book.html")


@router.post("/add_book/create")
async def add_book_create(request: Request,
                          book_in: BookCreate = Form(...)):
    await create_book(book_in)
    return templates.TemplateResponse(
        request=request,
        name="add_book_create.html")