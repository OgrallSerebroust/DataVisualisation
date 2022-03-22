from matplotlib.cbook import index_of
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import projections, rcParams
from mpl_toolkits.mplot3d import Axes3D


def paint_first_plot():
    dict_of_nomenclatures = dict()
    for _ in nomenclature:
        if _ in dict_of_nomenclatures:
            dict_of_nomenclatures[_] += 1
        else:
            dict_of_nomenclatures[_] = 1
    ax = fig.add_subplot(2, 1, 1)
    ax.set_title("Количество позиций по каждой номенклатуре")
    ax.bar(dict_of_nomenclatures.keys(), dict_of_nomenclatures.values())
    x_of_ax = ax.get_xaxis()
    y_of_ax = ax.get_yaxis()
    xlabels = x_of_ax.get_ticklabels()
    ylabels = y_of_ax.get_ticklabels()
    for xlabel in xlabels:
        xlabel.set_rotation(90)
        xlabel.set_fontsize(10)
    for ylabel in ylabels:
        ylabel.set_fontsize(10)
    y_of_ax.grid(True)
    with open("results/nomenclatures_totals.txt", "w") as nomenclatures_totals:
        sum_of_nomenclatures_positions = sum(dict_of_nomenclatures.values()) / 100
        for _ in dict_of_nomenclatures.keys():
            nomenclatures_totals.write(_ + " ----- "+ str(dict_of_nomenclatures[_] / sum_of_nomenclatures_positions) + "%\n")
        

def paint_second_plot():
    dict_of_nomenclatures_percents = dict()
    list_of_values_percents = list()
    for _ in nomenclature:
        if _ in dict_of_nomenclatures_percents:
            dict_of_nomenclatures_percents[_] += 1
        else:
            dict_of_nomenclatures_percents[_] = 1
    sum_of_nomenclatures_positions = sum(dict_of_nomenclatures_percents.values()) / 100
    for _ in dict_of_nomenclatures_percents.values():
        list_of_values_percents.append(_ / sum_of_nomenclatures_positions)
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Количество позиций по каждой номенклатуре в процентах")
    ax.pie(list_of_values_percents, labels = dict_of_nomenclatures_percents.keys())

def paint_third_plot():
    dict_of_models = dict()
    for _ in models:
        if _ in dict_of_models:
            dict_of_models[_] += 1
        else:
            dict_of_models[_] = 1
    ax = fig.add_subplot(2, 1, 1)
    ax.set_title("Количество позиций по каждой модели")
    ax.bar(dict_of_models.keys(), dict_of_models.values())
    x_of_ax = ax.get_xaxis()
    y_of_ax = ax.get_yaxis()
    xlabels = x_of_ax.get_ticklabels()
    ylabels = y_of_ax.get_ticklabels()
    for xlabel in xlabels:
        xlabel.set_rotation(90)
        xlabel.set_fontsize(10)
    for ylabel in ylabels:
        ylabel.set_fontsize(10)
    y_of_ax.grid(True)
    with open("results/models_totals.txt", "w") as nomenclatures_totals:
        sum_of_models_positions = sum(dict_of_models.values()) / 100
        for _ in dict_of_models.keys():
            nomenclatures_totals.write(_ + " ----- "+ str(dict_of_models[_] / sum_of_models_positions) + "%\n")

def paint_fourth_plot():
    dict_of_models_percents = dict()
    list_of_values_percents = list()
    for _ in models:
        if _ in dict_of_models_percents:
            dict_of_models_percents[_] += 1
        else:
            dict_of_models_percents[_] = 1
    sum_of_models_positions = sum(dict_of_models_percents.values()) / 100
    for _ in dict_of_models_percents.values():
        list_of_values_percents.append(_ / sum_of_models_positions)
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Количество позиций по каждой модели в процентах")
    ax.pie(list_of_values_percents, labels = dict_of_models_percents.keys())

def paint_fifth_plot():
    dict_of_nomenclature = dict()
    dict_of_models = dict()
    dict_of_private_models = dict()
    i, j, k = 1, 1, 1
    for _ in nomenclature:
        dict_of_nomenclature[i] = _
        i += 1
    for _ in models:
        dict_of_models[j] = _
        j += 1
    for _ in private_models:
        dict_of_private_models[k] = _
        k += 1
    print(dict_of_nomenclature.values())
    print(dict_of_models.values())
    print(dict_of_private_models.values())
    a = dict_of_nomenclature.values()
    b = dict_of_models.values()
    c = dict_of_private_models.values()
    print(list(a))
    print(list(b))
    print(list(c))
    ax = fig.add_subplot(1, 1, 1 , projection = "3d")
    ax.scatter(dict_of_nomenclature.keys(), dict_of_models.keys(), dict_of_private_models.keys())
    ax.set_xlabel("Номенклатура")
    ax.set_ylabel("Модель")
    ax.set_zlabel("Частная модель")


data_file = "C:/Users/sklepikov/Desktop/ЗИП v2.xlsx"
xl = pd.ExcelFile(data_file)
data_frame = xl.parse('Общий свод')
nomenclature = data_frame["Номенклатура"]
models = data_frame["Модель"]
private_models = data_frame["Частная модель"]
rcParams['font.family'] = 'Times New Roman'
rcParams['font.fantasy'] = 'Times New Roman'
fig = plt.figure()
print("Данные по количеству позиций по каждой номенклатуре - 1")
print("Данные по количеству позиций по каждой номенклатуре в процентах - 2")
print("Данные по количеству позиций по каждой модели - 3")
print("Данные по количеству позиций по каждой модели в процентах - 4")
number_of_plot = int(input())
if number_of_plot == 1:
    paint_first_plot()
    plt.show()
elif number_of_plot == 2:
    paint_second_plot()
    plt.show()
elif number_of_plot == 3:
    paint_third_plot()
    plt.show()
elif number_of_plot == 4:
    paint_fourth_plot()
    plt.show()
elif number_of_plot == 5:
    paint_fifth_plot()
    plt.show()