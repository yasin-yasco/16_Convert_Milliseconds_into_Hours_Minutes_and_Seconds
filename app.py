def convert(milliseconds):
    seconds=(milliseconds/1000)%60
    seconds = int(seconds)
    minutes=(milliseconds/(1000*60))%60
    minutes = int(minutes)
    hours=(milliseconds/(1000*60*60))%24
    result = ''
    if milliseconds < 1000:
        result = ("Just %d millisecond/s" % (milliseconds))
    elif milliseconds < 60000:
        result = ("%d second/s" % (seconds))
    elif milliseconds < 360000:
        result = ("%d minute/s %d second/s" % (minutes, seconds))
    elif milliseconds < (24*360000):
        result = ("%d hour/s %d minute/s %d second/s" % (hours, minutes, seconds))
    return result