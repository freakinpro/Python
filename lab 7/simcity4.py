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

def fill_gaps(grid: list[list[int]]) -> list[list[int]]:
    """
    Fill the gaps in the grid
    Creates a new grid with the same dimensions as the original grid
    Calls find_neighbor_values() to find the neighbors of each cell
    Do NOT modify the original grid!
    """
    new_grid = grid

    for i in range(len(new_grid)):
        for j in range(len(new_grid[i])):
            if new_grid[i][j] == 0:
                neighbors = find_neighbor_values(new_grid, j, i)
                avg = sum(neighbors)/len(neighbors)
                new_grid[i][j] = round(avg)
    
    return new_grid

def find_max(grid: list[list[int]]) -> int:
    max = 0
    # iterate through 2 loops
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # checks if the element is greater then the max value then assigns the value to the max variable
            # iterates again to check if the element is greater than the previously stored max value then if true so it assigns the value of the element to the max variable
            if max < grid[i][j]:
                max = grid[i][j]
    # returns the max value
    return max


def find_average(grid: list[list[int]]) -> int:
    """
    Find the average value in the grid (rounded to the nearest integer)
    """
    Sum = 0
    count = 0
    # iterate through 2 loops
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # calculates the sum by adding each element in the sum variable
            Sum += grid[i][j]
            # calculates how much elements are their in total to calculate the average
            count += 1 
    # returns the average rounded to the nearest integer
    return round(Sum/count)


def main() -> None:
    """
    Main program.
    """
    grid = create_grid("data_0.txt")
    print("Sim City Land Values:")
    display_grid(grid)
    print("\nCalculated Sim City land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)
    print("\nSTATS")
    print(f"Average land value in this city: {find_average(new_grid)}")
    print(f"Maximum land value in this city: {find_max(new_grid)}")



if __name__ == '__main__':
    main()