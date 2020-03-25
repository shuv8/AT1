from StringAnalyzer import generator
from RegEx import regex
from SMC import SMC
import os.path

while True:
    print('1. Generate new file')
    print('2. Check file with RegEx')
    print('3. Check file with SMC')
    print('4. Enter string from keyboard')
    print('5. Show time of analyzing')
    print('6. Clear time statistics')
    print('0. Quit')
    print('Make your choice: ')
    c = input()
    if c.isdigit():
        choice = int(c)
        if choice == 1:
            generator.generate()
        elif choice == 2:
            regex.checkfromgeneratedfile()
        elif choice == 3:
            SMC.SMCfilecheck()
        elif choice == 4:
            print('Enter the string: ')
            str = input()
            print('RegEx result:', regex.check(str).rstrip('\n'))
            print('SMC result:', SMC.SMCconsolecheck(str))
        elif choice == 5:
            if os.path.isfile('time.txt'):
                times = open('time.txt', 'r')
                for line in times.readlines():
                    print(line.rstrip('\n'))
                print('\n')
                times.close()
            else:
                print('Sorry, but you haven\'t analyzed file yet')
        elif choice == 6:
            times = open('time.txt', 'w')
            times.close()
        elif choice == 0:
            break
        else:
            print('Wrong choice, try again!')
    else:
        print('Wrong choice, try again!')
print('The end!')