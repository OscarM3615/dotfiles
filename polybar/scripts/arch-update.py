import subprocess
from subprocess import check_output
import argparse
import os
import re

def create_argparse():
    def _default(name, default='', arg_type=str):
        val = default
        if name in os.environ:
            val = os.environ[name]
        return arg_type(val)

    strbool = lambda s: s.lower() in ['t', 'true', '1']
    strlist = lambda s: s.split()

    parser = argparse.ArgumentParser(description='Check for pacman updates')
    parser.add_argument(
        '-a',
        '--aur',
        action = 'store_const',
        const = True,
        default = _default('AUR', 'False', strbool),
        help='Include AUR packages. Attn: Yay must be installed'
    )
    parser.add_argument(
        '-q',
        '--quiet',
        action = 'store_const',
        const = True,
        default = _default('QUIET', 'False', strbool),
        help = 'Do not produce output when system is up to date'
    )
    return parser.parse_args()

def get_updates():
    output = ''
    try:
        output = check_output(['checkupdates']).decode('utf-8')
    except subprocess.CalledProcessError as exc:
        # checkupdates exits with 2 and no output if no updates are available.
        # we ignore this case and go on
        if not (exc.returncode == 2 and not exc.output):
            raise exc
    if not output:
        return []

    updates = [line.split(' ')[0]
               for line in output.split('\n')
               if line]

    return updates

def get_aur_updates():
    output = ''
    try:
        output = check_output(['yay', '-Qua']).decode('utf-8')
    except subprocess.CalledProcessError as exc:
        if not (exc.returncode == 1 and not exc.output):
            raise exc
    if not output:
        return []

    aur_updates = [line.split(' ')[0] for line in output.split('\n') if line]

    return aur_updates

args = create_argparse()
updates = get_updates()

if args.aur:
    updates += get_aur_updates()

update_count = len(updates)
if update_count > 0:
    print(update_count)
elif not args.quiet:
    print('system up to date')
