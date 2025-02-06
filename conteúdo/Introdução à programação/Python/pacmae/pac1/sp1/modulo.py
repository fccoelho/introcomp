import sys
x=10

if __name__=="__main__":
    print(sys.path)
    from pacmae.pac2.sp1 import modulo
    print(x + modulo.x)