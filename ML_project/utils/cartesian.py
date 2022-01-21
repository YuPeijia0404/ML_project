class Cartesian():
    def __init__(self, datagroup):
        self.datagroup = datagroup
        self.counterIndex = len(datagroup)-1
        self.counter = [0 for i in range(0, len(self.datagroup))]

    def countlength(self):
        i = 0
        length = 1
        while(i < len(self.datagroup)):
            length *= len(self.datagroup[i])
            i += 1
        return length

    def handle(self):
        self.counter[self.counterIndex]+=1
        if self.counter[self.counterIndex] >= len(self.datagroup[self.counterIndex]):   

            self.counter[self.counterIndex] = 0
            self.counterIndex -= 1
            if self.counterIndex >= 0:
                self.handle()
            self.counterIndex = len(self.datagroup)-1

    def assemble(self):
        combinations = []
        length = self.countlength()
        i = 0
        while(i < length):
            attrlist = []
            j = 0
            while(j<len(self.datagroup)):
                attrlist.append(int(self.datagroup[j][self.counter[j]]))
                j += 1
            combinations.append(attrlist)
            self.handle()
            i += 1
        return combinations