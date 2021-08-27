class FA(object):
    def __init__(self, nStates, initState, finalState, transitions):
        self.nStates = nStates
        self.initState = initState
        self.finalState = finalState
        self.transitions = transitions
        self.states = []
        self.states.append(initState)

    def step(self, letter):
        tmp = []
        for s in self.states:
            possibleTransitions = self.transitions[s-1]
            if not possibleTransitions:
                pass
            elif letter in possibleTransitions:
                tmp.append(possibleTransitions[letter])

        # print(f"{self.states=}")
        self.states = tmp   # Update possible states
        # print(f"{self.states=}")
        # print('---------')
        return self.states

    def print(self):
        print(f'''
{self.nStates=}
{self.initState=}
{self.finalState=}
{self.transitions=}
            ''')