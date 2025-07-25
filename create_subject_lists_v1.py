#### LOAD NECESSARY PACKAGES ####
import random
import pandas as pd
import numpy as np
import os

# Set participant number
# need this to create a folder with each subs design matrix
participant_number = "test"  # Edward, if you put this code in PsychoPy this would need to be changed to refelect the expInfo

# set directory path
_thisDir = os.path.dirname(os.path.abspath(__file__))

# create a subject specific folder to save all lists
list_foldername = os.path.join(_thisDir, "subject lists", f"sub-{participant_number}")

phase_subFolder = ["localizer", "main_task"]

# Create the subject folder if it doesn't exist
if not os.path.exists(list_foldername):
    os.makedirs(list_foldername)
    print(f"List folder successfully created for sub-{participant_number}")
else:
    print(f"List folder already exists for sub-{participant_number}...")

# Create each phase subfolder within the subject's folder
for subfolder in phase_subFolder:
    phase_folder_path = os.path.join(list_foldername, subfolder)
    # Create the phase folder
    if not os.path.exists(phase_folder_path):
        os.makedirs(phase_folder_path)
        print(f"Created phase folder: {subfolder}")
    else:
        print(f"Phase folder '{subfolder}' already exists...")

#### SETUP STIMULUS MASTER LISTS ####
# set a random seed
random.seed()

# read in the master stimulus lists
faces_mainTask_list_infile = (
    _thisDir
    + os.sep
    + "stimuli"
    + os.sep
    + "csvs"
    + os.sep
    + "main_task"
    + os.sep
    + "faces_mainTask.csv"
)

places_mainTask_list_infile = (
    _thisDir
    + os.sep
    + "stimuli"
    + os.sep
    + "csvs"
    + os.sep
    + "main_task"
    + os.sep
    + "places_mainTask.csv"
)

fruits_mainTask_list_infile = (
    _thisDir
    + os.sep
    + "stimuli"
    + os.sep
    + "csvs"
    + os.sep
    + "main_task"
    + os.sep
    + "fruits_mainTask.csv"
)

faces_novel_list_infile = (
    _thisDir
    + os.sep
    + "stimuli"
    + os.sep
    + "csvs"
    + os.sep
    + "main_task"
    + os.sep
    + "faces_novel.csv"
)

places_novel_list_infile = (
    _thisDir
    + os.sep
    + "stimuli"
    + os.sep
    + "csvs"
    + os.sep
    + "main_task"
    + os.sep
    + "places_novel.csv"
)

fruits_novel_list_infile = (
    _thisDir
    + os.sep
    + "stimuli"
    + os.sep
    + "csvs"
    + os.sep
    + "main_task"
    + os.sep
    + "fruits_novel.csv"
)

# open stimulus mater files
faces_mainTask_inbook = pd.read_csv(faces_mainTask_list_infile)
places_mainTask_inbook = pd.read_csv(places_mainTask_list_infile)
fruits_mainTask_inbook = pd.read_csv(fruits_mainTask_list_infile)

faces_novel_inbook = pd.read_csv(faces_novel_list_infile)
places_novel_inbook = pd.read_csv(places_novel_list_infile)
fruits_novel_inbook = pd.read_csv(fruits_novel_list_infile)

# load the lists
faces_mainTask_list = []
for _, row in faces_mainTask_inbook.iterrows():
    faces_mainTask_list.append(row.tolist())

places_mainTask_list = []
for _, row in places_mainTask_inbook.iterrows():
    places_mainTask_list.append(row.tolist())

fruits_mainTask_list = []
for _, row in fruits_mainTask_inbook.iterrows():
    fruits_mainTask_list.append(row.tolist())

faces_novel_list = []
for _, row in faces_novel_inbook.iterrows():
    faces_novel_list.append(row.tolist())

places_novel_list = []
for _, row in places_novel_inbook.iterrows():
    places_novel_list.append(row.tolist())

fruits_novel_list = []
for _, row in fruits_novel_inbook.iterrows():
    fruits_novel_list.append(row.tolist())

#### CREATE MAIN TASK LISTS ####
# create the encoding category labels for item 1 (left of screen) and item 2 (right of screen)
encode_1_cat = (
    ["faces"] * 4
    + ["places"] * 4
    + ["faces"] * 4
    + ["fruits"] * 4
    + ["places"] * 4
    + ["fruits"] * 4
) * 6
encode_2_cat = (
    ["places"] * 4
    + ["faces"] * 4
    + ["fruits"] * 4
    + ["faces"] * 4
    + ["fruits"] * 4
    + ["places"] * 4
) * 6

# intiate df
mainTask_df = pd.DataFrame({"encode_1_cat": encode_1_cat, "encode_2_cat": encode_2_cat})

# create lst of operations
operation_list_run1 = (["maintain"] * 2 + ["suppress"] * 2 + ["replace"] * 2) * 4
operation_list_run2 = (["suppress"] * 2 + ["replace"] * 2 + ["maintain"] * 2) * 4
operation_list_run3 = (["replace"] * 2 + ["maintain"] * 2 + ["suppress"] * 2) * 4
operation_list_run4 = (["maintain"] * 2 + ["suppress"] * 2 + ["replace"] * 2) * 4
operation_list_run5 = (["suppress"] * 2 + ["replace"] * 2 + ["maintain"] * 2) * 4
operation_list_run6 = (["replace"] * 2 + ["maintain"] * 2 + ["suppress"] * 2) * 4

operation_list_allRuns = (
    operation_list_run1
    + operation_list_run2
    + operation_list_run3
    + operation_list_run4
    + operation_list_run5
    + operation_list_run6
)

mainTask_df["operation"] = operation_list_allRuns

# set replacement category
stim_cats = {"faces", "places", "fruits"}


def find_replace_cat(row):
    if row["operation"] == "replace":
        present = {row["encode_1_cat"], row["encode_2_cat"]}
        missing = stim_cats - present
        return missing.pop() if missing else "NA"
    else:
        return "NA"


mainTask_df["replace_cat"] = mainTask_df.apply(find_replace_cat, axis=1)

# set probe types


# set run number
mainTask_run_num = (
    [1 for i in range(24)]
    + [2 for i in range(24)]
    + [3 for i in range(24)]
    + [4 for i in range(24)]
    + [5 for i in range(24)]
    + [6 for i in range(24)]
)
mainTask_df["run_num"] = mainTask_run_num

# set trial num
mainTask_trial_num = list(range(1, 25)) * 6
mainTask_df["trial_num"] = mainTask_trial_num

# benchmark
mainTask_df.to_csv("/Users/cnj678/Desktop/remlure_mainTask_benchmark.csv", index=False)
