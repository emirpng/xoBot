import os

from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv('API_ID', '9248715'))
API_HASH = os.getenv('API_HASH', 'a9c1288681c2d3265175ff96c619d064')
SESSION_NAME = os.getenv('SESSION_NAME', 'ragnar')
XO_BOT = os.getenv('XO_BOT', '5841942016:AAEUeDRIkS7IdlKKnNWHBme6T1GfKHQGeSM')
