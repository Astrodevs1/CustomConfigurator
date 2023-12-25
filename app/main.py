from app.gui import CarConfiguratorGUI
import tkinter as tk

def main ():
    root = tk.Tk()
    app = CarConfiguratorGUI(root)
    app.run()
    root.mainloop()

if __name__ == "__main__":
    main()