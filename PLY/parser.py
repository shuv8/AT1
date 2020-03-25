from PLY import lexer
import ply.yacc as yacc

class Parser:
    tokens = lexer.Lexer.tokens

    def __init__(self):
        self._lexer = lexer.Lexer()
        self._parser = yacc.yacc(module=self, optimize=1, debug=False, write_tables=False)
        self._stats = {}
        self.flag = False


    def p_array(self, p):
        """array : TYPE NAME SIZE EQUAL ELEMS NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
        _size_str = p[3].lstrip('[')
        _size_str = _size_str.rstrip(']')
        _elems_str = p[5].lstrip('{')
        _elems_str = _elems_str.rstrip('}')
        if len(_size_str) != 0:
            if int(_size_str) != 0:
                _size = int(_size_str)
            else:
                _size = -1
        else:
            _size = 0
        if len(_elems_str) != 0:
            _realsize = len(_elems_str.split(','))
        else:
            _realsize = 0

        if _size == _realsize:
            self.flag = True
            if self._stats.get(p[2]):
                self._stats[p[2]][1] = True
            else:
                self._stats[p[2]] = [p[1], False]

    #def p_error(self, p):

    def p_array_zero_error(self, p):
        """array : err NL"""
        p[0] = p[1] + p[2]

    def p_array_first_error(self, p):
        """array : TYPE err NL"""
        p[0] = p[1] + p[2] + p[3]

    def p_array_second_error(self, p):
        """array : TYPE NAME err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4]

    def p_array_third_error(self, p):
        """array : TYPE NAME SIZE err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

    def p_array_fourth_error(self, p):
        """array : TYPE NAME SIZE EQUAL err NL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

    def p_err(self, p):
        """err : UNKNOWN"""
        p[0] = p[1]

    def p_error(self, p):
        pass

    def PLYCheck(self, _str, _file = False):
        if _file == False:
            self._stats.clear()
        self.flag = False
        _res = self._parser.parse(_str)
        return _str
