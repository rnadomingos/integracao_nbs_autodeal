import  src.utils.metadatakeys as md

company = md.MetadatakeyCompany
os = md.MetadatakeyOSCover
os_client = md.MetadatakeyOSClient
os_service = md.MEtadatakeyOSServices
process = md.MetadatakeyProcess
os_items = md.MetadatakeyOSItems
os_related = md.MetadatakeyOSRelated

teste = {
    "CompanyId": company.tiveo.value,
    "ProcessId": process.garantia.value,
    "ObjectIdParent": "null",
    "Metadatas": [
        {
            "MetadataKeyId": os.numero_os.value,
            "MetadataValue": 89999,
            "MetadataOrder": "null"
        },
        {
            "MetadataKeyId": os_related.numero_os_relacionada.value,
            "MetadataValue": 70001,
            "MetadataOrder": 1
        },
        {
            "MetadataKeyId": os_related.numero_os_relacionada.value,
            "MetadataValue": 70002,
            "MetadataOrder": 2
        },
        {
            "MetadataKeyId": os.data_emissao.value,
            "MetadataValue": "31/03/2023 09:16",
            "MetadataOrder": "null"
        },
        {
            "MetadataKeyId": os.razao_social.value,
            "MetadataValue": "GPBB - BMW ALPHAVILLE",
            "MetadataOrder": "null"
        },
        {
            "MetadataKeyId": os.tipo.value,
            "MetadataValue": "M5 M5-RECALL MOTOS",
            "MetadataOrder": "null"
        },
        {
            "MetadataKeyId": os.responsavel.value,
            "MetadataValue": "DOMENICO MARCELO GUERREIRO",
            "MetadataOrder": "null"
        },
        {
            "MetadataKeyId": os.chassi.value,
            "MetadataValue": "99Z0M0002NZ903707",
            "MetadataOrder": "null"
        },
        {
            "MetadataKeyId": os.veic_modelo.value,
            "MetadataValue": "BMW MOTO R / R 1250 GS MU",
            "MetadataOrder": "null"
        },
        {
            "MetadataKeyId": os.ano.value,
            "MetadataValue": "21/22",
            "MetadataOrder": "null"
        },
        {
            "MetadataKeyId": os.km.value,
            "MetadataValue": 2000,
            "MetadataOrder": "null"
        },        
        {
            "MetadataKeyId": os.placa.value,
            "MetadataValue": "CBB 2F14",
            "MetadataOrder": "null"
        },        
        {
            "MetadataKeyId": os.data_da_venda.value,
            "MetadataValue": "01/02/2022",
            "MetadataOrder": "null"
        },        
        {
            "MetadataKeyId": os_client.nome.value,
            "MetadataValue": "COMPANY TEST",
            "MetadataOrder": "null"
        },        
        {
            "MetadataKeyId": os_client.cpf_cnpj.value,
            "MetadataValue": "12030750000195",
            "MetadataOrder": "null"
        },
        {
            "MetadataKeyId": os_client.telefone.value,
            "MetadataValue": "(11) 9769-9808",
            "MetadataOrder": "null"
        },
        {
            "MetadataKeyId": os_client.celular.value,
            "MetadataValue": "(11) 9 7699-9808",
            "MetadataOrder": "null"
        },
        {
            "MetadataKeyId": os_service.reclamacao.value,
            "MetadataValue": "Campanha automática: 0000232600, Ação Técnica Programação com função de proteção da transmissão",
            "MetadataOrder": 1
        },
        {
            "MetadataKeyId": os_service.codigo_servico.value,
            "MetadataValue": "0060712",
            "MetadataOrder": 1
        },
        {
            "MetadataKeyId": os_service.codigo_servico.value,
            "MetadataValue": "90023",
            "MetadataOrder": 1
        },
        {
            "MetadataKeyId": os_service.descritivo.value,
            "MetadataValue": "Atualizar a versão do software",
            "MetadataOrder": 1
        },
        {
            "MetadataKeyId": os_service.valor_mdo_os.value,
            "MetadataValue": "79.08",
            "MetadataOrder": 1
        },
        {
            "MetadataKeyId": os_items.codigo_do_item.value,
            "MetadataValue": "10000",
            "MetadataOrder": 1
        },
        {
            "MetadataKeyId": os_items.codigo_de_defeito.value,
            "MetadataValue": "09786",
            "MetadataOrder": 1
        },
        {
            "MetadataKeyId": os_items.descritivo.value,
            "MetadataValue": "CHIP XYZ",
            "MetadataOrder": 1
        },
        {
            "MetadataKeyId": os_items.valor_os.value,
            "MetadataValue": "20.00",
            "MetadataOrder": 1
        },
        {
            "MetadataKeyId": os.valor_estimado_os.value,
            "MetadataValue": "99.08",
            "MetadataOrder": "null"
        }
    ],
    "Comments": [],
    "Files": [ ],
    "ActionValue": "REGISTRAR"
}