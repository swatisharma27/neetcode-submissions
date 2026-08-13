class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        st = []
        pos_spd = []

        for i, j in zip(position, speed):
           pos_spd.append((i, j)) 

        pos_spd.sort(key=lambda x:x[0], reverse=True)

        for i in range(len(pos_spd)):

            time_i = (target - pos_spd[i][0]) / pos_spd[i][1]

            if not st:
                st.append(time_i)

            if st and time_i > st[-1]:
                st.append(time_i)

        return len(st)
