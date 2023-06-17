from tkinter import Tk, Button, Label, filedialog, ttk, font, Canvas, Toplevel
import tkinter
from views import ViewOptions

window = tkinter.Tk()


def rgb2hex(rgb):
    return '#%02x%02x%02x' % rgb


color_rgb = (101, 47, 185)
color_hex = rgb2hex(color_rgb)
window.geometry("1366x768")
window.title("ProbGraph")
window.configure(bg=color_hex)

ViewOptions.options_file(window)

window.mainloop()
