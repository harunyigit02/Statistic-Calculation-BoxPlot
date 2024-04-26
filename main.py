import harun_yigit as h

list1 = []
outliers_list = []
h.file_to_list("C:/Users/ASUS/Desktop/istveriler.txt", list1)
h.boxplot_with_outliers(list1)
no_outliers_list = h.aykiri_deger(list1)

h.bilgileri_yaz(no_outliers_list)
h.list_to_file("C:/Users/ASUS/Desktop/istveriler.txt", list1)
