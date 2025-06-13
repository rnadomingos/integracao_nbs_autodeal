import requests as req
import json

# LOGON PARAMS
URL_API = 'https://hmlsvc.organizaprime.com.br'
USERLOGIN = 'tiveo.service'
USERPASSWORD = 'r7?P2c#E'
GRANT_TYPE = 'password'

# JSON LOAD TO SEND TEST
with open('dados.json', 'r', encoding='utf-8') as f:
    json_load = json.load(f)

# CONVERT VARIABLE TO JSON DUMP 
send_json = json.dumps(json_load)

# MAKE HEADER TO LOGON
headers_login = {'Content-Type':'application/x-www-form-urlencoded'}
payload = {
  'username': USERLOGIN,
  'password': USERPASSWORD,
  'grant_type': GRANT_TYPE
}

# GEN TOKEN TO ACCESS FUNCTION 
def get_token_acesso():
    '''
    Function to receive token
    '''
    response = req.post(f'{URL_API}/api/token', data=payload, headers=headers_login)
    token = response.json()
    return token['access_token']

# ASSIGN TOKEN
token = get_token_acesso()

# MAKE HEADER TO SEND CREATE PROCESS IN AUTO DEAL
headers_process = {'Content-Type':'application/json', 'accept':'*/*', "authorization":f'bearer {token}'}

#SEND DATA TO CREATE PROCESS
response_teste = req.post(f'{URL_API}/api/instance/start', data=send_json, headers=headers_process )

#PRINT RESULT
print('Return: ', response_teste.json(), 'status code:', response_teste.status_code)

#if __name__=='__main__': 
