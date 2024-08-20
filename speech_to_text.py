import requests

def speech_to_text(file_path, url="https://arbazkhan-cs-speech-to-text.hf.space/transcribe", chunk_size=12090):  # 1 MB chunks
    headers = {'X-Complete': 'false'}
    
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break

            response = requests.post(url, data=chunk, headers=headers)
            if response.status_code != 200:
                print(f"Error: {response.json()}")
                return None
            print(response.json())
    
    headers['X-Complete'] = 'true'
    response = requests.post(url, data=b'', headers=headers)
    json_response = response.json()
    print(json_response)
    return json_response['transcript']

if __name__ == "__main__":
    print("Processing audio ...")
    audio_file_path = 'recorded_audio.raw'
    speech_to_text(audio_file_path)
