import tkinter as tk
from tkinter import font
from calculadora.main import sumar, restar, multiplicar, dividir
from calculadora.cientifica import calcular_raiz, calcular_seno, calcular_coseno, calcular_log

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#2E2E2E')
        
        # Variables
        self.operacion = ""
        self.resultado = 0
        self.modo_cientifico = False
        
        # Fuentes personalizadas
        self.fuente_display = font.Font(family='Helvetica', size=24, weight='bold')
        self.fuente_botones = font.Font(family='Arial', size=14)
        
        self._crear_ui()
    
    def _crear_ui(self):
        # Display
        self.display = tk.Entry(
            self.root, font=self.fuente_display, 
            borderwidth=0, justify='right', 
            bg='#1E1E1E', fg='white', insertbackground='white'
        )
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=20, ipady=20, sticky='we')
        
        # Botones numéricos
        botones_numericos = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2)
        ]
        
        for (texto, fila, col) in botones_numericos:
            tk.Button(
                self.root, text=texto, font=self.fuente_botones,
                command=lambda t=texto: self._click_boton(t),
                bg='#3E3E3E', fg='white', activebackground='#4E4E4E',
                borderwidth=0, height=2, width=5
            ).grid(row=fila, column=col, padx=5, pady=5)
        
        # Botones operaciones básicas
        operaciones_basicas = [
            ('C', 1, 3), ('/', 1, 4),
            ('*', 2, 3), ('-', 3, 3), ('+', 4, 3)
        ]
        
        for (texto, fila, col) in operaciones_basicas:
            tk.Button(
                self.root, text=texto, font=self.fuente_botones,
                command=lambda t=texto: self._click_boton(t),
                bg='#FF9500', fg='white', activebackground='#FFAA33',
                borderwidth=0, height=2, width=5
            ).grid(row=fila, column=col, padx=5, pady=5)
        
        # Botón modo científico
        tk.Button(
            self.root, text="Científica", font=self.fuente_botones,
            command=self._cambiar_modo,
            bg='#007AFF', fg='white', activebackground='#0095FF',
            borderwidth=0, height=2, width=12
        ).grid(row=5, column=0, columnspan=3, padx=5, pady=5)
        
        # Botón de salida
        tk.Button(
            self.root, text="Salir", font=self.fuente_botones,
            command=self.root.quit,
            bg='#FF3B30', fg='white', activebackground='#FF5E55',
            borderwidth=0, height=2, width=12
        ).grid(row=5, column=3, columnspan=2, padx=5, pady=5)
    
    def _cambiar_modo(self):
        self.modo_cientifico = not self.modo_cientifico
        if self.modo_cientifico:
            self._mostrar_botones_cientificos()
        else:
            self._ocultar_botones_cientificos()
    
    def _mostrar_botones_cientificos(self):
        operaciones_cientificas = [
            ('√', 6, 0), ('sin', 6, 1), ('cos', 6, 2), ('ln', 6, 3)
        ]
        
        for (texto, fila, col) in operaciones_cientificas:
            tk.Button(
                self.root, text=texto, font=self.fuente_botones,
                command=lambda t=texto: self._click_boton(t),
                bg='#5856D6', fg='white', activebackground='#7D7AFF',
                borderwidth=0, height=2, width=5
            ).grid(row=fila, column=col, padx=5, pady=5)
    
    def _ocultar_botones_cientificos(self):
        for widget in self.root.grid_slaves():
            if int(widget.grid_info()["row"]) == 6:
                widget.grid_forget()
    
    def _click_boton(self, valor):
        if valor == 'C':
            self.display.delete(0, tk.END)
        elif valor == '=':
            try:
                expresion = self.display.get()
                resultado = eval(expresion)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(resultado))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif valor == '√':
            try:
                num = float(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, calcular_raiz(num))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif valor in ('sin', 'cos', 'ln'):
            try:
                num = float(self.display.get())
                self.display.delete(0, tk.END)
                if valor == 'sin':
                    self.display.insert(0, calcular_seno(num))
                elif valor == 'cos':
                    self.display.insert(0, calcular_coseno(num))
                elif valor == 'ln':
                    self.display.insert(0, calcular_log(num))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, valor)

# Iniciar la aplicación
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    app.run()