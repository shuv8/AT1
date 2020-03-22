from StringAnalyzer import generator
import re
import time
import os.path

# def checkfromconsole():
#     while True:
#         _string = input()
#         if _string == 'stop':
#             break
#         if check(_string):
#             print(_string, '   --- Correct')
#         else:
#             print(_string, '  --- Incorrect')
#         print('Enter \'stop\' to stop entering strings')

def check(_str):
    _str1 = _str.strip(' ')
    _reg = r'(?i)^(int|short|long)\s+([a-z]([a-z0-9]){0,15})\[([1-9][0-9]{0,8})?'
    _reg += r'\]\=\{((\-{0,1}[0-9]+\,)*(\-{0,1}[0-9]+))?\}$'
    _res = re.match(_reg, _str1)
    if _res is not None:
        if _res.group(5):
            _buf = _res.group(5).split(',')
        else:
            _buf = []
        if _res.group(4):
            _number = int(_res.group(4))
        else:
            _number = 0
        if _number == len(_buf):
            return _str.rstrip('\n') + ' --- Correct\n'
        else:
            return _str.rstrip('\n') + ' --- Incorrect\n'
    else:
        return _str.rstrip('\n') + ' --- Incorrect\n'

def checkfromgeneratedfile():
    #_genstime = time.time()
    #_num = 10000
    #generator.generate(_num)
    #print('Generation completed in', time.time() - _genstime, 'seconds')
    conflicts = {}
    inf = open('strings.txt', 'r')
    ouf = open('REGEXoutput.txt', 'w')
    _starttime = time.time()
    _crct = 0
    while True:
        _string = inf.readline()
        if not _string:
            break
        _reg = r'(?i)^(int|short|long)\s+([a-z]([a-z0-9]){0,15})\[([1-9][0-9]{0,8})?'
        _reg += r'\]\=\{((\-{0,1}[0-9]+\,)*(\-{0,1}[0-9]+))?\}$'
        _str = _string.strip(' ')
        _res = re.match(_reg, _str)
        if _res is not None:
            if _res.group(5):
                _buf = _res.group(5).split(',')
            else:
                _buf = []
            if _res.group(4):
                _number = int(_res.group(4))
            else:
                _number = 0
            if _number == len(_buf):
                ouf.write(_string.rstrip('\n') + ' --- Correct\n')
                _crct += 1
                if conflicts.get(_res.group(2)):
                    conflicts[_res.group(2)][1] = True
                else:
                    conflicts[_res.group(2)] = [_res.group(1), False]
            else:
                ouf.write(_string.rstrip('\n') + ' --- Incorrect\n')
        else:
            ouf.write(_string.rstrip('\n') + ' --- Incorrect\n')
    _endtime = time.time()
    ouf.write('\n-----Name conflicts-----\n')
    for key in conflicts.keys():
        if conflicts[key][1]:
            ouf.write(key + ' ' + conflicts[key][0] + '\n')
    print('Analyzing completed in', _endtime - _starttime, 'seconds')
    if os.path.isfile('time.txt'):
        timefile = open('time.txt', 'a')
        timefile.write('Analyzing with RegEx completed in ' + str(_endtime - _starttime) + ' seconds\n')
    else:
        timefile = open('time.txt', 'w')
        timefile.write('Analyzing with RegEx completed in ' + str(_endtime - _starttime) + ' seconds\n')
    timefile.close()
    #print('All program completed in', time.time() - _genstime, 'seconds')
    #print('Some statistics:',_num, 'strings,', _crct, 'correct')
    inf.close()
    ouf.close()