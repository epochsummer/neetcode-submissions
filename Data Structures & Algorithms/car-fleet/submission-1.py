class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = {}
        stack = []
        for pos, spe in zip(position,speed):
            dest = (target - pos)
            time[pos] = float(dest / spe)

        position.sort(reverse=True)
        stack.append(time[position[0]])
        for i in range(1,len(position)):
            if time[position[i]] > stack[-1]:
                stack.append(time[position[i]])
        return len(stack)

            

            

        



        