def ImageBase():

    #Image
    imageHeight = 256
    imageWidth = 256

    print("P3\n" + str(imageWidth) + ' ' + str(imageHeight))
    
    #Render

    for j in range(imageHeight-1,-1,-1):
        for i in range(imageWidth):
            r = i/(imageWidth-1)
            g = j / (imageHeight-1)
            b = 0.25

            ir = int(255.999*r)
            ig = int(255.999*g)
            ib = int(255.999*b)

            print(str(ir) + ' ' + str(ig) + ' ' + str(ib))
    return None
ImageBase()