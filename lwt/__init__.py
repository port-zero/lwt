import time

from lwt.args      import parse_args
from lwt.processes import filter_processes
from lwt.report    import report

def run():
    args = parse_args()

    while True:
        offending = filter_processes(args)

        report(offending)

        if not args.monitor:
            return

        time.sleep(args.monitor_time)
