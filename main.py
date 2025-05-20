import os
import tkinter as tk
from src.ui import PPPGenerator

def main():
    """Inicializa e executa a aplicação principal"""
    root = tk.Tk()
    
    # Configura DPI awareness no Windows
    if os.name == 'nt':
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    
    app = PPPGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()