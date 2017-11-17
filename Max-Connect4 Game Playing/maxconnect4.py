import sys
import re

inputfile1 = sys.argv[2]
table =[]

try:
    file1=open(inputfile1, 'r')
    data=[]
    line=0
    for line in file1:
        for ch in line:
            if ch!="\n":
                data.append(int(ch))
except IOError:
    sys.exit("\nError.\nFile name invalid.\n")

#represents the table
def printcomputer(a=[]):
    def piece(a):
        if a==0: return "0"
        if a==1: return "1"
        if a==2: return "2"

    print " ---------------------- "
    print " | %s| %s| %s| %s| %s| %s| %s|"%(piece(a[5][0]),piece(a[5][1]),piece(a[5][2]),piece(a[5][3]),piece(a[5][4]),piece(a[5][5]),piece(a[5][6]))
    print " ---------------------- "
    print " | %s| %s| %s| %s| %s| %s| %s|"%(piece(a[4][0]),piece(a[4][1]),piece(a[4][2]),piece(a[4][3]),piece(a[4][4]),piece(a[4][5]),piece(a[4][6]))
    print " ---------------------- "
    print " | %s| %s| %s| %s| %s| %s| %s|"%(piece(a[3][0]),piece(a[3][1]),piece(a[3][2]),piece(a[3][3]),piece(a[3][4]),piece(a[3][5]),piece(a[3][6]))
    print " ---------------------- "
    print " | %s| %s| %s| %s| %s| %s| %s|"%(piece(a[2][0]),piece(a[2][1]),piece(a[2][2]),piece(a[2][3]),piece(a[2][4]),piece(a[2][5]),piece(a[2][6]))
    print " ---------------------- "
    print " | %s| %s| %s| %s| %s| %s| %s|"%(piece(a[1][0]),piece(a[1][1]),piece(a[1][2]),piece(a[1][3]),piece(a[1][4]),piece(a[1][5]),piece(a[1][6]))
    print " ---------------------- "
    print " | %s| %s| %s| %s| %s| %s| %s|"%(piece(a[0][0]),piece(a[0][1]),piece(a[0][2]),piece(a[0][3]),piece(a[0][4]),piece(a[0][5]),piece(a[0][6]))
    print " ---------------------- "

    f=open("computer.txt", "w+")
    f.write("%s%s%s%s%s%s%s"%(piece(a[5][0]),piece(a[5][1]),piece(a[5][2]),piece(a[5][3]),piece(a[5][4]),piece(a[5][5]),piece(a[5][6])))
    f.write("\n")
    f.write("%s%s%s%s%s%s%s"%(piece(a[4][0]),piece(a[4][1]),piece(a[4][2]),piece(a[4][3]),piece(a[4][4]),piece(a[4][5]),piece(a[4][6])))
    f.write("\n")
    f.write("%s%s%s%s%s%s%s"%(piece(a[3][0]),piece(a[3][1]),piece(a[3][2]),piece(a[3][3]),piece(a[3][4]),piece(a[3][5]),piece(a[3][6])))
    f.write("\n")
    f.write("%s%s%s%s%s%s%s"%(piece(a[2][0]),piece(a[2][1]),piece(a[2][2]),piece(a[2][3]),piece(a[2][4]),piece(a[2][5]),piece(a[2][6])))
    f.write("\n")
    f.write("%s%s%s%s%s%s%s"%(piece(a[1][0]),piece(a[1][1]),piece(a[1][2]),piece(a[1][3]),piece(a[1][4]),piece(a[1][5]),piece(a[1][6])))
    f.write("\n")
    f.write("%s%s%s%s%s%s%s"%(piece(a[0][0]),piece(a[0][1]),piece(a[0][2]),piece(a[0][3]),piece(a[0][4]),piece(a[0][5]),piece(a[0][6])))
    f.write("\n")
    f.write("2")

    

