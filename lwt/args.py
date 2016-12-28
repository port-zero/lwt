import argparse
import sys

def parse_args():
    descr = "Get processes with open sockets but no permission to use them"

    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('--pids', '-p',
                        type=argparse.FileType('r'),
                        help='the PID file')
    parser.add_argument('--names', '-n',
                        type=argparse.FileType('r'),
                        help='the process name file')
    parser.add_argument('--monitor', '-m', action='store_true',
                        help='continuously monitor the system')
    parser.add_argument('--monitor-time', '-t', type=float,
                        default=1,
                        help='the number of seconds to wait between monitor runs (can be fraction)')

    args = parser.parse_args()

    if not args.pids and not args.names:
        print("[x] Must specify either a PID file or a process name file")
        sys.exit(1)

    if args.pids:
        args.pids = args.pids.read().splitlines()
    else:
        args.pids = []

    if args.names:
        args.names = args.names.read().splitlines()
    else:
        args.names = []

    return args
