liste = [[1, 2], [3, 4], [5, 6, 7]]
listea = liste[0]
listeb = liste[1]
listec = liste[2]

listea = listea[::-1]
listeb = listeb[::-1]
listec = listec[::-1]

liste1 = [listec, listeb, listea]
liste = [liste1]

print(f"{liste}")