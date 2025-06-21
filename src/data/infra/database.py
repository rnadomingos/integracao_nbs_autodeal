from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

MYSQL_DATABASE_DEV_URL = "mysql+pymysql://autodeal_user:pR8cHu#0USen@192.168.18.240:3306/dev_autodeal"

engine = create_engine(MYSQL_DATABASE_DEV_URL, echo=True)

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