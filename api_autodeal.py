from dotenv import load_dotenv
import requests as req
import json
import os

load_dotenv()

# LOGON PARAMS
URL_API = os.getenv("URL_API")
USERLOGIN = os.getenv("USERLOGIN")
USERPASSWORD = os.getenv("USERPASSWORD")
GRANT_TYPE = os.getenv("GRANT_TYPE")

# JSON LOAD TO SEND TEST
with open('dados.json', 'r', encoding='utf-8') as f:
    json_load = json.load(f)

# CONVERT VARIABLE TO JSON DUMP 
send_json = json.dumps(json_load)


# GEN TOKEN TO ACCESS FUNCTION 
def get_token_acesso():
    '''
    Function to receive token
    '''
    # MAKE HEADER TO LOGON
    headers_login = {'Content-Type':'application/x-www-form-urlencoded'}
    payload = {
      'username': USERLOGIN,
      'password': USERPASSWORD,
      'grant_type': GRANT_TYPE
    }

    response = req.post(f'{URL_API}/api/token', data=payload, headers=headers_login)
    token = response.json()
    return token['access_token']

def create_process():
    '''
    Function to create a new process
    '''
    # ASSIGN TOKEN
    token = get_token_acesso()

    # MAKE HEADER TO SEND CREATE PROCESS IN AUTO DEAL
    headers_process = {'Content-Type':'application/json', 'accept':'*/*', "authorization":f'bearer {token}'}

    #SEND DATA TO CREATE PROCESS
    response_teste = req.post(f'{URL_API}/api/instance/start', data=send_json, headers=headers_process )

    #PRINT RESULT
    process = {
        'body': response_teste.json(), 
        'status code': response_teste.status_code
    }
    print('retorno: ', process)
    return process

if __name__=='__main__': 

  create_process()