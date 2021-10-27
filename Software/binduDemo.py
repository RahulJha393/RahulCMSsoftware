import matplotlib

print("This is just a demo file")

for x in range(5) :
  print(x%2)
  
import tkinter as tk
import os, psutil
process = psutil.Process(os.getpid())
def mem(): print(f'{process.memory_info().rss:,}')

# initial memory usage
mem()

# 21,475,328
for i in range(20):
    root.append(tk.Tk())
    root[-1].destroy()
    mem()
# 24,952,832
# 26,251,264
# ...
# 47,591,424
# 48,865,280

# try deleting the root instead

del root
mem()

lass Foo():
    def __init__(self):
        # create a list that takes up approximately the same size as a Tk() on average
        self.lst = list(range(11500))    

for i in range(20):
    root.append(Foo())
    del root[-1]
    mem() # this is for memory management 

# 50,819,072