def printhuman(a=[]):
    def piece(a):
        if a==0: return "0"
        if a==1: return "1"
        if a==2: return "2"

    print " ---------------------- "
    print " | %s| %s| %s| %s| %s| %s| %s|"%(piece(a[5][0]),piece(a[5][1]),piece(a[5][2]),piece(a[5][3]),piece(a[5][4]),piece(a[5][5]),piece(a[5][6]))
    print " ---------------------- "
    print " | %s| %s| %s| %s| %s| %s| %s|"%(piece(a[4][0]),piece(a[4][1]),piece(a[4][2]),piece(a[4][3]),piece(a[4][4]),piece(a[4][5]),piece(a[4][6]))
    print " ---------------------- "
    print " | %s| %s| %s| %s| %s| %s| %s|"%(piece(a[3][0]),piece(a[3][1]),piece(a[3][2]),piece(a[3][3]),piece(a[3][4]),piece(a[3][5]),piece(a[3][6]))
    print " ---------------------- "
    print " | %s| %s| %s| %s| %s| %s| %s|"%(piece(a[2][0]),piece(a[2][1]),piece(a[2][2]),piece(a[2][3]),piece(a[2][4]),piece(a[2][5]),piece(a[2][6]))
    print " ---------------------- "
    print " | %s| %s| %s| %s| %s| %s| %s|"%(piece(a[1][0]),piece(a[1][1]),piece(a[1][2]),piece(a[1][3]),piece(a[1][4]),piece(a[1][5]),piece(a[1][6]))
    print " ---------------------- "
    print " | %s| %s| %s| %s| %s| %s| %s|"%(piece(a[0][0]),piece(a[0][1]),piece(a[0][2]),piece(a[0][3]),piece(a[0][4]),piece(a[0][5]),piece(a[0][6]))
    print " ---------------------- "


    f=open("human.txt", "w+")
    f.write("%s%s%s%s%s%s%s"%(piece(a[5][0]),piece(a[5][1]),piece(a[5][2]),piece(a[5][3]),piece(a[5][4]),piece(a[5][5]),piece(a[5][6])))
    f.write("\n")
    f.write("%s%s%s%s%s%s%s"%(piece(a[4][0]),piece(a[4][1]),piece(a[4][2]),piece(a[4][3]),piece(a[4][4]),piece(a[4][5]),piece(a[4][6])))
    f.write("\n")
    f.write("%s%s%s%s%s%s%s"%(piece(a[3][0]),piece(a[3][1]),piece(a[3][2]),piece(a[3][3]),piece(a[3][4]),piece(a[3][5]),piece(a[3][6])))
    f.write("\n")
    f.write("%s%s%s%s%s%s%s"%(piece(a[2][0]),piece(a[2][1]),piece(a[2][2]),piece(a[2][3]),piece(a[2][4]),piece(a[2][5]),piece(a[2][6])))
    f.write("\n")
    f.write("%s%s%s%s%s%s%s"%(piece(a[1][0]),piece(a[1][1]),piece(a[1][2]),piece(a[1][3]),piece(a[1][4]),piece(a[1][5]),piece(a[1][6])))
    f.write("\n")
    f.write("%s%s%s%s%s%s%s"%(piece(a[0][0]),piece(a[0][1]),piece(a[0][2]),piece(a[0][3]),piece(a[0][4]),piece(a[0][5]),piece(a[0][6])))
    f.write("\n")
    f.write("1")

def checkstatus(grid=[]):
    win1=[1,1,1,1]
    win2=[2,2,2,2]
    a=0
    b=0
    #Check horizontally
    for i in range(6):
        for j in range(4):
            if [grid[i][j],grid[i][j+1],grid[i][j+2],grid[i][j+3]]==win1:
                a+=1
            if [grid[i][j],grid[i][j+1],grid[i][j+2],grid[i][j+3]]==win2:
                b+=1

    #Check vertically
    for i in range(7):
        for j in range(3):
            if [grid[j][i], grid[j+1][i], grid[j+2][i], grid[j+3][i]]==win1:
                a+=1
            if [grid[j][i], grid[j+1][i], grid[j+2][i], grid[j+3][i]]==win2:
                b+=1

    #Check diagonally
    for j in range(3):
        for i in range(4):
            if [grid[j][i], grid[j+1][i+1], grid[j+2][i+2], grid[j+3][i+3]]==win1:
                a+=1
            if [grid[j][i], grid[j+1][i+1], grid[j+2][i+2], grid[j+3][i+3]]==win2:
                b+=1
    for j in range(3):
        for i in range(6,2,-1):
            if [grid[j][i], grid[j+1][i-1], grid[j+2][i-2], grid[j+3][i-3]]==win1:
                a+=1
            if [grid[j][i], grid[j+1][i-1], grid[j+2][i-2], grid[j+3][i-3]]==win2:
                b+=1
    return a

def winhuman(grid=[]):
    win1=[1,1,1,1]
    win2=[2,2,2,2]
    a=0
    b=0
    #Check horizontally
    for i in range(6):
        for j in range(4):
            if [grid[i][j],grid[i][j+1],grid[i][j+2],grid[i][j+3]]==win1:
                a+=1
            if [grid[i][j],grid[i][j+1],grid[i][j+2],grid[i][j+3]]==win2:
                b+=1

    #Check vertically
    for i in range(0,7):
        for j in range(0,3):
            if [grid[j][i], grid[j+1][i], grid[j+2][i], grid[j+3][i]]==win1:
                a+=1
            if [grid[j][i], grid[j+1][i], grid[j+2][i], grid[j+3][i]]==win2:
                b+=1

    #Check diagonally
    for j in range(3):
        for i in range(4):
            if [grid[j][i], grid[j+1][i+1], grid[j+2][i+2], grid[j+3][i+3]]==win1:
                a+=1
            if [grid[j][i], grid[j+1][i+1], grid[j+2][i+2], grid[j+3][i+3]]==win2:
                b+=1
    for j in range(3):
        for i in range(6,2,-1):
            if [grid[j][i], grid[j+1][i-1], grid[j+2][i-2], grid[j+3][i-3]]==win1:
                a+=1
            if [grid[j][i], grid[j+1][i-1], grid[j+2][i-2], grid[j+3][i-3]]==win2:
                b+=1
    return b

