x=[6,5,-90,87,34,88,-12]
y=[44,86,-256,98,5,1,-3,94]
p=1
#suma primilor 3 termeni ale variabilei x
print(x[0]+x[1]+x[2])
#suma tuturor termenilor ale variabilei y
print(sum(y))
#produsul componentelor variabilei x
for i in x:
    p=p*i
print(p, 'produsul')
#valoarea absoluta a componentei a treia a variabilei x
print(abs(x[2]), 'valoare absoluta')
#suma primelor componente ale variabilei x si y
print(x[0]+y[0])