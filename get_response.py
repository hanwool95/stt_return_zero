import requests

import config

resp = requests.get(
    'https://openapi.vito.ai/v1/transcribe/'+ config.TEST_TRANSCRIBE_ID,
    headers={'Authorization': 'bearer '+config.SECRET_KEY},
)
resp.raise_for_status()
print(resp.json())