# 🧮 Scientific Calculator in Python

A versatile calculator developed in Python offering both basic and scientific functions, with a terminal and graphical interface. It also stores a history of operations performed by the user.

---

## ✨ Features

✅ **Basic Operations**  
- Addition  
- Subtraction  
- Multiplication  
- Division  

🧠 **Scientific Functions**  
- Square root  
- Sine and cosine (in degrees)  
- Natural logarithm  

📝 **Extras**  
- Saves operation history in `historial.txt`  
- Converts results to words (from 0 to 10)  
- Optional graphical interface using `tkinter`

---

## 📁 Project Structure

```
calculadora-cientifica/
├── calculadora/
│   ├── main.py          # Terminal version
│   ├── gui.py           # Graphical version
│   ├── cientifica.py    # Scientific functions
│   ├── saludo.py        # Welcome/farewell messages
│   ├── historial.py     # History management
│   └── __init__.py
├── tests/
│   └── __init__.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🛠️ Requirements

- Python **3.8 or higher**

---

## 🚀 Installation and Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JM90AR/calculadora-cientifica.git
   cd calculadora-cientifica
   ```

2. **Install dependencies (if any)**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the terminal version**:
   ```bash
   python calculadora/main.py
   ```

4. **Or run the graphical version (requires tkinter)**:
   ```bash
   python calculadora/gui.py
   ```

---

## 🧪 Testing

> (In progress) Unit tests will be included in the `tests/` module.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

---

## 💡 Author

Developed by **Miguel Alba** — Focused on clarity, learning, and usefulness!

Feel free to contribute or suggest improvements — pull requests are welcome! 🚀