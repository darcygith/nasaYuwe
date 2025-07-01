from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher

# Diccionarios de traducción
TRADUCCIONES_NASA = {
    "kwe'sx uma kiwe îtxi": "Madre Tierra",
    "nasa we'sxa": "Pueblos indigenas",
    "txanteywe'sxa": "Historia"
}
TRADUCCIONES_NASA_1_2 = {
    "Kwe'sx uma kiwe meewãça": "Sin la Madre Tierra",
    "nasawe'sx fxi'zeçxa çxhãçxha ûsnxi": "no hay tradiciones culturales",
}

TRADUCCIONES_NASA_2 = {
    "eka nasawe'sxa": "Estados",
    "nasa we'sx": "Participación Comunitaria",
    "thêsa kiwe yuwe puiinxitxis eskhe vxitna yuhta": "derechos territoriales tradicionales"
}

TRADUCCIONES_NASA_3 = {
    "çxhab walan u'jn ûsta":"vulnerables"

 }

TRADUCCIONES_NASA_4 = {
    "Çxhaçxçxhaçxha waki'jn u'jwena'w yuwe tuthtxis puuin": "resistiendo  y vamos a luchar"
 }

TRADUCCIONES_NASA_5 = {
    "Çaam atuwe'sxa'": "actores armados",
    "txãntey dxi'j kikxnxitxis kaasxigun": "procesos ancestrales memoriales"
}

TRADUCCIONES_NASA_6 = {
    "fxiy fxiy nasa we'sxa": "diversidad de pueblos indígenas",
    "çxhaçxçxhaçxha yujun ûswa' yuuna": "resistencia"
}

TRADUCCIONES_NASA_7 = {
    "Çxhaçxha yahtxte": "Resistencia pacifica",
    "u'jwena çxhaçxçxhaçxha": "propuesta de transformación"
}

TRADUCCIONES_NASA_8 = {
    "kwe'sx uma kiwes puiinxi": "luchar por nuestra Madre tierra",
    "kiwe pa'ka meh puîn ûsthaw": "liberando nuestra Madre Tierra",
    "kwe'sx uma kiwe puiinxi": "Recuperar de nuestra Madre Tierra"
}

TRADUCCIONES_NASA_9 = {
    "kwe'sx uma kiwe puiinxi dxi'j": "los procesos de la lucha por la tierra",
    "neeyunxa  ûs yahtxna u'jwa'json": "memorias historicas",
    "Kwe'sx uma kiwe pa'ka puuîn": "lucha por la Madre Tierra",
    "txãw yuçxha'wãt fxi'zena'w": "recuperar nuestra dignidad humana"
}

TRADUCCIONES_NASA_10 = {
    "txanteywe'sxa": "ancestrales memoriales",
    "Ksxa'w we'sxyak neesnxi": "Seres Espirituales"
}

TRADUCCIONES_NASA_11 = {
    "kwe'sx uma kiwe": "Nuestro Territorio",
    "nasawe'sx fxi'zeçxa çxhãçxha ûsnxi": "Tradiciones Culturales",
    "ukawe'sxa": "Autoridades Propias"
}
# #limpiar comillas
# def clean_Comillas(frase):
#     return frase.replace("’","'")

# Función de traducción segura
def traducir(slot_value, traducciones):
    if not slot_value:
        return ""
    clave = slot_value.strip()
    return traducciones.get(clave, slot_value)  

class ActionTraducirNasa(Action):
    def name(self):
        return "action_frase_123"  

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
        mensaje = f" El indígena se refiere a la profunda relación entre {tierra_trad}, la {historia_trad} y la sabiduría de su pueblo. Para los {autonomia_trad}, la tierra es vida, memoria y espiritualidad; su cuidado es colectivo y refleja la autonomía para decidir sobre su uso y protección."
        
        
        dispatcher.utter_message(text=mensaje)
        return []

# class ActionTraducirNasa(Action):
#     def name(self):
#         return "action_frase_1_2"  

#     def run(self, dispatcher, tracker, domain):
#         # Obtener los valores de los slots
#         ter = tracker.get_slot("Territorio_Madre_Tierra")
#         autonomia = tracker.get_slot("Cultura_Autonomia")

#         # Aplicar la traducción
#         ter_trad = traducir(ter, TRADUCCIONES_NASA_1_2)
#         autonomia_trad = traducir(autonomia, TRADUCCIONES_NASA_1_2)

