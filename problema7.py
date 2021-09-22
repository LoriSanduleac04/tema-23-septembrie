v=[5120, 3800, 3780, 3010, 4900, 4100, 3290]
y=['Luni','Marti','Miercuri','Joi','Vineri','Sambata','Duminica']
#venitul saptamanal al intreprinderii
print(sum(v), "$")
#media venitului zilnic
print(sum(v)/7, "$")
#ziua in care a fost obtinut cel mai mare venit
max=v.index(max(v))
print(y[max])
#ziua in care a fost obtinut cel mai mic venit
min=v.index(min(v))
print(y[min])