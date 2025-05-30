import tweepy
import pyjokes
import time
import tweepy.errors
import random
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv(dotenv_path="./Apis.evn")

API_KEY = os.getenv("YOU API_KEY")
API_SECRET = os.getenv("YOU API_SECRET")
BEARER_TOKEN = os.getenv("YOU BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("YOU ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("YOU ACCESS_SECRET")

# Crear el cliente de Tweepy
client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

try:
    response = client.get_me()
    print("Conexión exitosa:", response.data)
except Exception as e:
    print("Error de conexión:", e)

# Configuración del query para buscar posts (tweets)
query = "Funny, imagefunny OR memes lang:en -is:retweet"

# Lista de hashtags relevantes
hashtags_list = [
    "#programming", "#humor", "#coding"
]

# Función para generar hashtags aleatorios
def generate_hashtags(hashtags_list, count = 3):
    return " ".join(random.sample(hashtags_list, count))

# Ciclo principal
while True:
    try:
        # Generar un chiste en inglés
        joke = pyjokes.get_joke(language = 'en', category = 'all')

        # Generar hashtags aleatorios
        hashtags = generate_hashtags(hashtags_list)

        # Validacion de la longitud del tweets
        tweet_text = f"{hashtags}\n\n{joke}"
        if len(tweet_text) > 280:
            tweet_text = tweet_text[:277] + "..."

        # Publicar el tweet (post)
        client.create_tweet(text = tweet_text)
        print("Tweet publicado: ", tweet_text)
        
        # Buscar tweets recientes (posts)
        tweets = client.search_recent_tweets(query=query, max_results=20)
        
        if tweets and tweets.data:
            for tweet in tweets.data:
                # Comprobar si el tweet es una respuesta
                if tweet.in_reply_to_user_id is None:
                    # Generar un chiste en ingles
                    joke = pyjokes.get_joke(language = 'en', category = 'all')
                    
                    # Generar hashtags aleatorios
                    hashtags = generate_hashtags(hashtags_list)

                    # Crear el texto del comentario
                    reply_text = f"🤖 Bot: {hashtags}\n\n{joke}"
                    
                    # Comentar el tweet original (post)
                    client.create_tweet(text = reply_text, in_reply_to_tweet_id = tweet.id)
                    print(f"Se ha comentado en el tweet (post): {tweet.id} con: {reply_text}")
                    
                    # Pausa para evitar spam
                    time.sleep(300)
                else:
                    print(f"El tweet {tweet.id} es una respuesta, no se ha comentado.")
        
        # Espera 15 minutos antes de volver a publicar un tweet (post)
        time.sleep(900)
        
    except tweepy.errors.TooManyRequests as e:
        print("Límite alcanzado. Esperando 15 minutos.")
        time.sleep(900)
        
    except Exception as e: 
        print("Error:", e)
        time.sleep(300)  # Espera 5 minutos ante un error inesperado
    finally:
        print("Reintentando...")
