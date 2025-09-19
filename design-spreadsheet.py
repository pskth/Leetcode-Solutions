class Spreadsheet:
    sheet = []
    def __init__(self, rows: int):
        self.sheet = [[0 for _ in range(26)] for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        c = ord(cell[0]) - ord('A')
        r = int(cell[1:]) - 1
        self.sheet[r][c] = value

    def resetCell(self, cell: str) -> None:
        c = ord(cell[0]) - ord('A')
        r = int(cell[1:]) - 1
        self.sheet[r][c] = 0

    def getValue(self, formula: str) -> int:
        op1, op2 = formula[1:].split("+")

        if ord(op1[0]) >= ord('A') and ord(op1[0]) <= ord('Z'):
            c = ord(op1[0]) - ord('A')
            r = int(op1[1:]) - 1
            value1 = self.sheet[r][c]
        else:
            value1 = int(op1)

        if ord(op2[0]) >= ord('A') and ord(op2[0]) <= ord('Z'):
            r = int(op2[1:]) - 1
            c = ord(op2[0]) - ord('A')
            value2 = self.sheet[r][c]
        else:
            value2 = int(op2)

        return value1 + value2


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)