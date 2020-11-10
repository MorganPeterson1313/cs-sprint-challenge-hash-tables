from itertools import chain
import string

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # numbers = list(chain(arrays))
    # print(numbers) 
    x = {}
    # str1 = ' '.join([str(elem) for elem in numbers])
    # # str2 = str1.strip("[] ,")
    # str2  = str1.translate(str1.maketrans("","",',[]'))
    # y = str2.split()
    # for l in numbers:
    #     str1 += l
    # print(str2)
    # print(y)
    results =[]
    for i in arrays:
        for s in i:
            if s not in x:
    
                x[s] = 0
            x[s] += 1



            if x[s] == len(arrays):
                results.append(s)
    return results

        
        
    

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(100, 200)) + [1, 2, 3])
    arrays.append(list(range(200, 300)) + [1, 2, 3])
    arrays.append(list(range(300, 400)) + [1, 2, 3])

    print(intersection(arrays))
