import random


def handle_responses(message) -> str:
    p_message = message.lower()

    if p_message == "hola paco":
      return "Hola me llamo paco"
    
    if p_message == "como estas?":
     return "Bien y tu? Como estan Harlys y Maria?"
    
    if p_message == "dame un numero random":
      return str(random.ranInt(1,6))
    
    if p_message == "a los capys les gustan los patos?":
      return "Claro que si, somos muy amigos... y aveces no, son muy peligrosos"
    
    if p_message == "luis ama a maria?":
     return "El la ama con su vida, el nos ha dicho eso"
    
    if p_message == "que elegante estas hoy":
      return "Muchas gracias caballero, usted tambien"
    
    if p_message == "todo bien por aqui":
     return "Me alegra mi compatriota"
