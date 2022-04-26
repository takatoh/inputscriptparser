from inputscriptparser import Parser
from argparse import ArgumentParser


def main():
    options = parse_options()

    with open(options.input_file, 'r') as f:
        input_data = f.read()

    parser = Parser()
    script = parser.parse(input_data)

    print('SCRIPT')
    for (cmd, args) in script:
        print('  COMMAND: ' + cmd)
        print('     ARGS: ' + repr(args))


def parse_options():
    parser = ArgumentParser(
        description='Example for InputScriptParser'
    )
    parser.add_argument(
        'input_file',
        metavar='INPUT_FILE',
        help='input script file'
    )
    args = parser.parse_args()
    return args
