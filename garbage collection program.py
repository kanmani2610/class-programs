import gc
collected = gc.collect()
print(f"Garbage collector {collected } objects")