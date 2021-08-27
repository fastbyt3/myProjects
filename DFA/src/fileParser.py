def parseFile(f):
    # No of states : first line
    l = f.readline()
    nState = int(l.split('\n')[0])

    # Initial state
    l = f.readline()
    initState = int(l.split('\n')[0])

    # Final state
    l = f.readline()
    finalState = int(l.split('\n')[0])

    # Transitions
    transitions = [None] * nState

    while True:
        l = f.readline()
        if not l:
            break

        x = (l.rsplit('\n')[0]).split(' ')
        srcState = int(x[0])
        destState = int(x[2])
        symbol = x[1]

        if transitions[srcState - 1] is None:
            currTransition = {
                symbol: destState
            }
            transitions[srcState - 1] = currTransition
        else:
            transitions[srcState - 1][symbol] = destState

    return nState, initState, finalState, transitions
