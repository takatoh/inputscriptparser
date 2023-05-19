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
        print_input_script(script)
    elif options.parser == 'labeled':
        print_labeled_script(script)


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


def print_input_script(script):
    print('SCRIPT')
    for (cmd, args) in script:
        print('  COMMAND: ' + cmd)
        print('     ARGS: ' + repr(args))


def print_labeled_script(script):
    print('SCRIPT')
    for (cmd, args, substmnts) in script:
        print('  COMMAND: ' + cmd)
        print('    ARGS: ' + repr(args))
        for (subcmd, subargs) in substmnts:
            print('    SUBCOMMAND: ' + subcmd)
            print('      ARGS: ' + repr(subargs))
