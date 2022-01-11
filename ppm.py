import sys

def ImageBase():

    #Image
    imageHeight = 256
    imageWidth = 256

    print("P3\n" + str(imageWidth) + ' ' + str(imageHeight) +"\n255")
    
    #Render

    for j in range(imageHeight-1,-1,-1):
        #print("\rScanlines Remaining: " + str(j)+ " ",file=sys.stderr)
        sys.stderr.write("\rScanlines Remaining: " + str(j)+ " ")
        sys.stderr.flush()
        for i in range(imageWidth):
            r = i/(imageWidth-1)
            g = j / (imageHeight-1)
            b = 0.25

            ir = int(255.999*r)
            ig = int(255.999*g)
            ib = int(255.999*b)

            print(str(ir) + ' ' + str(ig) + ' ' + str(ib))
    print("\nDone",file=sys.stderr)
    return None
ImageBase()