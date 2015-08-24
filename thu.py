import signal
TIMEOUT = 5 # number of seconds your want for timeout

def interrupted(signum, frame):
    "called when read times out"
    print 'interrupted!'
signal.signal(signal.SIGALRM, interrupted)

def input():
    try:
            print 'You have 5 seconds to type in your stuff...'
            foo = raw_input()
            return foo
    except:
            # timeout
            return

# set alarm
signal.alarm(TIMEOUT)
# disable the alarm after success
s = input()
print "Bye bye"
