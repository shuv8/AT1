from SMC import AutomataAnalyzer_sm


class AutomataAnalyzer:
    def __init__(self):
        self._fsm = AutomataAnalyzer_sm.AutomataAnalyzer_sm(self)
        self._isAcceptable = False
        self._fsm.enterStartState()
        self._bufstr = ''
        self._type = ''
        self._name = ''
        self._numberofelems = 0
        self._length = 0

    def GetType(self):
        return self._type
    def GetName(self):
        return self._name
    def GetNumOfElems(self):
        return self._numberofelems
    def Acceptable(self):
        self._isAcceptable = True
    def Unacceptable(self):
        self._isAcceptable = False
    def Check(self, string):
        self._fsm.Start()
        for c in string:
            if c == '0':
                self._fsm.ZeroS(c)
            elif c.isalpha():
                self._fsm.Letter(c)
            elif c.isdigit():
                self._fsm.Digit(c)
            elif c == '[':
                self._fsm.SqBracket1S()
            elif c == ']':
                self._fsm.SqBracket2S()
            elif c == '=':
                self._fsm.EqualS()
            elif c == '{':
                self._fsm.Brace1S()
            elif c == '}':
                self._fsm.Brace2S()
            elif c == ' ':
                self._fsm.SpaceS()
            elif c == '-':
                self._fsm.MinusS()
            elif c == ',':
                self._fsm.CommaS()
            elif c == '\n':
                self._fsm.EOS()
                break
            else:
                self._fsm.Unknown()
        self._fsm.EOS()
        return  self._isAcceptable
    def InsToBuf(self, string):
        self._bufstr += string
    def IncLength(self):
        self._length += 1
    def ZeroLength(self):
        self._length = 0
    def InsType(self):
        self._type = self._bufstr
    def InsName(self):
        self._name = self._bufstr
    def ClearBuf(self):
        self._bufstr = ''
    def InsElemNum(self):
        self._numberofelems = int(self._bufstr)
    def LessThan16(self):
        return self._length <= 16
    def LessThan9(self):
        return self._length <= 9
    def CheckLength(self):
        return self._length == self._numberofelems
    def CheckType(self):
        a = False
        if self._bufstr.lower() == 'int' or self._bufstr.lower() == 'short' or self._bufstr.lower() == 'long':
            a = True
        return a
    def ClearSMC(self):
        self._isAcceptable = True
        self._bufstr = ''
        self._type = ''
        self._name = ''
        self._numberofelems = 0
        self._length = 0
