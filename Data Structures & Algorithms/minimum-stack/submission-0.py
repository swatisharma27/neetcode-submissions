class MinStack:
    """
    We will maintain two stacks - 
        1. One stack for normal operations
        2. Second stack for minStack operations 
    """

    def __init__(self):
        self.st = []
        self.minSt = []        

    def push(self, val: int) -> None:
        # Enter in stack
        self.st.append(val)

        # Enter in min stack
        if self.minSt:
            val = min(self.minSt[-1], val)
            self.minSt.append(val)
        else:
            self.minSt.append(val)

    def pop(self) -> None:
        if self.st:
            self.st.pop() 
        
        if self.minSt:
            self.minSt.pop()
        
    def top(self) -> int:
        return self.st[-1] if self.st else None

    def getMin(self) -> int:
        return self.minSt[-1] if self.minSt else None
        
