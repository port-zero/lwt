def report(offending):
    tpl = "[x] Offending process found: {} (PID: {})"
    for proc in offending:
        print(tpl.format(proc["name"], proc["pid"]))

    return 0
