# Readme file of the basic ETL using mainly python 
###### Extracting data from a .csv file
  - the code fist ask you the file that you wish to import(for this project you have to chose only file that are present the link below, or in the same layout).

###### Cleaning the data
      - after the file being selected a simple cleaning and renaming of columns will be done on the file(that now is inside a dataframe)
      - the cleaning process include rename the columns to lowercase and some change in the name to not have problems in the sql part of the process
      - also in the cleaning the columns are converted to float type

######  Moving it to a docker with postgresql database.
      - for now the is aimed to work with postgresql connection, in this caso the table where the data is inserted already exist, so the data get appended to the end of it
      - some rule are inforced on database side, mainly to have a good quality of data and consistence on it(constraints to no duplicate the data).
      
## File used in the process is from this link https://www.kaggle.com/datasets/vivovinco/league-of-legends-stats-s13
