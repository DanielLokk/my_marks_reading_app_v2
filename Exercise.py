class Exercise:
    name = ''
    rest_time = 0
    n_reps = 0
    sets = []

    def __init__(self, name, rest_time):
        self.name = name
        self.rest_time = rest_time
        self.n_reps = 0
        self.sets = []

    def setNReps(self, n_reps):
        self.n_reps = n_reps

    def addSet(self, rep):
        self.sets.append(rep)

    def whatSets(self):
        my_string = ""
        for sets in self.sets:
            my_string = my_string + sets.getSet() + "\n"
        return my_string

    # show the info of the exercise
    def whatExercise(self):
        return ('This exercise name is ' + '\033[94m' + self.name + '\033[0m\n'
                + 'With ' + '\033[94m' +
                str(self.n_reps) + '\033[0m' + ' sets.\n'
                + 'And I only rest' + '\033[94m' + self.rest_time + '\033[0m')

    # get the best set of the exercise
    def getBestWeight(self):
        best = 0
        for i in range(0, len(self.sets)):
            best = i if self.sets[i].getWeight > self.sets[best].getWeight else best
        return best
