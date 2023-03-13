import geopandas as gpd

class dataSetReader:
    #fileRead function takes fileLocation as an argument
    def fileRead(fileLocation):

        try: #geopandas library is used to read .TAB and associated files
<<<<<<< HEAD
            gdf = geopandas.read_file(fileLocation) #gdf stands for GeoDataFrame
            print(gdf)
=======
            tabFile = gpd.read_file(fileLocation)
            return tabFile
>>>>>>> 2ba7c2e4bb992614292a8f1456f8752b32eabf4b
        except: #if file is not found, error message is passed
            print("File could not be found")
