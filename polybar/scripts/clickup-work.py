import os
import requests
from dotenv import load_dotenv

envfile = os.path.join(os.path.expanduser('~'), '.config', 'polybar', '.env')
load_dotenv(envfile)

API_KEY = os.environ.get('CLICKUP_API_KEY', '')

try:
    response = requests.get(
        'https://api.clickup.com/api/v2/folder/114538688', headers={'Authorization': API_KEY})
except requests.exceptions.ConnectionError:
    exit()

if not response.ok:
    exit()

data = response.json()
task_count = int(data['task_count'])

if task_count > 0:
    print(' ', task_count)
