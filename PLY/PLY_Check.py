from PLY import parser
import time
import os.path

def PLYconsolecheck(_str):
    _parser = parser.Parser()
    _str += '\n'
    _res = _parser.PLYCheck(_str)
    if _parser.flag:
        return _str.rstrip('\n') + ' --- Correct\n'
    else:
        return _str.rstrip('\n') + ' --- Incorrect\n'


def PLYfilecheck():
    _parser = parser.Parser()
    inf = open('../StringAnalyzer/strings.txt', 'r')
    ouf = open('../StringAnalyzer/PLYoutput.txt', 'w')
    _starttime = time.time()
    for line in inf.readlines():
        _res = _parser.PLYCheck(line, _file=True)
        if _parser.flag:
            ouf.write(line.rstrip('\n') + ' --- Correct\n')
        else:
            ouf.write(line.rstrip('\n') + ' --- Incorrect\n')
    _endtime = time.time()
    ouf.write('\n-----Name conflicts-----\n')
    for key in _parser._stats.keys():
        if _parser._stats[key][1]:
            ouf.write(key + ' ' + _parser._stats[key][0] + '\n')
    if os.path.isfile('../StringAnalyzer/time.txt'):
        timefile = open('../StringAnalyzer/time.txt', 'a')
        timefile.write('Analyzing with PLY completed in ' + str(_endtime - _starttime) + ' seconds\n')
    else:
        timefile = open('../StringAnalyzer/time.txt', 'w')
        timefile.write('Analyzing with PLY completed in ' + str(_endtime - _starttime) + ' seconds\n')
    timefile.close()
    print('Analyzing with PLY completed in', _endtime - _starttime, 'seconds')
    inf.close()
    ouf.close()