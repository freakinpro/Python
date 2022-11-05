def create_grid(filename: str) -> list[list[int]]:
    file = open(filename, 'r')

    a =[]
    # first two lines of the file for the row and column respectively
    loop1 = file.readline()
    loop2 = file.readline()

    data = []
    # iterate first loop to make rows in the list
    for row in range(int(loop1.strip())):
        data.append([])
        # 2nd loop to insert data in each row one by one
        # Used the int() method to convert string from the file to int
        for col in range(int(loop2.strip())):
            num = file.readline()
            data[row].append(int(num.strip()))

    return data

def display_grid(grid: list[list[int]]) -> None:
    # iterate through 2 loops to display rows and then and a break "\n" after the inner loop is done excecuting
    # to make a matrix 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # as mentioned in the lab v1 used this to add spaces
            print(f"{grid[i][j]:10}", end=" ")
        print("\n")

# main function
def main():
    grid = create_grid('data_2.txt')
    print("Sim City Land Values:")
    display_grid(grid)

if __name__ == '__main__':
    main()