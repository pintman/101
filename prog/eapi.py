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


# EA-Modul
# Standard Pin-Belegung:
# 3,3V=1 
# Taster0=29, Taster1=31,
# LED: rot=33, gelb=35, gruen=37
# GND=39
