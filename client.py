import base64
from PIL import Image
import requests
import io

img = Image.open('imagens/imagem_positiva.png')
img = img.resize((8,8))

buffered = io.BytesIO()
img.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

url = 'http://localhost:8000/predict'

response = requests.post(url, json={'image': img_str})

print(response.json())