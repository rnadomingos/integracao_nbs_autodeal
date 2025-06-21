from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from data.infra.database import Base

class CompanyModel(Base):
  __tablename__ = 'companies'

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  created_at = Column(DateTime(timezone=True), default=func.now())
  updated_at = Column(DateTime(timezone=True), default=func.now())