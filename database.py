import psycopg2
from sqlalchemy import create_engine
import geoalchemy2
from fileReader import dataSetReader


class database:
    def createDB():
        #connects to the database
        conn = psycopg2.connect("dbname=lincolnBiodiversity user=postgres password=lincolnBio")

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
        
        gdf = dataSetReader.fileRead(fileLocation)
        conn = psycopg2.connect("dbname=lincolnBiodiversity user=postgres password=lincolnBio")
        gdf.to_postGIS()

        cur = conn.cursor()

        cur.execute()