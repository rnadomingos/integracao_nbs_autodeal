from enum import Enum

class MetadatakeyCompany(Enum):
    gpbb = 2
    gpbl = 3
    gpbc = 4
    tiveo = 98

class MetadatakeyOSCover(Enum):
    numero_os = 430
    data_emissao = 431
    razao_social = 432
    tipo = 433
    responsavel = 434
    chassi = 435
    veic_modelo = 436
    ano = 437
    km = 494
    placa = 438
    data_da_venda = 439

class MetadatakeyOSClient(Enum):
    cod_empresa = MetadatakeyOSCover.numero_os.value
    numero_os = MetadatakeyOSCover.numero_os.value
    nome = 440
    cpf_cnpj = 441
    telefone = 442
    celular = 443

class MEtadatakeyOSServices(Enum):
    cod_empresa = MetadatakeyOSCover.numero_os.value
    numero_os = MetadatakeyOSCover.numero_os.value
    reclamacao = 444
    codigo_servico = 456
    codigo_defeito = 549
    descritivo = 445
    valor_mdo_os = 446
    valor_oc = 457
    quantidade_oc = 1010
    nr_sg = 546
    
class MetadatakeyOSItems(Enum):
    cod_empresa = MetadatakeyOSCover.numero_os.value
    numero_os = MetadatakeyOSCover.numero_os.value
    codigo_do_item = 458
    codigo_de_defeito = 534
    descritivo = 447
    valor_os = 448
    valor_oc = 459
    quantidade_oc = 1011
    nr_sg = 547
