from lark import Lark
from lark.exceptions import UnexpectedInput
from lark.visitors import Interpreter
from inputscriptparser.grammers import SCRIPT_GRAMMER
from inputscriptparser.common import Keyword, flatten


class Parser():
    def __init__(self):
        self.parser = Lark(SCRIPT_GRAMMER, start="script")

    def parse(self, input_data):
        try:
            tree = self.parser.parse(input_data)
        except UnexpectedInput as e:
            context = e.get_context(input_data)
            print(f"Syntax error:  line = {e.line}  column = {e.column}\n")
            print(context)
            exit(1)

        script = ScriptInterpreter().visit(tree)
        return script


class ScriptInterpreter(Interpreter):
    def script(self, tree):
        return [self.visit(c) for c  in tree.children]

    def statement(self, tree):
        (cmd, args1) = self.visit(tree.children[0])
        args2 = flatten([ self.visit(a) for a in tree.children[1:] ])
        return (cmd, args1 + args2)

    def line(self, tree):
        cmd = self.visit(tree.children[0])
        if len(tree.children) > 1:
            args = flatten(self.visit(tree.children[1]))
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
