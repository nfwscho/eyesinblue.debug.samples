import pdb

def add(a, b):
    return a + b

def samplefunc():
    import pdb; pdb.set_trace() # -- added breakpoint
    var = 10
    print("One. Line 1 ..")
    print("Two. Line 2 ..!")
    out = add("summy", var)
    print('Three. Line 3 .. Done!')
    return out

samplefunc()
