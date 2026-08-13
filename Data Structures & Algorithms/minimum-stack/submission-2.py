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
            curr_val = min(self.minSt[-1], val)
        else:
            curr_val = val

        self.minSt.append(curr_val)

    def pop(self) -> None:
        # non-empty stacks
        self.st.pop()         
        self.minSt.pop()
        
    def top(self) -> int:
        # non-empty stacks
        return self.st[-1] 

    def getMin(self) -> int:
        # non-empty stacks
        return self.minSt[-1] 
        
