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
            allTabFile = glob.glob("{}/*.tab".format(fileLocation))     #glob library is used to select all files in the directory which end with .tab
            print(f"found {len(allTabFile)} files: {allTabFile}")
        except:
            print("No files were found in this directory.")

        gdfs = []

        try:
            for filename in allTabFile:     #each file is read in to a geodataframe and then appended to the list
                gdf = gpd.read_file(filename)
                gdfs.append(gdf)
                print(f"Successfully read {filename} into a geoDataFrame.")
        except:
            print(f"Error reading {filename} into a geoDataFrame.")

        try:
            merged_gdf = gpd.GeoDataFrame(pd.concat(gdfs,ignore_index=True)).to_crs("EPSG:4326").set_index('Site_ID')       #each geodataframe in the list is concatinated, set to a co-ordinate reference system of EPSG:4326 and indexed via Site_ID
        except:
            print("No files were found in the directory.")

        try:
            merged_gdf.to_postgis(name="sites", con = engine, if_exists="replace", index=True)      #The concatinated geodataframe is then added to postGIS, the table sites is created, or if it exists it is replaced by a new table
            print("Items added to the database.")
        except:
            print("Items were not added to the database.")



    def displayData():
        try:
            engine = create_engine("postgresql://postgres:lincolnBio@localHost:5432/lincolnBiodiversity")

            query = "SELECT * FROM sites"
            gdf = gpd.GeoDataFrame.from_postgis(query, con=engine, geom_col="geometry")     #database is read into a geodataframe, then printed to the console
            print(gdf) 
        except:
            print("Unable to display the database.")


    def removeData(siteID):
        
            conn = psycopg2.connect(database='lincolnBiodiversity',user='postgres',password='lincolnBio')       #psycopg2 library used for connection here

            cur = conn.cursor()     #cursor object is created for accessing the DB

            cur.execute(f"SELECT COUNT(*) FROM public.sites WHERE \"Site_ID\" = '{siteID}'")        #SQL statement counts how many rows contain the site id input, if 0, the user is informed that the DB does not contain that siteID
            row_count = cur.fetchone()[0]

            if row_count == 0:
                print(f"Site {siteID} does not exist in the DB.")
                
            else:
                choice = input(f"Are you sure you want to delete site ID {siteID} from the database? y/n:\t").lower()
                if choice == 'y':
                    cur.execute(f"DELETE FROM public.sites WHERE \"Site_ID\" = '{siteID}'")     #If the siteID exists in the database, the function removes it and gives a confirmation message to the user

                    conn.commit()
                    cur.close()
                
                    print(f"Site {siteID} was successfully removed from the database.")

                elif choice =='n':
                    print(f"SiteID {siteID} was not deleted.")
                    
                else:
                    print("Input must be a y/n.")
