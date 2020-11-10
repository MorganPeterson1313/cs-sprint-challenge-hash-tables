# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """      
    # Your code here
    x = {}
    results = []
    # for i in files:
    #     for x in queries:
    #         if i.endswith(x):
    #             o.append(i)
    
    # return o

    for file in files:
        split_string = file.split("/")
        if split_string[-1] not in x:
           x[split_string[-1]]= [file]
        else:
            x[split_string[-1]].append(file)

    for query in queries:
        if query in x:
            results.extend(x[query])
    return results





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
