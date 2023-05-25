from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_HOST, DB_PORT, DB_USER, DB_NAME, DB_PASS

# строка подключения
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# создание движка
engine = create_engine(SQLALCHEMY_DATABASE_URL)


# создаем сессию подключения к бд
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)
db = SessionLocal()

# создаем модель, объекты которой будут храниться в бд
Base = declarative_base()
