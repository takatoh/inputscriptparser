from lark import Lark
from lark.visitors import Interpreter
from lark.exceptions import UnexpectedInput
from inputscriptparser.grammer import SCRIPT_GRAMMER
import sys


def main():
    parser = Lark(SCRIPT_GRAMMER, start="script")

    with open(sys.argv[1], "r") as f:
        input_data = f.read()

    try:
        tree = parser.parse(input_data)
    except UnexpectedInput as e:
        context = e.get_context(input_data)
        print(f"Syntax error:  line = {e.line}  column = {e.column}\n")
        print(context)
        exit(1)

    #print(tree.pretty())
    MyInterpreter().visit(tree)


class MyInterpreter(Interpreter):
    def script(self, tree):
        print("SCRIPT")
        for c in tree.children:
            (cmd, args) = self.visit(c)
            print("    COMMAND: " + cmd)
            print("    ARGS:    " + repr(args))

    def statement(self, tree):
        (cmd, args1) = self.visit(tree.children[0])
        args2 = _flatten([ self.visit(a) for a in tree.children[1:] ])
        return (cmd, args1 + args2)

    def line(self, tree):
        cmd = self.visit(tree.children[0])
        if len(tree.children) > 1:
            args = _flatten(self.visit(tree.children[1]))
        else:
            args = []
        return (cmd, args)

    def continued(self, tree):
        return self.visit(tree.children[0])

    def command(self, tree):
        return tree.children[0]

    def arglist(self, tree):
        args = [ self.visit(a) for a in tree.children ]
        return args

    def arg(self, tree):
        return self.visit(tree.children[0])

    def number(self, tree):
        return float(tree.children[0])

    def string(self, tree):
        return tree.children[0].strip('"')

    def keyword(self, tree):
        return Keyword(str(tree.children[0]))

    def boolean(self, tree):
        return self.visit(tree.children[0])

    def true(self, tree):
        return True

    def false(self, tree):
        return False


class Keyword():
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f'Keyword<{self.val}>'

    def __repr__(self):
        return f'Keyword<{self.val}>'


def _flatten(lis):
    result = []
    for elem in lis:
        if isinstance(elem, list):
            result += _flatten(elem)
        else:
            result.append(elem)
    return result



main()
