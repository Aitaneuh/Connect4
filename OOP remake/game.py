class Game:
    board = [[" " for cols in range(7)] for rows in range(6)]

    def __str__(self):
        res = ("\n 0 1 2 3 4 5 6")
        res += ("\n+" + "--"*(6) + "-" + "+")
        for row in self.board:
            res += ("\n|" + "|".join(row) + "|")
        res += "\n+" + "--"*(6) + "-" + "+\n"
        return res
