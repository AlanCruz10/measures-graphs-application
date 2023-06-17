import math
from statistics import median, mode, variance, pvariance, median_grouped, geometric_mean
import numpy as np
from services import OperationsGraphics

# Dates pompadours


def arithmetic_mean_ungrouped(colum_values):
    ungrouped_arithmetic_mean = sum(colum_values.values)/len(colum_values.values)
    return ungrouped_arithmetic_mean


def arithmetic_mean_grouped(colum_values):
    frequency_absolute = list(OperationsGraphics.frequency_absolute(colum_values))
    mark_class = OperationsGraphics.mark_class(colum_values)
    number_classes = OperationsGraphics.number_of_classes(colum_values)
    frequency_x_mark = []
    sum_frequency_x_mark = 0
    for i in range(number_classes):
        freq_x_mark = frequency_absolute[i] * mark_class[i]
        frequency_x_mark.append(freq_x_mark)
        sum_frequency_x_mark = sum_frequency_x_mark + frequency_x_mark[i]
    grouped_arithmetic_mean = sum_frequency_x_mark/len(colum_values.values)
    return grouped_arithmetic_mean


def median_ungrouped(colum_values):
    return median(sorted(colum_values.values))


def grouped_median(colum_values):
    mark_class = OperationsGraphics.mark_class(colum_values)
    return median(mark_class)


def mode_grouped(colum_values):
    frequency_absolute = OperationsGraphics.frequency_absolute(colum_values)
    mark_class = OperationsGraphics.mark_class(colum_values)
    values = list(frequency_absolute)
    max_value = max(values)
    modes = [mark_class[i] for i, value in enumerate(values) if value == max_value]
    if len(modes) == 1:
        return modes[0]
    elif 1 < len(modes) < len(colum_values):
        return modes
    else:
        return "No hay moda"


def mode_ungrouped(column_values):
    counts_values = column_values.value_counts()
    max_count = counts_values.max()
    modes = counts_values[counts_values == max_count].index.tolist()
    if len(modes) == 1:
        return modes[0]
    elif 1 < len(modes) < len(column_values):
        return modes
    else:
        return "No hay moda"


def ungrouped_variance(colum_values):
    values = list(colum_values.values)
    mean = arithmetic_mean_ungrouped(colum_values)
    values_rest_mean = []
    for i in values:
        val_rest_mean = (i - mean) ** 2
        values_rest_mean.append(val_rest_mean)
    variance_ungrouped = sum(values_rest_mean)/len(values)
    return variance_ungrouped


def grouped_variance(colum_values):
    mark_class = OperationsGraphics.mark_class(colum_values)
    frequency_absolute = OperationsGraphics.frequency_absolute(colum_values)
    mean = arithmetic_mean_grouped(colum_values)
    freq_x_mark_two = [(c ** 2) * f for f, c in zip(frequency_absolute, mark_class)]
    top = sum(freq_x_mark_two[0:]) - (len(colum_values.values) * (mean ** 2))
    total = top / (len(colum_values.values) - 1)
    return total


def grouped_standard_deviation(colum_values):
    variance_grouped = grouped_variance(colum_values)
    return math.sqrt(variance_grouped)


def ungrouped_standard_deviation(colum_values):
    variance_ungrouped = ungrouped_variance(colum_values)
    return math.sqrt(variance_ungrouped)


def ungrouped_bias(colum_values):
    ungrouped_mode = mode_ungrouped(colum_values)
    mean = arithmetic_mean_ungrouped(colum_values)
    ungrouped_median = median_ungrouped(colum_values)
    type_mode = type(ungrouped_mode)
    if type_mode == int or type_mode == float:
        if mean < ungrouped_median < ungrouped_mode:
            return "Sesgado a la izquierda"
        elif mean == ungrouped_median == ungrouped_mode:
            return "Simétrico"
        elif ungrouped_mode < ungrouped_median < mean:
            return "Sesgado a la derecha"
        else:
            return "Indeterminado"
    elif type_mode == str:
        return "No hay sesgo"
    else:
        return "Hay muchas modas"


def grouped_bias(colum_values):
    grouped_mode = mode_grouped(colum_values)
    mean = arithmetic_mean_grouped(colum_values)
    median_grouped_bias = median_grouped(colum_values)
    type_mode = type(grouped_mode)
    if type_mode == int or type_mode == float:
        if mean < median_grouped_bias < grouped_mode:
            return "Sesgado a la izquierda"
        elif mean == median_grouped_bias == grouped_mode:
            return "Simétrico"
        elif grouped_mode < median_grouped_bias < mean:
            return "Sesgado a la derecha"
        else:
            return "Indeterminado"
    elif type_mode == str:
        return "No hay sesgo"
    else:
        return "Hay muchas modas"


# def mean_geometric_ungrouped(colum_values):
#    mean_geometric = 0
#    g = 1
#    for i in colum_values.values:
#        if i == 0 or i == 0.0:
#            mean_geometric = 0
#        else:
#            mean_geometric = mean_geometric + 1
#    if mean_geometric != 0:
#        try:
#            for i in colum_values.values:
#                g = g * i
#            mean_geometric = g ** (1 / len(colum_values.values))
#            return mean_geometric
#        except ValueError:
#            return "No es posible calcular"
#    else:
#        return mean_geometric


def ungrouped_geometric_mean(colum_values):
    values_x_values = []
    for x in colum_values:
        g = x == 0 or x == 0.0
        values_x_values.append(g)
    if values_x_values.count(True) >= 1:
        return 0.0
    else:
        try:
            media_geometrica = geometric_mean(colum_values)
            return media_geometrica
        except ValueError:
            return "No es posible calcular"


def half_truncated(colum_values, percentage):
    sorted_colum_values = sorted(colum_values.values)
    numbers_truncate = round(len(sorted_colum_values) * percentage)
    trimmed_colum_values = sorted_colum_values[numbers_truncate: len(sorted_colum_values) - numbers_truncate]
    truncated_mean = sum(trimmed_colum_values) / len(trimmed_colum_values)
    return truncated_mean


def qualitative_mode(colum_values):
    frequency_qualitative = colum_values.value_counts()
    frequency_qualitative_max = max(frequency_qualitative.values)
    value_list = list(frequency_qualitative.values)
    index_list = list(frequency_qualitative.index)
    list_positions = []
    list_modes = []
    for i in range(len(frequency_qualitative)):
        if value_list[i] == frequency_qualitative_max:
            list_positions.append(i)
    for i in list_positions:
        list_modes.append(index_list[i])
    if len(list_positions) == len(index_list):
        return "No hay moda"
    else:
        return list_modes


# def temporal_mean(data, window):
#    weights = np.ones(window) / window
#    media_temporal = np.convolve(data, weights, mode='valid')
#    print(len(media_temporal))
#    return media_temporal
