from string import Template

def Main():
    cart = []
    cart.append(dict(name="Ali", age=23, grade="C"))
    cart.append(dict(name="Reza", age=16, grade="A"))
    cart.append(dict(name="Sasan", age=43, grade="C"))
    cart.append(dict(name="Nima", age=31, grade="B"))
    cart.append(dict(name="Morteza", age=20, grade="D"))

    t = Template("$name with age $age and grade $grade")

    print("Persons : ")
    for data in cart:
        print(t.substitute(data))

if __name__ == "__main__":
    Main()