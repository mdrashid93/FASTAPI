from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from config import settings
engine=create_async_engine(settings.DATABASE_URL,echo=True)
AsyncSessionFactory=sessionmaker("sessionmaker":Unknownword. engine,
                                 class_=AsyncSession,
                                 expire_on_commit=False)