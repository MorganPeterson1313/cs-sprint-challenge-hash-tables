from itertools import chain 
def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    numbers = list(chain(arrays))
    # print(numbers) 
    x = {}
    
    for i in numbers:
        
        if i not in x:
    
            x[i] = 0
        x[i] += 1
        
        if i[1] == len(arrays):
            return i[0]
    

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
