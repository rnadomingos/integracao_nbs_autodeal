import requests as req

URL_API = 'https://hmlsvc.organizaprime.com.br'
USERLOGIN = 'tiveo.service'
USERPASSWORD = 'r7?P2c#E'
GRANT_TYPE = 'password'

headers = {'Content-Type': 'application/x-www-form-urlencoded'}
payload = {
  'username': USERLOGIN,
  'password': USERPASSWORD,
  'grant_type': GRANT_TYPE
}


def get_token_acesso():
    response = req.post(f'{URL_API}/api/token', data=payload, headers=headers)
    token = response.json()
    return token['access_token']


if __name__=='__main__': 
    None
