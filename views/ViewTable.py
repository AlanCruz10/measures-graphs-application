import tkinter
from pandastable import Table
import pandas as pd
from services import OperationsGraphics
from views import ViewMetrics
import numpy as np


def create_table(colum_values, window, type_graphic, type_attribute):
    def rgb2hex(rgb):
        return '#%02x%02x%02x' % rgb

    color_rgb = (11, 93, 187)
    color_hex = rgb2hex(color_rgb)
    label_title_parametric = tkinter.Label(window, background="black", foreground="white", text="PARAMETRICOS")
    label_title_parametric.place(x=1, y=506, width=681, height=34)
    label_title_statisticians = tkinter.Label(window, background="black", foreground="white", text="ESTADISTICOS")
    label_title_statisticians.place(x=684, y=506, width=678, height=34)
    select_type_table(colum_values, window, color_hex, type_graphic, type_attribute)


def create_frequency_table_parametric(window, color_hex, type_table):
    canvas_table_parametric = tkinter.Canvas(window, background=color_hex)
    canvas_table_parametric.place(anchor="nw", width=681, height=200, x=1, y=542, bordermode="inside")
    table = Table(canvas_table_parametric, dataframe=type_table, width=681, background="blue")
    table.autoResizeColumns()
    table.show()
    table.update_idletasks()
    canvas_table_parametric.config(scrollregion=canvas_table_parametric.bbox("all"))


def create_frequency_table_statisticians(window, color_hex, type_table):
    canvas_table_statisticians = tkinter.Canvas(window, background=color_hex)
    canvas_table_statisticians.place(anchor="nw", width=678, height=200, x=684, y=542, bordermode="inside")
    table = Table(canvas_table_statisticians, dataframe=type_table, width=681, background="blue")
    table.autoResizeColumns()
    table.show()
    table.update_idletasks()
    canvas_table_statisticians.config(scrollregion=canvas_table_statisticians.bbox("all"))


def table_qualitative(colum_values):
    frequency_absolute_accumulated = []
    accumulate = 0
    total = 0
    for i in colum_values.value_counts().values:
        accumulate = accumulate + i
        frequency_absolute_accumulated.append(accumulate)
    for i in frequency_absolute_accumulated:
        total += i
    frequency_relative_values = []
    for i in frequency_absolute_accumulated:
        relative_frequency = i / total
        frequency_relative_values.append(relative_frequency)
    accumulate_relative_frequency = np.cumsum(frequency_relative_values)
    qualitative_table = pd.DataFrame({
        "Class": colum_values.value_counts().index,
        "Frequency absolute": colum_values.value_counts().values,
        "Frequency absolute accumulated": frequency_absolute_accumulated,
        "Frequency relative": frequency_relative_values,
        "Frequency relative accumulated": accumulate_relative_frequency
    })
    columns_to_format = ['Frequency relative', 'Frequency relative accumulated']
    qualitative_table[columns_to_format] = qualitative_table[columns_to_format].applymap(
        lambda x: '{:.{}f}'.format(x, pd.get_option('display.precision')))
    return qualitative_table


def table_quantitative(colum_values):
    quantitative_table = pd.DataFrame({
        "# class": range(1, OperationsGraphics.number_of_classes(colum_values) + 1),
        "Lower limit": OperationsGraphics.lower_limits(colum_values),
        "Upper limit": OperationsGraphics.upper_limits(colum_values),
        "Class mark": OperationsGraphics.mark_class(colum_values),
        "Frequency absolute": OperationsGraphics.frequency_absolute(colum_values),
        "Frequency absolute accumulated": OperationsGraphics.frequency_absolute_accumulate(colum_values),
        "Frequency relative": OperationsGraphics.frequency_relative(colum_values),
        "Frequency relative accumulated": OperationsGraphics.frequency_relative_accumulate(colum_values)
    })
    columns_to_format = ['Lower limit', 'Upper limit', 'Class mark']
    quantitative_table[columns_to_format] = quantitative_table[columns_to_format].applymap(lambda x: '{:.{}f}'.format(
        x, pd.get_option('display.precision')))
    return quantitative_table


def select_type_table(colum_values, window, color_hex, type_graphic, type_attribute):
    if (type_attribute == "int64" and type_graphic == "Gráfica de barras") or (
            type_attribute == "int64" and type_graphic == "Gráfica de pastel") or (
            type_attribute == "float64" and type_graphic == "Gráfica de barras") or (
            type_attribute == "float64" and type_graphic == "Gráfica de pastel"):
        qualitative = table_qualitative(colum_values)
        create_frequency_table_parametric(window, color_hex, qualitative)
        create_frequency_table_statisticians(window, color_hex, qualitative)
    elif type_attribute == "object" or type_attribute == "bool":
        qualitative = table_qualitative(colum_values)
        create_frequency_table_parametric(window, color_hex, qualitative)
        create_frequency_table_statisticians(window, color_hex, qualitative)
    else:
        quantitative = table_quantitative(colum_values)
        create_frequency_table_parametric(window, color_hex, quantitative)
        create_frequency_table_statisticians(window, color_hex, quantitative)