#         # Formatear y enviar el mensaje con las traducciones
#         mensaje = f" El indígena se refiere que  {ter_trad}, la {autonomia_trad}  ni posibilidad para los pueblos indígenas"
        
#         dispatcher.utter_message(text=mensaje)
#         return []
    
class ActionTraducirNasa2(Action):
    def name(self):
        return "action_frase_45" 

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
        mensaje = f"El indígena se refiere al derecho de ser consultado de buena fe por los {estado_trad} antes de que se aprueben proyectos que afecten sus tierras. Sin embargo, estos han ignorado históricamente la {participacion_trad} y los { derechoT_trad} de los pueblos indígenas, priorizando intereses externos."

        dispatcher.utter_message(text=mensaje)
        return []

class ActionTraducirNasa3(Action):
    def name(self):
        return "action_frase_6" 

    def run(self, dispatcher, tracker, domain):
        # Obtener los valores de los slots
        desplazamiento= tracker.get_slot("Desplazamiento")
        print(f"Valor slot Desplazamiento: '{desplazamiento}'")

        # Aplicar la traducción
        desplazamiento_trad = traducir(desplazamiento, TRADUCCIONES_NASA_3)

        # Formatear y enviar el mensaje con las traducciones
        mensaje = f"El indigena se refiere  al conflicto armado en especial las personas {desplazamiento_trad}"
        dispatcher.utter_message(text=mensaje)
        return []

class ActionTraducirNasa4(Action):
    def name(self):
        return "action_frase_50" 

    def run(self, dispatcher, tracker, domain):
        # Obtener los valores de los slots
        rUnidad = tracker.get_slot("Resistencia_Unidad")

        # Aplicar la traducción
        unidad_trad = traducir(rUnidad, TRADUCCIONES_NASA_4)

        # Formatear y enviar el mensaje con las traducciones
        mensaje = f"El indigena se refiere que vamos a seguir {unidad_trad} sin olvidar el tejido social."
        dispatcher.utter_message(text=mensaje)
        return []

class ActionTraducirNasa5(Action):
    def name(self):
        return "action_frase_43_45" 

    def run(self, dispatcher, tracker, domain):
        # Obtener los valores de los slots
        conflicto = tracker.get_slot("Conflicto_Armado")
        historia = tracker.get_slot("Memoria_Historica")

        # Aplicar la traducción
        conflicto_trad = traducir(conflicto, TRADUCCIONES_NASA_5)
        historia_trad = traducir(historia, TRADUCCIONES_NASA_5)

        # Formatear y enviar el mensaje con las traducciones
        mensaje = f"El indigena se refiere {conflicto_trad} han dejado profundas heridas marcando dolorosos momentos en los {historia_trad} del Cauca "
        dispatcher.utter_message(text=mensaje)
        return []

class ActionTraducirNasa6(Action):
    def name(self):
        return "action_frase_42_46" 

    def run(self, dispatcher, tracker, domain):
        # Obtener los valores de los slots
        diversidad = tracker.get_slot("Diversidad_Etnica_Cultural")
        resistencia = tracker.get_slot("Resistencia_Pacificica")

        # Aplicar la traducción
        diversidad_trad = traducir(diversidad, TRADUCCIONES_NASA_6)
        resistencia_trad = traducir(resistencia, TRADUCCIONES_NASA_6)

        # Formatear y enviar el mensaje con las traducciones
        mensaje = f"El indigena se refiere a construir un pais que respete {diversidad_trad} se ha unido a una sola voz {resistencia_trad}"
        dispatcher.utter_message(text=mensaje)
        return []
    
class ActionTraducirNasa7(Action):
    def name(self):
        return "action_frase_49" 

    def run(self, dispatcher, tracker, domain):
        # Obtener los valores de los slots
        resistencia = tracker.get_slot("Resistencia_Pacifica")
        caminoR = tracker.get_slot("Caminos_Resistencia")

        # Aplicar la traducción
        resistencia_trad = traducir(resistencia, TRADUCCIONES_NASA_7)
        caminoR_trad = traducir(caminoR, TRADUCCIONES_NASA_7)

        # Formatear y enviar el mensaje con las traducciones
        mensaje = f"El indigena se refiere a la {resistencia_trad} surge como {caminoR_trad} para la comunidad."
        dispatcher.utter_message(text=mensaje)
        return []

