from StringAnalyzer import AutomataAnalyzer
import time
import os.path

def SMCconsolecheck(str):
    statemachine = AutomataAnalyzer.AutomataAnalyzer()
    match = statemachine.Check(str)
    if match:
        return str.rstrip('\n') + ' --- Correct\n'
    else:
        return str.rstrip('\n') + ' --- Incorrect\n'

def SMCfilecheck():
    statemachine = AutomataAnalyzer.AutomataAnalyzer()
    inf = open('strings.txt', 'r')
    ouf = open('SMCoutput.txt', 'w')
    _conflicts = {}
    _starttime = time.time()
    for line in inf.readlines():
        match = statemachine.Check(line)
        if match:
            if _conflicts.get(statemachine.GetName()):
                _conflicts[statemachine.GetName()][1] = True
            else:
                _conflicts[statemachine.GetName()] = [statemachine.GetType(), False]
            ouf.write(line.rstrip('\n') + ' --- Correct\n')
        else:
            ouf.write(line.rstrip('\n') + ' --- Incorrect\n')
    _endtime = time.time()
    ouf.write('\n-----Name conflicts-----\n')
    for key in _conflicts.keys():
        if _conflicts[key][1]:
            ouf.write(key + ' ' + _conflicts[key][0] + '\n')
    if os.path.isfile('time.txt'):
        timefile = open('time.txt', 'a')
        timefile.write('Analyzing with SMC completed in ' + str(_endtime - _starttime) + ' seconds\n')
    else:
        timefile = open('time.txt', 'w')
        timefile.write('Analyzing with SMC completed in '+  str(_endtime - _starttime) + ' seconds\n')
    timefile.close()
    print('Analyzing with SMC completed in', _endtime - _starttime, 'seconds')
    inf.close()
    ouf.close()
