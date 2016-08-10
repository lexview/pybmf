#!/usr/bin/python

import os


class Application(object):
    DEFAULT_CHAR_COUNT = 256
    DEFAULT_CHAR_HEIGHT = 16

    def __init__(self):
        self.__char_height = Application.DEFAULT_CHAR_HEIGHT
        self.__char_count = Application.DEFAULT_CHAR_COUNT

    def _detect_information(self, name):
        size = os.path.getsize(name)
        self.__char_height = size / self.__char_count

    def __write_char(self, num, scan_line_buffer):
        result = []
        for ch in scan_line_buffer:
            ch = ord(ch)
            scan_line = ""
            for i in xrange(0, 8):
                #print i
                val = 1 << i
                if ch & val:
                    scan_line = "#" + scan_line
                else:
                    scan_line = " " + scan_line
            result.append(scan_line)
        return result

    def _read(self, name):
        result = {}
        with open(name, "rb") as stream:
            items = {}
            for num in xrange(Application.DEFAULT_CHAR_COUNT):
                scan_line_buffer = stream.read(self.__char_height)
                scan_lines = self.__write_char(num, scan_line_buffer)
                result[num] = scan_lines
            stream.close()
        return result

    def run(self):
        self._detect_information("resources/font0.sfn")
        font = self._read("resources/font0.sfn")
        print(font)


if __name__ == "__main__":
    app = Application()
    app.run()
