import schemdraw
import schemdraw.elements as elm
from schemdraw import logic
from ipywidgets import widgets, HBox, interact, Layout
from IPython.display import display, clear_output

@interact(a=[0,1], b=[0,1])
def logical_nand_gate(a, b):
    display(HBox(layout=Layout(padding='35px')))
    
    display(logic.Nor().label(f'A={a}', loc='in1').label(f'B={b}', loc='in2').label(f'A&B = {1-a*b}', loc='right'))
    logic.Nor().label(f'A={b}', loc='in1').label(f'B={b}', loc='in2').label(f'A&B = {1-a*b}', loc='right')
