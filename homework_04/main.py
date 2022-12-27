import os
import asyncio

from sqlalchemy.ext.asyncio import create_async_engine

from homework_04.models import Base, User, Post, Session
from homework_04.jsonplaceholder_requests import get_api_data


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"


async def async_main():
    engine = create_async_engine(PG_CONN_URI, echo=True)
    Session.configure(bind=engine)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    users_data, posts_data = await get_api_data()

    async with Session() as session:
        async with session.begin():
            session.add_all(
                [
                    User(
                        id=u['id'],
                        username=u['username'],
                        name=u['name'],
                        email=u['email']
                    ) for u in users_data
                ]
            )

            session.add_all(
                [
                    Post(
                        id=p['id'],
                        title=p['title'],
                        body=p['body'],
                        user_id=p['userId']
                    ) for p in posts_data
                ]
            )
        await session.commit()
    await engine.dispose()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
