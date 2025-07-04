from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from data.infra.database import Base

class OSCoverModel(Base):
  __tablename__ = 'os_capa'

id = Column(Integer, primary_key=True)
cod_empresa = Column(Integer, nullable=False)
numero_os = Column(Integer, nullable=False)
os_original = Column(Integer, nullable=False)
data_emissao = 
data_encerramento
data_cancelamento
data_ultima_atualizacao
razao_social
tipo
responsavel
chassi
veic_modelo
ano
km
placa
data_da_venda
status_os
numero_do_dealer
razao_social_dealer
valor_estimado_os