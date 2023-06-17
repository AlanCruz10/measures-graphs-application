import tkinter
from services import OperationsMetrics, OperationsGraphics
canvas_data_additional = None


def show_data_metrics(window, colum_values, type_attribute, type_graphics):
    canvas_metrics = tkinter.Canvas(window, background="black")
    canvas_metrics.place(anchor="n", width=559, height=412, x=481, y=1, bordermode="inside")
    if (type_attribute == "int64" and (type_graphics == "Gráfica de barras" or type_graphics == "Gráfica de pastel")) or (type_attribute == "float64" and (type_graphics == "Gráfica de barras" or type_graphics == "Gráfica de pastel")):
        data_qualitative_mode(canvas_metrics, colum_values)
    elif type_attribute == "object":
        if canvas_data_additional is not None:
            canvas_data_additional.destroy()
        data_qualitative_mode(canvas_metrics, colum_values)
    else:
        data_parametric(canvas_metrics, colum_values)
        data_statisticians(canvas_metrics, colum_values)
        additional_data(window, colum_values)


def rgb2hex():
    color_rgb = (68, 21, 169)
    return '#%02x%02x%02x' % color_rgb


def data_parametric(canvas_metrics, colum_values):
    label_title_parametric = tkinter.Label(canvas_metrics, text="PARAMETRICOS")
    label_title_parametric.pack(padx=1, pady=4, ipady=2, ipadx=229)
    grouped_data = tkinter.Label(canvas_metrics, background=rgb2hex(), foreground="white", justify="left", anchor="w",
                                 text=f'DATOS AGRUPADOS\n\n'
                                      f'Media aritmética: {OperationsMetrics.arithmetic_mean_grouped(colum_values)}\n'
                                      f'Mediana: {OperationsMetrics.grouped_median(colum_values)}\n'
                                      f'Moda: {OperationsMetrics.mode_grouped(colum_values)}\n'
                                      f'Rango: {OperationsGraphics.limit_range(colum_values)}\n'
                                      f'Varianza: {OperationsMetrics.grouped_variance(colum_values)}\n'
                                      f'Desviacion estandar: {OperationsMetrics.grouped_standard_deviation(colum_values)}\n'
                                      f'Sesgo: {OperationsMetrics.grouped_bias(colum_values)}')

    ungrouped_data = tkinter.Label(canvas_metrics, background=rgb2hex(), foreground="white", justify="left", anchor="w",
                                   text=f'DATOS NO AGRUPADOS\n\n'
                                        f'Media aritmética: {OperationsMetrics.arithmetic_mean_ungrouped(colum_values)}\n'
                                        f'Media truncada: {OperationsMetrics.half_truncated(colum_values, 0.1)} \n'
                                        f'Media geométrica: {OperationsMetrics.ungrouped_geometric_mean(colum_values)}\n'
                                        f'Mediana: {OperationsMetrics.median_ungrouped(colum_values)}\n'
                                        f'Moda: {OperationsMetrics.mode_ungrouped(colum_values)}\n'
                                        f'Rango: {OperationsGraphics.limit_range(colum_values)}\n'
                                        f'Varianza: {OperationsMetrics.ungrouped_variance(colum_values)}\n'
                                        f'Desviacion estandar: {OperationsMetrics.ungrouped_standard_deviation(colum_values)}\n'
                                        f'Sesgo: {OperationsMetrics.ungrouped_bias(colum_values)}')
    grouped_data.pack(padx=4, pady=0, ipady=15, ipadx=75, anchor="nw")
    ungrouped_data.place(x=280, y=33, width=275)


