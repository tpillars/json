#!/usr/bin/env python3

###############################################################################
## given a file_path, function will select jsons starting with given pattern,##
## and  optionally remove columns provided in list form                      ##
###############################################################################

import json
import pandas as pd
import glob

def json2df (path_to_json, jsonprefix, rmcols): 
    json_files = glob.glob(path_to_json + jsonprefix + '.json')    # find non-parent JSON files
    data_frames = []   # list to hold json dataframes

    # for look through all json files that are not parent files
    for json_file in json_files:
        file_name = json_file[::-4]    # extract file name
        with open(path_to_json + file_name, 'r') as f:    # read each json
            data_dict = json.load(f)    # take json data and put into dictionary format
        df = pd.json_normalize(data_dict)    # make into pandas dataframe
        df.insert(loc = 0, column = 'file name', value = file_name)    # create new co˚lumn and name it after file name
        df = df.drop(columns = rmcols)    # remove complex data related to chem-structure
        data_frames.append(df)    # add each json>pd.dataframe to a list for concatenation

    df_merged = pd.concat(data_frames)    # combine all json>pd.dataframes to one merged dataframe

    df_merged.to_csv('json_df.csv', index=False)    # save table to csv

    # get extra info on table columns & save to txt
    f = open("json_df_info.txt", "w")        
    df_merged.info(buf = f)
    f.close()

    print(df_merged)    # look at merged dataframe
    print(df_merged.info())    # list all columns and some column info





json2df(path_to_json = 'file/path/here',
        jsonprefix = '*',  # selects every file ending in .json 
        rmcols = ['column name 1', 'column name 2', 'etc...'],
        )
