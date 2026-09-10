class MinStack:

    def __init__(self):
        self.st = []
        self.minSt = []
        
    def push(self, val: int) -> None:

        self.st.append(val)

        if self.minSt:
            if val <= self.minSt[-1]:
                self.minSt.append(val)
        else:
            self.minSt.append(val)

    def pop(self) -> None:
        if self.st[-1] == self.minSt[-1]:
            self.minSt.pop()   
        
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minSt[-1]
        