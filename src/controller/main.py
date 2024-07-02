import sys

from antlr4 import FileStream, CommonTokenStream
from ..Parser.GraphLangLexer import GraphLangLexer
from ..Parser.GraphLangParser import GraphLangParser
from ..Parser.CustomVisitor import CustomVisitor

def main():
    file_path = 'input03.txt'
    input_stream = FileStream(file_path)
    lexer = GraphLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GraphLangParser(stream)
    tree = parser.programa()

    visitor = CustomVisitor()
    visitor.visit(tree)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)