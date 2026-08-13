import logging 
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        combine = []
        try:
            for p, s in zip(position, speed):
                combine.append((p, s))
        except IndexError:
            logging.warning("Position and Speed not of matching lengths")
            return 

        combine.sort(key=lambda x:x[0])

        st = []
        N = len(combine)
        for i in range(N-1, -1, -1):
            try:
                arrival_time = (target - combine[i][0]) / combine[i][1]
                if st:
                    if st[-1] < arrival_time:
                        st.append(arrival_time)
                else:
                    st.append(arrival_time)
            except ZeroDivisionError:
                logging.warning("Speed is zero")
                return

        return len(st)





        
