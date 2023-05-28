# downloadmusic.py

## Instalação
```bash
pip install pafy
pip install youtube_dl
pip install python-dotenv
```
---
## Uso
No arquivo lista.txt, coloque o link da playlist que deseja baixar e o nome que deseja no seguinte formato:
```
https://www.youtube.com/playlist?list=aaaaa -- teste
```
---
## Pré-requisitos
Deve se ter uma chave registrada no Google API com permissões para utilizar a API do Youtube. Somente é utilizada para listar os links da playlist, para que seja feito o download individualmente pelo programa.

Crie um arquivo .env com a seguinte sintaxe:
```
GOOGLE_API_ID="SEU ID FICA AQUI"
MAIN_PATH="CAMINHO DE ARMAZENAMENTO DOS AUDIOS"
```

### Ferramenta utilizada estritamente para estudo e testes.