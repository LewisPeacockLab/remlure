import pandas as pd
import numpy as np
from itertools import permutations
import os

participant_number = "test"  # Edward, if you put this code in PsychoPy this would need to be changed to refelect the expInfo
# expInfo['participant']

# set directory path
try:
    _thisDir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    print("__file__ does not exist")
    _thisDir = os.getcwd()

# create a subject specific folder to save all lists
list_foldername = os.path.join(_thisDir, "subject lists", f"sub-{participant_number}")

phase_subFolder = "localizer"

# Create the subject folder if it doesn't exist
if not os.path.exists(list_foldername):
    os.makedirs(list_foldername)
    print(f"List folder successfully created for sub-{participant_number}")
else:
    print(f"List folder already exists for sub-{participant_number}...")

# Create each phase subfolder within the subject's folder
phase_folder_path = os.path.join(list_foldername, phase_subFolder)
# Create the phase folder
if not os.path.exists(phase_folder_path):
    os.makedirs(phase_folder_path)
    print(f"Created phase folder: {phase_subFolder}")
else:
    print(f"Phase folder '{phase_subFolder}' already exists...")

# Import stimuli csvs
faces_df = pd.read_csv("stimuli/csvs/main_task/faces_mainTask.csv", header=None)
places_df = pd.read_csv("stimuli/csvs/main_task/places_mainTask.csv", header=None)
fruits_df = pd.read_csv("stimuli/csvs/main_task/fruits_mainTask.csv", header=None)
# Define some experiment variables
categories = ["faces", "places", "fruits"]
stim_dict = {"faces": faces_df[0].tolist(),
             "places": places_df[0].tolist(),
             "fruits": fruits_df[0].tolist()}
num_runs = 3
run_len = 60
total_runs = num_runs * run_len
perms = np.random.permutation(list(permutations(categories, 3)))

# Initiate dataframe to store stims
locstim_df = pd.DataFrame()
for n in range(num_runs):
    run_list = []
    for cat in perms[n]:
        run_list += np.random.permutation(stim_dict[cat]).tolist()
    run_df = pd.DataFrame(run_list, columns=["img"])
    run_df["run"] = n + 1
    locstim_df = pd.concat([locstim_df, run_df], ignore_index=True)

# add trial num
locstim_df["trial_num"] = [i for i in range(1, locstim_df.shape[0] + 1)]
# add rest trigger
locstim_df["rest_trigger"] = [int(not (i % run_len)) if i < total_runs else 0 for i in range(1, stims_df.shape[0] + 1)]

# Add jitter, randomized within run
jitter = []
for i in range(num_runs):
    jitter += np.random.permutation([3, 4, 5] * (run_len // 3)).tolist()
locstim_df["jitter"] = jitter

locstim_df_infile = f"{phase_folder_path}/loc_stim_list.csv"
# Save to maintask folder
locstim_df.to_csv(
    locstim_df_infile , index=False
)
locstim_list = locstim_df_infile


