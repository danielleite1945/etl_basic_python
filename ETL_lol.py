import pandas as pd 
import re 
import database
import openfile as of

def getnum_from_filename(filename:str):
    """Function to extract the version number from the filename."""
    ini = re.search(r'\s\d*\.',filename)
    en = re.search(r'\.[a-zA-Z]',filename)
    if filename[(ini.start())+1:en.start()]:
        num:str = filename[(ini.start())+1:en.start()]
        return num
    else:
        return None

def data_transformation(dtfr):
    """Function to transform the raw data into a format that is more suitable for the database."""
    dtfr["winrate"] = dtfr["Win %"].str.replace('%','').astype(float)
    dtfr.drop(columns=["Win %"],inplace=True)
    dtfr["pickrate"] = dtfr["Pick %"].str.replace('%','').astype(float)
    dtfr.drop(columns=["Pick %"],inplace=True)
    dtfr["banrate"] = dtfr["Ban %"].str.replace('%','').astype(float)
    dtfr.drop(columns=["Ban %"],inplace=True)
    dtfr["rolerate"] = dtfr["Role %"].str.replace('%','').astype(float)
    dtfr.drop(columns=["Role %"],inplace=True)
    return dtfr

def filename_to_column(dataframe,filename):
    """Function to add the season number to the dataframe."""
    dataframe["version"] = getnum_from_filename(filename)
    dataframe = dataframe.rename(columns=str.lower)
    return dataframe

def load_data_to_db():
    """Function to load the transformed data into the database."""
    filepath = of.open_file() #call the function to open the file dialog and get the filepath as you may guess by the name of the variable  
    RawDataFrame = pd.read_csv(filepath,sep=';') #import the chosen file to a dataframe format using pandas

    transformed_df =  filename_to_column(data_transformation(RawDataFrame),filepath.split('/')[-1]) #cleaning of the data and appending new column on dataframe
    
    transformed_df.to_sql('champ_season_info',database.get_engine('postgres'),if_exists='append',index=False,method='multi')

def main ():
    load_data_to_db()
if __name__ == '__main__':
    main()
