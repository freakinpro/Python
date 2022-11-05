def create_grid(filename: str) -> list[list[int]]:
    file = open(filename, 'r')

    a =[]
    loop1 = file.readline()
    loop2 = file.readline()

    data = []

    for row in range(int(loop1.strip())):
        data.append([])
    
        for col in range(int(loop2.strip())):
            num = file.readline()
            data[row].append(int(num.strip()))

    return data

def display_grid(grid: list[list[int]]) -> None:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(f"{grid[i][j]:10}", end=" ")
        print("\n")

def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    """
    Find the neighbors of a cell
    """
    result = []
    for rowAdd in range(-1, 2):
        newRow = row + rowAdd
        if newRow >= 0 and newRow <= len(grid)-1:
            for colAdd in range(-1, 2):
                newCol = col + colAdd
                if newCol >= 0 and newCol <= len(grid)-1:
                    if newCol == col and newRow == row:
                        continue
                    result.append(grid[newCol][newRow])
    return result

# def practice(grid, row, col):
#     newArr = []
    
#     if grid[row][col+1] == 1:
#         newArr.append(grid[row][col+1])
#     if grid[row][col-1] == 1:
#         newArr.append(grid[row][col-1])
#     if grid[row+1][col] == 1:
#         newArr.append(grid[row+1][col])
#     if grid[row+1][col+1] == 1:
#         newArr.append(grid[row+1][col+1])
#     if grid[row+1][col-1] == 1:
#         newArr.append(grid[row+1][col-1])    
#     if grid[row-1][col] == 1:
#         newArr.append(grid[row-1][col])
#     if grid[row-1][col+1] == 1:
#         newArr.append(grid[row-1][col+1])
#     if grid[row-1][col-1] == 1:
#         newArr.append(grid[row-1][col-1])

#     return newArr


def fill_gaps(grid: list[list[int]]) -> list[list[int]]:
    """
    Fill the gaps in the grid
    Creates a new grid with the same dimensions as the original grid
    Calls find_neighbor_values() to find the neighbors of each cell
    Do NOT modify the original grid!
    """
    # do not modify the original grid so thats why used another variable to store the list in
    new_grid = grid

    """ Iterate through two loops and check if the value of the 
        element in the list is equal to zero
    """
    for i in range(len(new_grid)):
        for j in range(len(new_grid[i])):
            if new_grid[i][j] == 0:
                neighbors = find_neighbor_values(new_grid, j, i)
                # sum is a function in which we put a list so it returns sum of the list
                # avg is calculated from sum divided by the length of the list
                avg = sum(neighbors)/len(neighbors)
                # assign the avg value to the zero element of the list
                new_grid[i][j] = avg
    # returns the modified 
    return new_grid


# main function
def main():
    grid = create_grid('data_1.txt')
    print("Sim City Land Values:")
    display_grid(grid)
    print(find_neighbor_values(grid, 0, 0))
    print("\nCalculated Sim City land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)

# main function call
if __name__ == '__main__':
    main()