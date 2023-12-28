import os
import csv
import json
import requests
import config


# 폴더 내의 모든 파일을 찾는 함수
def find_files(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.mp3')]


# API 호출 및 ID 추출 함수
def call_api(file_path, api_config):
    with open(file_path, 'rb') as file:
        resp = requests.post(
            'https://openapi.vito.ai/v1/transcribe',
            headers={'Authorization': 'bearer ' + config.SECRET_KEY},
            data={'config': json.dumps(api_config)},
            files={'file': file}
        )
        resp.raise_for_status()
        return resp.json().get('id')


# 메인 프로세스
def process_files(directory):
    api_config = {'use_diarization': True, 'domain': 'CALL', 'diarization': {'spk_count': 2}}
    file_paths = find_files(directory)
    ids = []

    count = 0
    try:
        for file_path in file_paths:
            id = call_api(file_path, api_config)
            if id:
                ids.append(id)
            count += 1
            print(count)
            print(id)
    except:
        print(ids)
        # CSV 파일로 저장
        with open('output.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            for id in ids:
                csvwriter.writerow([id])

    # CSV 파일로 저장
    with open('output.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for id in ids:
            csvwriter.writerow([id])


# 'voice_files' 폴더의 파일들을 처리
process_files('voice_files')