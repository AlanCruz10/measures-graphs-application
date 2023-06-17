import math
import numpy as np


def number_of_classes(colum_values):
    total_data = int(len(colum_values))
    number_class = 1 + (3.3 * math.log10(total_data))
    return number_class.__round__()


def limit_range(colum_values):
    range_limits = max(colum_values) - min(colum_values)
    return range_limits


def class_width(colum_values):
    width_class = limit_range(colum_values) / number_of_classes(colum_values)
    return width_class


def lower_limits(colum_values):
    width_class = class_width(colum_values)
    limits_lower = [float(min(colum_values))]
    for i in range(1, number_of_classes(colum_values)):
        limits = limits_lower[i - 1] + width_class
        limits_lower.append(limits)
    return limits_lower


def upper_limits(colum_values):
    width_class = class_width(colum_values)
    lower_limit = lower_limits(colum_values)
    limits_upper = [limit + width_class for limit in lower_limit]
    return limits_upper


def mark_class(colum_values):
    lower_limit = lower_limits(colum_values)
    upper_limit = upper_limits(colum_values)
    class_marks = [(lower_limit[i] + upper_limit[i]) / 2 for i in range(number_of_classes(colum_values))]
    return class_marks


def frequency_absolute(colum_values):
    lower_limit = lower_limits(colum_values)
    upper_limit = upper_limits(colum_values)
    j = 0
    j2 = 1
    values = 0
    values2 = 0
    freq = {}
    for i in colum_values.values:
        if lower_limit[j] <= i <= upper_limit[j]:
            values = values + 1
            freq[lower_limit[j], upper_limit[j]] = values
    for y in range(1, number_of_classes(colum_values)):
        for i in colum_values.values:
            if lower_limit[j2] < i <= upper_limit[j2]:
                values2 = values2 + 1
                freq[lower_limit[j2], upper_limit[j2]] = values2
            else:
                freq[lower_limit[j2], upper_limit[j2]] = values2
        j2 = j2 + 1
        values2 = 0
    x = number_of_classes(colum_values) - 1
    value3 = 0
    for i in colum_values.values:
        if i > upper_limit[x]:
            value3 = value3 + 1
            freq[lower_limit[x], upper_limit[x]] = freq[lower_limit[x], upper_limit[x]] + value3
            value3 = 0
    return freq.values()


def frequency_absolute_accumulate(colum_values):
    frequency_absolute_values = frequency_absolute(colum_values)
    accumulate = 0
    accumulate_absolute_frequency = []
    for i in frequency_absolute_values:
        accumulate = accumulate + i
        accumulate_absolute_frequency.append(accumulate)
    return accumulate_absolute_frequency


# def frequency_absolute_dos(colum_values):
#    lower_limit = lower_limits(colum_values)
#    upper_limit = upper_limits(colum_values)
#    array_count = []
#    array_first = []
#    contain = list(zip(lower_limit, upper_limit))
#    for v in colum_values.values:
#        if lower_limit[0] <= v <= upper_limit[0]:
#            array_first.append(v)
#    array_count.append(len(array_first))
#    for j, (x, y) in enumerate(contain):
#        if j > 0:
#            count = sum(x < v <= y for v in colum_values.values)
#            array_count.append(count)
#    print("frec2", array_count)
#    return array_count


def frequency_relative(colum_values):
    absolute_frequency = frequency_absolute(colum_values)
    total = 0
    for i in absolute_frequency:
        total += i
    frequency_relative_values = []
    for i in absolute_frequency:
        relative_frequency = i / total
        frequency_relative_values.append(relative_frequency)
    return frequency_relative_values


def frequency_relative_accumulate(colum_values):
    relative_frequency_values = frequency_relative(colum_values)
    accumulate_relative_frequency = np.cumsum(relative_frequency_values)
    return accumulate_relative_frequency
