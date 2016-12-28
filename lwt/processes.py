from subprocess import check_output

def cmd():
    lines = str(check_output(["lsof", "-i"]))

    ret = []
    for line in lines.split("\\n")[1:]:
        line = line.split()[:2]

        if len(line) < 2:
            continue

        name, pid = line

        ret.append({"name": name, "pid": pid})

    return ret


def filter_processes(args):
    return [proc for proc in cmd() if  proc["name"] not in args.names
                                   and proc["pid"] not in args.pids]
