#

from __future__ import absolute_import

import logging

from ._model import Font, Char
from ._parser import LineParser


class FontReader(object):
    class State(object):
        UNKNOWN = 0
        FONT = 1
        PROPERTIES = 2
        CHAR = 3
        BITMAP = 4

    def __init__(self, path):
        self.__path = path
        self.__state = FontReader.State.UNKNOWN
        self.__line = 0
        self.__font = None
        self.__char_scan = []
        self.__log = logging.getLogger("pybmf.reader.FontReader")

    def __process_line_args(self, line):
        line_parser = LineParser()
        return line_parser.parse(line)

    def __process_line(self, line):
        self.__line += 1
        #
        params = self.__process_line_args(line)
        self.__log.debug("Params %r", params)
        command = params[0]
        args = params[1:]
        #
        if self.__state == FontReader.State.BITMAP:
            if command == "ENDBITMAP":
                self.__state = FontReader.State.CHAR
                self.__current_char.set_scan_line( self.__char_scan )
                self.__char_scan = None
            else:
                self.__char_scan.append(command)
        elif self.__state == FontReader.State.UNKNOWN:
            if command == "STARTFONT":
                self.__state = FontReader.State.FONT
                self.__font = Font()
            else:
                raise Exception("Unexpected statement `{statement}` on line {line}".format(statement=line, line=self.__line))
        elif self.__state == FontReader.State.CHAR:
            if command == "ENDCHAR":
                self.__state = FontReader.State.FONT
                char_id = self.__current_char.get_encoding()
                self.__font.set_char(char_id, self.__current_char)
                self.__current_char = None
            elif command == "ENCODING":
                code = int(args[0])
                self.__current_char.set_encoding(code)
            elif command == "BBX":
                pass
            elif command == "STARTBITMAP":
                self.__state = FontReader.State.BITMAP
                self.__char_scan = []
            else:
                raise Exception("Unexpected statement `{statement}` on line {line}".format(statement=line, line=self.__line))
        elif self.__state == FontReader.State.FONT:
            if command == "ENDFONT":
                self.__state = FontReader.State.UNKNOWN
            elif command == "FONT":
                self.__font.set_name(args[0])
            elif command == "CONTENTVERSION":
                pass
            elif command == "STARTCHAR":
                self.__current_char = Char(code=args[0])
                self.__state = FontReader.State.CHAR
            elif command == "COMMENT":
                self.__font.set_comment(args[0])
            else:
                raise Exception("Unexpected statement `{statement}` on line {line}".format(statement=line, line=self.__line))
        else:
            raise Exception("Not implement state")

    def read(self):
        with open(self.__path, "rb") as stream:
            while True:
                line = stream.readline()
                if not line:
                    break
                line = line.strip()
                if len(line) == 0:
                    continue
                if line[0] == "#":
                    continue
                self.__process_line(line)
            stream.close()
        return self.__font
