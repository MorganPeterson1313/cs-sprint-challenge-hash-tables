import string
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    x = {}
    results = []
    
    
    
    
    # a = map(str, a)  
    # b = list(a)
    # c = b.strip("'")
    # y = c.split(",")
    
   
    for i in a:
        if -i in x:
            results.append(abs(i))
            
        x[i] = 1
    return results
    # for i, p in x.items():
    #     if i[0] > 0 or i[0] < 0 and i[0]

    # result = dict((k, v) for k, v in x.items() if int(v) > 0)
    # result1 = list(result.keys())
    
    # integers = map(int, result1)
        
    # o.append(integers)
    # print(o)
        


   

        
    
       

        
    
    	


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
