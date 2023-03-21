reset = "\x1b[0m"
bgRed = "\x1b[41m"
bgGreen = "\x1b[42m"
bgYellow = "\x1b[43m"
bgMagenta = "\x1b[45m"
bgCyan = "\x1b[46m"

def o2j(list_of_objs):
    j = json.dumps( list_of_objs )
    return j 

def red(msg): 
    x = "{}{}{}".format(bgRed,  msg, reset)
    print(x)

def green(msg):
    x = "{}{}{}".format(bgGreen,  msg, reset)
    print(x)

def yellow(msg):
    x = "{}{}{}".format(bgYellow,  msg, reset)
    print(x)

def magenta(msg): 
    x = "{}{}{}".format(bgMagenta,  msg, reset)
    print(x)


def cyan(msg): 
    x = "{}{}{}".format(bgCyan,  msg, reset)
    print(x)

def verdict(a, b, msg):
    if a == b:
        cyan("PASS " + msg )
    else:
        yellow("FAIL " + msg)
