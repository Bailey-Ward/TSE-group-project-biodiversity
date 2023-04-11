import psycopg2
import pandas as pd
import glob as glob
import geopandas as gpd
from sqlalchemy import create_engine
import geoalchemy2
import fiona 

fiona.supported_drivers

class database:

    def insertData(fileLocation):

        engine = create_engine("postgresql://postgres:lincolnBio@localHost:5432/lincolnBiodiversity")

        #geopandas library is used to read .TAB and associated files
        tabFile = gpd.read_file("{}.tab".format(fileLocation))
        print(tabFile)

        gdf = gpd.GeoDataFrame(tabFile)

        gdf.to_file("{}.shp".format(fileLocation), index=False, driver= "ESRI Shapefile")
    
        shpFile = gpd.read_file("{}.shp".format(fileLocation))
        
        gdf = gpd.GeoDataFrame(shpFile)

        gdf.to_postgis(name="sites", con = engine, if_exists="append", index=False) #adds items to the DB (not working as intended yet)


    def displayData():
        engine = create_engine("postgresql://postgres:lincolnBio@localHost:5432/lincolnBiodiversity")

        query = "SELECT * FROM sites"
        gdf = gpd.GeoDataFrame.from_postgis(query, con=engine, geom_col="geometry")
        print(gdf) #logic for printing the DB


    def removeData(siteID):

        engine = create_engine("postgresql://postgres:lincolnBio@localHost:5432/lincolnBiodiversity")

        query = f"DELETE FROM sites WHERE sites.Site_ID = {siteID}" 

        with engine.connect() as conn:
            conn.execute(query)

        gdf = gpd.GeoDataFrame.from_postgis(query, con=engine, geom_col="geometry")

        gdf #removing records from the DB (also not working as intended yet)



