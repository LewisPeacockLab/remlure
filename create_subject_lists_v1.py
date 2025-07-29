#### LOAD NECESSARY PACKAGES ####
import random
import pandas as pd
import numpy as np
import os

# Set participant number
# need this to create a folder with each subs design matrix
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
faces_mainTask_inbook = pd.read_csv(faces_mainTask_list_infile)    # 19 count
places_mainTask_inbook = pd.read_csv(places_mainTask_list_infile)    # 19 count
fruits_mainTask_inbook = pd.read_csv(fruits_mainTask_list_infile)     # 19 count

faces_novel_inbook = pd.read_csv(faces_novel_list_infile)    # 76 count
places_novel_inbook = pd.read_csv(places_novel_list_infile)    # 74 count
fruits_novel_inbook = pd.read_csv(fruits_novel_list_infile)    # 76 count

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
# Define some experiment variables
run_len = 24    # trials per run
num_runs = 6    # number of runs
num_oper_per_run = run_len // 3    # 3 operations

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

# set cue location
mainTask_cue_loc = (["left" for i in range(1)] + ["right" for i in range(1)]) * 72
mainTask_df["cue_position"] = mainTask_cue_loc

# set probe types
mainTask_probeType = (
    # run 1
    ["match" for i in range(12)]
    + ["non-match" for i in range(12)]
    # run 2
    + ["match" for i in range(6)]
    + ["non-match" for i in range(12)]
    + ["match" for i in range(6)]
    # run 3
    + ["non-match" for i in range(12)]
    + ["match" for i in range(12)]
) * 2
mainTask_df["probe_type"] = mainTask_probeType

# set probe sub-type
maintain_probes = ["cued", "uncued", "novel", "novel"]
replace_probes = ["lure", "replacement", "uncued", "novel"]
suppress_probes = ["lure", "uncued", "uncued", "novel"]
# iterate through dataframe to add probe_subtypes
probe_subType = []
for i, row in mainTask_df.iterrows():
    # print(i)
    if row["trial_num"] == 1:
        # num_probes * (run_len // (num_probes * num_operations))
        run_maintain_probes = np.random.permutation(maintain_probes * (num_oper_per_run // len(maintain_probes))).tolist()
        run_replace_probes = np.random.permutation(replace_probes * (num_oper_per_run // len(replace_probes))).tolist()
        run_suppress_probes = np.random.permutation(suppress_probes * (num_oper_per_run // len(suppress_probes))).tolist()
    if row["operation"] == "maintain":
        probe_subType.append(run_maintain_probes.pop())
    elif row["operation"] == "replace":
        probe_subType.append(run_replace_probes.pop())
    elif row["operation"] == "suppress":
        probe_subType.append(run_suppress_probes.pop())
# add column to dataframe
mainTask_df["probe_subType"] = probe_subType


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

# Add jitter, randomized within run
jitter = []
for i in range(num_runs):
    jitter += np.random.permutation([3, 4, 5] * int(run_len / 3)).tolist()
mainTask_df["jitter"] = jitter

# Add rest trigger
mainTask_df["rest_trigger"] = [int(r.trial_num == run_len) for _, r in mainTask_df.iterrows()]

# Assign stim to trials
stims_dict = {}
# create dictionary for each operation
for oper in ["maintain", "suppress", "replace"]:
    stims_dict[oper] = {"face": np.random.permutation(faces_mainTask_list).tolist(),
                        "places": np.random.permutation(places_mainTask_list).tolist(),
                        "fruits": np.random.permutation(fruits_mainTask_list).tolist(),}
#

# benchmark
mainTask_df.to_csv(
    f"{_thisDir}/remlure_mainTask_benchmark_v2.csv", index=False
)

