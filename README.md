# 📱 Phone Farm Controller

Controlador automatizado para múltiples dispositivos Android conectados por USB, diseñado para manejar acciones básicas como abrir aplicaciones, tocar coordenadas específicas, hacer swipes, y más.

Este proyecto te permite controlar una granja de teléfonos desde un único punto de comando utilizando `adb` y scripts de Python.

---

## 🚀 Características

- Detecta automáticamente dispositivos Android conectados por USB.
- Ejecuta acciones automatizadas como:
  - Abrir aplicaciones por nombre de paquete.
  - Tocar coordenadas en la pantalla.
  - Ir a la pantalla de inicio.
- Control simultáneo de múltiples dispositivos.
- Modularidad para agregar nuevas acciones fácilmente.

---

## 📁 Estructura del Proyecto

## Comando para ejecutar los dos telefonos el mastro y esclavo
python .\mirror_controlado.py

## Comandos para ejecutar el entorno virtual en Windows
Primero se tiene que habilitar para poder ejecutar el scrip
 Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
Luego ejecutamos el entorno virtual situandonos en la carpeta que corresponde
 .\Activate.ps1


