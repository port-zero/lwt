# lwt

`lwt` is a simple tool that, given a whitelist of process IDs and/or
process names, will print out any process and its ID that has an
open socket but is not in either whitelist. It is a thin, simple
wrapper around `lsof` without dependencies.

`lwt` stands for **l**ook **w**ho's **t**alking.

## Installation

`lwt` is not registered to PYPI yet, so you will have to clone the
repository and run `python setup.py install` from within the directory
manually.

## Usage

From the help text of `lwt`:

```
usage: lwt [-h] [--pids PIDS] [--names NAMES] [--monitor]
           [--monitor-time MONITOR_TIME]

Get processes with open sockets but no permission to use them

optional arguments:
  -h, --help            show this help message and exit
  --pids PIDS, -p PIDS  the PID file
  --names NAMES, -n NAMES
                        the process name file
  --monitor, -m         continuously monitor the system
  --monitor-time MONITOR_TIME, -t MONITOR_TIME
                        the number of seconds to wait between monitor runs
                        (can be fraction)
```

`lwt` needs either a PID file or a process name file (or both).

Monitor mode will continuously run the inspection, waiting an interval
of `MONITOR_TIME` seconds (monitor time can be a floating point number
or integer and will default to 1).

<hr/>

Have fun!
