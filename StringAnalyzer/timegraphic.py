import matplotlib.pyplot as plt

lines = [10000, 100000, 1000000]
linesn = [0.1, 1, 10]
_RegEx = [0.04088926315307617, 0.39594078063964844, 4.009277582168579]
_SMC = [0.4587721824645996, 4.758274078369141, 46.469724893569946]
_PLY = [0.2872626781463623, 2.852336883544922, 28.9057719707489]

plt.title('Зависимость времени обработки от кол-ва строк')
plt.xlabel('Кол-во строк, шт * 10^5')
plt.ylabel('Время, с')
plt.grid()

#fig, ax = plt.subplots()

plt.plot(linesn, _RegEx, label='RegEx')
plt.plot(linesn, _SMC, label='SMC')
plt.plot(linesn, _PLY, label='PLY')



plt.legend()

plt.show()