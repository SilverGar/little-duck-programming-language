import sys
from antlr4 import *
from LittleDuckLexer import LittleDuckLexer
from LittleDuckParser import LittleDuckParser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = LittleDuckLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LittleDuckParser(stream)
    tree = parser.prog()


if __name__ == '__main__':
    main(sys.argv)

symbolTable = {
}
