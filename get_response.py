import csv
import requests

import config

def save_result(csv_name, updated_data):
    # 결과를 새로운 CSV 파일로 저장
    with open(csv_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in updated_data:
            writer.writerow(row)

def update_csv_with_transcriptions(input_csv, output_csv, secret_key):
    # CSV 파일 읽기
    with open(input_csv, 'r') as file:
        reader = csv.reader(file)
        transcribe_ids = [row[0] for row in reader]

    # 결과를 저장할 리스트 초기화
    updated_data = []

    count = 0
    try:
        # 각 transcribe ID에 대해 API 호출 및 결과 저장
        for transcribe_id in transcribe_ids:
            print(count)

            response = requests.get(
                f'https://openapi.vito.ai/v1/transcribe/{transcribe_id}',
                headers={'Authorization': f'Bearer {secret_key}'}
            )
            response.raise_for_status()
            result = response.json()

            # 각 utterance에 대한 정보 저장
            for utterance in result['results']['utterances']:
                updated_data.append([result['id'], utterance['spk'], utterance['msg']])
            count += 1
    except:
        save_result(output_csv, updated_data)

    # 결과를 새로운 CSV 파일로 저장
    save_result(output_csv, updated_data)


# 이 함수를 사용하여 'output.csv' 파일을 읽고 각 ID에 대한 응답을 받아 'updated_output.csv'에 저장
# config.SECRET_KEY를 여기에 직접 입력하거나 다른 방식으로 제공해야 합니다.
update_csv_with_transcriptions('output.csv', 'updated_output.csv', config.SECRET_KEY)

