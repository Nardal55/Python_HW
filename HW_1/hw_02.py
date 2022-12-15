print("W Z Y X")
for W in range(2):
    for Z in range(2):
        for Y in range(2):
            for X in range(2):
                if (W and Z) or not Y or not X == (not W):
                    print(W, Z, Y, X)