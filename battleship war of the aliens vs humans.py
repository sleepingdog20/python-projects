print("welcome to battleship load up and ship out move it move it now maggots!!!!")

w = '~'

grid = [
[' ',0,1,2,3,4,5,6,7,8,9],
['A',w,w,w,w,w,w,w,w,w,w],
['b',w,w,w,w,w,w,w,w,w,w],
['C',w,w,w,w,w,w,w,w,w,w],
['D',w,w,w,w,w,w,w,w,w,w],
['E',w,w,w,w,w,w,w,w,w,w],
['F',w,w,w,w,w,w,w,w,w,w],
['G',w,w,w,w,w,w,w,w,w,w],
['H',w,w,w,w,w,w,w,w,w,w],
['I',w,w,w,w,w,w,w,w,w,w],
['J',w,w,w,w,w,w,w,w,w,w]
]



grid[5][5] = '*'




for row in grid:
    for col in row:
        print(col,end=' ')
    print()






