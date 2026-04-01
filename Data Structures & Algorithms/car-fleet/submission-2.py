class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        A car fleet is a non-empty set of cars at same position and speed.
        if one car gets to target the whole car fleet makes it

        We probably want a stack that stays in non decreasing order for speed
        We will have a loop that will add cars to the stack from starting from
        lowest postion to greatest if the current num breaks the non decreasing order
        we check if curr car doesn't slow down cars from top of stack
        (target - position[curr]) / speed[curr]
        for that we first sort the position list
        """
        cars = {}
        stack = []
        for i in range(len(position)):
            cars[position[i]] = speed[i]
        
        for p, s in sorted(cars.items(), key=lambda item:item[0], reverse=True):
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        

        return len(stack)

        