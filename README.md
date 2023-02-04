# ChatGPT
¿Quieres usar ChatGPT en Python?

<div align="center">
<img src="https://cdn.fstoppers.com/styles/full/s3/media/2022/12/08/chatgpt_screen_rec_cropped.gif" width="600">
</div>

## 1. Entra a la página de OpenAI
https://platform.openai.com/

Tienes que registrarte, ya sea con tu correo o cuenta de Google. 

## 2. Obtén tu API KEY
La API KEY sirve para tener acceso a ChatGPT, para obtenerla búscala en tu cuenta y das click en "View Api Keys"
En la parte de la izquierda podrás ver hasta abajo la sección de Api Keys. 
<b>Tienes que crear una nueva en "Create new secret key"</b>

## 3. Librerias necesarias
Abre una nueva carpeta para comenzar tu proyecto e instala la libreria de open sea con el siguiente comando: 

-> <b>pip install openai</b>

## 4. Crea un archivo de python y copia el código. 
```python
import openai
import config


openai.api_key = config.API_KEY

model_engine = "text-davinci-003"
prompt = "Quién es Pikachu?"

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5
)

response = completion.choices[0].text
print(response)
```

En la variable openai.api_key debes pegar tu api key así: 
```
openai.api_key = config.API_KEY = "TU API KEY"
```

## 5. Dile algo
Para hacer esto es necesario modificar la variable <b>prompt</b> y una vez que lo hagas ya esta casi todo listo!

## 6. Corre el programa
Puede ejecutar un programa de Python en la consola de la siguiente manera:

1. Abra la consola o el terminal en su computadora.

2. Navegue hasta la ubicación del archivo Python utilizando el comando cd seguido de la ruta del archivo. Por ejemplo, si su archivo está en la carpeta Documents, puede navegar hasta allí con el comando cd Documents.

3. Escriba el comando python seguido del nombre del archivo. Por ejemplo, si el nombre de su archivo es hello.py, puede ejecutar el archivo con el comando python hello.py.

Si su archivo Python está escrito correctamente, se ejecutará y se mostrarán los resultados en la consola.

Tenga en cuenta que debe tener instalado Python en su computadora para poder ejecutar archivos Python en la consola.
