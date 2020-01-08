from ipywidgets import interact, interactive, fixed


def to_f(x):
    return (x * 1.8) + 32



#a=interact(to_f,x=float(input("Enter In Celcius: ")))
print ('The Ferenhite equivalent is {} :'.format(interact(to_f,x=float(input("Enter In Celcius: ")))))