import psycopg2
import geopandas as gpd
from fileReader import dataSetReader


class database:
    def createDB():
        #connects to the database
        conn = psycopg2.connect(dbname="lincolnBiodiversity", user="postgres", password="lincolnBio")

        #creates a cursor object to work on the database
        cur = conn.cursor()

        cur.execute("CREATE DATABASE lincolnBiodiversity;")

        #creates the table
        cur.execute("CREATE EXTENSION postgis;")
        cur.execute("CREATE EXTENSION postgis_topology;")
        cur.execute("DROP TABLE IF EXISTS sites;")
        cur.execute("CREATE TABLE sites;")

        #commits the changes
        conn.commit()

        #closes database connection
        cur.close()
        conn.close()

    def insertData(fileLocation):

        conn = psycopg2.connect(dbname="lincolnBiodiversity", user="postgres", password="lincolnBio")
        cur = conn.cursor()


        gdf = dataSetReader.fileRead(fileLocation)

        gdf.to_postgis(name="sites", con=conn, if_exists="append", index=False)

        cur.close()
        conn.close()

    def removeData(siteID):
        conn = psycopg2.connect(dbname="lincolnBiodiversity", user="postgres", password="lincolnBio")
        cur = conn.cursor()
        
        sql = "SELECT * FROM mytable"
        gdf = gpd.read_postgis(sql, con=conn, geom_col="geom", crs="EPSG:4326")
        print(gdf)

        cur.execute("DELETE FROM sites WHERE siteID = '{}' ".format(siteID))

        cur.close()
        conn.close()
