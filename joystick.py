from machine import ADC, Pin
from time import *

canx = ADC(Pin(34))               # crée un objet ADC sur la broche 34
canx.atten(ADC.ATTN_11DB)         # étendue totale : 3.3V
cany = ADC(Pin(35))               # crée un objet ADC sur la broche 35
cany.atten(ADC.ATTN_11DB)         # étendue totale : 3.3V

bp = Pin(32, mode=Pin.IN, pull=Pin.PULL_UP)


while True:
    x = canx.read()        # conversion analogique-numérique 0-4095
    y = cany.read()        # conversion analogique-numérique 0-4095
    bouton = bp.value()
    print("Joystick | Axe X : ", x,", Axe Y : ",y, "Bouton = ", bouton)     # affichage sur la console REPL de la valeur numérique
    sleep_ms(100)