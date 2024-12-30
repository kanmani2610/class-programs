import gc
gc.enable()
gc.disable()
l1=[1,2,3]
d1={'a':1,'b':2}
s1="Garbage collection"
del l1
del d1
del s1
gc.set_threshold(100,5,5)
print("threshold",gc.get_threshold())
collected=gc.collect()
print(collected)