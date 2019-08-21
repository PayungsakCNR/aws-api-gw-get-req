'''
AWS API Gateway Request by GET Method.
for this example , this is json output:
  {
    "data1" : "This is Data 1" 
  }

Please set up your AWS Access Key , Secret Key , your involk host , region in .env file

Please install python-dotenv  , aws-requests-auth using this command ->

pip3 install aws-requests-auth
pip3 install python-dotenv

'''

import os
import requests
from dotenv import load_dotenv
from aws_requests_auth.aws_auth import AWSRequestsAuth

load_dotenv()

auth = AWSRequestsAuth(aws_access_key = os.getenv("accessKey"),
                       aws_secret_access_key = os.getenv("secretKey"),
                       aws_host = os.getenv("apiHost"),
                       aws_region = os.getenv("region"),
                       aws_service ='execute-api')

headers = {
  'x-api-key': os.getenv("apiKey"), # If you enable API Key.
  'x-your-custom-header': os.getenv("your-custom-header") # Your custom header.
}


response = requests.get(os.getenv("apiUrl"),auth=auth, headers=headers)
jsonRes = response.json()

if response.status_code == 200: # If return 200 OK
  print('Data1: ' + str(jsonRes['data1']))
else:
  print(response.status_code)
  print(str(jsonRes['message']))
