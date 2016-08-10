#


class LineParser(object):
    CHAR_QUOTE = '"'
    CHAR_ESCAPE = '\\'

    def parse(self, line):
        result = []
        quote = False
        escape = False
        buffer = ""
        for ch in line:
            if quote is True:
                if escape is True:
                    buffer += ch
                    escape = False
                else:
                    if ch == LineParser.CHAR_ESCAPE:
                        escape = True
                    elif ch == LineParser.CHAR_QUOTE:
                        quote = False
                    else:
                        buffer += ch
            else:
                if ch == LineParser.CHAR_QUOTE:
                    quote = True
                elif ch.isspace():
                    result.append(buffer)
                    buffer = ""
                else:
                    buffer += ch
        result.append(buffer)
        return result
