from adb_controller import obtener_dispositivos
from actions import abrir_app, tocar, ir_inicio
from utils import log, esperar

def main():
    dispositivos = obtener_dispositivos()
    log(f"{len(dispositivos)} dispositivos detectados.")

    for d in dispositivos:
        log(f"Controlando {d}")
        abrir_app(d, "chrome")
        esperar(2)
        tocar(d, 500, 900)
        esperar(1)
        ir_inicio(d)

if __name__ == "__main__":
    main()
