x = 50
def test():
    global x 
    print(f"x : {x}")
    x=100
    print(f"changed of the x : {x}")

test()
print(x)