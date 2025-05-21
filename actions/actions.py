from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher

# Diccionarios de traducción
TRADUCCIONES_NASA = {
    "kwe'sx uma kiwe îtxi": "Madre Tierra",
    "nasa we'sxa": "Pueblos indigenas",
    "txanteywe'sxa": "Historia"
}

TRADUCCIONES_NASA_2 = {
    "eka nasawe'sxa": "Estados",
    "nasa we'sx": "Participación Comunitaria",
    "thêsa kiwe yuwe puiinxitxis eskhe vxitna yuhta": "derechos territoriales tradicionales"
}

# TRADUCCIONES_NASA_3 = {
#     "nasa' çxhab walan u'jn ûsta":"vulnerabilidad"

# }

# TRADUCCIONES_NASA_4 = {
#     "Çxhaçxçxhaçxha waki'jn u'jwena'w yuwe tuthtxis puuin": "resistiendo  y vamos a luchar"
# }

# TRADUCCIONES_NASA_5 = {
#     "Çaam atuwe'sxa": "actores armados",
#     "txãntey dxi'j kikxnxitxis kaasxigun": "procesos ancestrales memoriales"
# }

# TRADUCCIONES_NASA_6 = {
#     "fxiy fxiy nasa we'sxa'": "diversidad de pueblos indígenas",
#     "çxhaçxçxhaçxha yujun ûswa' yuuna": "resistencia"
# }

# TRADUCCIONES_NASA_7 = {
#     "Çxhaçxha yahtxte": "Resistencia pacifica",
#     "u'jwena çxhaçxçxhaçxha": "propuesta de transformación"
# }

# #limpiar comillas
# def clean_Comillas(frase):
#     return frase.replace("’","'")

# Función de traducción segura
def traducir(slot_value, traducciones):
    if not slot_value:
        return ""
    clave = slot_value.strip().lower()
    return traducciones.get(clave, slot_value)  

class ActionTraducirNasa(Action):
    def name(self):
        return "action_traduccion_nasa"  

    def run(self, dispatcher, tracker, domain):
        # Obtener los valores de los slots
        tierra = tracker.get_slot("Territorio_Madre_Tierra")
        autonomia = tracker.get_slot("Autonomia_Territorial")
        historia = tracker.get_slot("Memoria_Historica")

        # Aplicar la traducción
        tierra_trad = traducir(tierra, TRADUCCIONES_NASA)
        autonomia_trad = traducir(autonomia, TRADUCCIONES_NASA)
        historia_trad = traducir(historia, TRADUCCIONES_NASA)


        # Formatear y enviar el mensaje con las traducciones
        mensaje = f" El indigena se refiere a la existencia de una relación fundamental entre {tierra_trad} donde los {autonomia_trad} tejen  {historia_trad} en la comunidad."
        
        dispatcher.utter_message(text=mensaje)
        return []

class ActionTraducirNasa2(Action):
    def name(self):
        return "action_traduccion_nasa_2" 

    def run(self, dispatcher, tracker, domain):
        # Obtener los valores de los slots
        estado = tracker.get_slot("Estados")
        participacion = tracker.get_slot("Participacion_Comunitaria")
        derechoT = tracker.get_slot("Derecho_Territorial")

        # Aplicar la traducción
        estado_trad = traducir(estado, TRADUCCIONES_NASA_2)
        participacion_trad = traducir(participacion, TRADUCCIONES_NASA_2)
        derechoT_trad = traducir(derechoT, TRADUCCIONES_NASA_2)

        # Formatear y enviar el mensaje con las traducciones
        mensaje = f"El indigena se refiere  {estado_trad}, {participacion_trad} y {derechoT_trad}"
        dispatcher.utter_message(text=mensaje)
        return []

# class ActionTraducirNasa3(Action):
#     def name(self):
#         return "action_frase_3" 

#     def run(self, dispatcher, tracker, domain):
#         # Obtener los valores de los slots
#         desplazamiento= tracker.get_slot("Desplazamiento")

#         # Aplicar la traducción
#         desplazamiento_trad = traducir(desplazamiento, TRADUCCIONES_NASA_3)

#         # Formatear y enviar el mensaje con las traducciones
#         mensaje = f"El indigena se refiere  al conflicto armado en especial {desplazamiento_trad}"
#         dispatcher.utter_message(text=mensaje)
#         return []

# class ActionTraducirNasa4(Action):
#     def name(self):
#         return "action_frase_4" 

#     def run(self, dispatcher, tracker, domain):
#         # Obtener los valores de los slots
#         rUnidad = tracker.get_slot("Resistencia_Unidad")

#         # Aplicar la traducción
#         unidad_trad = traducir(rUnidad, TRADUCCIONES_NASA_4)

#         # Formatear y enviar el mensaje con las traducciones
#         mensaje = f"El indigena se refiere que vamos a seguir {unidad_trad} sin olvidar el tejido social."
#         dispatcher.utter_message(text=mensaje)
#         return []

# class ActionTraducirNasa5(Action):
#     def name(self):
#         return "action_frase_5" 

#     def run(self, dispatcher, tracker, domain):
#         # Obtener los valores de los slots
#         conflicto = tracker.get_slot("Conflicto_Armado")
#         historia = tracker.get_slot("Memoria_Historica")

#         # Aplicar la traducción
#         conflicto_trad = traducir(conflicto, TRADUCCIONES_NASA_5)
#         historia_trad = traducir(historia, TRADUCCIONES_NASA_5)

#         # Formatear y enviar el mensaje con las traducciones
#         mensaje = f"El indigena se refiere {conflicto_trad} han dejado profundas heridas marcando dolorosos momentos en los {historia_trad} del Cauca "
#         dispatcher.utter_message(text=mensaje)
#         return []

# class ActionTraducirNasa6(Action):
#     def name(self):
#         return "action_frase_6" 

#     def run(self, dispatcher, tracker, domain):
#         # Obtener los valores de los slots
#         diversidad = tracker.get_slot("Diversidad_Etnica_Cultural")
#         resistencia = tracker.get_slot("Resistencia_Pacificica")

#         # Aplicar la traducción
#         diversidad_trad = traducir(diversidad, TRADUCCIONES_NASA_6)
#         resistencia_trad = traducir(resistencia, TRADUCCIONES_NASA_6)

#         # Formatear y enviar el mensaje con las traducciones
#         mensaje = f"El indigena se refiere a construir un pais que respete {diversidad_trad} se ha unido a una sola voz {resistencia_trad} y la vida uniendose a una voz de {resistencia_trad}"
#         dispatcher.utter_message(text=mensaje)
#         return []
    
# class ActionTraducirNasa7(Action):
#     def name(self):
#         return "action_frase_7" 

#     def run(self, dispatcher, tracker, domain):
#         # Obtener los valores de los slots
#         resistencia = tracker.get_slot("Resistencia_Pacifica")
#         caminoR = tracker.get_slot("Caminos_Resistencia")

#         # Aplicar la traducción
#         resistencia_trad = traducir(resistencia, TRADUCCIONES_NASA_7)
#         caminoR_trad = traducir(caminoR, TRADUCCIONES_NASA_7)

#         # Formatear y enviar el mensaje con las traducciones
#         mensaje = f"El indigena se refiere a la {resistencia_trad} surge como {caminoR_trad} para la comunidad."
#         dispatcher.utter_message(text=mensaje)
#         return []
