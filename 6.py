# Mario pyramid in a terminal
def height():
    try:
        global h
        h = int(input("Please enter height of the pyramid: "))
        if not 0 < h <= 23: # height value range is between 0 and 23
            print("Height out of range!")
            return height()
    except ValueError:
        print("Must be integer value!")
        return height()
    
    b = 2 # amount of hashes to print at the first ln
    def pyramid(h, b):
        a = h-1
        while h>0:
            print(f' '*a, '#'*b)
            h -= 1
            a -= 1
            b += 1
            return pyramid(h, b)
    pyramid(h, b)

height()