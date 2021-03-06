# Dynamic Programming 
# The box stacking problem

# A class box was created.
# This is the blueprint for creating a box object
class Box: 
      
    # Representation of a box 
    """ 
      When instantiated, a box object contains a height, width and depth.
    """
    def __init__(self, h, w, d): 
        self.h = h 
        self.w = w 
        self.d = d 
  
    def __lt__(self, other): 
        return self.d * self.w < other.d * other.w 


    """
    Each box can be rotated into 3 seperate configurations.  For instance, 
    consider a box with the following dimenions (2,1,3).  This box can be rearranged into
    3 seperate configurations --> (2,1,3), (3,1,2), (1,2,3).
    """ 


def maxStackHeight(arr, n): 
  
    # Create an array of all rotations of  
    # given boxes. For example, for a box {1, 2, 3},  
    # we consider three instances{{1, 2, 3}, 
    # {2, 1, 3}, {3, 1, 2}} 
    rot = [Box(0, 0, 0) for _ in range(3 * n)] 
    index = 0
  
    for i in range(n): 
  
        # Copy the original box 
        rot[index].h = arr[i].h 
        rot[index].d = max(arr[i].d, arr[i].w) 
        rot[index].w = min(arr[i].d, arr[i].w) 
        index += 1
  
        # First rotation of the box 
        rot[index].h = arr[i].w 
        rot[index].d = max(arr[i].h, arr[i].d) 
        rot[index].w = min(arr[i].h, arr[i].d) 
        index += 1
  
        # Second rotation of the box 
        rot[index].h = arr[i].d 
        rot[index].d = max(arr[i].h, arr[i].w) 
        rot[index].w = min(arr[i].h, arr[i].w) 
        index += 1
    
    """
    The total number of boxes is now reassigned to n = 3 * original n.
    The array you pass to the maxstackheight function has a length of n. 
    """
    n *= 3
  
    """
    Values are sorted in descending order based on base area.
    """
    rot.sort(reverse = True) 
   
    # Uncomment following two lines to print  
    # all rotations  
    # for i in range(n): 
    #     print(rot[i].h, 'x', rot[i].w, 'x', rot[i].d) 
  
    # Initialize msh values for all indexes 
    # msh[i] --> Maximum possible Stack Height  
    # with box i on top 
    """
    MSH stands for maximum stack height.   
    The following line of code created a list of length n. 
    Each value in the list is initialized at 0.

    [0,0,0,0......n]
    """
    msh = [0] * n 
    

    """
    This block of code iterates over every value in msh
    and assigns the height of each box as the max stack height for each
    respective box. 
    """
    for i in range(n): 
        msh[i] = rot[i].h 
  
    # Compute optimized msh values 
    # in bottom up manner 

    """
    This block of code is comprised of 2 for loops. 
    The first for loop iterates over the length of n.
    """
    for i in range(1, n): 
        """
        The nested for loop iterates over every value from 0 to i from the previous
        for loop. 
        """
        for j in range(0, i): 
            """
            if the boxes width is less than the the previous boxes width
            and the boxes depth is less than the previous boxes depth move to the next if
            statement.
            """
            if (rot[i].w < rot[j].w and 
                rot[i].d < rot[j].d): 
                """
                If the max stack height for box i (msh[i]) is less than the  msh of the previous box (msh[j]) +
                msh[i] we change msh[i] to the msh[j] + msh[i]
                """
                if msh[i] < msh[j] + rot[i].h: 
                    msh[i] = msh[j] + rot[i].h 
  
    maxm = -1
    """
    Iterates over every msh value and finds the maximum value
    """
    for i in range(n): 
        maxm = max(maxm, msh[i]) 
  
    # Returns the maximum stack height
    return maxm 


 # Driver Code 
if __name__ == "__main__": 
    arr = [Box(4, 6, 7), Box(1, 2, 3), 
           Box(4, 5, 6), Box(10, 12, 32)] 
    n = len(arr) 
    print("The maximum possible height of stack is", 
           maxStackHeight(arr, n)) 
  


"""
Dynamic Programming is an optimization technique used in programming.  The main problem is divided into sub-problems.  The
thought is that by solving sub-problems you will eventually reach an optimal solution for the full problem. Results
from sub-problems are cached so they do not have to be recomputed.  The process of storing the results of already
solved sub-problems is called Memoization. 


Walkthrough

Consider an array 
[height,width,depth]
[[1,2,3],[4,5,6]] of size n = 2

Step 1)  Create an Empty array of size n = n * 3

[[0,0,0],[0,0,0].......3 * n]

Step 2) Each box has 3 potential orientations.  Create each orientation

[0,0,0] = [1,2,3]
[0,0,0] = [2,1,3]
[0,0,0] = [3,1,2]

rot = [[1,2,3],[2,1,3],[3,1,2]........]

Step 3) Each box in rot should be organized by descending order box base area.

Step 4) A list named msh (max stack height) is initiated 

msh = [0,0,0,0 ..... 3*n]

Step 5) Every value in msh is equal to a corresponding rot.h value. 
        for example msh[1] = rot[1].h

Step 6) Iterate through every box in the array rot.  If the boxes base dimensions are smaller
than the previous boxes base dimensions and the boxes height is less than the previous boxes height + boxes height 
we stack the box.  i.e msh[i] = msh[j] + msh[i].  NOTE this is memoization where we cache the previous iterations result
so that it doesn't have to be recalculated.  This step is what makes this a dynamic programming problem. 

Step 7) Iterate over msh to find the maximum stack height. 




"""