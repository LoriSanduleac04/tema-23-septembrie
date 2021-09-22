temp=[8,8,8,8,8,7,7,6,7,7,8,9,10,11,11,12,12,12,12,13,11,10,10,9]
ora=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
#temperatura medie
print(sum(temp)/24)
#max si min temperaturii
print(max(temp),'maximul temperaturii',min(temp),'minimul temperaturii')
#ora cand s-a inregistrat temperatura maxima
max=temp.index(max(temp))
print('ora',ora[max])
#ora cand s-a inregistrat temperatura minima
min=temp.index(min(temp))
print('ora',ora[min])
