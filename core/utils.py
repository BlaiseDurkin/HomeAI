import math


#Multi Line Message

#todo -> pause = say nothing

class LongMessage:
    def __init__(self, message):
        self.message = message
        self.phases = self.parsePhases()
        self.current = 0

    def parsePhases(self):
        """
        break message into phases of length ~ 3 or 4
        """
        #mu = mean bin size
        """
        arr = self.message.split()
        l = len(arr)

        if l >7 and l <= 15:
            mu = 4
        elif l >15 and l <= 25:
            mu = 5
        elif l >25 and l <= 35:
            mu = 6
        elif l >35:
            mu = 7
        else:
            return [self.message]
        num_bins = math.floor(l/mu)
        phases = []
        i = 0
        for k in range(num_bins):
            s = ''
            num = mu
            if k == num_bins-1:
                num = l - i #remainder
            for j in range(num):

                s += arr[i+j] + ' '
            i += mu
            phases.append(s)
        return phases
        """
        return self.message.split(".")




