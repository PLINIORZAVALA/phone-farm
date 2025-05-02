from adb_controller import ejecutar_comando
from config import PAQUETES
from utils import log, esperar

DISPOSITIVOS = [
    "NSXDU17627001880",  # Maestro
    "R92W500PNSL"        # Esclavo
]

def abrir_app_en_todos(app_nombre):
    paquete = PAQUETES.get(app_nombre)
    if not paquete:
        log(f"No se encontró el paquete para {app_nombre}")
        return

    for d in DISPOSITIVOS:
        log(f"Abrir {app_nombre} en {d}")
        comando = ['shell', 'monkey', '-p', paquete, '-c', 'android.intent.category.LAUNCHER', '1']
        ejecutar_comando(d, comando)
        esperar(1)

if __name__ == "__main__":
    abrir_app_en_todos("metatrader")
