# eapi-Bibliothek
# Installation: pip install eapi
# Hilfe: 
#  python -m pydoc eapi.hw
#  github.com/pintman/ea_rpi_modul

from eapi.hw import EAModul
eam = EAModul()
eam.schalte_led(EAModul.LED_ROT, True)
eam.cleanup()

def taster0_gedrueckt(pin):
  print("Taster 0 wurde gedrückt.")
eam = EAModul()
eam.taster_event_registrieren(0, taster0_gedrueckt)
