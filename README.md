# 🧮 Calculadora Científica en Python

Una calculadora versátil desarrollada en Python que ofrece tanto funciones básicas como científicas, con interfaz de terminal y gráfica. Además, guarda el historial de operaciones realizadas por el usuario.

---

## ✨ Características

✅ **Operaciones Básicas**  
- Suma  
- Resta  
- Multiplicación  
- División  

🧠 **Funciones Científicas**  
- Raíz cuadrada  
- Seno y coseno (en grados)  
- Logaritmo natural  

📝 **Extras**  
- Guardado de historial en `historial.txt`  
- Conversión de resultados a palabras (del 0 al 10)  
- Interfaz gráfica opcional con `tkinter`

---

## 📁 Estructura del Proyecto

```
calculadora-cientifica/
├── calculadora/
│   ├── main.py          # Versión terminal
│   ├── gui.py           # Versión gráfica
│   ├── cientifica.py    # Funciones científicas
│   ├── saludo.py        # Mensajes de bienvenida/despedida
│   ├── historial.py     # Gestión de historial
│   └── __init__.py
├── tests/
│   └── __init__.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🛠️ Requisitos

- Python **3.8 o superior**

---

## 🚀 Instalación y Uso

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/calculadora-cientifica.git
   cd calculadora-cientifica
   ```

2. **Instala las dependencias (si las hay)**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la versión en terminal**:
   ```bash
   python calculadora/main.py
   ```

4. **O ejecuta la versión gráfica (requiere tkinter)**:
   ```bash
   python calculadora/gui.py
   ```

---

## 🧪 Pruebas

> (En construcción) Se incluirán pruebas unitarias en el módulo `tests/`.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](./LICENSE) para más detalles.

---

## 💡 Autor

Desarrollado por **Miguel Alba** — ¡Con enfoque en la claridad, aprendizaje y utilidad!

¿Tienes sugerencias o quieres contribuir? ¡Pull requests y feedbacks son bienvenidos! 🚀
