class Mayor:
    def __init__(self) -> None:
        pass

    def mayor(self, n1: int, n2: int) -> int:
        result = None
        if n1 > n2:
            result = n1
        elif n2 > n1:
            result = n2
        elif n2 == n1:
            result = None
        return result
