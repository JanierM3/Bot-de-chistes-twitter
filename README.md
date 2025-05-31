Bot de twitter que dice chistes de programacion

La idea al crear este bot fue meramente educativo la logica de este es simple 


✅1. IMPORTAR LAS LIBRERIAS
![image](https://github.com/user-attachments/assets/69bf1d3d-768a-42c1-a544-4da773baa7cb)

✅2. CARGAR VARIABLES DE ENTORNO:
![image](https://github.com/user-attachments/assets/17930a91-4363-4ff6-b32c-8742f3481b1c)

Se cargan las credenciales de la api de twitter de un archivo llamado Api.env
![image](https://github.com/user-attachments/assets/4bbd62ae-d31b-4eeb-8e8b-482382284b84)

✅3. CREAR EL CLIENTE DE TWEEPY
![image](https://github.com/user-attachments/assets/848b3176-98aa-4d99-a648-2fd70e597d13)

Se establece la conexión con la API de Twitter usando las credenciales, la try exept la uso para manejar erros de conexion con la api esto me ayuda a encontrar el  error mas rapido y solucionarlo.
Verifica si la conexion es valida imprimiendo la cuenta conectada.
![image](https://github.com/user-attachments/assets/adf1fd3f-f05b-4d27-970f-8f0530378da3)

✅4. PARAMETRO PARA BUSQUEDA Y HASHTAGS
![image](https://github.com/user-attachments/assets/510ae4ca-538b-4fd8-a010-82a1e9e74455)
![image](https://github.com/user-attachments/assets/40773e76-6ecd-4f97-b564-81129af5c623)
busca tweet que sean de humor o memes pero que no sean retweets

 ![image](https://github.com/user-attachments/assets/ee8910b0-a77b-414a-a61a-7569c6168f02)

 ![image](https://github.com/user-attachments/assets/a34c3a91-45a1-4d30-8feb-ef146b9ea3c4)

![image](https://github.com/user-attachments/assets/5ed254bb-45b1-49d1-b319-e2363ab2438f)

CONCLUSION

Este bot tiene algunos errores entre ellos esta el uso execivo de try except esto hace que el bot se ejecute lento y tambien uso demasiado time.sleep 

