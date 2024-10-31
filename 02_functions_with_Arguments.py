# Types of functions
# 1.Built-in function(Already present in python)
# 2.User-defined function(defined by the users)


def goodDay(name, ending):
    print("Hello boss," + name+ " " + ending)
    # print(ending)

goodDay("Aman", "Thankyou")
goodDay("Kriti", "Thankyou")


# ............................
def goodDay(name, ending):
    print("Hello boss," + name+ " " + ending)
    return "ok"

a = goodDay("gaurav", "Thankyou")
print(a)

def goodDay(name, ending="Thankyou"):
    print(f"Good day, {name}")
    print(ending)

goodDay("Aman")
goodDay("Rohan", "Thanks")