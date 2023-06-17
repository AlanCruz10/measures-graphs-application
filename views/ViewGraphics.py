import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import numpy as np
from services import OperationsGraphics
import mplcursors
from views import ViewMetrics


def print_graphics(column_values, window, type_graphic):
    def rgb2hex(rgb):
        return '#%02x%02x%02x' % rgb

    color_rgb = (117, 35, 161)
    color_hex = rgb2hex(color_rgb)
    canvas_graphics = tkinter.Canvas(window, background=color_hex)
    graphic_select(column_values, type_graphic, canvas_graphics)
    canvas_graphics.place(anchor="n", width=600, height=500, x=1062, y=4, bordermode="inside")


def graphic_select(column_values, type_graphic, canvas_graphics):
    if type_graphic == "Histograma":
        histogram_plot(column_values, canvas_graphics)
    elif type_graphic == "Polígono de frecuencias":
        frequency_polygon_graph(column_values, canvas_graphics)
    elif type_graphic == "Ojivas":
        warhead_graph(column_values, canvas_graphics)
    elif type_graphic == "Gráfica de barras":
        bar_graph(column_values, canvas_graphics)
    elif type_graphic == "Gráfica de pastel":
        pie_chart(column_values, canvas_graphics)


def histogram_plot(column_values, canvas_graphics):
    frequency_absolute = OperationsGraphics.frequency_absolute(column_values)
    mark_class = OperationsGraphics.mark_class(column_values)
    mark_class_round = []
    for i in range(len(mark_class)):
        mark_round = mark_class[i].__round__(4)
        mark_class_round.append(mark_round)
    fig, ax = plt.subplots(figsize=(6, 5), dpi=100)
    ax.bar(np.arange(len(mark_class)), frequency_absolute, align='center', edgecolor="black")
    ax.set_xticks(np.arange(len(mark_class)), labels=mark_class_round, rotation=30)
    mplcursors.cursor(hover=True)
    canvas_figure = FigureCanvasTkAgg(fig, master=canvas_graphics)
    canvas_figure.draw()
    canvas_figure_widget = canvas_figure.get_tk_widget()
    canvas_figure_widget.place(x=0, y=0)


def frequency_polygon_graph(column_values, canvas_graphics):
    mark_class = OperationsGraphics.mark_class(column_values)
    frequency_relative = OperationsGraphics.frequency_relative(column_values)
    frequency_relative.insert(0, 0)
    frequency_relative.append(0)
    mark_class.insert(0, 0)
    mark_class.append(0)
    mark_class_round = []
    for i in range(len(mark_class)):
        mark_round = mark_class[i].__round__(4)
        mark_class_round.append(mark_round)
    relative_frequency = [i * 100 for i in frequency_relative]
    fig, ax = plt.subplots(figsize=(6, 5), dpi=100)
    ax.plot(np.arange(len(mark_class)), relative_frequency, marker="o")
    ax.set_xticks(np.arange(len(mark_class)), labels=mark_class_round, rotation=30)
    mplcursors.cursor(hover=True)
    canvas_figure = FigureCanvasTkAgg(fig, master=canvas_graphics)
    canvas_figure.draw()
    canvas_figure_widget = canvas_figure.get_tk_widget()
    canvas_figure_widget.place(x=0, y=0)


def warhead_graph(column_values, canvas_graphics):
    frequency_relative_accumulate = OperationsGraphics.frequency_relative_accumulate(column_values)
    mark_class = OperationsGraphics.mark_class(column_values)
    accumulate_relative_frequency = np.insert(frequency_relative_accumulate, 0, 0)
    frequency_relative_accumulate_value = accumulate_relative_frequency[0:] * 100
    mark_class.insert(0, 0)
    mark_class_round = []
    for i in range(len(mark_class)):
        mark_round = mark_class[i].__round__(4)
        mark_class_round.append(mark_round)
    fig, ax = plt.subplots(figsize=(6, 5), dpi=100)
    ax.plot(np.arange(len(mark_class)), frequency_relative_accumulate_value, marker="o")
    ax.set_xticks(np.arange(len(mark_class)), labels=mark_class_round, rotation=30)
    mplcursors.cursor(hover=True)
    canvas_figure = FigureCanvasTkAgg(fig, master=canvas_graphics)
    canvas_figure.draw()
    canvas_figure_widget = canvas_figure.get_tk_widget()
    canvas_figure_widget.place(x=0, y=0)


def bar_graph(colum_values, canvas_graphics):
    values_bar_graphics = colum_values.value_counts().sort_index()
    y = np.arange(len(values_bar_graphics.index[0:]))
    fig, ax = plt.subplots(figsize=(6, 5), dpi=100)
    ax.barh(y, values_bar_graphics)
    ax.set_yticks(y, labels=values_bar_graphics.index, rotation=20)
    mplcursors.cursor(hover=True)
    canvas_figure = FigureCanvasTkAgg(fig, master=canvas_graphics)
    canvas_figure.draw()
    canvas_figure_widget = canvas_figure.get_tk_widget()
    canvas_figure_widget.place(x=0, y=0)


def pie_chart(colum_values, canvas_graphics):
    data_pie = colum_values.value_counts()
    total = 0
    for i in data_pie.values:
        total = i + total
    frequency_relative_pie = []
    for i in data_pie.values:
        frequency_relative = i / total
        frequency_relative_pie.append(frequency_relative * 100)
    fig, ax = plt.subplots(figsize=(6, 5), dpi=100)
    ax.pie(frequency_relative_pie, labels=data_pie.values[0:], autopct='%1.1f%%', shadow=True)
    ax.legend(data_pie.index.tolist(), title="Data", loc="upper left")
    canvas_figure = FigureCanvasTkAgg(fig, master=canvas_graphics)
    canvas_figure.draw()
    canvas_figure_widget = canvas_figure.get_tk_widget()
    canvas_figure_widget.place(x=0, y=0)


# def temporal_mean_g(column_values, window, canvas):
#    plt.close()
#    temporal = do.temporal_mean(column_values, window)
#    fig, ax = plt.subplots(figsize=(9.3, 11.6), dpi=60)
#    x = np.arange(len(temporal))
#    ax.plot(column_values)
#    ax.plot(x, temporal)
#    ax.set_xticks(x, labels=temporal)
#    fig.savefig("./GraphicsExports/warhead-graphic.png")
#    canvas.figure = fig
#    canvas.draw()
