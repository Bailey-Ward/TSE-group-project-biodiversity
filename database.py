import geopandas as gpd
import pandas as pd
import glob
from sqlalchemy import create_engine
import geoalchemy2
import psycopg2

class database:

    def insertData(fileLocation):
        

        engine = create_engine("postgresql://postgres:lincolnBio@localHost:5432/lincolnBiodiversity")

        #geopandas library is used to read .TAB and associated files
        try:
            allTabFile = glob.glob("{}/*.tab".format(fileLocation))
            print(f"found {len(allTabFile)} files: {allTabFile}")
        except:
            print("No files were found in this directory")

        gdfs = []

        try:
            for filename in allTabFile:
                gdf = gpd.read_file(filename)
                gdfs.append(gdf)
                print(f"Successfully read {filename} into a geoDataFrame")
        except:
            print(f"Error reading {filename} into a geoDataFrame")

        try:
            merged_gdf = gpd.GeoDataFrame(pd.concat(gdfs,ignore_index=True)).to_crs("EPSG:4326").set_index('Site_ID')
        except:
            print("No files were found in the directory")

        try:
            merged_gdf.to_postgis(name="sites", con = engine, if_exists="replace", index=True) #adds items to the DB (not working as intended yet)
            print("Items added to the database")
        except:
            print("Items were not added to the database")



    def displayData():
        try:
            engine = create_engine("postgresql://postgres:lincolnBio@localHost:5432/lincolnBiodiversity")

            query = "SELECT * FROM sites"
            gdf = gpd.GeoDataFrame.from_postgis(query, con=engine, geom_col="geometry")
            print(gdf) #logic for printing the DB
        except:
            print("Database could not be connected to")


    def removeData(siteID):

        engine = create_engine("postgresql://postgres:lincolnBio@localHost:5432/lincolnBiodiversity")

        query = f"DELETE FROM sites WHERE sites.Site_ID = {siteID}" 

        with engine.connect() as conn:
            conn.execute(query)

        gdf = gpd.GeoDataFrame.from_postgis(query, con=engine, geom_col="geometry")

        gdf #removing records from the DB (also not working as intended yet)



