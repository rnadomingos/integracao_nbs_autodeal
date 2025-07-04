from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from load_settings import load_settings

settings = load_settings()

connection_string = f"mysql+pymysql://{settings['db_user']}:{settings['db_pass']}@{settings['db_host']}:{settings['db_port']}/{settings['db_name']}"

engine = create_engine(connection_string, echo=True)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

# PARA USAR COM FAST API
# def get_db():
#   '''
#   Function to create connection and session with database
#   '''
#   db = SessionLocal()
#   try:
#       yield db
#   finally:
#       db.close()