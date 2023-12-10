
# 二叉树节点类
class BinTNode:
    def __init__(self, data=None, left_child=None, right_child=None) -> None:
        self.data = data  # 节点数据
        self.left_child = left_child  # 左孩子节点
        self.right_child = right_child  # 右孩子节点


root = BinTNode(data=1, left_child=BinTNode(2), right_child=BinTNode(3))


def pre_order(T):
    """

    :param T: 根节点
    :return:
    """
    if T:
        print(T.data)
        pre_order(T.left_child)
        pre_order(T.right_child)

# pre_order(root)


def in_order(T):
    """

    :param T: 根节点
    :return:
    """
    if T:
        in_order(T.left_child)
        print(T.data)
        in_order(T.right_child)

# in_order(root)


def post_order(T):
    if T:
        post_order(T.left_child)
        post_order(T.right_child)

        print(T.data)


if __name__ == '__main__':

    post_order(root)