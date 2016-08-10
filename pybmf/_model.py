#

class Char(object):
    def __init__(self, code=None, scan_line=None, encoding=None):
        self.__code = code
        self.__scan_line = scan_line
        self.__encoding = encoding

    def get_id(self):
        return self.__code

    def set_encoding(self, encoding):
        self.__encoding = encoding

    def get_encoding(self):
        return self.__encoding

    def get_scan_line(self):
        return self.__scan_line

    def set_scan_line(self, scan_line):
        self.__scan_line = scan_line

    def __repr__(self):
        return "<Char %r>" % (self.__scan_line, )


class UCode(object):
    def __init__(self, u_code=None):
        self.__u_code = u_code


class Font(object):
    def __init__(self, name=None, comment=None):
        self.__name = name
        self.__comment = comment
        self.__chars = {}

    def set_name(self, name):
        self.__name = name

    def get_chars(self):
        return self.__chars

    def set_comment(self, comment):
        self.__comment = comment

    def get_char(self, u_code):
        return self.__chars[u_code]

    def set_char(self, u_code, char):
        self.__chars[u_code] = char

    def get_char_count(self):
        return len(self.__chars)

