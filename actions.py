from adb_controller import ejecutar_comando
from config import PAQUETES, COORDENADAS

def abrir_app(dispositivo, app):
    paquete = PAQUETES.get(app)
    if paquete:
        comando = ['shell', 'monkey', '-p', paquete, '-c', 'android.intent.category.LAUNCHER', '1']
        ejecutar_comando(dispositivo, comando)

def tocar(dispositivo, x, y):
    comando = ['shell', 'input', 'tap', str(x), str(y)]
    ejecutar_comando(dispositivo, comando)

def ir_inicio(dispositivo):
    comando = ['shell', 'input', 'keyevent', '3']
    ejecutar_comando(dispositivo, comando)
