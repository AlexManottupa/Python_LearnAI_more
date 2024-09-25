import pywhatkit as kit
import time
from datetime import datetime

# Número de WhatsApp al que se enviarán los mensajes.
numero = "+51904306242"  # Asegúrate de usar el formato completo con código de país.

# Mensaje que se enviará.
mensaje = "Hola, espero que te guste la idea de automatizar las cosas, la IA es el futuro."

# Cantidad de mensajes que deseas enviar.
cantidad_mensajes = 10

# Intervalo de tiempo en segundos entre cada mensaje.
intervalo = 60  # Puedes ajustar esto según tus necesidades.

# Función para enviar los mensajes.
for i in range(cantidad_mensajes):
    try:
        # Obtener la hora y minuto actual.
        ahora = datetime.now()
        hora_envio = ahora.hour
        minuto_envio = ahora.minute + 1  # Agregar un minuto para programar el envío.

        # Enviar mensaje de inmediato.
        kit.sendwhatmsg(numero, f"{mensaje} (Mensaje {i + 1})", hora_envio, minuto_envio, 15, True, 2)

        # Esperar para el próximo mensaje.
        print(f"Mensaje {i + 1} enviado automáticamente a las {hora_envio}:{minuto_envio}.")
        
        # Esperar antes de enviar el próximo mensaje.
        time.sleep(intervalo)

    except Exception as e:
        print(f"Error al enviar el mensaje {i + 1}: {e}")
