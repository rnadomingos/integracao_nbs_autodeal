from data.models.company import CompanyModel
from sqlalchemy.orm import Session

def get_all_companies(db: Session):
    '''
    Get all companies
    '''
    return db.query(CompanyModel).all()
