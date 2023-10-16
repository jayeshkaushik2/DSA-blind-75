class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
if __name__ == "__main__":
    cmds = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    input = [[], [-2], [0], [-3], [], [], [], []]
    print(f"Cmds : {cmds}, input: {input}")
    output = []
    for i, cmd in enumerate(cmds):
        if cmd == "MinStack":
            obj = MinStack()
            output.append(None)
            continue
        if cmd == "push":
            res = getattr(obj, cmd)(input[i][0])
        else:
            res = getattr(obj, cmd)()
        output.append(res)

    print(f"Ouput: {output}")
