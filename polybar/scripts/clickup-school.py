import os
import requests
from dotenv import load_dotenv

envfile = os.path.join(os.path.expanduser('~'), '.config', 'polybar', '.env')
load_dotenv(envfile)

API_KEY = os.environ.get('CLICKUP_API_KEY', '')

try:
    response = requests.get(
        'https://api.clickup.com/api/v2/space/14976905/list', headers={'Authorization': API_KEY})
except requests.exceptions.ConnectionError:
    exit()

if not response.ok:
    exit()

data = response.json()

task_count = 0
for lst in data['lists']:
    task_count += lst.get('task_count', 0)

if task_count > 0:
    print(task_count)
