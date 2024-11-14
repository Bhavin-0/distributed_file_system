import requests

STORAGE_NODES = [
    'http://localhost:5001',
    'http://localhost:5002',
]

def sync_files():
    for node in STORAGE_NODES:
        response = requests.get(f'{node}/files')
        if response.ok:
            files = response.json()
            for filename in files:
                for other_node in STORAGE_NODES:
                    if other_node != node:
                        res = requests.get(f'{other_node}/files')
                        if filename not in res.json():
                            download = requests.get(f'{node}/download/{filename}')
                            requests.post(f'{other_node}/upload', files={'file': (filename, download.content)})

sync_files()
