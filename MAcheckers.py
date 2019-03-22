from graphics import*
print("Please insert a size for checkers board") 
while True:
    try:
        square = int(input())
        break
    except ValueError:
        print("That is not an integer!")

checkersWin = GraphWin("Checkers", square*10,square*10)
checkersWin.setCoords(0,0,square*10,square*10)

def draw(col,row,sqCol):
    global square
    SQ = Rectangle(Point(square*(row+1),square*(col+1)),
                   Point(square*(row+2),square*(col+2)))
    SQ.setFill(sqCol)
    SQ.draw(checkersWin)

for j in range (8):
    for i in range (8):
        if j % 2 == 0:
            if i % 2 == 0:
                color = "red"
            else:
                color = "black"
        else:
            if i % 2 == 0:
                color = "black"
            else:
                color = "red"
        draw(i,j,color)
  
checkersWin.getMouse()
checkersWin.close()
