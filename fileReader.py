import geopandas

class dataSetReader:

    def fileRead(fileLocation):

        try:
            test = geopandas.read_file(fileLocation)
            print(test)
        except:
            print("File could not be found")
