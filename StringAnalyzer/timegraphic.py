import matplotlib.pyplot as plt

lines = [1000, 10000]
linesn = [1, 10]
_RegEx = [0.495011568069458, 4.502769947052002]
_SMC = [0.5235984325408936, 4.8832848072052]
_PLY = [9.894445419311523, 97.56702589988708]

plt.title('Зависимость времени обработки от кол-ва строк')
plt.xlabel('Кол-во строк, шт * 10^3')
plt.ylabel('Время, с')
plt.grid()

#fig, ax = plt.subplots()

plt.plot(linesn, _RegEx, label='RegEx')
plt.plot(linesn, _SMC, label='SMC')
plt.plot(linesn, _PLY, label='PLY')



plt.legend()

plt.show()