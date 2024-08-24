import os
import random
import discord

# Configuración del cliente
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!meme':
        try:
            # Ruta completa a la carpeta de imágenes
            image_folder = 'C:/Users/User/OneDrive/Escritorio/Proyecto/Memes-Mios'
            image_files = ['meme1.jpg', 'meme2.jpg', 'meme3.jpg']

            # Seleccionar un archivo aleatorio
            selected_image = random.choice(image_files)
            file_path = f'{image_folder}/{selected_image}'

            # Imprimir la ruta para depuración
            print(f'Intentando abrir: {file_path}')

            # Abrir y enviar la imagen seleccionada
            with open(file_path, 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file=picture)

        except Exception as e:
            await message.channel.send(f"Ocurrió un error: {e}")

client.run('Token')




