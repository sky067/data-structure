
class BinTNode:
    def __init__(self, data, lchild, rchild) -> None:
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


root = BinTNode(data=1, lchild=BinTNode(2), rchild=BinTNode(3))


def f(T):
    stack = []  # 栈
    if T:
        stack.append(T)

    while T and T.lchild:
        stack.append(T)
        
    t = stack.pop()
    print(t.data)

    if t.rchild:
        