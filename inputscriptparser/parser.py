from lark.visitors import Interpreter


class ScriptInterpreter(Interpreter):
    def script(self, tree):
        return [self.visit(c) for c  in tree.children]

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
