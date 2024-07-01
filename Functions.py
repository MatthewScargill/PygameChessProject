def ListToIntCoord(Position):
    x_pos, y_pos = Position
    IntPosition = x_pos // 100 + 8 * (7 - y_pos // 100)
    return IntPosition

def IntToListCoord(IntPosition):
    x_pos = int((IntPosition % 8) * 100 + 50)
    y_pos = int(800 - (IntPosition // 8 * 100 + 50))

    return x_pos, y_pos
