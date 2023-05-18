from lark import Lark
from lark.exceptions import UnexpectedInput
from lark.visitors import Interpreter, Transformer
from inputscriptparser.common import Keyword, flatten
from os import path

here = path.dirname(path.abspath(__file__))
grammer_file = path.join(here, '../grammers/labeledscript.lark')
with open(grammer_file) as f:
    SCRIPT_GRAMMER = f.read()


class Parser():
    def __init__(self):
        self.parser = Lark(SCRIPT_GRAMMER, start='script')

    def parse(self, input_data):
        try:
            tree = self.parser.parse(input_data)
        except UnexpectedInput as e:
            context = e.get_context(input_data)
            print(f'Syntax error:  line = {e.line}  column = {e.column}\n')
            print(context)
            exit(1)
#        print(tree.pretty())

        return tree
