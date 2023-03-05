import geopandas

fileLocation = (input("Enter the name of the file you wish to read (Example: C:/TSE datasets/CoL_LGS_21-22.tab)"))

try:
    test = geopandas.read_file(fileLocation)
    print(test)
except:
    print("File could not be found")
