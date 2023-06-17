import tkinter
from tkinter import filedialog, ttk
import pandas
from views import ViewGraphics, ViewTable, ViewMetrics

label_graphics = None
combobox_graphics = None
label_attribute = None
combobox_attributes = None
button_open_graphic = None
button_export_table = None
# button_show_temporal_mean = None
# button_show_conglomerate = None
# button_show_mode_qualitative = None


def options_file(window):
    def rgb2hex(rgb):
        return '#%02x%02x%02x' % rgb

    color_rgb = (140, 222, 242)
    color_hex = rgb2hex(color_rgb)
    canvas_options = tkinter.Canvas(window, background=color_hex)
    text_file = tkinter.Label(canvas_options, text="Select file '.csv'")
    text_file.pack(padx=2, pady=8, ipady=2, ipadx=8)
    open_button = tkinter.Button(canvas_options, text="Open file", command=lambda: open_file(canvas_options, window))
    open_button.pack(padx=2, ipady=2, ipadx=8)
    canvas_options.place(anchor="nw", width=200, height=412, x=1, y=1, bordermode="inside")


def open_file(canvas_options, window):
    tkinter.Tk().withdraw()
    file = tkinter.filedialog.askopenfile(filetypes=[('CSV Files', '*.csv')])
    options_attributes_graphics(file, canvas_options, window)


def options_attributes_graphics(file, canvas_options, window):
    content_file = pandas.read_csv(file)
    attributes = content_file.columns.tolist()
    validate_file_change = 1
    validate_attribute = 1
    column_values = 1
    graphics_select = 1
    validate_file(canvas_options, graphics_select, column_values, window, attributes, content_file, validate_attribute, validate_file_change)


def validated_type_attribute(content_file, attributes, canvas_options, window):
    attribute = attributes.get()
    validate_attribute = 2
    if attribute:
        column_values = content_file[attribute]
        is_numeric = all(isinstance(item, (int, float)) for item in column_values)
        is_string = all(isinstance(item, str) for item in column_values)
        is_boolean = all(isinstance(item, bool) for item in column_values)
        if is_numeric:
            graphics_select = ["Histograma", "Polígono de frecuencias", "Ojivas", "Gráfica de barras",
                               "Gráfica de pastel"]
        elif is_string or is_boolean or is_numeric:
            graphics_select = ["Gráfica de barras", "Gráfica de pastel"]
        else:
            graphics_select = []
        validate_file_change = 2
        validate_file(canvas_options, graphics_select, column_values, window, attributes, content_file, validate_attribute, validate_file_change)


def options_graphics(canvas_options, graphics_select, column_values, window):
    global label_graphics, combobox_graphics
    label_graphics = tkinter.Label(canvas_options, text="Select type graphics")
    label_graphics.pack(padx=2, pady=8, ipady=2, ipadx=8)
    combobox_graphics = ttk.Combobox(canvas_options, values=graphics_select)
    combobox_graphics.pack(padx=2, ipady=2, ipadx=8)
    combobox_graphics.bind("<<ComboboxSelected>>",
                           lambda event: validate_options_buttons(canvas_options, column_values, window, combobox_graphics))


def options_attributes(canvas_options, attributes, content_file, window):
    global label_attribute, combobox_attributes
    label_attribute = tkinter.Label(canvas_options, text="Select attribute")
    label_attribute.pack(padx=2, pady=8, ipady=2, ipadx=8)
    combobox_attributes = ttk.Combobox(canvas_options, values=attributes)
    combobox_attributes.pack(padx=2, ipady=2, ipadx=8)
    combobox_attributes.bind("<<ComboboxSelected>>", lambda event: validated_type_attribute(content_file,
                                                                                            combobox_attributes,
                                                                                            canvas_options, window))


