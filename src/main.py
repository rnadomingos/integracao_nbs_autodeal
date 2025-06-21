from data.infra.database import engine, Base, SessionLocal
from modules.companies.use_case.get_companies import get_all_companies

Base.metadata.create_all(bind=engine)

db = SessionLocal()

companies = get_all_companies(db)

for cp in companies:
    print(f'ID: {cp.id}, Empresa: {cp.name}')