from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher

# Diccionarios de traducción
TRADUCCIONES_NASA = {
    "kwe'sx uma kiwe îtxi": "Madre Tierra",
    "nasa we'sxa": "Pueblos indigenas"
}

TRADUCCIONES_NASA_2 = {
    "eka nasawe’sxa": "Estados",
    "nasa we’sx": "Participación Comunitaria"
}

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

        # Aplicar la traducción
        tierra_trad = traducir(tierra, TRADUCCIONES_NASA)
        autonomia_trad = traducir(autonomia, TRADUCCIONES_NASA)


        # Formatear y enviar el mensaje con las traducciones
        mensaje = f"Traducción: {tierra_trad} y {autonomia_trad}"
        dispatcher.utter_message(text=mensaje)
        return []

class ActionTraducirNasa2(Action):
    def name(self):
        return "action_traduccion_nasa_2" 

    def run(self, dispatcher, tracker, domain):
        # Obtener los valores de los slots
        estado = tracker.get_slot("Estados")
        participacion = tracker.get_slot("Participacion_Comunitaria")

        # Debug: Mostrar valores de los slots
        dispatcher.utter_message(text=f"DEBUG — Estado: '{estado}', Participación: '{participacion}'")

        # Validación de los slots
        if not estado and not participacion:
            dispatcher.utter_message(text="No se encontraron datos para traducir.")
            return []

        # Aplicar la traducción
        estado_trad = traducir(estado, TRADUCCIONES_NASA_2)
        participacion_trad = traducir(participacion, TRADUCCIONES_NASA_2)

        # Formatear y enviar el mensaje con las traducciones
        mensaje = f"Traducción: {estado_trad} y {participacion_trad}"
        dispatcher.utter_message(text=mensaje)
        return []
