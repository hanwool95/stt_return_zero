import json
import requests
import config

api_config = {'use_diarization': True, 'domain': 'CALL', 'diarization': {'spk_count': 2}}
resp = requests.post(
    'https://openapi.vito.ai/v1/transcribe',
    headers={'Authorization': 'bearer '+ config.SECRET_KEY},
    data={'config': json.dumps(api_config)},
    files={'file': open('voice_files/bosalpi2_202309151809586_050803510027_01051992168_01063571191.mp3', 'rb')}
)
resp.raise_for_status()
print(resp.json())