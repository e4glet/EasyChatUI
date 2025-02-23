import requests
import json

response = requests.post(
    "http://localhost:8000/v1/chat/completions",
    json={
        "messages": [{"role": "user", "content": "解释人工智能"}],
        "stream": True
    },
    stream=True
)

for line in response.iter_lines():
    if line:
        decoded = line.decode('utf-8').strip()
        if decoded.startswith('data: '):
            content = decoded[6:]
            if content == '[DONE]':
                break
            try:
                data = json.loads(content)
                print(data['choices'][0]['delta'].get('content', ''), end='', flush=True)
            except:
                pass