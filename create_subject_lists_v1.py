#### LOAD NECESSARY PACKAGES ####
import random
import pandas as pd
import numpy as np
import os
from collections import Counter
import copy

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
faces_mainTask_list = pd.read_csv(faces_mainTask_list_infile, header=None).loc[:,0].tolist()   # 20 count
places_mainTask_list = pd.read_csv(places_mainTask_list_infile, header=None).loc[:,0].tolist()    # 20 count
fruits_mainTask_list = pd.read_csv(fruits_mainTask_list_infile, header=None).loc[:,0].tolist()     # 20 count

faces_novel_list = pd.read_csv(faces_novel_list_infile, header=None).loc[:,0].tolist()    # 77 count
places_novel_list = pd.read_csv(places_novel_list_infile, header=None).loc[:,0].tolist()    # 75 count
fruits_novel_list = pd.read_csv(fruits_novel_list_infile, header=None).loc[:,0].tolist()    # 77 count


#### CREATE MAIN TASK LISTS ####
# Define some experiment variables
total_trials = 144    # number of trials
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

# set trial num
mainTask_trial_num = list(range(1, 25)) * 6
mainTask_df["trial_num"] = mainTask_trial_num

# set probe sub-type
maintain_probes = ["cued", "uncued", "novel", "novel"]
replace_probes = ["lure", "replacement", "uncued", "novel"]
suppress_probes = ["lure", "uncued", "uncued", "novel"]
# iterate through dataframe to add probe_subtypes
probe_subtype = []
for i, row in mainTask_df.iterrows():
    # print(i)
    if row["trial_num"] == 1:
        # num_probes * (run_len // (num_probes * num_operations))
        run_maintain_probes = np.random.permutation(maintain_probes * (num_oper_per_run // len(maintain_probes))).tolist()
        run_replace_probes = np.random.permutation(replace_probes * (num_oper_per_run // len(replace_probes))).tolist()
        run_suppress_probes = np.random.permutation(suppress_probes * (num_oper_per_run // len(suppress_probes))).tolist()
    if row["operation"] == "maintain":
        probe_subtype.append(run_maintain_probes.pop())
    elif row["operation"] == "replace":
        probe_subtype.append(run_replace_probes.pop())
    elif row["operation"] == "suppress":
        probe_subtype.append(run_suppress_probes.pop())
# add column to dataframe
mainTask_df["probe_subtype"] = probe_subtype

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


# Add jitter, randomized within run
jitter = []
for i in range(num_runs):
    jitter += np.random.permutation([3, 4, 5] * int(run_len / 3)).tolist()
mainTask_df["jitter"] = jitter

# Add rest trigger
mainTask_df["rest_trigger"] = [int(r.trial_num == run_len) for _, r in mainTask_df.iterrows()]

## Select stims for each trial
def select_stim(probecounter, crs_list, allstims, reverse=False, skip=0, shuffle=False):
    timesprobed_sorted = [l[0] for l in sorted(probecounter.items(), key=lambda item: item[1])]

    t = 0
    if skip > 0:
        sortedstims = sortedstims * skip
    if shuffle:
        sortedstims = np.random.permutation(sortedstims).tolist()
    # Iterate through the sorted stim list (sorted by number of times used as probe)
    for probecount in np.unique(list(probecounter.values())):
        sortedstims = [k for k,v in probecounter.items() if v == probecount]
        for s in sortedstims:
            # find if sim is in current category and if stim has been used in current run
            if s not in crs_list and s in allstims:
                if t == skip:
                    allstims.remove(s)    # remove stim from stims dict
                    crs_list.append(s)    # add stim to current run stims
                    return s
                else:
                    t += 1
    print("No stimuli selected")
    viable_list = [s for s in allstims if s not in crs_list]
    print("viable_list = ", viable_list)
    if len(viable_list) == 0:
        print("all_stims = ", allstims)
    if all([s in crs_list for s in allstims]):
        print("failed crs")
    if all([s not in sortedstims for s in allstims]):
        print("failed allstims")
    # print(allstims)
    # print(crs_list)
    return None

def check_trials(imglist: list, numtrials: int):
    """
    checks a list of dictionaries to ensure that all the necesssary imgs have been selected for each trial in numtrials
    """
    return len([i["left"] for i in imglist if i["left"] is not None]) == numtrials and \
        len([i["right"] for i in imglist if i["right"] is not None]) == numtrials and \
        len([i["replacement"] for i in imglist if i["replacement"] is not None]) == (numtrials // 3) and \
        len([i["probe"] for i in imglist if i["probe"] is not None]) == numtrials


# initiate a list to store the stims
check = False
# Build the lists
while not check:
    # Assign stim to trials
    stims_dict = {}
    # create dictionary for each operation, cue-type and img category 3*2*3*19 = 342
    for oper in ["maintain", "suppress", "replace"]:
        stims_dict[oper] = {}
        for probe in ["cued", "uncued", "replacement"]:
            if oper != "replace" and probe == "replacement":    # only create replacement category for replace trials
                continue
            stims_dict[oper][probe] = {"faces": np.random.permutation(faces_mainTask_list).tolist(),
                                       "places": np.random.permutation(places_mainTask_list).tolist(),
                                       "fruits": np.random.permutation(fruits_mainTask_list).tolist(), }
    # Save novel stims into dict
    novel_stims_dict = {"faces": np.random.permutation(faces_novel_list).tolist(),
                        "places": np.random.permutation(places_novel_list).tolist(),
                        "fruits": np.random.permutation(fruits_novel_list).tolist(), }
    # initiate counter
    timesprobed_counter = Counter(faces_mainTask_list + places_mainTask_list + fruits_mainTask_list)
    # reset the counter to 0
    for entry in timesprobed_counter:
        timesprobed_counter[entry] = 0
    # initiate the image list
    image_list = []
    # Perform the build chunked by run
    for run in range(1, num_runs + 1):
        df = mainTask_df[mainTask_df["run_num"] == run]
        # Loop until run has completed building
        run_check = False
        skip = 0
        shuffle = False
        while not run_check:
            random.seed()
            # initiate a run specific image list
            run_image_list = []
            # Initiate list to keep track of images in current run
            current_run_stims = []
            # Create copies of the master tracking lists
            run_timesprobed_counter = copy.deepcopy(timesprobed_counter)
            run_stims_dict = copy.deepcopy(stims_dict)
            run_novel_stims_dict = copy.deepcopy(novel_stims_dict)
            for i, r in df.iterrows():
                # Determine the image to be probed
                if r.probe_subtype == "cued" or r.probe_subtype == "lure":
                    probe_pos = r.cue_position
                elif r.probe_subtype == "uncued":
                    probe_pos = "left" if r.cue_position == "right" else "right"
                elif r.probe_subtype == "replacement":
                    probe_pos = "replacement"
                else:
                    probe_pos = None
                # Find an image for each position
                images_dict = {}
                for imgnum in ["left", "right", "replacement"]:
                    # determine the image category
                    if imgnum == "left":
                        imgcat = r.encode_1_cat
                    elif imgnum == "right":
                        imgcat = r.encode_2_cat
                    elif imgnum == "replacement":
                        if r.operation != "replace":
                            images_dict["replacement"] = None
                            continue
                        else:
                            imgcat = r.replace_cat
                    # Create sorted lists of stims based on number of times probed
                    if imgnum == probe_pos:
                        timesprobed_sorted = [l[0] for l in sorted(run_timesprobed_counter.items(), key=lambda item: item[1])]
                    else:
                        timesprobed_sorted = [l[0] for l in sorted(run_timesprobed_counter.items(), key=lambda item: item[1])]
                        timesprobed_sorted.reverse()
                    # determine cue status for image
                    cue_status = "replacement" if imgnum == "replacement" else ("uncued", "cued")[r.cue_position == imgnum]
                    # select the image
                    img = select_stim(run_timesprobed_counter, current_run_stims, run_stims_dict[r.operation][cue_status][imgcat], skip=skip, shuffle=shuffle)
                    # For debugging:
                    if img is None:
                        print(run)
                        print(i)
                        print(len(current_run_stims))
                    # Save the image into the dict
                    images_dict[imgnum] = img
                # Select a probe image
                if probe_pos is not None:
                    probe_img = images_dict[probe_pos]
                    # Update the run timesprobed counter
                    run_timesprobed_counter[probe_img] += 1
                else:
                    probe_cat = np.random.choice([r.encode_1_cat, r.encode_2_cat])
                    probe_img = run_novel_stims_dict[probe_cat].pop()
                # Save the probe image
                images_dict["probe"] = probe_img
                # Save the image dict into the run image list
                run_image_list.append(images_dict)

            # Perform a check for the run
            run_check = check_trials(run_image_list, run_len)
            # add skip
            skip += 1
            shuffle = True
            print("runcheck = ", run_check)
            print("skip = ", skip)
            print("shuffle = ", shuffle)
            if skip > 1:
                break
        # If run passes check, overwrite all ongoing saves onto counters/lists
        image_list += run_image_list
        timesprobed_counter = run_timesprobed_counter
        stims_dict = run_stims_dict
        novel_stims_dict = run_novel_stims_dict

    if len(image_list) == total_trials:
        print("completed build, now checking")
        check = check_trials(image_list, total_trials)
    else:
        print(len(image_list))
        print("DNF, restarting...")
        continue
# Add stims to df
mainTask_df["encode_1_img"] = [i["left"] for i in image_list]
mainTask_df["encode_2_img"] = [i["right"] for i in image_list]
mainTask_df["replace_img"] = [i["replacement"] for i in image_list]
mainTask_df["probe_img"] = [i["probe"] for i in image_list]



# benchmark
mainTask_df.to_csv(
    f"{_thisDir}/remlure_mainTask_benchmark_v3.csv", index=False
)

