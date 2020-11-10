# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """      
    # Your code here
    o = []
    for i in files:
        for x in queries:
            if i.endswith(x):
                o.append(i)
    
    return o



if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
