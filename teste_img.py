import plotly.express as px
import base64

def get_file_content(file_path):
    '''
    Get text file content
    '''

    with open(file_path, "r", encoding='utf-8') as file:
        file_content = file.read()
    return file_content


# Cria a figura
fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])

# Transforma ela no formato correto
img_binary_64 = base64.b64encode(fig.to_image(format="png")).decode('utf-8')

# Lê o arquivo html base
html_content=get_file_content("base.html")

# Salva o arquivo com a figura "anexada"
with open("result.html", "w", encoding='utf-8') as html_file:
    html_file.write(html_content.format(img_binary=img_binary_64))

print("Salvou arquivo html!")