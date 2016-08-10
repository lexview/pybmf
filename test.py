#!/usr/bin/python

from pybmf import FontReader



class Application(object):

    def __show_all_chars(self, font):
        for encoding, char in font.get_chars().items():
            print("encoding %s" % encoding)
            self.__show_char(char)

    def __show_char(self, char):
        scan_line_list = char.get_scan_line()
        for scan_line in scan_line_list:
            print(scan_line)

    def run(self):
        """ Main point
        """
        font_reader = FontReader("resources/font.bmf")
        font = font_reader.read()
        #
        print("Char count: {char_count}".format(char_count=font.get_char_count()))
        #
        self.__show_all_chars(font)
        # Step 2. Search char
        code = ord('1')
        h_code = "{code:X}".format(code=code)
        #
        char = font.get_char(code)
        self.__show_char(char)


if __name__ == "__main__":
    app = Application()
    app.run()
