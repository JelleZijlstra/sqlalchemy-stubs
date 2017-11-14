#!/usr/bin/env python3
"""Test runner for typeshed.

Depends on mypy being installed.

Approach:

1. Parse sys.argv
2. Compute appropriate arguments for mypy
3. Stuff those arguments into sys.argv
4. Run mypy.main('')
5. Repeat steps 2-4 for other mypy runs (e.g. --py2)
"""

import os
import re
import sys
import argparse

parser = argparse.ArgumentParser(description="Test runner for typeshed. "
                                             "Patterns are unanchored regexps on the full path.")
parser.add_argument('-v', '--verbose', action='count', default=0, help="More output")
parser.add_argument('-n', '--dry-run', action='store_true', help="Don't actually run mypy")
parser.add_argument('-x', '--exclude', type=str, nargs='*', help="Exclude pattern")
parser.add_argument('-p', '--python-version', type=str, nargs='*',
                    help="These versions only (major[.minor])")
parser.add_argument('--no-implicit-optional', action='store_true',
                    help="Run mypy with --no-implicit-optional (causes lots of errors)")
parser.add_argument('--warn-unused-ignores', action='store_true',
                    help="Run mypy with --warn-unused-ignores "
                    "(hint: only git rid of warnings that are "
                    "unused for all platforms and Python versions)")

parser.add_argument('filter', type=str, nargs='*', help="Include pattern (default all)")


def log(args, *varargs):
    if args.verbose >= 2:
        print(*varargs)


def match(fn, args):
    if not args.filter and not args.exclude:
        log(args, fn, 'accept by default')
        return True
    if args.exclude:
        for f in args.exclude:
            if re.search(f, fn):
                log(args, fn, 'excluded by pattern', f)
                return False
    if args.filter:
        for f in args.filter:
            if re.search(f, fn):
                log(args, fn, 'accepted by pattern', f)
                return True
    if args.filter:
        log(args, fn, 'rejected (no pattern matches)')
        return False
    log(args, fn, 'accepted (no exclude pattern matches)')
    return True


def libpath(major, minor):
    versions = ['%d.%d' % (major, minor)
                for minor in reversed(range(minor + 1))]
    versions.append(str(major))
    versions.append('2and3')
    paths = []
    for v in versions:
        for top in ['stdlib', 'third_party']:
            p = os.path.join(top, v)
            if os.path.isdir(p):
                paths.append(p)
    return paths


def main():
    args = parser.parse_args()

    try:
        from mypy.main import main as mypy_main
    except ImportError:
        print("Cannot import mypy. Did you install it?")
        sys.exit(1)

    versions = [(3, 6), (3, 5), (3, 4), (3, 3), (2, 7)]
    code = 0
    for major, minor in versions:
        flags = ['--python-version', '%d.%d' % (major, minor)]
        flags.append('--strict-optional')
        if args.no_implicit_optional:
            flags.append('--no-implicit-optional')
        if args.warn_unused_ignores:
            flags.append('--warn-unused-ignores')
        sys.argv = ['mypy'] + flags + ['sqlalchemy']
        if args.verbose:
            print("running", ' '.join(sys.argv))
        else:
            print("running mypy", ' '.join(flags))
        try:
            if not args.dry_run:
                mypy_main('')
        except SystemExit as err:
            code = max(code, err.code)
        if code:
            print("--- exit status", code, "---")
            sys.exit(code)


if __name__ == '__main__':
    main()
