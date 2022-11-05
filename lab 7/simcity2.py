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
    # iterates through 3 values in the row
    for rowAdd in range(-1, 2):
        # makes a new row from the row parameter and index
        newRow = row + rowAdd
        # checks if the new row is greater then or equal to zero and if the length of the grid is greater than the row
        # len(grid) - 1 is used because the index starts from zero
        if newRow >= 0 and newRow <= len(grid)-1:
            # iterates through 3 values in the column
            for colAdd in range(-1, 2):
                # makes a new column from the col parameter and index
                newCol = col + colAdd
                # checks if the new column is greater then or equal to zero and if the length of the grid is greater than the row
                if newCol >= 0 and newCol <= len(grid)-1:
                    # continue to the next iteration if the row and column match the parameters
                    if newCol == col and newRow == row:
                        continue
                    # else put the value in the result list
                    result.append(grid[newCol][newRow])
    return result

# main function call
def main():
    grid = create_grid('data_1.txt')
    print("Sim City Land Values:")
    display_grid(grid)
    print(find_neighbor_values(grid, 2, 2))

if __name__ == '__main__':
    main()