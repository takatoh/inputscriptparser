from inputscriptparser import Parser
from inputscriptparser.labeledscript import Parser as LParser
from argparse import ArgumentParser


def main():
    options = parse_options()

    with open(options.input_file, 'r') as f:
        input_data = f.read()

    if options.parser == 'script':
        parser = Parser()
    elif options.parser == 'labeled':
        parser = LParser()

    script = parser.parse(input_data)

    if options.parser == 'script':
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
    parser.add_argument(
        '-p', '--parser',
        action='store',
        choices=[ 'script', 'labeled' ],
        default='script',
        help='specify parser. default to `script`'
    )
    args = parser.parse_args()
    return args
