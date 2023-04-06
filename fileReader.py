import geopandas as gpd


class dataSetReader:
    #fileRead function takes fileLocation as an argument
    def fileRead(fileLocation):

        try: #geopandas library is used to read .TAB and associated files
            tabFile = gpd.read_file(fileLocation)
            gdf = gpd.GeoDataFrame(tabFile)
            return gdf
        except: #if file is not found, error message is passed
            print("File could not be found")
