#Single Line Comment
#Single Line Comment Start With Hash(#) Sign
#This Is SIngle Line Comment
from pydoc import doc


A=10
B=20
C=A+B
#This Statement Is Print 30
print(C)

"""Multilline Comment"""
"""Multiline Comment Is Unclose Comment Statement In Triple Quates(""" """)"""
"""This
    Is 
Multiline Comment"""
C=A-B
"""This Statement Print -10"""
print(C)

#Docstring Comment
#It Return The Comments String From The Document

def Printc():
    """This Is Docstring Comments"""

print(Printc.__doc__)