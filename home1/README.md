EJECUCIÓN DE CÓDIGO:

![imagen](https://github.com/SebastianZamalloa/EDA_THEO_2023B/assets/104155286/fcea3e98-dd6e-4760-9080-a8aa72972cd9)

Comprobamos que Insertion Sort y Merge Sort se mantienen parcialmente iguales al inicio de la grafica, pero conforme aumentan los datos Merge sort mantiene un crecimiento uniforme e Insertion sort crece de forma exponencial

Tomar en cuenta:
- Aleatoriedad: al generarse números aleatorios el inicio de ambas gráficas puede variar, por lo que depende mucho de esas listas iniciales, en mi ejemplo de ejecución pareciese que Insertion Sort en un punto es más eficiente que Merge, pero esto se debe a los datos que se generaron, por ejemplo esta es otra ejecución:

![imagen](https://github.com/SebastianZamalloa/EDA_THEO_2023B/assets/104155286/272d1aed-15e4-4278-92e4-6219bd2c4653)

Como vemos hay variaciones, aquí hay una ejecución con cantidades de datos más pequeñas:

![imagen](https://github.com/SebastianZamalloa/EDA_THEO_2023B/assets/104155286/51336eea-e3c9-456a-929e-e0ecf9526c8a)

- Uso: Las gráficas nos demuestran que la eficiencia de Insertion Sort solo se ven relflejados en conjuntos de datos pequeños, Merge Sort también es eficiente en este caso, sin embargo dependiendo de como esté nuestro algoritmo hecho es mucho mejor recurrir a Insertion en estos casos, Merge debe reservarse para conjuntos de datos grandes, donde Insertion no puede ser tan eficiente
