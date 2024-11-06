# Author: Shanto Mathew. Written on 09\07\2018

!pip install pygame
import pygame

def draw_board(board, final=False):
    N = len(board)

    # Define some colors
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    GREY = (211,211,211)

    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    screen = pygame.display.set_mode([50 * N + 5 * (N+1), 50 * N + 5 * (N+1)])

    # Set title of screen
    pygame.display.set_caption("N Queens Problem")


    # Draw the grid
    for row in range(N):
        for column in range(N):
            color = WHITE
            if board[row][column] == 'Q':
                color = GREEN
            if not final and board[row][column] == 1:
                color = GREY
            pygame.draw.rect(screen,
                             color,
                             [(5 + 50) * column + 5,
                              (5 + 50) * row + 5,
                              50,
                              50])
    pygame.display.flip()

    # Loop until the user clicks the close button.

    while pygame.QUIT not in [x.type for x in pygame.event.get()]:
        pass
    if final:
        pygame.quit()

def find_four_routes(i, j, M, N):
    coord_set = set()
    coord_set.update({(k, j)for k in range(M) if k!=i})  # All cells in the same row
    coord_set.update({(i, l)for l in range(N) if l!=j}) # All cells in the same column

    zip_obj = zip(range(i-j, M), range(N-(i-j))) if i>j else zip(range(M-(j-i)), range(j-i, N))  # All cells in the diagonal
    zip_obj2 = zip(range(i-min(i, N-j-1), i+min(M-i-1, j)+1), reversed(range(j-min(j, M-i-1), j+min(N-j-1, i)+1))) # All cells in the other diagonal

    coord_set.update({(k, l)for (k, l) in zip_obj if not(i==k and j==l)})
    coord_set.update({(k, l)for (k, l) in zip_obj2 if not(i==k and j==l)})
    return coord_set

def n_queen(N):
    board = [[0]*N for x in range(N)]
    coord_list = list()

    def attacked(coord_set):
        coord_to_remove = set()
        for i, j in coord_set:
            if not board[i][j]:
                board[i][j] = 1
            else:
                coord_to_remove.add((i, j))
        for param in coord_to_remove:
            coord_set.remove(param)
    def deattacked(coord_set):
        for i, j in coord_set:
            board[i][j] = 0

    def find_cells(index):
        global iterr
        if index==N:
            return True
        for pos in range(N):
            if not board[index][pos]:
                board[index][pos] = 'Q'
                coord_list.append((index, pos))
                coord_set = find_four_routes(index, pos, N, N)
                attacked(coord_set)
                if find_cells(index+1):
                    return True
                else:
                    # print(f'Removing Q on row {index}, index {pos}')
                    board[index][pos] = 0
                    deattacked(coord_set)
                    coord_list.remove((index, pos))

    if find_cells(0):
        draw_board(board, final=True)
        return coord_list
    else:
        print('Couldnt get all the rows working')


n_queen(10)
print('FINISHED')
