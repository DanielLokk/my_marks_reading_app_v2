class Set:
    reps = 0
    kg = 0
    rir = 0
    
    def __init__(self, reps, rir, kg=0):
        self.reps = reps
        self.kg = kg
        self.rir = rir

    def getSet(self):
        return f"{self.reps} reps X {self.kg} kg with {self.rir} reps remaining"

    def getWeight(self):
        return self.kg
    
    def getReps(self):
        return self.reps
    
    def getRir(self):
        return self.rir