class ActionTraducirNasa8(Action):
    def name(self):
        return "action_frase_33_34_35" 

    def run(self, dispatcher, tracker, domain):
        # Obtener los valores de los slots
        lucha_tierras = tracker.get_slot("Recuperacion_Tierras_Resguardo")
        libertad_tierras = tracker.get_slot("Recuperacion_Tierras_Resguardo")
        recuper_tierras = tracker.get_slot("Recuperacion_Tierras_Resguardo")

        # Aplicar la traducción
        lucha_trad = traducir(lucha_tierras, TRADUCCIONES_NASA_8)
        libertad_trad = traducir(libertad_tierras, TRADUCCIONES_NASA_8)
        recup_trad = traducir(recuper_tierras, TRADUCCIONES_NASA_8)

        # Formatear y enviar el mensaje con las traducciones
        mensaje = f"El indigena se refiere a la {lucha_trad} donde el departamento del Cauca estamos {libertad_trad} y {recup_trad} ha sido una causa histórica del movimiento indigena."
        dispatcher.utter_message(text=mensaje)
        return []

class ActionTraducirNasa9(Action):
    def name(self):
        return "action_frase_38_39" 

    def run(self, dispatcher, tracker, domain):
        # Obtener los valores de los slots
        proceso_tierras = tracker.get_slot("Recuperacion_Tierras_Resguardo")
        historico = tracker.get_slot("Memoria_Historico")
        lucha_tierras = tracker.get_slot("Recuperacion_Tierras_Resguardo")
        recuper = tracker.get_slot("(Dignidad_Humana")

        # Aplicar la traducción
        proceso_trad = traducir(proceso_tierras, TRADUCCIONES_NASA_9)
        historico_trad = traducir(historico, TRADUCCIONES_NASA_9)
        lucha_trad = traducir(lucha_tierras, TRADUCCIONES_NASA_9)
        recup_trad = traducir(recuper, TRADUCCIONES_NASA_9)

        # Formatear y enviar el mensaje con las traducciones
        mensaje = f"El indigena se refiere a la {proceso_trad} son tambien{historico_trad}  y la {lucha_trad}  tambien es  {recup_trad}"
        dispatcher.utter_message(text=mensaje)
        return []

class ActionTraducirNasa10(Action):
    def name(self):
        return "action_frase_41_48" 

    def run(self, dispatcher, tracker, domain):
        # Obtener los valores de los slots
        historico = tracker.get_slot("Memoria_Historico")
        esp = tracker.get_slot("Espiritualidad_Nasa")

        # Aplicar la traducción
        historico_trad = traducir(historico, TRADUCCIONES_NASA_10)
        esp_trad = traducir(esp, TRADUCCIONES_NASA_10)

        # Formatear y enviar el mensaje con las traducciones
        mensaje = f"El indigena se refiere a los procesos  {historico_trad} han guiado nuestros pasos, los {esp_trad} fortalecen la resistencia frente a la violencia."
        dispatcher.utter_message(text=mensaje)
        return []

class ActionTraducirNasa11(Action):
    def name(self):
        return "action_frase_37_40_45" 

    def run(self, dispatcher, tracker, domain):
        # Obtener los valores de los slots
        defensa = tracker.get_slot("Defensa_Territorio")
        autonomia  = tracker.get_slot("Cultura_Autonomia")
        autoridad  = tracker.get_slot("Autoridad_Propia")

        """
        "kwe'sx uma kiwe": "Nuestro Territorio",
        "kwe'sx fxi'zenxitxis": "Tradiciones Culturales",
        "ukawe'sxa": "Autoridades Propias"
        """
        # Aplicar la traducción
        defensa_trad = traducir(defensa, TRADUCCIONES_NASA_11)
        autonomia_trad = traducir(autonomia, TRADUCCIONES_NASA_11)
        autoridad_trad = traducir(autoridad, TRADUCCIONES_NASA_11)

        # Formatear y enviar el mensaje con las traducciones
        mensaje = f"El indigena se refiere cuando {defensa_trad} ha enfrentado intereses extractivos y armados, siendo las {autonomia_trad} han sido atacadas, pero no han podido vencer, y aun las {autoridad_trad} han sufrido amenazas y asesinatos"
        dispatcher.utter_message(text=mensaje)
        return []