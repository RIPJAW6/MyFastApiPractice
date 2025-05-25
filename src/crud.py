from sqlalchemy import select, delete
from src.schemas import BookCreate, Book
from src.models import BookModel
from src.database import SessionDep, new_session

async def create_book(book_in: BookCreate) -> BookCreate:
    async with new_session() as session:
        book = BookModel(title=book_in.title, description=book_in.description)
        session.add(book)
        await session.commit()
        return book_in


async def get_books(session: SessionDep) -> list[Book]:
    stmt = select(BookModel)
    results = await session.execute(stmt)
    return results.scalars().all()


async def get_book(book_id: int) -> Book | None:
    async with new_session() as session:
        stmt = select(BookModel).filter_by(id=book_id)
        results = await session.execute(stmt)
        return results.scalars().one_or_none()


async def delete_books():
    async with new_session() as session:
        stmt = delete(BookModel)
        await session.execute(stmt)
        await session.commit()
        return {"message": "Все книги удалены!"}