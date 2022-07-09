def chess_castle(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return "Yes"
    else:
        return "No"
print(chess_castle(1, 2, 4, 4))