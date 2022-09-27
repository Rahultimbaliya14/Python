#Simple Try And Except Block Example
a=10
b=0
try:
    global c
    c=a/b
except:
    print("You Can Not Devide Any Number By 0")
else:
    print(c)

#Try Except With Finally
try:
    f=open("link",'r')
    print("Open File Sccessfully")
except IOError as e:
    print(e)
finally:
    print("This Is Finnaly Bock")
    print("It Block Execute Definetly")

#Try And Except With Argument
def convert(val):
    try:
        return int(val)
    except ValueError as a:
        print("Argument",a,val)
convert("yrl")

#Raise The Exception
try:
    raise IOError("This Is Raised Exception")
except IOError as e:
    print(e)

#User Define Exception
class UserError(RuntimeError):
      def __init__(self, arg):
          self.args = arg

try:
    raise UserError("Raised Error")
except UserError as e:
      r=str(e)
      print(r)