fh = open( "ImageData.txt" );

x = []
for line in fh.readlines():
    y = [value for value in line.split()]
    x.append( y )

fh.close()
print (x)