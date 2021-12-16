from lark import Lark
from lark.exceptions import UnexpectedInput
from inputscriptparser.grammer import SCRIPT_GRAMMER
from inputscriptparser.parser import ScriptInterpreter
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
    script = ScriptInterpreter().visit(tree)
    print("SCRIPT")
    for (cmd, args) in script:
        print("  COMMAND: " + cmd)
        print("     ARGS: " + repr(args))



main()
