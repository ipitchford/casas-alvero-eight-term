"""Portable POSIX native-replay options; compiler commands never use a shell."""
import argparse
import math
import os
import shlex


def positive_seconds(value):
    try:
        seconds = float(value)
    except (TypeError, ValueError) as error:
        raise argparse.ArgumentTypeError('expected a positive finite number of seconds') from error
    if not math.isfinite(seconds) or seconds <= 0:
        raise argparse.ArgumentTypeError('expected a positive finite number of seconds')
    return seconds


def compiler_argv(value=None):
    command = shlex.split(value if value is not None else os.environ.get('CXX', 'c++'))
    if not command:
        raise ValueError('CXX/--cxx must name a C++17 compiler')
    return command


def add_native_options(parser, native_default):
    parser.add_argument('--cxx', default=None,
                        help='compiler command, parsed as argv without a shell; default: CXX or c++')
    parser.add_argument('--compile-timeout', type=positive_seconds, default=30,
                        help='compiler wall limit in seconds (default: 30)')
    parser.add_argument('--native-timeout', type=positive_seconds, default=native_default,
                        help='native enumeration wall limit in seconds')


def native_flags(args, native_timeout=None):
    flags = ['--compile-timeout', str(args.compile_timeout),
             '--native-timeout', str(args.native_timeout if native_timeout is None else native_timeout)]
    if args.cxx is not None:
        flags += ['--cxx', args.cxx]
    return flags
