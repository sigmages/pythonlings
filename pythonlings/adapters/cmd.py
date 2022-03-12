import os
import sys
import i18n
import argparse

from pythonlings.services.exercises import process_exercises, process_single_exercise

i18n.config.set('locale', os.getenv('PYTHONLINGS_LANGUAGE', 'en'))
i18n.load_path.append('pythonlings/i18n')
_ = i18n.t


def run():
    parser = argparse.ArgumentParser(
        description=_('p.description')
    )
    parser.set_defaults(func=parser.print_help, type=bool)

    subparsers = parser.add_subparsers(dest='command')
    start_command = subparsers.add_parser('start', help=_('p.start_help'))
    start_command.set_defaults(func=process_exercises)

    exec_command = subparsers.add_parser('exec', help=_('p.exec_help'))
    exec_command.set_defaults(func=process_single_exercise)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    argx = parser.parse_args()
    argx.func(argx)
