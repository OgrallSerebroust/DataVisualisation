import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import rcParams
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
    fig.savefig("assets/tmp/tmp_pic.png")
    sum_of_nomenclatures_positions = sum(dict_of_nomenclatures.values()) / 100
    dict_of_percents = dict()
    for _ in dict_of_nomenclatures.keys():
        dict_of_percents[_] = str(dict_of_nomenclatures[_] / sum_of_nomenclatures_positions)
    return dict_of_percents
        
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
    fig.savefig("assets/tmp/tmp_pic.png")

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

def paint_sixth_plot():
    list_of_mm_mk_count, list_of_mega, list_of_tb = list(), list(), list(), list()
    for _ in mm_mk_count:
        list_of_mm_mk_count.append(_)
    for _ in tb_count:
        list_of_tb.append(_)
    for _ in megamart_count:
        list_of_mega.append(_)
    ind = np.arange(len(list_of_mm_mk_count))
    bar_padding = np.add(list_of_mm_mk_count, list_of_mega).tolist()
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(ind, list_of_mm_mk_count, label="ММ МК, шт.")
    ax.bar(ind, list_of_mega, bottom=list_of_mm_mk_count, label="Мегамарт, шт.")
    ax.bar(ind, list_of_tb, bottom=bar_padding, label="ТБ, шт.")
    ax.legend()

def paint_seventh_plot():
    list_of_all_count, list_of_mm_mk_count, list_of_mega, list_of_tb = list(), list(), list(), list()
    dict_of_salers_percents = dict()
    counter = 0
    for _ in mm_mk_count:
        list_of_mm_mk_count.append(_)
    for _ in tb_count:
        list_of_tb.append(_)
    for _ in megamart_count:
        list_of_mega.append(_)
    for _ in all_count:
        list_of_all_count.append(_)
    for _ in list_of_mm_mk_count:
        if _ > 0:
            counter += 1
    dict_of_salers_percents["ММ МК, шт."] = counter / len(list_of_all_count) / 100
    counter = 0
    for _ in list_of_mega:
        if _ > 0:
            counter += 1
    dict_of_salers_percents["Мегамарт, шт."] = counter / len(list_of_all_count) / 100
    counter = 0
    for _ in list_of_tb:
        if _ > 0:
            counter += 1
    dict_of_salers_percents["ТБ, шт."] = counter / len(list_of_all_count) / 100
    counter = 0
    ax = fig.add_subplot(1, 1, 1)
    ax.pie(dict_of_salers_percents.values(), labels = dict_of_salers_percents.keys())
        

data_file = "C:/Users/sklepikov/Desktop/ЗИП v2.xlsx"
xl = pd.ExcelFile(data_file)
data_frame = xl.parse('Общий свод')
nomenclature = data_frame["Номенклатура"]
models = data_frame["Модель"]
private_models = data_frame["Частная модель"]
mm_mk_count = data_frame["ММ МК, шт."]
megamart_count = data_frame["Мегамарт, шт."]
tb_count = data_frame["ТБ, шт."]
all_count = data_frame["Общая потребность, шт."]
rcParams['font.family'] = 'Times New Roman'
rcParams['font.fantasy'] = 'Times New Roman'
fig = plt.figure()