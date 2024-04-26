import math
import matplotlib.pyplot as plt
import numpy as np


def boxplot_with_outliers(list1):
    q1 = alt_ceyrek_bul(list1)
    q3 = ust_ceyrek_bul(list1)
    iqr = q3 - q1
    alt_sinir = q1 - 1.5 * iqr
    ust_sinir = q3 + 1.5 * iqr

    aykiri_degerler = [x for x in list1 if x < alt_sinir or x > ust_sinir]

    plt.figure(figsize=(8, 6))
    plt.boxplot(list1)
    plt.scatter(np.ones(len(aykiri_degerler)), aykiri_degerler, color='red', label='Aykırı Değerler')
    plt.title('Boxplot with Outliers')
    plt.xlabel('Veri')
    plt.ylabel('Değer')
    plt.legend()
    plt.show()


def aykiri_deger(list1):
    list_copy = list1.copy()
    list_aykiri = []

    aykiri_alt_sinir = alt_ceyrek_bul(list1) - (ceyrekler_acikigi_bul(list1) * 1.5)
    aykiri_ust_sinir = ust_ceyrek_bul(list1) - (ceyrekler_acikigi_bul(list1) * 1.5)

    for value in list1:
        if value < aykiri_alt_sinir:
            list_aykiri.append(value)
            list_copy.remove(value)

    return list_copy


def bubble_sorted_list(list1):
    n = len(list1)
    list2 = list1.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if list2[j] > list2[j + 1]:
                list2[j], list2[j + 1] = list2[j + 1], list2[j]

    return list2


def arortalama_bul(list1):
    sum = 0
    for value in list1:
        sum += value

    return sum / len(list1)


def medyan_bul(list1):
    if len(list1) % 2 == 0:
        return (bubble_sorted_list(list1)[len(list1) // 2 - 1] + bubble_sorted_list(list1)[
            (len(list1) // 2)]) / 2
    else:
        return bubble_sorted_list(list1)[((len(list1) + 1) // 2) - 1]


def mod_bul(list1):
    frekanslar = {}

    # Veri setindeki her bir değerin frekansını hesapla
    for eleman in list1:
        if eleman in frekanslar:
            frekanslar[eleman] += 1
        else:
            frekanslar[eleman] = 1
    max_count = list(frekanslar.values())[0]
    for value in frekanslar:
        if frekanslar[value] > max_count:
            max_count = frekanslar[value]

    for key, value in frekanslar.items():
        if value == max_count:
            return key


def file_to_list(file_name, list1):
    with open(file_name, "r") as file:
        for line in file:
            for word in line.split():
                try:
                    float_number = float(word)

                    list1.append(float_number)

                except:
                    pass


def list_to_file(file_name, list1):
    aykirisiz_list = aykiri_deger(list1)
    with open(file_name, "w") as file:
        for item in list1:
            file.write(str(item) + " ")

        file.write("\n\n\n")
        file.write("aritmetik ortalama: {}\n".format(arortalama_bul(list1)))
        file.write("medyan: {}\n".format(medyan_bul(list1)))
        file.write("mod: {}\n".format(medyan_bul(list1)))
        file.write("degisim araligi: {}\n".format(degisim_araligi_bul(list1)))
        file.write("ortalama mutlak sapma: {}\n".format(ort_mutlak_sapma_bul(list1)))
        file.write("varyans: {}\n".format(varyans_bul(list1)))
        file.write("standart sapma: {}\n".format(standart_sapma_bul(list1)))
        file.write("değişim katsayısı: {}\n".format(degisim_katsayisi_bul(list1)))
        file.write("çeyrekler açıklığı: {}\n".format(ceyrekler_acikigi_bul(list1)))


def degisim_araligi_bul(list1):
    max_value = list1[0]
    for value in list1:
        if value > max_value:
            max_value = value
    min_value = list1[0]
    for value2 in list1:
        if value2 < min_value:
            min_value = value2

    return max_value - min_value


def ort_mutlak_sapma_bul(list1):
    oms_sum = 0

    for value in list1:
        oms_sum += abs(arortalama_bul(list1) - value)

    return oms_sum / len(list1)


def varyans_bul(list1):
    var_sum = 0
    for value in list1:
        var_sum += pow(abs(value - arortalama_bul(list1)), 2)
    return pow(var_sum / (len(list1) - 1), 2)


def standart_sapma_bul(list1):
    return math.sqrt(varyans_bul(list1))


def degisim_katsayisi_bul(list1):
    return standart_sapma_bul(list1) / arortalama_bul(list1)


def alt_ceyrek_bul(list1):
    list2 = bubble_sorted_list(list1)
    n = len(list2)
    alt_ceyrek_index = (n + 1) / 4
    if isinstance(alt_ceyrek_index, int):
        alt_ceyrek = list2[((n + 1) // 4) - 1]

    else:
        alt_ceyrek = (list2[int(alt_ceyrek_index) - 1] + list2[int(alt_ceyrek_index)]) / 2

    return alt_ceyrek


def ust_ceyrek_bul(list1):
    n = len(list1)
    ust_ceyrek_index = 3 * (n + 1) / 4
    if not isinstance(ust_ceyrek_index, int):
        ust_ceyrek = (bubble_sorted_list(list1)[int(ust_ceyrek_index) - 1] + bubble_sorted_list(list1)[
            int(ust_ceyrek_index)]) / 2
    else:
        ust_ceyrek = bubble_sorted_list(list1)[((3 * (n + 1)) // 4) - 1]

    return ust_ceyrek


def ceyrekler_acikigi_bul(list1):
    return ust_ceyrek_bul(list1) - alt_ceyrek_bul(list1)


def bilgileri_yaz(list1):
    print("\n\n\n")
    print("aritmetik ortalama:", arortalama_bul(list1))
    print("medyan:", medyan_bul(list1))
    print("mod:", mod_bul(list1))
    print("degisim araligi:", degisim_araligi_bul(list1))
    print("ortalama mutlak sapma:", ort_mutlak_sapma_bul(list1))
    print("varyans:", varyans_bul(list1))
    print("standart sapma:", standart_sapma_bul(list1))
    print("değişim katsayısı:", degisim_katsayisi_bul(list1))
    print("çeyrekler açıklığı:", ceyrekler_acikigi_bul(list1))
