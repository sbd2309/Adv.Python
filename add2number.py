from ipywidgets import interact
import ipywidgets as widgets

def sum(a,b):
    return a+b


interact(sum,a=widgets.IntSlider(min=0,max=100,value=int(input("Enter"))),b=widgets.IntSlider(min=0,max=100,value=int(input("Enter"))))