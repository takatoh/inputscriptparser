from inputscriptparser.parser import Parser
import sys


def main():
    parser = Parser()

    with open(sys.argv[1], "r") as f:
        input_data = f.read()

    script = parser.parse(input_data)

    print("SCRIPT")
    for (cmd, args) in script:
        print("  COMMAND: " + cmd)
        print("     ARGS: " + repr(args))



main()
