# Function to calculate the median of a 3x3 grid centered at (i, j)
def med(i, j, l, r, c):
   
    l1 = [l[i][j]]
    for k in range(3):
        # Check the top row of the 3x3 grid
        if i - 1 >= 0 and (j - 1 + k) >= 0 and (j - 1 + k) < c:
            l1.append(l[i - 1][j - 1 + k])  # Add the value if within bounds
        else:
            l1.append(0)  # Add 0 if out of bounds
        # Check the bottom row of the 3x3 grid
        if i + 1 < r and (j - 1 + k) >= 0 and (j - 1 + k) < c:
            l1.append(l[i + 1][j - 1 + k])  # Add the value if within bounds
        else:
            l1.append(0)  # Add 0 if out of bounds
    
    # Check the right neighbor of the center
    if j + 1 < c:
        l1.append(l[i][j + 1])  
    else:
        l1.append(0)  # Add 0 if out of bounds
    # Check the left neighbor of the center
    if j - 1 >= 0:
        l1.append(l[i][j - 1])  #
    else:
        l1.append(0)  # Add 0 if out of bounds
    l1.sort()
    return l1[4]

# Input 
r, c = map(int, input().split())
l = [list(map(int, input().split())) for i in range(r)]
for i in range(r):
    for j in range(c):
        # Calculate the median for the 3x3 grid centered at (i, j)
        me = med(i, j, l, r, c)
        if j == c - 1:
            print(me)
        else:
            print(me, end=' ')
