import geopandas as gpd
import pandas as pd
import glob
from sqlalchemy import create_engine, text
import geoalchemy2
import psycopg2

class database:


    def insertData(fileLocation, user, password, databaseName):
        engine = create_engine(f"postgresql://{user}:{password}@localHost:5432/{databaseName}")

        with engine.connect() as conn:
            conn.execute(text('CREATE EXTENSION IF NOT EXISTS "postgis";'))
            conn.execute(text('CREATE EXTENSION IF NOT EXISTS "postgis_raster";')) #adds postgresql extensions

        #geopandas library is used to read .TAB and associated files
        try:
            allTabFile = glob.glob("{}/*.tab".format(fileLocation))     #glob library is used to select all files in the directory which end with .tab
            print(f"found {len(allTabFile)} files: {allTabFile}")   #prints a list of all files found
        except:
            print("No files were found in this directory.") #popup

        gdfs = []

        try:
            for filename in allTabFile:     #each file is read in to a geodataframe and then appended to the list
                gdf = gpd.read_file(filename)
                gdfs.append(gdf)
                print(f"Successfully read {filename} into a geoDataFrame.") #popup
        except:
            print(f"Error reading {filename} into a geoDataFrame.") #popup

        try:
            merged_gdf = gpd.GeoDataFrame(pd.concat(gdfs,ignore_index=False),crs="EPSG:27700",geometry='geometry')  #each geodataframe in the list is concatinated, set to a co-ordinate reference system of EPSG:27700
        except:
            print("No files were found in the directory.") #popup

        try:
            tableName = input("What table would you like to export the data to?:\t").lower() #input for table name
            merged_gdf.to_postgis(name=tableName, con = engine, if_exists="replace", index=False)      #The concatinated geodataframe is then added to postGIS, the table sites is created, or if it exists it is replaced by a new table
            print("Items added to the database.") #confirmation message
        except:
            print("Items were not added to the database.") #error message



    def displayData(user, password, databaseName):
        try:
            engine = create_engine(f"postgresql://{user}:{password}@localHost:5432/{databaseName}")
            tableName = input("Which table would you like to see?:\t").lower() #input for table name
            query = f"SELECT * FROM {tableName}"
            gdf = gpd.GeoDataFrame.from_postgis(query, con=engine, geom_col="geometry")     #database is read into a geodataframe, then printed to the console
            print(gdf) #this is where the table would be printed
        except:
            print("Unable to display the database.") #error


    def removeData(user, password, databaseName):
        
            conn = psycopg2.connect(database=databaseName, user=user, password=password)       #psycopg2 library used for connection here

            cur = conn.cursor()     #cursor object is created for accessing the DB

            tableName = input("Which table would you like to remove data from?").lower() #table name input

            siteID = int(input("Enter the siteID you which to remove:\t")) #input site id for deletion

            cur.execute(f"SELECT COUNT(*) FROM {tableName} WHERE \"Site_ID\" = '{siteID}'")        #SQL statement counts how many rows contain the site id input, if 0, the user is informed that the DB does not contain that siteID
            row_count = cur.fetchone()[0]

            if row_count == 0:
                print(f"Site {siteID} does not exist in the DB.") #error message
                
            else:
                choice = input(f"Are you sure you want to delete site ID {siteID} from the database? y/n:\t").lower() #y or n command for confirmation
                if choice == 'y':
                    cur.execute(f"DELETE FROM {tableName} WHERE \"Site_ID\" = '{siteID}'")     #If the siteID exists in the database, the function removes it and gives a confirmation message to the user

                    conn.commit()
                    cur.close()
                
                    print(f"Site {siteID} was successfully removed from {tableName}.") #confirmation message

                elif choice =='n':
                    print(f"SiteID {siteID} was not deleted.") #error message
                    
                else:
                    print("Input must be a y/n.") #error message