def data_statisticians(canvas_metrics, colum_values):
    label_title_statisticians = tkinter.Label(canvas_metrics, text="ESTADISTICOS")
    label_title_statisticians.pack(padx=3, pady=4, ipady=2, ipadx=234)
    grouped_data = tkinter.Label(canvas_metrics, background=rgb2hex(), foreground="white", justify="left", anchor="w",
                                 text=f'DATOS AGRUPADOS\n\n'
                                      f'Media aritmética: {OperationsMetrics.arithmetic_mean_grouped(colum_values)}\n'
                                      f'Mediana: {OperationsMetrics.grouped_median(colum_values)}\n'
                                      f'Moda: {OperationsMetrics.mode_grouped(colum_values)}\n'
                                      f'Rango: {OperationsGraphics.limit_range(colum_values)}\n'
                                      f'Varianza: {OperationsMetrics.grouped_variance(colum_values)}\n'
                                      f'Desviacion estandar: {OperationsMetrics.grouped_standard_deviation(colum_values)}\n'
                                      f'Sesgo: {OperationsMetrics.grouped_bias(colum_values)}')

    ungrouped_data = tkinter.Label(canvas_metrics, background=rgb2hex(), foreground="white", justify="left", anchor="w",
                                   text=f'DATOS NO AGRUPADOS\n\n'
                                        f'Media aritmética: {OperationsMetrics.arithmetic_mean_ungrouped(colum_values)}\n'
                                        f'Media truncada: {OperationsMetrics.half_truncated(colum_values, 0.1)} \n'
                                        f'Media geométrica: {OperationsMetrics.ungrouped_geometric_mean(colum_values)}\n'
                                        f'Mediana: {OperationsMetrics.median_ungrouped(colum_values)}\n'
                                        f'Moda: {OperationsMetrics.mode_ungrouped(colum_values)}\n'
                                        f'Rango: {OperationsGraphics.limit_range(colum_values)}\n'
                                        f'Varianza: {OperationsMetrics.ungrouped_variance(colum_values)}\n'
                                        f'Desviacion estandar: {OperationsMetrics.ungrouped_standard_deviation(colum_values)}\n'
                                        f'Sesgo: {OperationsMetrics.ungrouped_bias(colum_values)}')
    grouped_data.pack(padx=4, pady=0, ipady=15, ipadx=75, anchor="nw")
    ungrouped_data.place(x=280, y=237, width=275)


def data_qualitative_mode(canvas_metrics, colum_values):
    label_title_parametric = tkinter.Label(canvas_metrics, text="PARAMETRICOS")
    label_title_parametric.pack(padx=1, pady=4, ipady=2, ipadx=229)
    mode_parametric = tkinter.Label(canvas_metrics, background=rgb2hex(), foreground="white", justify="left",
                                    anchor="w", text=f'MODA\n\n{OperationsMetrics.qualitative_mode(colum_values)}\n')
    mode_parametric.pack(padx=4, pady=0, ipady=53, ipadx=250, anchor="nw")
    label_title_statisticians = tkinter.Label(canvas_metrics, text="ESTADISTICOS")
    label_title_statisticians.pack(padx=3, pady=4, ipady=2, ipadx=234)
    mode_statisticians = tkinter.Label(canvas_metrics, background=rgb2hex(), foreground="white", justify="left",
                                       anchor="w", text=f'MODA\n\n{OperationsMetrics.qualitative_mode(colum_values)}\n')
    mode_statisticians.pack(padx=4, pady=0, ipady=52, ipadx=250, anchor="nw")


def additional_data(window, colum_values):
    global canvas_data_additional
    canvas_data_additional = tkinter.Canvas(window, background="pink")
    canvas_data_additional.place(anchor="w", width=760, height=89, x=1, y=459, bordermode="inside")
    label_title_parametric = tkinter.Label(canvas_data_additional, text="PARAMETRICOS")
    label_title_parametric.place(x=4, y=3, width=375)
    mode_parametric = tkinter.Label(canvas_data_additional, background=rgb2hex(), foreground="white", justify="left",
                                    anchor="w", text=f'Ancho de clase: {OperationsGraphics.class_width(colum_values)}\n'
                                        f'Numero de clases: {OperationsGraphics.number_of_classes(colum_values)} \n')
    mode_parametric.place(x=4, y=26, width=375, height=59)
    label_title_statisticians = tkinter.Label(canvas_data_additional, text="ESTADISTICOS")
    label_title_statisticians.place(x=381, y=3, width=375)
    mode_statisticians = tkinter.Label(canvas_data_additional, background=rgb2hex(), foreground="white", justify="left",
                                       anchor="w", text=f'Ancho de clase: {OperationsGraphics.class_width(colum_values)}\n'
                                        f'Numero de clases: {OperationsGraphics.number_of_classes(colum_values)} \n')
    mode_statisticians.place(x=381, y=26, width=375, height=59)
