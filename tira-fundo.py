### instalar pip install rembg ###

from rembg import remove
from PIL import Image
import os

input_path = 'imagem.jpg' # Aqui você adiciona a imagem que deseja remover o fundo #
output_path = 'semfundo.png' # Aqui você adiciona o nome da imagem que será gerada #

valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')


if not os.path.exists(input_path):
    print(f"Erro: O arquivo '{input_path}' não foi encontrado.")
elif not input_path.lower().endswith(valid_extensions):
    print("Erro: O arquivo deve ser uma imagem nos formatos JPG, JPEG, PNG, BMP ou GIF.")
else:
    try:
        
        with Image.open(input_path) as img:
            output = remove(img)
            output.save(output_path)
            print(f"Imagem salva como '{output_path}' com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar a imagem: {e}")