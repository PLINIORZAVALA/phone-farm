import subprocess
import threading
import re

MAESTRO = "NSXDU17627001880"
ESCLAVOS = ["R92W500PNSL"]

def leer_eventos(maestro_id):
    print(f"[INFO] Escuchando eventos del maestro ({maestro_id})...")
    proceso = subprocess.Popen(['adb', '-s', maestro_id, 'shell', 'getevent', '-lt'], stdout=subprocess.PIPE, text=True)

    coord_x, coord_y = None, None

    for linea in proceso.stdout:
        if 'ABS_MT_POSITION_X' in linea:
            x = int(linea.split()[-1], 16)
            coord_x = x
        elif 'ABS_MT_POSITION_Y' in linea:
            y = int(linea.split()[-1], 16)
            coord_y = y
        elif 'SYN_REPORT' in linea and coord_x is not None and coord_y is not None:
            print(f"[EVENT] Tap detectado en ({coord_x}, {coord_y})")
            replicar_toque(coord_x, coord_y)
            coord_x, coord_y = None, None

def replicar_toque(x, y):
    for esclavo in ESCLAVOS:
        comando = ['adb', '-s', esclavo, 'shell', 'input', 'tap', str(x), str(y)]
        subprocess.run(comando)
        print(f"[REPLICA] Tap en {esclavo} -> ({x}, {y})")

if __name__ == "__main__":
    leer_eventos(MAESTRO)
