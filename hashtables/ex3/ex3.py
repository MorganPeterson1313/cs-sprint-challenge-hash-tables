from itertools import chain
import string

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    numbers = list(chain(arrays))
    # print(numbers) 
    x = {}
    str1 = ' '.join([str(elem) for elem in numbers])
    str2 = str1.strip("[] ,")
    # str1.translate(str1.maketrans("","",'":;,.-+=/\\|[]{}()*^&'))
    y = str2.split()
    # for l in numbers:
    #     str1 += l
    # print(str1)
    for i in y:
        
        if i not in x:
    
            x[i] = 0
        x[i] += 1
        # print(x)

        if i[len(1)] == len(arrays):
            return i[0]
        
        
    

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
