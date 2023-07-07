from random import randint
# №1
# size = int(input("Enter list size :: "))
# list = [randint(0,20) for i in range(20)]

# print(f"Before :: {' '.join(map(str,list))}")

# max_index = list.index(max(list))
# min_index = list.index(min(list))

# start_index = min(min_index,max_index) + 1
# end_index = max(min_index,max_index)

# for i in range(start_index,end_index):
#     list[i] *= 2

# print(f"After  :: {' '.join(map(str,list))}")

# №2
# size = int(input("Enter list size :: "))
# list = [randint(0,20) for i in range(20)]

# print(f"Before :: {' '.join(map(str,list))}")
# for i in range(0,len(list)-1,2):
#     list[i],list[i+1] = list[i+1],list[i] 
# print(f"After  :: {' '.join(map(str,list))}")

# №3
# size = int(input("Enter list size :: "))
# list = [randint(0,20) for i in range(20)]
# print(f"List :: {' '.join(map(str,list))}")
# repeat = []
# count = {} 
# for i in list:
#     if list.count(i) > 1 and not i in repeat:
#         repeat.append(i)
# print(f"Result :: {' '.join(map(str,repeat))}")

# №4
# width,height = map(int,input("Enter matrix size  in format 1x1 (wxh):: ").split('x'))
# matrix = [[randint(0,20) for _ in range(width)] for i in range(height)]
# pading = len(str(sum(_ for rows in matrix for _ in rows)))
# row = ""
# for _ in matrix:
#     for num in _:
#          row += f"{num:<{pading}d}"
#     row += f" |{sum(_):<{pading}d}"
#     print(row)
#     row = ""
# column = ''
# for i in range(width):
#    column += f"{sum(rows[i] for rows in matrix):<{pading}d}"
# column += f" |{sum(_ for rows in matrix for _ in rows):<{pading}d}"
# print("-"*len(column))
# print(column)

# №5

# №7
# officer_position = input("Enter the position of the Officer :: ")
# column = ord(officer_position[0]) - ord('a')
# row = int(officer_position[1]) - 1
def відмітити_клітинки_під_загрозою_тури(позиція):
    стовпець = ord(позиція[0]) - ord('a')
    рядок = int(позиція[1]) - 1

    дошка = [['.' for _ in range(8)] for _ in range(8)]

    # Відмітити клітинки в одному рядку
    for i in range(8):
        дошка[рядок][i] = '*'

    # Відмітити клітинки в одному стовпці
    for i in range(8):
        дошка[i][стовпець] = '*'

    # Позицію тури позначити як 'T'
    дошка[рядок][стовпець] = 'T'

    # Вивести шахову дошку
    print("  a b c d e f g h")
    for i in range(8):
        рядок_вивід = ' '.join(дошка[i])
        print(f"{i + 1} {рядок_вивід}")

позиція_тури = 'f6'
відмітити_клітинки_під_загрозою_тури(позиція_тури)
horse_position = input("Enter the position of the horse :: ")
column = ord(horse_position[0]) - ord('a')
row = int(horse_position[1]) - 1

board = [['.' for _ in range(8)] for _ in range(8)]
board[row][column] = 'H'
horse_walk = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
for walk in horse_walk:
    new_row = row + walk[0]
    new_column = column + walk[1]
    if 0 <= new_row < 8 and 0 <= new_column < 8:
        board[new_row][new_column] = '*'

print("  a b c d e f g h")
for i, row in enumerate(board):
    print(f"{i+1} {' '.join(row)}")


