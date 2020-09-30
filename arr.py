fh = open( "ImageData.txt" );

x = []
#For loop starts here
for line in fh.readlines():
    y = [value for value in line.split()]
    x.append( y )

fh.close()
print (x)
