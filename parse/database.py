from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_HOST, DB_PORT, DB_USER, DB_NAME, DB_PASS

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

db_session = sessionmaker(autocommit=False,
                          autoflush=False,
                          bind=engine)
db = db_session()
Base = declarative_base()

Base.metadata.create_all(bind=engine)