def options_button(canvas_options, column_values, window, type_graphics):
    type_attribute = column_values.dtype
    type_graphic = type_graphics.get()
    global button_open_graphic, button_export_table, button_show_temporal_mean, button_show_conglomerate, button_show_mode_qualitative
    button_open_graphic = tkinter.Button(canvas_options, text="Show graphic", bg="red",
                                         command=lambda: ViewGraphics.print_graphics(column_values, window,
                                                                                     type_graphic))
    button_open_graphic.bind("<Button-1>", lambda event: (ViewTable.create_table(column_values, window, type_graphic, type_attribute), ViewMetrics.show_data_metrics(window, column_values, type_attribute, type_graphics)))
    button_export_table = tkinter.Button(canvas_options, text="Export table/graphics", bg="black", fg="white",
                                         command=lambda: print("metodo para exportar las tablas"))
    # button_show_temporal_mean = tkinter.Button(canvas_options, text="Show temporal mean", bg="gray", command=lambda: print("metodo para ver las medias temporales"))
    # button_show_conglomerate = tkinter.Button(canvas_options, text="Show table conglomerate", bg="green", command=lambda: print("metodo para ver la tabla de conglomerados"))
    # button_show_mode_qualitative = tkinter.Button(canvas_options, text="Show moda qualitative", bg="yellow", command=lambda: print("metodo para ver la moda de cualitativos"))
    button_open_graphic.pack(pady=8, padx=2, ipady=2, ipadx=8)
    button_export_table.pack(pady=4, padx=2, ipady=2, ipadx=8)
    # button_show_temporal_mean.pack(pady=4, padx=2, ipady=2, ipadx=8)
    # button_show_conglomerate.pack(pady=4, padx=2, ipady=2, ipadx=8)
    # button_show_mode_qualitative.pack(pady=4, padx=2, ipady=2, ipadx=8)


def validate_file(canvas_options, graphics_select, column_values, window, attributes, content_file, validate_attribute, validate_file_change):
    if validate_file_change == 1:
        if label_attribute is None:
            validate_option_attributes(canvas_options, attributes, content_file, window)
        elif button_open_graphic is None:
            destroy_attributes_options()
            destroy_graphics_options()
            validate_option_attributes(canvas_options, attributes, content_file, window)
        else:
            destroy_buttons_options()
            destroy_graphics_options()
            destroy_attributes_options()
            validate_option_attributes(canvas_options, attributes, content_file, window)
    elif validate_attribute == 2:
        if label_graphics is None:
            validate_options_graphics(canvas_options, graphics_select, column_values, window)
        elif button_open_graphic is None:
            destroy_buttons_options()
            validate_options_graphics(canvas_options, graphics_select, column_values, window)
        else:
            destroy_buttons_options()
            destroy_graphics_options()
            validate_options_graphics(canvas_options, graphics_select, column_values, window)


def validate_options_buttons(canvas_options, column_values, window, type_graphics):
    if button_open_graphic is None:
        options_button(canvas_options, column_values, window, type_graphics)
    else:
        destroy_buttons_options()
        options_button(canvas_options, column_values, window, type_graphics)


def validate_options_graphics(canvas_options, graphics_select, column_values, window):
    if button_open_graphic is None:
        options_graphics(canvas_options, graphics_select, column_values, window)
    else:
        destroy_buttons_options()
        options_graphics(canvas_options, graphics_select, column_values, window)


def validate_option_attributes(canvas_options, attributes, content_file, window):
    if button_open_graphic is None:
        options_attributes(canvas_options, attributes, content_file, window)
    else:
        destroy_buttons_options()
        options_attributes(canvas_options, attributes, content_file, window)


def destroy_graphics_options():
    label_graphics.destroy()
    combobox_graphics.destroy()


def destroy_attributes_options():
    label_attribute.destroy()
    combobox_attributes.destroy()


def destroy_buttons_options():
    button_open_graphic.destroy()
    button_export_table.destroy()
    # button_show_temporal_mean.destroy()
    # button_show_conglomerate.destroy()
    # button_show_mode_qualitative.destroy()
