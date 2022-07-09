def chess_knight(x1, y1, x2, y2):
    if x1 == x2-1 and y1 == y2-2 and x1 != x2 and y1 != y2:
        return "Yes"
    elif x1 == x2-2 and y1 == y2-1 and x1 != x2 and y1 != y2:
        return "Yes"
    elif x1 == x2-1 and y1 == y2+2 and x1 != x2 and y1 != y2:
        return "Yes"
    elif x1 == x2-2 and y1 == y2+1 and x1 != x2 and y1 != y2:
        return "Yes"
    elif x1 == x2+1 and y1 == y2-2 and x1 != x2 and y1 != y2:
        return "Yes"
    elif x1 == x2+2 and y1 == y2-1 and x1 != x2 and y1 != y2:
        return "Yes"
    elif x1 == x2+1 and y1 == y2+2 and x1 != x2 and y1 != y2:
        return "Yes"
    elif x1 == x2+2 and y1 == y2+1 and x1 != x2 and y1 != y2:
        return "Yes"
    else:
        return "No"
print(chess_knight(5, 4, 6, 7))