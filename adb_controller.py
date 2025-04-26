import subprocess

def obtener_dispositivos():
    resultado = subprocess.check_output(['adb', 'devices']).decode().splitlines()
    return [linea.split('\t')[0] for linea in resultado[1:] if 'device' in linea]

def ejecutar_comando(dispositivo, comando):
    subprocess.run(['adb', '-s', dispositivo] + comando)