def humanMoves(grid=[]):
    column=[]; rows=[]
    for col in range(7):
        for row in range(6):
            if grid[row][col]==0:
                column.append(col)
                rows.append(row)
                break
    return column, rows

isNum=re.compile("[^0-9]")

def humanmove(grid, x):
    column, rows = humanMoves(grid)
    if isNum.match(x)==None and x!='': x=int(x)-1
    while x not in column:
        print "Invalid Move"
        x=raw_input('n: ')
        if isNum.match(x)==None and x!='': x=int(x)-1
    grid[rows[column.index(x)]][x]=2



p=0
table=[[data[p],data[p+1],data[p+2],data[p+3],data[p+4],data[p+5],data[p+6]],
         [data[p+7],data[p+8],data[p+9],data[p+10],data[p+11],data[p+12],data[p+13]],
         [data[p+14],data[p+15],data[p+16],data[p+17],data[p+18],data[p+19],data[p+20]],
         [data[p+21],data[p+22],data[p+23],data[p+24],data[p+25],data[p+26],data[p+27]],
         [data[p+28],data[p+29],data[p+30],data[p+31],data[p+32],data[p+33],data[p+34]],
         [data[p+35],data[p+36],data[p+37],data[p+38],data[p+39],data[p+40],data[p+41]]]

table.reverse()

#valid moves
order=[3,2,4,1,5,0,6]
def validMoves(grid):
    global order
    moves=[]
    for col in order:
        for row in range(0,6):
            if grid[row][col]==0:
                moves.append([row,col])
                break
    return moves

def move(grid,x,who):
    val=validMoves(grid)
    grid[val[x][0]][val[x][1]]=who

#Alpha Beta Pruning
def alphabeta(grid, depth):
    def ab(grid, depth, high, low):
        items=[];  v=-10000000
        for a,s in validMoves(grid):
            grid[a][s]=1
            v=max(v, abmin(grid, depth-1, high, low))
            items.append(v)
            grid[a][s]=0
        largest=max(items)
        dex=items.index(largest)
        return [dex, largest]

    def abmax(grid, depth, high, low):
        moves=validMoves(grid)
        if(depth==0 or not moves):
            return eval(grid)

        v=-10000000
        for a,s in moves:
            grid[a][s]=1
            v=max(v, abmin(grid, depth-1, high, low))
            grid[a][s]=0
            if v >= low: return v
            high=max(high, v)
        return v

    def abmin(grid, depth, high, low):
        moves=validMoves(grid)
        if(depth==0 or not moves):
            return eval(grid)

        v=+10000000
        for a,s in moves:
            grid[a][s]=2
            v=min(v, abmax(grid, depth-1, high, low))
            grid[a][s]=0
            if v <= high: return v
            low=min(low, v)
        return v
    
    return ab(grid, depth, -10000000, +10000000)

#IDS
def iterative_deepening(grid):
    global order
    depth=1
    res=alphabeta(grid, d)
    return res[0]

#Eval Function
def eval(grid=[]):
    w2=[2,2,2]
    i=0
    j=0
    #Check horizontally
    for i in range(6):
        for j in range(4):
            if [grid[i][j],grid[i][j+1],grid[i][j+2]]==w2:
                return 0

    #Check vertically
    for i in range(7):
        for j in range(4):
            if [grid[j][i], grid[j+1][i], grid[j+2][i]]==w2:
                return 0

    #Check diagonally
    for j in range(3):
        for i in range(4):
            if [grid[j][i], grid[j+1][i+1], grid[j+2][i+2]]==w2:
                return 0
    for j in range(3):
        for i in range(6,2,-1):
            if [grid[j][i], grid[j+1][i-1], grid[j+2][i-2]]==w2:
                return 0
    #print j+3
    return j
        
#MAIN
gamemode=sys.argv[1]
state=sys.argv[3]
dep=sys.argv[4]
d=int(dep)
if gamemode=='one-move' or gamemode=='interactive':
    print ""
else:
    print('%s : unrecognized game mode' % gamemode)
    sys.exit(1)
if state=='computer-next' or state=='human-next':
    print ""
else:
    print('%s : unrecognized game state' % state)
    sys.exit(1)

#Human plays first
if gamemode=='interactive':
    if state=='human-next':
        printhuman(table)    
        while validMoves(table):
            y=checkstatus(table)
            human=winhuman(table)
            print "Score: Computer =",y,", Human =",human
            n=raw_input("Enter column no: ")
            print "Human's move:"
            humanmove(table, n)
            printhuman(table)
            move(table, iterative_deepening(table), 1)
            print "Computer's Move:"
            printcomputer(table)
            
#Computer plays first
    else:
        while validMoves(table):
            move(table, iterative_deepening(table), 1)
            print "Computer's Move:"
            printcomputer(table)
            y=checkstatus(table)
            human=winhuman(table)
            print "Score: Computer =",y,", Human =",human
            n=raw_input("Enter column no: ")
            print "Human's Move:"
            humanmove(table, n)
            printhuman(table)

y=checkstatus(table)
human=winhuman(table)
if y==human: print "Score: Draw"
else: print "Score: Computer =",y,", Human =",human

