#### LOAD NECESSARY PACKAGES ####
import random
import pandas as pd
import numpy as np
import os
from collections import Counter
import copy
from itertools import permutations

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
# list_foldername = os.path.join(_thisDir, "subject lists", f"sub-{participant_number}")
list_foldername = "stimuli/csvs/maintask_stimlists"

phase_subFolder = "main_task"

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

## Create conditions structure
# Define the experiment conditions
cue_pos = ["left", "right"]
operations = ["maintain", "suppress", "replace"]
categories = ["faces", "places", "fruits"]
probe_types = range(4)

# Create the conditions list
conditions = [[(cat1, cat2, oper, probe)
               for cat1, cat2 in permutations(categories, 2)
               ]
              for oper in operations
              for probe in probe_types]
conditions = np.array(conditions)     # shape=(12, 6, 4)

# concatenate within operation to create 3 arrays of 24 (shape=[3, 24, 4])
combined_conds = np.array([np.vstack(conditions[:4]),
                           np.vstack(conditions[4:8]),
                           np.vstack(conditions[8:12])
                           ])

def create_list():
    # Create indices for the three conditions
    cond_inds = np.full((len(operations), run_len), np.nan)
    for i in range(run_len):
        cond_inds[:, i] = np.roll(np.arange(3), (i % 3) + i // 3)
    # Randomly roll to create unique structure
    cond_inds = np.roll(cond_inds, np.random.randint(24), axis=1)
    # Use boolean indexing to separate out the three runs
    run_1_conds = combined_conds[cond_inds == 0]
    run_2_conds = combined_conds[cond_inds == 1]
    run_3_conds = combined_conds[cond_inds == 2]

    # Run assertion checks to make sure that list creation ran properly
    for run, conds in enumerate([run_1_conds, run_2_conds, run_3_conds]):
        # Check the categories
        c = Counter([(r[0], r[1]) for r in conds])
        # print(c)
        assert all([cat in c.keys() for cat in permutations(categories, 2)]), \
            "list creation failed to include all category pairs"
        assert all([v == run_len // len(list(permutations(categories, 2))) for v in c.values()]), \
            f"list creation failed to properly balance category pairs within run {run + 1}"
        # Check the operations
        c = Counter(conds[:, 2])
        # print(c)
        assert all([op in c.keys() for op in operations]), \
            "list creation failed to include all operations"
        assert all([v == run_len // len(operations) for v in c.values()]), \
            f"list creation failed to properly balance operations within run {run + 1}"

    # Initialize the column order
    column_order = ["encode_1_cat", "encode_2_cat", "operation", "probe_type"]
    # Randomly permute the three runs for the first half and save into a dataframe
    conditions_df = pd.DataFrame(np.random.permutation([run_1_conds,
                                                      run_2_conds,
                                                      run_3_conds]).reshape((total_trials // 2, -1)),
                               columns=column_order)

    # Add list of cue_position
    cuepos_arr = np.concatenate((np.zeros(len(conditions_df) // 2, dtype=int),
                                 np.ones(len(conditions_df) // 2, dtype=int)))
    # Randomize cue positions
    conditions_df["cue_position"] = np.random.permutation(cuepos_arr)
    # Create the conditions for the second half
    secondhalf_conditions = conditions_df.copy()
    # Flip the cue positions for the second half
    secondhalf_conditions["cue_position"] = 1 - secondhalf_conditions["cue_position"]
    # Randomize the run structure again in second half and append to ongoing dataframe
    for i in np.random.permutation(np.arange(3)):
        conditions_df = pd.concat((conditions_df, secondhalf_conditions.iloc[24*i : 24*(i+1)]),
                                  ignore_index=True)

    # Add run_num
    conditions_df["run_num"] = [n + 1 for n in range(num_runs) for i in range(run_len)]


    ## Pseudorandomize trials within runs and append to mainTask dataframe
    # initialize mainTask df
    mainTask_df = pd.DataFrame()

    # this code is to make sure there are no more than 3 of the same operation repeated in a row
    for i in range(1, num_runs+1):
        # subselect the run dataframe
        run_df = conditions_df[conditions_df["run_num"] == i]
        wm_valid_sequence = False
        while not wm_valid_sequence:
            # resample the trials within this run
            run_df = run_df.sample(frac=1).reset_index(drop=True)
            # check the operation structures
            wm_valid_sequence = not any((run_df['operation'] == run_df['operation'].shift(1)) &
                                        (run_df['operation'] == run_df['operation'].shift(2)) &
                                        (run_df['operation'] == run_df['operation'].shift(3)))
        # Concat the now shuffled run into the main task dataframe
        mainTask_df = pd.concat((mainTask_df, run_df), ignore_index=True)


    ## recode the conditions into variable names used in PsychoPy
    # recode cue_position
    mainTask_df["cue_position"] = ["right" if cp else "left" for cp in mainTask_df.cue_position]

    # Convert the probe_type to int type
    mainTask_df["probe_type"] = mainTask_df["probe_type"].astype(int)
    # set probe sub-type
    maintain_probes = ["cued", "uncued", "novel", "novel"]
    replace_probes = ["lure", "replacement", "uncued", "novel"]
    suppress_probes = ["lure", "uncued", "uncued", "novel"]
    probe_subtype = []
    for i, r in mainTask_df.iterrows():
        if r.operation == "maintain":
            probe_subtype.append(maintain_probes[r.probe_type])
        elif r.operation == "suppress":
            probe_subtype.append(suppress_probes[r.probe_type])
        elif r.operation == "replace":
            probe_subtype.append(replace_probes[r.probe_type])
    mainTask_df["probe_subtype"] = probe_subtype

    # set replacement category
    def find_replace_cat(row):
        if row["operation"] == "replace":
            present = {row["encode_1_cat"], row["encode_2_cat"]}
            missing = set(categories) - present
            return missing.pop() if missing else "NA"
        else:
            return "NA"
    mainTask_df["replace_cat"] = mainTask_df.apply(find_replace_cat, axis=1)

    # set trial num
    mainTask_trial_num = list(range(1, 25)) * 6
    mainTask_df["trial_num"] = mainTask_trial_num

    # Add jitter, randomized within run
    jitter = []
    for i in range(num_runs):
        jitter += np.random.permutation([3, 4, 5] * int(run_len / 3)).tolist()
    mainTask_df["jitter"] = jitter

    # Add rest trigger
    mainTask_df["rest_trigger"] = [int(r.trial_num == run_len) if i != (total_trials - 1) else 0 for i, r in mainTask_df.iterrows()]

    ## Select stims for each trial
    def select_stim(probecounter, crs_list, stimsdict, useprobe=True,
                    oper=None, cuestatus=None, imgcat=None, reverse=False,):
        # Iterate through the sorted stim list (sorted by number of times used as probe)
        # initiate a counter for the entire stimsdict
        counter = Counter()
        for o in stimsdict:
            for p in stimsdict[o]:
                for c in stimsdict[o][p]:
                    counter.update(stimsdict[o][p][c])
        # subselect viable list (stim in current condition dict) then sort from most common to least commonly used
        viable_list = [sv for sv in counter.most_common() if sv[0] in stimsdict[oper][cuestatus][imgcat]]
        # iterate from least common to most common
        for value in np.unique([v for _, v in viable_list]):
            # Subselect stims matching the used-value
            stims = [s[0] for s in viable_list if s[1] == value]
            if useprobe:
                # Sort stims based on number of times probed
                sortedstims = [k for k in sorted(probecounter.items(), key=lambda x:x[1]) if k[0] in stims]
                if reverse:
                    sortedstims.reverse()
            else:
                sortedstims = np.random.permutation(stims)
            # iterate and pull stim
            if useprobe:
                for val in np.unique([k[1] for k in sortedstims]):
                    substims = np.random.permutation([k[0] for k in sortedstims if k[1] == val])
                    for s in substims:
                        if s not in crs_list:
                            stimsdict[oper][cuestatus][imgcat].remove(s)    # remove stim from stims dict
                            crs_list.append(s)  # add stim to current run stims
                            return s
            else:
                for s in sortedstims:
                    # find if sim is in current category and if stim has been used in current run
                    if s not in crs_list:
                        stimsdict[oper][cuestatus][imgcat].remove(s)    # remove stim from stims dict
                        crs_list.append(s)    # add stim to current run stims
                        return s
        # print("No stimuli selected")
        return None

    def check_trials(imglist: list, numtrials: int):
        """
        checks a list of dictionaries to ensure that all the necesssary imgs have been selected for each trial in numtrials
        """
        return len([i["left"] for i in imglist if i["left"] is not None]) == numtrials and \
            len([i["right"] for i in imglist if i["right"] is not None]) == numtrials and \
            len([i["replacement"] for i in imglist if i["replacement"] is not None]) == numtrials and \
            len([i["probe"] for i in imglist if i["probe"] is not None]) == numtrials


    # initiate a list to store the stims
    check = False
    retries = 0
    # Set the operation cue images
    opcue_dict = {"maintain": "stimuli/cues/maintain_cue_image.png",
                  "suppress": "stimuli/cues/suppress_cue_image.png",}
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
            t = 0
            # Try to use probe as much as possible
            # print("now using probe counter")
            useprobe = True
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
                                images_dict["replacement"] = opcue_dict[r.operation]
                                continue
                            else:
                                imgcat = r.replace_cat
                        # determine cue status for image
                        cue_status = "replacement" if imgnum == "replacement" else ("uncued", "cued")[r.cue_position == imgnum]
                        # select the image
                        # Create sorted lists of stims based on number of times probed
                        if imgnum == probe_pos:
                            img = select_stim(run_timesprobed_counter, current_run_stims, run_stims_dict, useprobe=useprobe,
                                              oper=r.operation, cuestatus=cue_status, imgcat=imgcat, reverse=False)
                        else:
                            img = select_stim(run_timesprobed_counter, current_run_stims, run_stims_dict, useprobe=useprobe,
                                              oper=r.operation, cuestatus=cue_status, imgcat=imgcat, reverse=True)
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
                # print("run = ", run)
                # print("runcheck = ", run_check)
                t += 1
                if t > 5:
                    # print("now turning useprobe to False")
                    useprobe = False
                if t > 10:
                    break
            # If run passes check, overwrite all ongoing saves onto counters/lists
            image_list += run_image_list
            timesprobed_counter = run_timesprobed_counter
            stims_dict = run_stims_dict
            novel_stims_dict = run_novel_stims_dict
        if len(image_list) == total_trials:
            print("completed build, now checking...")
            check = check_trials(image_list, total_trials)
        else:
            print(len(image_list))
            print("DNF, restarting...")
            continue
        retries += 1
        if retries > 20:
            print("failed list creation. exceeded retries")
            return None
    # Add stims to df
    mainTask_df["encode_1_img"] = [i["left"] for i in image_list]
    mainTask_df["encode_2_img"] = [i["right"] for i in image_list]
    mainTask_df["replace_img"] = [i["replacement"] for i in image_list]
    mainTask_df["probe_img"] = [i["probe"] for i in image_list]
    return mainTask_df

for i in range(10):
    mainTask_df_infile = f"{list_foldername}/main_stim_list_{i}.csv"
    mainTask_df = create_list()
    while mainTask_df is None:
        mainTask_df = create_list()
    # Save to maintask folder
    mainTask_df.to_csv(
        mainTask_df_infile , index=False
    )
