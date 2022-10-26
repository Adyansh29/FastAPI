from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# sqlite database connection url
# todos.db - will actually store the database
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:sunny1111@localhost/TodoApplicationDatabase"


# This engine will be used in other areas pf application.
engine = create_engine(
        SQLALCHEMY_DATABASE_URL
)


# To create a new database session by creating SessionLocal object.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base allows to create each database model.
Base = declarative_base()
