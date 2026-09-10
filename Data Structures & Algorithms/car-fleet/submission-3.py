class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pos_spd = list(zip(position, speed))
        pos_spd.sort(reverse=True, key=lambda x:x[0])
        st = []
        prev = 0
        count = 0

        for element in pos_spd:

            time_cal = (target - element[0])/element[1]

            # if (not st) or (st and time_cal > st[-1]):
            #     st.append(time_cal)
            
            if time_cal > prev:
                count += 1
                prev = time_cal

        # return len(st)
        return count
            

