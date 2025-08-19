#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.2),
    on Wed Aug  6 19:25:07 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from init_code
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
        break
if retries > 20:
    # Use a premade stim list
    premade_infile = f"stimuli/csvs/maintask_stimlists/main_stim_list_{random.randint(0,9)}.csv"
    print(f"using pre-made stim list {os.path.split(premade_infile)[1]}")
    mainTask_df = pd.read_csv(premade_infile)
else:
    # Add stims to df
    mainTask_df["encode_1_img"] = [i["left"] for i in image_list]
    mainTask_df["encode_2_img"] = [i["right"] for i in image_list]
    mainTask_df["replace_img"] = [i["replacement"] for i in image_list]
    mainTask_df["probe_img"] = [i["probe"] for i in image_list]

mainTask_df_infile = f"{list_foldername}/main_task/main_stim_list.csv"
# Save to maintask folder
mainTask_df.to_csv(
    mainTask_df_infile , index=False
)
stim_list = mainTask_df_infile

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.2'
expName = 'remlure_maintask'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'phase': 'maintask',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1512, 982]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/edwardleung/Desktop/remlure/remlure_maintask_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('welcome_keyResp') is None:
        # initialise welcome_keyResp
        welcome_keyResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='welcome_keyResp',
        )
    if deviceManager.getDevice('encode_instruct_keyResp') is None:
        # initialise encode_instruct_keyResp
        encode_instruct_keyResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='encode_instruct_keyResp',
        )
    if deviceManager.getDevice('operscreen_instruct_keyResp') is None:
        # initialise operscreen_instruct_keyResp
        operscreen_instruct_keyResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='operscreen_instruct_keyResp',
        )
    if deviceManager.getDevice('operations_instruct_keyResp') is None:
        # initialise operations_instruct_keyResp
        operations_instruct_keyResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='operations_instruct_keyResp',
        )
    if deviceManager.getDevice('probescreen_instruct_keyResp') is None:
        # initialise probescreen_instruct_keyResp
        probescreen_instruct_keyResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='probescreen_instruct_keyResp',
        )
    if deviceManager.getDevice('probe_instructions_keyResp') is None:
        # initialise probe_instructions_keyResp
        probe_instructions_keyResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='probe_instructions_keyResp',
        )
    if deviceManager.getDevice('prac_begin_keyResp') is None:
        # initialise prac_begin_keyResp
        prac_begin_keyResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='prac_begin_keyResp',
        )
    if deviceManager.getDevice('probe_keyResp') is None:
        # initialise probe_keyResp
        probe_keyResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='probe_keyResp',
        )
    if deviceManager.getDevice('pracend_keyResp') is None:
        # initialise pracend_keyResp
        pracend_keyResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='pracend_keyResp',
        )
    if deviceManager.getDevice('main_exp_begin') is None:
        # initialise main_exp_begin
        main_exp_begin = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='main_exp_begin',
        )
    if deviceManager.getDevice('rest_continue') is None:
        # initialise rest_continue
        rest_continue = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='rest_continue',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Welcome" ---
    welcome_text = visual.TextStim(win=win, name='welcome_text',
        text='Welcome to an experiment by the ... Lab!\n\nThis experiment is meant to be run in full-screen mode. DO NOT escape out of the full-screen. Otherwise you will have to restart the entire experiment from the beginning.\n\n\nPress <SPACE> to continue',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    welcome_keyResp = keyboard.Keyboard(deviceName='welcome_keyResp')
    
    # --- Initialize components for Routine "Encode_instruct" ---
    encode_instruct_img = visual.ImageStim(
        win=win,
        name='encode_instruct_img', 
        image='instructions/encode_instructions.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.075), draggable=False, size=(1.53, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    encode_instruct_cont_text = visual.TextStim(win=win, name='encode_instruct_cont_text',
        text='Press <SPACE> to continue.',
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    encode_instruct_keyResp = keyboard.Keyboard(deviceName='encode_instruct_keyResp')
    
    # --- Initialize components for Routine "Oper_screen_instruct" ---
    operscreen_instruct_img = visual.ImageStim(
        win=win,
        name='operscreen_instruct_img', 
        image='instructions/oper_screen_instructions.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.075), draggable=False, size=(1.53, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    operscreen_instruct_cont_text = visual.TextStim(win=win, name='operscreen_instruct_cont_text',
        text='Press <SPACE> to continue.',
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    operscreen_instruct_keyResp = keyboard.Keyboard(deviceName='operscreen_instruct_keyResp')
    
    # --- Initialize components for Routine "Operations_instruct" ---
    operations_instruct_img = visual.ImageStim(
        win=win,
        name='operations_instruct_img', 
        image='instructions/operation_instructions.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.53, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    operations_instruct_conttext = visual.TextStim(win=win, name='operations_instruct_conttext',
        text='Press <SPACE> to continue.',
        font='Arial',
        pos=(0, -0.43), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    operations_instruct_keyResp = keyboard.Keyboard(deviceName='operations_instruct_keyResp')
    
    # --- Initialize components for Routine "Probe_screen_instruct" ---
    probescreen_instruct_img = visual.ImageStim(
        win=win,
        name='probescreen_instruct_img', 
        image='instructions/probe_screen_instructions.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.47, 0.95),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    probescreen_instruct_conttext = visual.TextStim(win=win, name='probescreen_instruct_conttext',
        text='Press <SPACE> to continue.',
        font='Arial',
        pos=(0, -0.45), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    probescreen_instruct_keyResp = keyboard.Keyboard(deviceName='probescreen_instruct_keyResp')
    
    # --- Initialize components for Routine "Probe_instruct" ---
    probe_instructions_img = visual.ImageStim(
        win=win,
        name='probe_instructions_img', 
        image='instructions/probe_instructions.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(1.47, 0.9),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    probe_instructions_conttext = visual.TextStim(win=win, name='probe_instructions_conttext',
        text='Press <SPACE> to continue.',
        font='Arial',
        pos=(0, -0.45), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    probe_instructions_keyResp = keyboard.Keyboard(deviceName='probe_instructions_keyResp')
    
    # --- Initialize components for Routine "Practice_begin" ---
    prac_begin_text = visual.TextStim(win=win, name='prac_begin_text',
        text="Let's do a couple of practice trials!\n\n\n\nPress <RETURN> to continue.",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    prac_begin_keyResp = keyboard.Keyboard(deviceName='prac_begin_keyResp')
    # Run 'Begin Experiment' code from corrinit_code
    corr = 0
    
    # --- Initialize components for Routine "Trial_prepare" ---
    Trial_prepare_text = visual.TextStim(win=win, name='Trial_prepare_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Encode" ---
    encode_fixation = visual.ShapeStim(
        win=win, name='encode_fixation',
        size=(0.03, 0.03), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='dimgray', fillColor='dimgray',
        opacity=None, depth=0.0, interpolate=True)
    img_1_left = visual.ImageStim(
        win=win,
        name='img_1_left', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.3, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    img_2_right = visual.ImageStim(
        win=win,
        name='img_2_right', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.3, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "Delay_2000" ---
    delay_fixation_2000 = visual.ShapeStim(
        win=win, name='delay_fixation_2000',
        size=(0.03, 0.03), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='dimgray', fillColor='dimgray',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "Manipulate" ---
    manipulate_cue = visual.ImageStim(
        win=win,
        name='manipulate_cue', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    manipulate_fixation = visual.ShapeStim(
        win=win, name='manipulate_fixation',
        size=(0.03, 0.03), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='dimgray', fillColor='dimgray',
        opacity=None, depth=-2.0, interpolate=True)
    
    # --- Initialize components for Routine "Delay_4000" ---
    delay_fixation_4000 = visual.ShapeStim(
        win=win, name='delay_fixation_4000',
        size=(0.03, 0.03), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='dimgray', fillColor='dimgray',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "Probe" ---
    probe_image = visual.ImageStim(
        win=win,
        name='probe_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    probe_keyResp = keyboard.Keyboard(deviceName='probe_keyResp')
    yesKey_text = visual.TextStim(win=win, name='yesKey_text',
        text='[F]\nYES',
        font='Arial',
        pos=(-0.2, -0.35), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    noKey_text = visual.TextStim(win=win, name='noKey_text',
        text='[J]\nNO',
        font='Arial',
        pos=(0.2, -0.35), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "ITI" ---
    ITI_text = visual.TextStim(win=win, name='ITI_text',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Practice_end" ---
    practice_continue_text = visual.TextStim(win=win, name='practice_continue_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    pracend_keyResp = keyboard.Keyboard(deviceName='pracend_keyResp')
    
    # --- Initialize components for Routine "Main_exp_begin" ---
    mainexp_begin_text = visual.TextStim(win=win, name='mainexp_begin_text',
        text='The main experiment is about to begin.\n\n\n\nPress <ENTER> to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    main_exp_begin = keyboard.Keyboard(deviceName='main_exp_begin')
    
    # --- Initialize components for Routine "Trial_prepare" ---
    Trial_prepare_text = visual.TextStim(win=win, name='Trial_prepare_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Encode" ---
    encode_fixation = visual.ShapeStim(
        win=win, name='encode_fixation',
        size=(0.03, 0.03), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='dimgray', fillColor='dimgray',
        opacity=None, depth=0.0, interpolate=True)
    img_1_left = visual.ImageStim(
        win=win,
        name='img_1_left', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.3, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    img_2_right = visual.ImageStim(
        win=win,
        name='img_2_right', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.3, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "Delay_2000" ---
    delay_fixation_2000 = visual.ShapeStim(
        win=win, name='delay_fixation_2000',
        size=(0.03, 0.03), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='dimgray', fillColor='dimgray',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "Manipulate" ---
    manipulate_cue = visual.ImageStim(
        win=win,
        name='manipulate_cue', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    manipulate_fixation = visual.ShapeStim(
        win=win, name='manipulate_fixation',
        size=(0.03, 0.03), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='dimgray', fillColor='dimgray',
        opacity=None, depth=-2.0, interpolate=True)
    
    # --- Initialize components for Routine "Delay_4000" ---
    delay_fixation_4000 = visual.ShapeStim(
        win=win, name='delay_fixation_4000',
        size=(0.03, 0.03), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='dimgray', fillColor='dimgray',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "Probe" ---
    probe_image = visual.ImageStim(
        win=win,
        name='probe_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    probe_keyResp = keyboard.Keyboard(deviceName='probe_keyResp')
    yesKey_text = visual.TextStim(win=win, name='yesKey_text',
        text='[F]\nYES',
        font='Arial',
        pos=(-0.2, -0.35), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    noKey_text = visual.TextStim(win=win, name='noKey_text',
        text='[J]\nNO',
        font='Arial',
        pos=(0.2, -0.35), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "ITI" ---
    ITI_text = visual.TextStim(win=win, name='ITI_text',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Rest" ---
    rest_welcome = visual.TextStim(win=win, name='rest_welcome',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    rest_continue = keyboard.Keyboard(deviceName='rest_continue')
    rest_continue_text = visual.TextStim(win=win, name='rest_continue_text',
        text='Press <SPACE> if you would like to end the break early!',
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "Trial_prepare" ---
    Trial_prepare_text = visual.TextStim(win=win, name='Trial_prepare_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Debrief" ---
    debrief_text = visual.TextStim(win=win, name='debrief_text',
        text="In the experiment, you were asked to encode two items on each trial. You were then cued to manipulate one of the items in your working memory by either maintaining it, suppressing it, or replacing it. We then probed your memory of one item's position. The aim of this study is to test if semantic activation reduces your ability to suppress the individual items in that list. The results of this study will improve our understanding of when people are good at controlling their thoughts and when they are not, which in its extreme could result in symptoms of psychological disorders such as rumination and thought intrusions.\n\nYour participation is greatly appreciated! If you have any questions, please feel free to email me at {edjoeleung@utexas.edu}. THANK YOU!!",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.035, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Welcome" ---
    # create an object to store info about Routine Welcome
    Welcome = data.Routine(
        name='Welcome',
        components=[welcome_text, welcome_keyResp],
    )
    Welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for welcome_keyResp
    welcome_keyResp.keys = []
    welcome_keyResp.rt = []
    _welcome_keyResp_allKeys = []
    # store start times for Welcome
    Welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Welcome.tStart = globalClock.getTime(format='float')
    Welcome.status = STARTED
    thisExp.addData('Welcome.started', Welcome.tStart)
    Welcome.maxDuration = None
    # keep track of which components have finished
    WelcomeComponents = Welcome.components
    for thisComponent in Welcome.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Welcome" ---
    Welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcome_text* updates
        
        # if welcome_text is starting this frame...
        if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_text.frameNStart = frameN  # exact frame index
            welcome_text.tStart = t  # local t and not account for scr refresh
            welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_text.started')
            # update status
            welcome_text.status = STARTED
            welcome_text.setAutoDraw(True)
        
        # if welcome_text is active this frame...
        if welcome_text.status == STARTED:
            # update params
            pass
        
        # *welcome_keyResp* updates
        waitOnFlip = False
        
        # if welcome_keyResp is starting this frame...
        if welcome_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_keyResp.frameNStart = frameN  # exact frame index
            welcome_keyResp.tStart = t  # local t and not account for scr refresh
            welcome_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_keyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_keyResp.started')
            # update status
            welcome_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(welcome_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(welcome_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if welcome_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = welcome_keyResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _welcome_keyResp_allKeys.extend(theseKeys)
            if len(_welcome_keyResp_allKeys):
                welcome_keyResp.keys = _welcome_keyResp_allKeys[-1].name  # just the last key pressed
                welcome_keyResp.rt = _welcome_keyResp_allKeys[-1].rt
                welcome_keyResp.duration = _welcome_keyResp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Welcome" ---
    for thisComponent in Welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Welcome
    Welcome.tStop = globalClock.getTime(format='float')
    Welcome.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Welcome.stopped', Welcome.tStop)
    # check responses
    if welcome_keyResp.keys in ['', [], None]:  # No response was made
        welcome_keyResp.keys = None
    thisExp.addData('welcome_keyResp.keys',welcome_keyResp.keys)
    if welcome_keyResp.keys != None:  # we had a response
        thisExp.addData('welcome_keyResp.rt', welcome_keyResp.rt)
        thisExp.addData('welcome_keyResp.duration', welcome_keyResp.duration)
    thisExp.nextEntry()
    # the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Encode_instruct" ---
    # create an object to store info about Routine Encode_instruct
    Encode_instruct = data.Routine(
        name='Encode_instruct',
        components=[encode_instruct_img, encode_instruct_cont_text, encode_instruct_keyResp],
    )
    Encode_instruct.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for encode_instruct_keyResp
    encode_instruct_keyResp.keys = []
    encode_instruct_keyResp.rt = []
    _encode_instruct_keyResp_allKeys = []
    # store start times for Encode_instruct
    Encode_instruct.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Encode_instruct.tStart = globalClock.getTime(format='float')
    Encode_instruct.status = STARTED
    thisExp.addData('Encode_instruct.started', Encode_instruct.tStart)
    Encode_instruct.maxDuration = None
    # keep track of which components have finished
    Encode_instructComponents = Encode_instruct.components
    for thisComponent in Encode_instruct.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Encode_instruct" ---
    Encode_instruct.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *encode_instruct_img* updates
        
        # if encode_instruct_img is starting this frame...
        if encode_instruct_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encode_instruct_img.frameNStart = frameN  # exact frame index
            encode_instruct_img.tStart = t  # local t and not account for scr refresh
            encode_instruct_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encode_instruct_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'encode_instruct_img.started')
            # update status
            encode_instruct_img.status = STARTED
            encode_instruct_img.setAutoDraw(True)
        
        # if encode_instruct_img is active this frame...
        if encode_instruct_img.status == STARTED:
            # update params
            pass
        
        # *encode_instruct_cont_text* updates
        
        # if encode_instruct_cont_text is starting this frame...
        if encode_instruct_cont_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encode_instruct_cont_text.frameNStart = frameN  # exact frame index
            encode_instruct_cont_text.tStart = t  # local t and not account for scr refresh
            encode_instruct_cont_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encode_instruct_cont_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'encode_instruct_cont_text.started')
            # update status
            encode_instruct_cont_text.status = STARTED
            encode_instruct_cont_text.setAutoDraw(True)
        
        # if encode_instruct_cont_text is active this frame...
        if encode_instruct_cont_text.status == STARTED:
            # update params
            pass
        
        # *encode_instruct_keyResp* updates
        waitOnFlip = False
        
        # if encode_instruct_keyResp is starting this frame...
        if encode_instruct_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encode_instruct_keyResp.frameNStart = frameN  # exact frame index
            encode_instruct_keyResp.tStart = t  # local t and not account for scr refresh
            encode_instruct_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encode_instruct_keyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'encode_instruct_keyResp.started')
            # update status
            encode_instruct_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(encode_instruct_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(encode_instruct_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if encode_instruct_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = encode_instruct_keyResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _encode_instruct_keyResp_allKeys.extend(theseKeys)
            if len(_encode_instruct_keyResp_allKeys):
                encode_instruct_keyResp.keys = _encode_instruct_keyResp_allKeys[-1].name  # just the last key pressed
                encode_instruct_keyResp.rt = _encode_instruct_keyResp_allKeys[-1].rt
                encode_instruct_keyResp.duration = _encode_instruct_keyResp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Encode_instruct.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Encode_instruct.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Encode_instruct" ---
    for thisComponent in Encode_instruct.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Encode_instruct
    Encode_instruct.tStop = globalClock.getTime(format='float')
    Encode_instruct.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Encode_instruct.stopped', Encode_instruct.tStop)
    # check responses
    if encode_instruct_keyResp.keys in ['', [], None]:  # No response was made
        encode_instruct_keyResp.keys = None
    thisExp.addData('encode_instruct_keyResp.keys',encode_instruct_keyResp.keys)
    if encode_instruct_keyResp.keys != None:  # we had a response
        thisExp.addData('encode_instruct_keyResp.rt', encode_instruct_keyResp.rt)
        thisExp.addData('encode_instruct_keyResp.duration', encode_instruct_keyResp.duration)
    thisExp.nextEntry()
    # the Routine "Encode_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Oper_screen_instruct" ---
    # create an object to store info about Routine Oper_screen_instruct
    Oper_screen_instruct = data.Routine(
        name='Oper_screen_instruct',
        components=[operscreen_instruct_img, operscreen_instruct_cont_text, operscreen_instruct_keyResp],
    )
    Oper_screen_instruct.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for operscreen_instruct_keyResp
    operscreen_instruct_keyResp.keys = []
    operscreen_instruct_keyResp.rt = []
    _operscreen_instruct_keyResp_allKeys = []
    # store start times for Oper_screen_instruct
    Oper_screen_instruct.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Oper_screen_instruct.tStart = globalClock.getTime(format='float')
    Oper_screen_instruct.status = STARTED
    thisExp.addData('Oper_screen_instruct.started', Oper_screen_instruct.tStart)
    Oper_screen_instruct.maxDuration = None
    # keep track of which components have finished
    Oper_screen_instructComponents = Oper_screen_instruct.components
    for thisComponent in Oper_screen_instruct.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Oper_screen_instruct" ---
    Oper_screen_instruct.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *operscreen_instruct_img* updates
        
        # if operscreen_instruct_img is starting this frame...
        if operscreen_instruct_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            operscreen_instruct_img.frameNStart = frameN  # exact frame index
            operscreen_instruct_img.tStart = t  # local t and not account for scr refresh
            operscreen_instruct_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(operscreen_instruct_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'operscreen_instruct_img.started')
            # update status
            operscreen_instruct_img.status = STARTED
            operscreen_instruct_img.setAutoDraw(True)
        
        # if operscreen_instruct_img is active this frame...
        if operscreen_instruct_img.status == STARTED:
            # update params
            pass
        
        # *operscreen_instruct_cont_text* updates
        
        # if operscreen_instruct_cont_text is starting this frame...
        if operscreen_instruct_cont_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            operscreen_instruct_cont_text.frameNStart = frameN  # exact frame index
            operscreen_instruct_cont_text.tStart = t  # local t and not account for scr refresh
            operscreen_instruct_cont_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(operscreen_instruct_cont_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'operscreen_instruct_cont_text.started')
            # update status
            operscreen_instruct_cont_text.status = STARTED
            operscreen_instruct_cont_text.setAutoDraw(True)
        
        # if operscreen_instruct_cont_text is active this frame...
        if operscreen_instruct_cont_text.status == STARTED:
            # update params
            pass
        
        # *operscreen_instruct_keyResp* updates
        waitOnFlip = False
        
        # if operscreen_instruct_keyResp is starting this frame...
        if operscreen_instruct_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            operscreen_instruct_keyResp.frameNStart = frameN  # exact frame index
            operscreen_instruct_keyResp.tStart = t  # local t and not account for scr refresh
            operscreen_instruct_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(operscreen_instruct_keyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'operscreen_instruct_keyResp.started')
            # update status
            operscreen_instruct_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(operscreen_instruct_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(operscreen_instruct_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if operscreen_instruct_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = operscreen_instruct_keyResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _operscreen_instruct_keyResp_allKeys.extend(theseKeys)
            if len(_operscreen_instruct_keyResp_allKeys):
                operscreen_instruct_keyResp.keys = _operscreen_instruct_keyResp_allKeys[-1].name  # just the last key pressed
                operscreen_instruct_keyResp.rt = _operscreen_instruct_keyResp_allKeys[-1].rt
                operscreen_instruct_keyResp.duration = _operscreen_instruct_keyResp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Oper_screen_instruct.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Oper_screen_instruct.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Oper_screen_instruct" ---
    for thisComponent in Oper_screen_instruct.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Oper_screen_instruct
    Oper_screen_instruct.tStop = globalClock.getTime(format='float')
    Oper_screen_instruct.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Oper_screen_instruct.stopped', Oper_screen_instruct.tStop)
    # check responses
    if operscreen_instruct_keyResp.keys in ['', [], None]:  # No response was made
        operscreen_instruct_keyResp.keys = None
    thisExp.addData('operscreen_instruct_keyResp.keys',operscreen_instruct_keyResp.keys)
    if operscreen_instruct_keyResp.keys != None:  # we had a response
        thisExp.addData('operscreen_instruct_keyResp.rt', operscreen_instruct_keyResp.rt)
        thisExp.addData('operscreen_instruct_keyResp.duration', operscreen_instruct_keyResp.duration)
    thisExp.nextEntry()
    # the Routine "Oper_screen_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Operations_instruct" ---
    # create an object to store info about Routine Operations_instruct
    Operations_instruct = data.Routine(
        name='Operations_instruct',
        components=[operations_instruct_img, operations_instruct_conttext, operations_instruct_keyResp],
    )
    Operations_instruct.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for operations_instruct_keyResp
    operations_instruct_keyResp.keys = []
    operations_instruct_keyResp.rt = []
    _operations_instruct_keyResp_allKeys = []
    # store start times for Operations_instruct
    Operations_instruct.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Operations_instruct.tStart = globalClock.getTime(format='float')
    Operations_instruct.status = STARTED
    thisExp.addData('Operations_instruct.started', Operations_instruct.tStart)
    Operations_instruct.maxDuration = None
    # keep track of which components have finished
    Operations_instructComponents = Operations_instruct.components
    for thisComponent in Operations_instruct.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Operations_instruct" ---
    Operations_instruct.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *operations_instruct_img* updates
        
        # if operations_instruct_img is starting this frame...
        if operations_instruct_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            operations_instruct_img.frameNStart = frameN  # exact frame index
            operations_instruct_img.tStart = t  # local t and not account for scr refresh
            operations_instruct_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(operations_instruct_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'operations_instruct_img.started')
            # update status
            operations_instruct_img.status = STARTED
            operations_instruct_img.setAutoDraw(True)
        
        # if operations_instruct_img is active this frame...
        if operations_instruct_img.status == STARTED:
            # update params
            pass
        
        # *operations_instruct_conttext* updates
        
        # if operations_instruct_conttext is starting this frame...
        if operations_instruct_conttext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            operations_instruct_conttext.frameNStart = frameN  # exact frame index
            operations_instruct_conttext.tStart = t  # local t and not account for scr refresh
            operations_instruct_conttext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(operations_instruct_conttext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'operations_instruct_conttext.started')
            # update status
            operations_instruct_conttext.status = STARTED
            operations_instruct_conttext.setAutoDraw(True)
        
        # if operations_instruct_conttext is active this frame...
        if operations_instruct_conttext.status == STARTED:
            # update params
            pass
        
        # *operations_instruct_keyResp* updates
        waitOnFlip = False
        
        # if operations_instruct_keyResp is starting this frame...
        if operations_instruct_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            operations_instruct_keyResp.frameNStart = frameN  # exact frame index
            operations_instruct_keyResp.tStart = t  # local t and not account for scr refresh
            operations_instruct_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(operations_instruct_keyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'operations_instruct_keyResp.started')
            # update status
            operations_instruct_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(operations_instruct_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(operations_instruct_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if operations_instruct_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = operations_instruct_keyResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _operations_instruct_keyResp_allKeys.extend(theseKeys)
            if len(_operations_instruct_keyResp_allKeys):
                operations_instruct_keyResp.keys = _operations_instruct_keyResp_allKeys[-1].name  # just the last key pressed
                operations_instruct_keyResp.rt = _operations_instruct_keyResp_allKeys[-1].rt
                operations_instruct_keyResp.duration = _operations_instruct_keyResp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Operations_instruct.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Operations_instruct.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Operations_instruct" ---
    for thisComponent in Operations_instruct.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Operations_instruct
    Operations_instruct.tStop = globalClock.getTime(format='float')
    Operations_instruct.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Operations_instruct.stopped', Operations_instruct.tStop)
    # check responses
    if operations_instruct_keyResp.keys in ['', [], None]:  # No response was made
        operations_instruct_keyResp.keys = None
    thisExp.addData('operations_instruct_keyResp.keys',operations_instruct_keyResp.keys)
    if operations_instruct_keyResp.keys != None:  # we had a response
        thisExp.addData('operations_instruct_keyResp.rt', operations_instruct_keyResp.rt)
        thisExp.addData('operations_instruct_keyResp.duration', operations_instruct_keyResp.duration)
    thisExp.nextEntry()
    # the Routine "Operations_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Probe_screen_instruct" ---
    # create an object to store info about Routine Probe_screen_instruct
    Probe_screen_instruct = data.Routine(
        name='Probe_screen_instruct',
        components=[probescreen_instruct_img, probescreen_instruct_conttext, probescreen_instruct_keyResp],
    )
    Probe_screen_instruct.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for probescreen_instruct_keyResp
    probescreen_instruct_keyResp.keys = []
    probescreen_instruct_keyResp.rt = []
    _probescreen_instruct_keyResp_allKeys = []
    # store start times for Probe_screen_instruct
    Probe_screen_instruct.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Probe_screen_instruct.tStart = globalClock.getTime(format='float')
    Probe_screen_instruct.status = STARTED
    thisExp.addData('Probe_screen_instruct.started', Probe_screen_instruct.tStart)
    Probe_screen_instruct.maxDuration = None
    # keep track of which components have finished
    Probe_screen_instructComponents = Probe_screen_instruct.components
    for thisComponent in Probe_screen_instruct.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Probe_screen_instruct" ---
    Probe_screen_instruct.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *probescreen_instruct_img* updates
        
        # if probescreen_instruct_img is starting this frame...
        if probescreen_instruct_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            probescreen_instruct_img.frameNStart = frameN  # exact frame index
            probescreen_instruct_img.tStart = t  # local t and not account for scr refresh
            probescreen_instruct_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(probescreen_instruct_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'probescreen_instruct_img.started')
            # update status
            probescreen_instruct_img.status = STARTED
            probescreen_instruct_img.setAutoDraw(True)
        
        # if probescreen_instruct_img is active this frame...
        if probescreen_instruct_img.status == STARTED:
            # update params
            pass
        
        # *probescreen_instruct_conttext* updates
        
        # if probescreen_instruct_conttext is starting this frame...
        if probescreen_instruct_conttext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            probescreen_instruct_conttext.frameNStart = frameN  # exact frame index
            probescreen_instruct_conttext.tStart = t  # local t and not account for scr refresh
            probescreen_instruct_conttext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(probescreen_instruct_conttext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'probescreen_instruct_conttext.started')
            # update status
            probescreen_instruct_conttext.status = STARTED
            probescreen_instruct_conttext.setAutoDraw(True)
        
        # if probescreen_instruct_conttext is active this frame...
        if probescreen_instruct_conttext.status == STARTED:
            # update params
            pass
        
        # *probescreen_instruct_keyResp* updates
        waitOnFlip = False
        
        # if probescreen_instruct_keyResp is starting this frame...
        if probescreen_instruct_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            probescreen_instruct_keyResp.frameNStart = frameN  # exact frame index
            probescreen_instruct_keyResp.tStart = t  # local t and not account for scr refresh
            probescreen_instruct_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(probescreen_instruct_keyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'probescreen_instruct_keyResp.started')
            # update status
            probescreen_instruct_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(probescreen_instruct_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(probescreen_instruct_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if probescreen_instruct_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = probescreen_instruct_keyResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _probescreen_instruct_keyResp_allKeys.extend(theseKeys)
            if len(_probescreen_instruct_keyResp_allKeys):
                probescreen_instruct_keyResp.keys = _probescreen_instruct_keyResp_allKeys[-1].name  # just the last key pressed
                probescreen_instruct_keyResp.rt = _probescreen_instruct_keyResp_allKeys[-1].rt
                probescreen_instruct_keyResp.duration = _probescreen_instruct_keyResp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Probe_screen_instruct.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Probe_screen_instruct.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Probe_screen_instruct" ---
    for thisComponent in Probe_screen_instruct.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Probe_screen_instruct
    Probe_screen_instruct.tStop = globalClock.getTime(format='float')
    Probe_screen_instruct.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Probe_screen_instruct.stopped', Probe_screen_instruct.tStop)
    # check responses
    if probescreen_instruct_keyResp.keys in ['', [], None]:  # No response was made
        probescreen_instruct_keyResp.keys = None
    thisExp.addData('probescreen_instruct_keyResp.keys',probescreen_instruct_keyResp.keys)
    if probescreen_instruct_keyResp.keys != None:  # we had a response
        thisExp.addData('probescreen_instruct_keyResp.rt', probescreen_instruct_keyResp.rt)
        thisExp.addData('probescreen_instruct_keyResp.duration', probescreen_instruct_keyResp.duration)
    thisExp.nextEntry()
    # the Routine "Probe_screen_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Probe_instruct" ---
    # create an object to store info about Routine Probe_instruct
    Probe_instruct = data.Routine(
        name='Probe_instruct',
        components=[probe_instructions_img, probe_instructions_conttext, probe_instructions_keyResp],
    )
    Probe_instruct.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for probe_instructions_keyResp
    probe_instructions_keyResp.keys = []
    probe_instructions_keyResp.rt = []
    _probe_instructions_keyResp_allKeys = []
    # store start times for Probe_instruct
    Probe_instruct.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Probe_instruct.tStart = globalClock.getTime(format='float')
    Probe_instruct.status = STARTED
    thisExp.addData('Probe_instruct.started', Probe_instruct.tStart)
    Probe_instruct.maxDuration = None
    # keep track of which components have finished
    Probe_instructComponents = Probe_instruct.components
    for thisComponent in Probe_instruct.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Probe_instruct" ---
    Probe_instruct.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *probe_instructions_img* updates
        
        # if probe_instructions_img is starting this frame...
        if probe_instructions_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            probe_instructions_img.frameNStart = frameN  # exact frame index
            probe_instructions_img.tStart = t  # local t and not account for scr refresh
            probe_instructions_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(probe_instructions_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'probe_instructions_img.started')
            # update status
            probe_instructions_img.status = STARTED
            probe_instructions_img.setAutoDraw(True)
        
        # if probe_instructions_img is active this frame...
        if probe_instructions_img.status == STARTED:
            # update params
            pass
        
        # *probe_instructions_conttext* updates
        
        # if probe_instructions_conttext is starting this frame...
        if probe_instructions_conttext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            probe_instructions_conttext.frameNStart = frameN  # exact frame index
            probe_instructions_conttext.tStart = t  # local t and not account for scr refresh
            probe_instructions_conttext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(probe_instructions_conttext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'probe_instructions_conttext.started')
            # update status
            probe_instructions_conttext.status = STARTED
            probe_instructions_conttext.setAutoDraw(True)
        
        # if probe_instructions_conttext is active this frame...
        if probe_instructions_conttext.status == STARTED:
            # update params
            pass
        
        # *probe_instructions_keyResp* updates
        waitOnFlip = False
        
        # if probe_instructions_keyResp is starting this frame...
        if probe_instructions_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            probe_instructions_keyResp.frameNStart = frameN  # exact frame index
            probe_instructions_keyResp.tStart = t  # local t and not account for scr refresh
            probe_instructions_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(probe_instructions_keyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'probe_instructions_keyResp.started')
            # update status
            probe_instructions_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(probe_instructions_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(probe_instructions_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if probe_instructions_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = probe_instructions_keyResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _probe_instructions_keyResp_allKeys.extend(theseKeys)
            if len(_probe_instructions_keyResp_allKeys):
                probe_instructions_keyResp.keys = _probe_instructions_keyResp_allKeys[-1].name  # just the last key pressed
                probe_instructions_keyResp.rt = _probe_instructions_keyResp_allKeys[-1].rt
                probe_instructions_keyResp.duration = _probe_instructions_keyResp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Probe_instruct.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Probe_instruct.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Probe_instruct" ---
    for thisComponent in Probe_instruct.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Probe_instruct
    Probe_instruct.tStop = globalClock.getTime(format='float')
    Probe_instruct.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Probe_instruct.stopped', Probe_instruct.tStop)
    # check responses
    if probe_instructions_keyResp.keys in ['', [], None]:  # No response was made
        probe_instructions_keyResp.keys = None
    thisExp.addData('probe_instructions_keyResp.keys',probe_instructions_keyResp.keys)
    if probe_instructions_keyResp.keys != None:  # we had a response
        thisExp.addData('probe_instructions_keyResp.rt', probe_instructions_keyResp.rt)
        thisExp.addData('probe_instructions_keyResp.duration', probe_instructions_keyResp.duration)
    thisExp.nextEntry()
    # the Routine "Probe_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Practice_begin" ---
    # create an object to store info about Routine Practice_begin
    Practice_begin = data.Routine(
        name='Practice_begin',
        components=[prac_begin_text, prac_begin_keyResp],
    )
    Practice_begin.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for prac_begin_keyResp
    prac_begin_keyResp.keys = []
    prac_begin_keyResp.rt = []
    _prac_begin_keyResp_allKeys = []
    # Run 'Begin Routine' code from corrinit_code
    corr = 0
    # store start times for Practice_begin
    Practice_begin.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Practice_begin.tStart = globalClock.getTime(format='float')
    Practice_begin.status = STARTED
    thisExp.addData('Practice_begin.started', Practice_begin.tStart)
    Practice_begin.maxDuration = None
    # keep track of which components have finished
    Practice_beginComponents = Practice_begin.components
    for thisComponent in Practice_begin.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Practice_begin" ---
    Practice_begin.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_begin_text* updates
        
        # if prac_begin_text is starting this frame...
        if prac_begin_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_begin_text.frameNStart = frameN  # exact frame index
            prac_begin_text.tStart = t  # local t and not account for scr refresh
            prac_begin_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_begin_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_begin_text.started')
            # update status
            prac_begin_text.status = STARTED
            prac_begin_text.setAutoDraw(True)
        
        # if prac_begin_text is active this frame...
        if prac_begin_text.status == STARTED:
            # update params
            pass
        
        # *prac_begin_keyResp* updates
        waitOnFlip = False
        
        # if prac_begin_keyResp is starting this frame...
        if prac_begin_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_begin_keyResp.frameNStart = frameN  # exact frame index
            prac_begin_keyResp.tStart = t  # local t and not account for scr refresh
            prac_begin_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_begin_keyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prac_begin_keyResp.started')
            # update status
            prac_begin_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_begin_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_begin_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_begin_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = prac_begin_keyResp.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _prac_begin_keyResp_allKeys.extend(theseKeys)
            if len(_prac_begin_keyResp_allKeys):
                prac_begin_keyResp.keys = _prac_begin_keyResp_allKeys[-1].name  # just the last key pressed
                prac_begin_keyResp.rt = _prac_begin_keyResp_allKeys[-1].rt
                prac_begin_keyResp.duration = _prac_begin_keyResp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Practice_begin.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_begin.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Practice_begin" ---
    for thisComponent in Practice_begin.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Practice_begin
    Practice_begin.tStop = globalClock.getTime(format='float')
    Practice_begin.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Practice_begin.stopped', Practice_begin.tStop)
    # check responses
    if prac_begin_keyResp.keys in ['', [], None]:  # No response was made
        prac_begin_keyResp.keys = None
    thisExp.addData('prac_begin_keyResp.keys',prac_begin_keyResp.keys)
    if prac_begin_keyResp.keys != None:  # we had a response
        thisExp.addData('prac_begin_keyResp.rt', prac_begin_keyResp.rt)
        thisExp.addData('prac_begin_keyResp.duration', prac_begin_keyResp.duration)
    thisExp.nextEntry()
    # the Routine "Practice_begin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Trial_prepare" ---
    # create an object to store info about Routine Trial_prepare
    Trial_prepare = data.Routine(
        name='Trial_prepare',
        components=[Trial_prepare_text],
    )
    Trial_prepare.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for Trial_prepare
    Trial_prepare.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Trial_prepare.tStart = globalClock.getTime(format='float')
    Trial_prepare.status = STARTED
    thisExp.addData('Trial_prepare.started', Trial_prepare.tStart)
    Trial_prepare.maxDuration = None
    # keep track of which components have finished
    Trial_prepareComponents = Trial_prepare.components
    for thisComponent in Trial_prepare.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial_prepare" ---
    Trial_prepare.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Trial_prepare_text* updates
        
        # if Trial_prepare_text is starting this frame...
        if Trial_prepare_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Trial_prepare_text.frameNStart = frameN  # exact frame index
            Trial_prepare_text.tStart = t  # local t and not account for scr refresh
            Trial_prepare_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_prepare_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_prepare_text.started')
            # update status
            Trial_prepare_text.status = STARTED
            Trial_prepare_text.setAutoDraw(True)
        
        # if Trial_prepare_text is active this frame...
        if Trial_prepare_text.status == STARTED:
            # update params
            Trial_prepare_text.setText(f"The trial will begin in {5 - t:.0f} s.", log=False)
        
        # if Trial_prepare_text is stopping this frame...
        if Trial_prepare_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Trial_prepare_text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                Trial_prepare_text.tStop = t  # not accounting for scr refresh
                Trial_prepare_text.tStopRefresh = tThisFlipGlobal  # on global time
                Trial_prepare_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Trial_prepare_text.stopped')
                # update status
                Trial_prepare_text.status = FINISHED
                Trial_prepare_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Trial_prepare.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial_prepare.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial_prepare" ---
    for thisComponent in Trial_prepare.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Trial_prepare
    Trial_prepare.tStop = globalClock.getTime(format='float')
    Trial_prepare.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Trial_prepare.stopped', Trial_prepare.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Trial_prepare.maxDurationReached:
        routineTimer.addTime(-Trial_prepare.maxDuration)
    elif Trial_prepare.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    prac_trials = data.TrialHandler2(
        name='prac_trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('stimuli/csvs/maintask_stimlists/prac_stim_list.csv'), 
        seed=None, 
    )
    thisExp.addLoop(prac_trials)  # add the loop to the experiment
    thisPrac_trial = prac_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial.rgb)
    if thisPrac_trial != None:
        for paramName in thisPrac_trial:
            globals()[paramName] = thisPrac_trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPrac_trial in prac_trials:
        currentLoop = prac_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial.rgb)
        if thisPrac_trial != None:
            for paramName in thisPrac_trial:
                globals()[paramName] = thisPrac_trial[paramName]
        
        # --- Prepare to start Routine "Encode" ---
        # create an object to store info about Routine Encode
        Encode = data.Routine(
            name='Encode',
            components=[encode_fixation, img_1_left, img_2_right],
        )
        Encode.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        img_1_left.setImage(encode_1_img)
        img_2_right.setImage(encode_2_img)
        # store start times for Encode
        Encode.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Encode.tStart = globalClock.getTime(format='float')
        Encode.status = STARTED
        thisExp.addData('Encode.started', Encode.tStart)
        Encode.maxDuration = None
        # keep track of which components have finished
        EncodeComponents = Encode.components
        for thisComponent in Encode.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Encode" ---
        # if trial has changed, end Routine now
        if isinstance(prac_trials, data.TrialHandler2) and thisPrac_trial.thisN != prac_trials.thisTrial.thisN:
            continueRoutine = False
        Encode.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *encode_fixation* updates
            
            # if encode_fixation is starting this frame...
            if encode_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                encode_fixation.frameNStart = frameN  # exact frame index
                encode_fixation.tStart = t  # local t and not account for scr refresh
                encode_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(encode_fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'encode_fixation.started')
                # update status
                encode_fixation.status = STARTED
                encode_fixation.setAutoDraw(True)
            
            # if encode_fixation is active this frame...
            if encode_fixation.status == STARTED:
                # update params
                pass
            
            # if encode_fixation is stopping this frame...
            if encode_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > encode_fixation.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    encode_fixation.tStop = t  # not accounting for scr refresh
                    encode_fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    encode_fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'encode_fixation.stopped')
                    # update status
                    encode_fixation.status = FINISHED
                    encode_fixation.setAutoDraw(False)
            
            # *img_1_left* updates
            
            # if img_1_left is starting this frame...
            if img_1_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img_1_left.frameNStart = frameN  # exact frame index
                img_1_left.tStart = t  # local t and not account for scr refresh
                img_1_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img_1_left, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'img_1_left.started')
                # update status
                img_1_left.status = STARTED
                img_1_left.setAutoDraw(True)
            
            # if img_1_left is active this frame...
            if img_1_left.status == STARTED:
                # update params
                pass
            
            # if img_1_left is stopping this frame...
            if img_1_left.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > img_1_left.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    img_1_left.tStop = t  # not accounting for scr refresh
                    img_1_left.tStopRefresh = tThisFlipGlobal  # on global time
                    img_1_left.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'img_1_left.stopped')
                    # update status
                    img_1_left.status = FINISHED
                    img_1_left.setAutoDraw(False)
            
            # *img_2_right* updates
            
            # if img_2_right is starting this frame...
            if img_2_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img_2_right.frameNStart = frameN  # exact frame index
                img_2_right.tStart = t  # local t and not account for scr refresh
                img_2_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img_2_right, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'img_2_right.started')
                # update status
                img_2_right.status = STARTED
                img_2_right.setAutoDraw(True)
            
            # if img_2_right is active this frame...
            if img_2_right.status == STARTED:
                # update params
                pass
            
            # if img_2_right is stopping this frame...
            if img_2_right.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > img_2_right.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    img_2_right.tStop = t  # not accounting for scr refresh
                    img_2_right.tStopRefresh = tThisFlipGlobal  # on global time
                    img_2_right.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'img_2_right.stopped')
                    # update status
                    img_2_right.status = FINISHED
                    img_2_right.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Encode.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Encode.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Encode" ---
        for thisComponent in Encode.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Encode
        Encode.tStop = globalClock.getTime(format='float')
        Encode.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Encode.stopped', Encode.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Encode.maxDurationReached:
            routineTimer.addTime(-Encode.maxDuration)
        elif Encode.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "Delay_2000" ---
        # create an object to store info about Routine Delay_2000
        Delay_2000 = data.Routine(
            name='Delay_2000',
            components=[delay_fixation_2000],
        )
        Delay_2000.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for Delay_2000
        Delay_2000.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Delay_2000.tStart = globalClock.getTime(format='float')
        Delay_2000.status = STARTED
        thisExp.addData('Delay_2000.started', Delay_2000.tStart)
        Delay_2000.maxDuration = None
        # keep track of which components have finished
        Delay_2000Components = Delay_2000.components
        for thisComponent in Delay_2000.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Delay_2000" ---
        # if trial has changed, end Routine now
        if isinstance(prac_trials, data.TrialHandler2) and thisPrac_trial.thisN != prac_trials.thisTrial.thisN:
            continueRoutine = False
        Delay_2000.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *delay_fixation_2000* updates
            
            # if delay_fixation_2000 is starting this frame...
            if delay_fixation_2000.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                delay_fixation_2000.frameNStart = frameN  # exact frame index
                delay_fixation_2000.tStart = t  # local t and not account for scr refresh
                delay_fixation_2000.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(delay_fixation_2000, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'delay_fixation_2000.started')
                # update status
                delay_fixation_2000.status = STARTED
                delay_fixation_2000.setAutoDraw(True)
            
            # if delay_fixation_2000 is active this frame...
            if delay_fixation_2000.status == STARTED:
                # update params
                pass
            
            # if delay_fixation_2000 is stopping this frame...
            if delay_fixation_2000.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > delay_fixation_2000.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    delay_fixation_2000.tStop = t  # not accounting for scr refresh
                    delay_fixation_2000.tStopRefresh = tThisFlipGlobal  # on global time
                    delay_fixation_2000.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'delay_fixation_2000.stopped')
                    # update status
                    delay_fixation_2000.status = FINISHED
                    delay_fixation_2000.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Delay_2000.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Delay_2000.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Delay_2000" ---
        for thisComponent in Delay_2000.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Delay_2000
        Delay_2000.tStop = globalClock.getTime(format='float')
        Delay_2000.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Delay_2000.stopped', Delay_2000.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Delay_2000.maxDurationReached:
            routineTimer.addTime(-Delay_2000.maxDuration)
        elif Delay_2000.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "Manipulate" ---
        # create an object to store info about Routine Manipulate
        Manipulate = data.Routine(
            name='Manipulate',
            components=[manipulate_cue, manipulate_fixation],
        )
        Manipulate.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from cue_position_code
        if cue_position == "left":
            cuepos = (-0.3, 0)
        elif cue_position == "right":
            cuepos = (0.3, 0)
        print("cue_position = ", cue_position)
        manipulate_cue.setPos(cuepos)
        manipulate_cue.setImage(replace_img)
        # store start times for Manipulate
        Manipulate.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Manipulate.tStart = globalClock.getTime(format='float')
        Manipulate.status = STARTED
        thisExp.addData('Manipulate.started', Manipulate.tStart)
        Manipulate.maxDuration = None
        # keep track of which components have finished
        ManipulateComponents = Manipulate.components
        for thisComponent in Manipulate.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Manipulate" ---
        # if trial has changed, end Routine now
        if isinstance(prac_trials, data.TrialHandler2) and thisPrac_trial.thisN != prac_trials.thisTrial.thisN:
            continueRoutine = False
        Manipulate.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *manipulate_cue* updates
            
            # if manipulate_cue is starting this frame...
            if manipulate_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                manipulate_cue.frameNStart = frameN  # exact frame index
                manipulate_cue.tStart = t  # local t and not account for scr refresh
                manipulate_cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(manipulate_cue, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'manipulate_cue.started')
                # update status
                manipulate_cue.status = STARTED
                manipulate_cue.setAutoDraw(True)
            
            # if manipulate_cue is active this frame...
            if manipulate_cue.status == STARTED:
                # update params
                pass
            
            # if manipulate_cue is stopping this frame...
            if manipulate_cue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > manipulate_cue.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    manipulate_cue.tStop = t  # not accounting for scr refresh
                    manipulate_cue.tStopRefresh = tThisFlipGlobal  # on global time
                    manipulate_cue.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'manipulate_cue.stopped')
                    # update status
                    manipulate_cue.status = FINISHED
                    manipulate_cue.setAutoDraw(False)
            
            # *manipulate_fixation* updates
            
            # if manipulate_fixation is starting this frame...
            if manipulate_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                manipulate_fixation.frameNStart = frameN  # exact frame index
                manipulate_fixation.tStart = t  # local t and not account for scr refresh
                manipulate_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(manipulate_fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'manipulate_fixation.started')
                # update status
                manipulate_fixation.status = STARTED
                manipulate_fixation.setAutoDraw(True)
            
            # if manipulate_fixation is active this frame...
            if manipulate_fixation.status == STARTED:
                # update params
                pass
            
            # if manipulate_fixation is stopping this frame...
            if manipulate_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > manipulate_fixation.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    manipulate_fixation.tStop = t  # not accounting for scr refresh
                    manipulate_fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    manipulate_fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'manipulate_fixation.stopped')
                    # update status
                    manipulate_fixation.status = FINISHED
                    manipulate_fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Manipulate.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Manipulate.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Manipulate" ---
        for thisComponent in Manipulate.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Manipulate
        Manipulate.tStop = globalClock.getTime(format='float')
        Manipulate.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Manipulate.stopped', Manipulate.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Manipulate.maxDurationReached:
            routineTimer.addTime(-Manipulate.maxDuration)
        elif Manipulate.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "Delay_4000" ---
        # create an object to store info about Routine Delay_4000
        Delay_4000 = data.Routine(
            name='Delay_4000',
            components=[delay_fixation_4000],
        )
        Delay_4000.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for Delay_4000
        Delay_4000.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Delay_4000.tStart = globalClock.getTime(format='float')
        Delay_4000.status = STARTED
        thisExp.addData('Delay_4000.started', Delay_4000.tStart)
        Delay_4000.maxDuration = None
        # keep track of which components have finished
        Delay_4000Components = Delay_4000.components
        for thisComponent in Delay_4000.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Delay_4000" ---
        # if trial has changed, end Routine now
        if isinstance(prac_trials, data.TrialHandler2) and thisPrac_trial.thisN != prac_trials.thisTrial.thisN:
            continueRoutine = False
        Delay_4000.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 4.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *delay_fixation_4000* updates
            
            # if delay_fixation_4000 is starting this frame...
            if delay_fixation_4000.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                delay_fixation_4000.frameNStart = frameN  # exact frame index
                delay_fixation_4000.tStart = t  # local t and not account for scr refresh
                delay_fixation_4000.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(delay_fixation_4000, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'delay_fixation_4000.started')
                # update status
                delay_fixation_4000.status = STARTED
                delay_fixation_4000.setAutoDraw(True)
            
            # if delay_fixation_4000 is active this frame...
            if delay_fixation_4000.status == STARTED:
                # update params
                pass
            
            # if delay_fixation_4000 is stopping this frame...
            if delay_fixation_4000.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > delay_fixation_4000.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    delay_fixation_4000.tStop = t  # not accounting for scr refresh
                    delay_fixation_4000.tStopRefresh = tThisFlipGlobal  # on global time
                    delay_fixation_4000.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'delay_fixation_4000.stopped')
                    # update status
                    delay_fixation_4000.status = FINISHED
                    delay_fixation_4000.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Delay_4000.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Delay_4000.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Delay_4000" ---
        for thisComponent in Delay_4000.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Delay_4000
        Delay_4000.tStop = globalClock.getTime(format='float')
        Delay_4000.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Delay_4000.stopped', Delay_4000.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Delay_4000.maxDurationReached:
            routineTimer.addTime(-Delay_4000.maxDuration)
        elif Delay_4000.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-4.000000)
        
        # --- Prepare to start Routine "Probe" ---
        # create an object to store info about Routine Probe
        Probe = data.Routine(
            name='Probe',
            components=[probe_image, probe_keyResp, yesKey_text, noKey_text],
        )
        Probe.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        print("probesubtype = ", probe_subtype)
        print("trial = ", trial_num)
        
        if probe_subtype in ["cued", "uncued", "replacement"]:
            correct_ans = "f"
        else:
            correct_ans = "j"
        probe_image.setImage(probe_img)
        # create starting attributes for probe_keyResp
        probe_keyResp.keys = []
        probe_keyResp.rt = []
        _probe_keyResp_allKeys = []
        # store start times for Probe
        Probe.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Probe.tStart = globalClock.getTime(format='float')
        Probe.status = STARTED
        thisExp.addData('Probe.started', Probe.tStart)
        Probe.maxDuration = None
        # keep track of which components have finished
        ProbeComponents = Probe.components
        for thisComponent in Probe.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Probe" ---
        # if trial has changed, end Routine now
        if isinstance(prac_trials, data.TrialHandler2) and thisPrac_trial.thisN != prac_trials.thisTrial.thisN:
            continueRoutine = False
        Probe.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *probe_image* updates
            
            # if probe_image is starting this frame...
            if probe_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                probe_image.frameNStart = frameN  # exact frame index
                probe_image.tStart = t  # local t and not account for scr refresh
                probe_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'probe_image.started')
                # update status
                probe_image.status = STARTED
                probe_image.setAutoDraw(True)
            
            # if probe_image is active this frame...
            if probe_image.status == STARTED:
                # update params
                pass
            
            # if probe_image is stopping this frame...
            if probe_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > probe_image.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    probe_image.tStop = t  # not accounting for scr refresh
                    probe_image.tStopRefresh = tThisFlipGlobal  # on global time
                    probe_image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'probe_image.stopped')
                    # update status
                    probe_image.status = FINISHED
                    probe_image.setAutoDraw(False)
            
            # *probe_keyResp* updates
            waitOnFlip = False
            
            # if probe_keyResp is starting this frame...
            if probe_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                probe_keyResp.frameNStart = frameN  # exact frame index
                probe_keyResp.tStart = t  # local t and not account for scr refresh
                probe_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe_keyResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'probe_keyResp.started')
                # update status
                probe_keyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(probe_keyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(probe_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if probe_keyResp is stopping this frame...
            if probe_keyResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > probe_keyResp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    probe_keyResp.tStop = t  # not accounting for scr refresh
                    probe_keyResp.tStopRefresh = tThisFlipGlobal  # on global time
                    probe_keyResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'probe_keyResp.stopped')
                    # update status
                    probe_keyResp.status = FINISHED
                    probe_keyResp.status = FINISHED
            if probe_keyResp.status == STARTED and not waitOnFlip:
                theseKeys = probe_keyResp.getKeys(keyList=['f', 'j'], ignoreKeys=["escape"], waitRelease=False)
                _probe_keyResp_allKeys.extend(theseKeys)
                if len(_probe_keyResp_allKeys):
                    probe_keyResp.keys = _probe_keyResp_allKeys[-1].name  # just the last key pressed
                    probe_keyResp.rt = _probe_keyResp_allKeys[-1].rt
                    probe_keyResp.duration = _probe_keyResp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *yesKey_text* updates
            
            # if yesKey_text is starting this frame...
            if yesKey_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                yesKey_text.frameNStart = frameN  # exact frame index
                yesKey_text.tStart = t  # local t and not account for scr refresh
                yesKey_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(yesKey_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'yesKey_text.started')
                # update status
                yesKey_text.status = STARTED
                yesKey_text.setAutoDraw(True)
            
            # if yesKey_text is active this frame...
            if yesKey_text.status == STARTED:
                # update params
                pass
            
            # if yesKey_text is stopping this frame...
            if yesKey_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > yesKey_text.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    yesKey_text.tStop = t  # not accounting for scr refresh
                    yesKey_text.tStopRefresh = tThisFlipGlobal  # on global time
                    yesKey_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'yesKey_text.stopped')
                    # update status
                    yesKey_text.status = FINISHED
                    yesKey_text.setAutoDraw(False)
            
            # *noKey_text* updates
            
            # if noKey_text is starting this frame...
            if noKey_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                noKey_text.frameNStart = frameN  # exact frame index
                noKey_text.tStart = t  # local t and not account for scr refresh
                noKey_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noKey_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'noKey_text.started')
                # update status
                noKey_text.status = STARTED
                noKey_text.setAutoDraw(True)
            
            # if noKey_text is active this frame...
            if noKey_text.status == STARTED:
                # update params
                pass
            
            # if noKey_text is stopping this frame...
            if noKey_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noKey_text.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    noKey_text.tStop = t  # not accounting for scr refresh
                    noKey_text.tStopRefresh = tThisFlipGlobal  # on global time
                    noKey_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'noKey_text.stopped')
                    # update status
                    noKey_text.status = FINISHED
                    noKey_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Probe.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Probe.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Probe" ---
        for thisComponent in Probe.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Probe
        Probe.tStop = globalClock.getTime(format='float')
        Probe.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Probe.stopped', Probe.tStop)
        # Run 'End Routine' code from code
        keypressed = _probe_keyResp_allKeys[-1].name
        if keypressed == correct_ans:
            print("correct!")
            corr += 1
        # check responses
        if probe_keyResp.keys in ['', [], None]:  # No response was made
            probe_keyResp.keys = None
        prac_trials.addData('probe_keyResp.keys',probe_keyResp.keys)
        if probe_keyResp.keys != None:  # we had a response
            prac_trials.addData('probe_keyResp.rt', probe_keyResp.rt)
            prac_trials.addData('probe_keyResp.duration', probe_keyResp.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Probe.maxDurationReached:
            routineTimer.addTime(-Probe.maxDuration)
        elif Probe.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "ITI" ---
        # create an object to store info about Routine ITI
        ITI = data.Routine(
            name='ITI',
            components=[ITI_text],
        )
        ITI.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ITI
        ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ITI.tStart = globalClock.getTime(format='float')
        ITI.status = STARTED
        thisExp.addData('ITI.started', ITI.tStart)
        ITI.maxDuration = None
        # keep track of which components have finished
        ITIComponents = ITI.components
        for thisComponent in ITI.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ITI" ---
        # if trial has changed, end Routine now
        if isinstance(prac_trials, data.TrialHandler2) and thisPrac_trial.thisN != prac_trials.thisTrial.thisN:
            continueRoutine = False
        ITI.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ITI_text* updates
            
            # if ITI_text is starting this frame...
            if ITI_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ITI_text.frameNStart = frameN  # exact frame index
                ITI_text.tStart = t  # local t and not account for scr refresh
                ITI_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_text.started')
                # update status
                ITI_text.status = STARTED
                ITI_text.setAutoDraw(True)
            
            # if ITI_text is active this frame...
            if ITI_text.status == STARTED:
                # update params
                pass
            
            # if ITI_text is stopping this frame...
            if ITI_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_text.tStartRefresh + jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_text.tStop = t  # not accounting for scr refresh
                    ITI_text.tStopRefresh = tThisFlipGlobal  # on global time
                    ITI_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_text.stopped')
                    # update status
                    ITI_text.status = FINISHED
                    ITI_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ITI.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITI.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITI.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ITI
        ITI.tStop = globalClock.getTime(format='float')
        ITI.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ITI.stopped', ITI.tStop)
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'prac_trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "Practice_end" ---
    # create an object to store info about Routine Practice_end
    Practice_end = data.Routine(
        name='Practice_end',
        components=[practice_continue_text, pracend_keyResp],
    )
    Practice_end.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    practice_continue_text.setText("That is the end of the practice! Your accuracy was " + str(corr) + "/6.\n\nPress <SPACE> to continue!")
    # create starting attributes for pracend_keyResp
    pracend_keyResp.keys = []
    pracend_keyResp.rt = []
    _pracend_keyResp_allKeys = []
    # store start times for Practice_end
    Practice_end.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Practice_end.tStart = globalClock.getTime(format='float')
    Practice_end.status = STARTED
    thisExp.addData('Practice_end.started', Practice_end.tStart)
    Practice_end.maxDuration = None
    # keep track of which components have finished
    Practice_endComponents = Practice_end.components
    for thisComponent in Practice_end.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Practice_end" ---
    Practice_end.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_continue_text* updates
        
        # if practice_continue_text is starting this frame...
        if practice_continue_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_continue_text.frameNStart = frameN  # exact frame index
            practice_continue_text.tStart = t  # local t and not account for scr refresh
            practice_continue_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_continue_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_continue_text.started')
            # update status
            practice_continue_text.status = STARTED
            practice_continue_text.setAutoDraw(True)
        
        # if practice_continue_text is active this frame...
        if practice_continue_text.status == STARTED:
            # update params
            pass
        
        # *pracend_keyResp* updates
        waitOnFlip = False
        
        # if pracend_keyResp is starting this frame...
        if pracend_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracend_keyResp.frameNStart = frameN  # exact frame index
            pracend_keyResp.tStart = t  # local t and not account for scr refresh
            pracend_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracend_keyResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pracend_keyResp.started')
            # update status
            pracend_keyResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(pracend_keyResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(pracend_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if pracend_keyResp.status == STARTED and not waitOnFlip:
            theseKeys = pracend_keyResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _pracend_keyResp_allKeys.extend(theseKeys)
            if len(_pracend_keyResp_allKeys):
                pracend_keyResp.keys = _pracend_keyResp_allKeys[-1].name  # just the last key pressed
                pracend_keyResp.rt = _pracend_keyResp_allKeys[-1].rt
                pracend_keyResp.duration = _pracend_keyResp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Practice_end.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_end.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Practice_end" ---
    for thisComponent in Practice_end.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Practice_end
    Practice_end.tStop = globalClock.getTime(format='float')
    Practice_end.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Practice_end.stopped', Practice_end.tStop)
    # check responses
    if pracend_keyResp.keys in ['', [], None]:  # No response was made
        pracend_keyResp.keys = None
    thisExp.addData('pracend_keyResp.keys',pracend_keyResp.keys)
    if pracend_keyResp.keys != None:  # we had a response
        thisExp.addData('pracend_keyResp.rt', pracend_keyResp.rt)
        thisExp.addData('pracend_keyResp.duration', pracend_keyResp.duration)
    thisExp.nextEntry()
    # the Routine "Practice_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Main_exp_begin" ---
    # create an object to store info about Routine Main_exp_begin
    Main_exp_begin = data.Routine(
        name='Main_exp_begin',
        components=[mainexp_begin_text, main_exp_begin],
    )
    Main_exp_begin.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for main_exp_begin
    main_exp_begin.keys = []
    main_exp_begin.rt = []
    _main_exp_begin_allKeys = []
    # store start times for Main_exp_begin
    Main_exp_begin.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Main_exp_begin.tStart = globalClock.getTime(format='float')
    Main_exp_begin.status = STARTED
    thisExp.addData('Main_exp_begin.started', Main_exp_begin.tStart)
    Main_exp_begin.maxDuration = None
    # keep track of which components have finished
    Main_exp_beginComponents = Main_exp_begin.components
    for thisComponent in Main_exp_begin.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Main_exp_begin" ---
    Main_exp_begin.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mainexp_begin_text* updates
        
        # if mainexp_begin_text is starting this frame...
        if mainexp_begin_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mainexp_begin_text.frameNStart = frameN  # exact frame index
            mainexp_begin_text.tStart = t  # local t and not account for scr refresh
            mainexp_begin_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mainexp_begin_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'mainexp_begin_text.started')
            # update status
            mainexp_begin_text.status = STARTED
            mainexp_begin_text.setAutoDraw(True)
        
        # if mainexp_begin_text is active this frame...
        if mainexp_begin_text.status == STARTED:
            # update params
            pass
        
        # *main_exp_begin* updates
        waitOnFlip = False
        
        # if main_exp_begin is starting this frame...
        if main_exp_begin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            main_exp_begin.frameNStart = frameN  # exact frame index
            main_exp_begin.tStart = t  # local t and not account for scr refresh
            main_exp_begin.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_exp_begin, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'main_exp_begin.started')
            # update status
            main_exp_begin.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(main_exp_begin.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(main_exp_begin.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if main_exp_begin.status == STARTED and not waitOnFlip:
            theseKeys = main_exp_begin.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
            _main_exp_begin_allKeys.extend(theseKeys)
            if len(_main_exp_begin_allKeys):
                main_exp_begin.keys = _main_exp_begin_allKeys[-1].name  # just the last key pressed
                main_exp_begin.rt = _main_exp_begin_allKeys[-1].rt
                main_exp_begin.duration = _main_exp_begin_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Main_exp_begin.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Main_exp_begin.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Main_exp_begin" ---
    for thisComponent in Main_exp_begin.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Main_exp_begin
    Main_exp_begin.tStop = globalClock.getTime(format='float')
    Main_exp_begin.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Main_exp_begin.stopped', Main_exp_begin.tStop)
    # check responses
    if main_exp_begin.keys in ['', [], None]:  # No response was made
        main_exp_begin.keys = None
    thisExp.addData('main_exp_begin.keys',main_exp_begin.keys)
    if main_exp_begin.keys != None:  # we had a response
        thisExp.addData('main_exp_begin.rt', main_exp_begin.rt)
        thisExp.addData('main_exp_begin.duration', main_exp_begin.duration)
    thisExp.nextEntry()
    # the Routine "Main_exp_begin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Trial_prepare" ---
    # create an object to store info about Routine Trial_prepare
    Trial_prepare = data.Routine(
        name='Trial_prepare',
        components=[Trial_prepare_text],
    )
    Trial_prepare.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for Trial_prepare
    Trial_prepare.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Trial_prepare.tStart = globalClock.getTime(format='float')
    Trial_prepare.status = STARTED
    thisExp.addData('Trial_prepare.started', Trial_prepare.tStart)
    Trial_prepare.maxDuration = None
    # keep track of which components have finished
    Trial_prepareComponents = Trial_prepare.components
    for thisComponent in Trial_prepare.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial_prepare" ---
    Trial_prepare.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Trial_prepare_text* updates
        
        # if Trial_prepare_text is starting this frame...
        if Trial_prepare_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Trial_prepare_text.frameNStart = frameN  # exact frame index
            Trial_prepare_text.tStart = t  # local t and not account for scr refresh
            Trial_prepare_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_prepare_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_prepare_text.started')
            # update status
            Trial_prepare_text.status = STARTED
            Trial_prepare_text.setAutoDraw(True)
        
        # if Trial_prepare_text is active this frame...
        if Trial_prepare_text.status == STARTED:
            # update params
            Trial_prepare_text.setText(f"The trial will begin in {5 - t:.0f} s.", log=False)
        
        # if Trial_prepare_text is stopping this frame...
        if Trial_prepare_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Trial_prepare_text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                Trial_prepare_text.tStop = t  # not accounting for scr refresh
                Trial_prepare_text.tStopRefresh = tThisFlipGlobal  # on global time
                Trial_prepare_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Trial_prepare_text.stopped')
                # update status
                Trial_prepare_text.status = FINISHED
                Trial_prepare_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Trial_prepare.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial_prepare.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial_prepare" ---
    for thisComponent in Trial_prepare.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Trial_prepare
    Trial_prepare.tStop = globalClock.getTime(format='float')
    Trial_prepare.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Trial_prepare.stopped', Trial_prepare.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Trial_prepare.maxDurationReached:
        routineTimer.addTime(-Trial_prepare.maxDuration)
    elif Trial_prepare.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(stim_list), 
        seed=None, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "Encode" ---
        # create an object to store info about Routine Encode
        Encode = data.Routine(
            name='Encode',
            components=[encode_fixation, img_1_left, img_2_right],
        )
        Encode.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        img_1_left.setImage(encode_1_img)
        img_2_right.setImage(encode_2_img)
        # store start times for Encode
        Encode.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Encode.tStart = globalClock.getTime(format='float')
        Encode.status = STARTED
        thisExp.addData('Encode.started', Encode.tStart)
        Encode.maxDuration = None
        # keep track of which components have finished
        EncodeComponents = Encode.components
        for thisComponent in Encode.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Encode" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        Encode.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *encode_fixation* updates
            
            # if encode_fixation is starting this frame...
            if encode_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                encode_fixation.frameNStart = frameN  # exact frame index
                encode_fixation.tStart = t  # local t and not account for scr refresh
                encode_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(encode_fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'encode_fixation.started')
                # update status
                encode_fixation.status = STARTED
                encode_fixation.setAutoDraw(True)
            
            # if encode_fixation is active this frame...
            if encode_fixation.status == STARTED:
                # update params
                pass
            
            # if encode_fixation is stopping this frame...
            if encode_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > encode_fixation.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    encode_fixation.tStop = t  # not accounting for scr refresh
                    encode_fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    encode_fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'encode_fixation.stopped')
                    # update status
                    encode_fixation.status = FINISHED
                    encode_fixation.setAutoDraw(False)
            
            # *img_1_left* updates
            
            # if img_1_left is starting this frame...
            if img_1_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img_1_left.frameNStart = frameN  # exact frame index
                img_1_left.tStart = t  # local t and not account for scr refresh
                img_1_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img_1_left, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'img_1_left.started')
                # update status
                img_1_left.status = STARTED
                img_1_left.setAutoDraw(True)
            
            # if img_1_left is active this frame...
            if img_1_left.status == STARTED:
                # update params
                pass
            
            # if img_1_left is stopping this frame...
            if img_1_left.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > img_1_left.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    img_1_left.tStop = t  # not accounting for scr refresh
                    img_1_left.tStopRefresh = tThisFlipGlobal  # on global time
                    img_1_left.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'img_1_left.stopped')
                    # update status
                    img_1_left.status = FINISHED
                    img_1_left.setAutoDraw(False)
            
            # *img_2_right* updates
            
            # if img_2_right is starting this frame...
            if img_2_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                img_2_right.frameNStart = frameN  # exact frame index
                img_2_right.tStart = t  # local t and not account for scr refresh
                img_2_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img_2_right, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'img_2_right.started')
                # update status
                img_2_right.status = STARTED
                img_2_right.setAutoDraw(True)
            
            # if img_2_right is active this frame...
            if img_2_right.status == STARTED:
                # update params
                pass
            
            # if img_2_right is stopping this frame...
            if img_2_right.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > img_2_right.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    img_2_right.tStop = t  # not accounting for scr refresh
                    img_2_right.tStopRefresh = tThisFlipGlobal  # on global time
                    img_2_right.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'img_2_right.stopped')
                    # update status
                    img_2_right.status = FINISHED
                    img_2_right.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Encode.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Encode.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Encode" ---
        for thisComponent in Encode.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Encode
        Encode.tStop = globalClock.getTime(format='float')
        Encode.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Encode.stopped', Encode.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Encode.maxDurationReached:
            routineTimer.addTime(-Encode.maxDuration)
        elif Encode.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "Delay_2000" ---
        # create an object to store info about Routine Delay_2000
        Delay_2000 = data.Routine(
            name='Delay_2000',
            components=[delay_fixation_2000],
        )
        Delay_2000.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for Delay_2000
        Delay_2000.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Delay_2000.tStart = globalClock.getTime(format='float')
        Delay_2000.status = STARTED
        thisExp.addData('Delay_2000.started', Delay_2000.tStart)
        Delay_2000.maxDuration = None
        # keep track of which components have finished
        Delay_2000Components = Delay_2000.components
        for thisComponent in Delay_2000.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Delay_2000" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        Delay_2000.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *delay_fixation_2000* updates
            
            # if delay_fixation_2000 is starting this frame...
            if delay_fixation_2000.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                delay_fixation_2000.frameNStart = frameN  # exact frame index
                delay_fixation_2000.tStart = t  # local t and not account for scr refresh
                delay_fixation_2000.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(delay_fixation_2000, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'delay_fixation_2000.started')
                # update status
                delay_fixation_2000.status = STARTED
                delay_fixation_2000.setAutoDraw(True)
            
            # if delay_fixation_2000 is active this frame...
            if delay_fixation_2000.status == STARTED:
                # update params
                pass
            
            # if delay_fixation_2000 is stopping this frame...
            if delay_fixation_2000.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > delay_fixation_2000.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    delay_fixation_2000.tStop = t  # not accounting for scr refresh
                    delay_fixation_2000.tStopRefresh = tThisFlipGlobal  # on global time
                    delay_fixation_2000.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'delay_fixation_2000.stopped')
                    # update status
                    delay_fixation_2000.status = FINISHED
                    delay_fixation_2000.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Delay_2000.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Delay_2000.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Delay_2000" ---
        for thisComponent in Delay_2000.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Delay_2000
        Delay_2000.tStop = globalClock.getTime(format='float')
        Delay_2000.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Delay_2000.stopped', Delay_2000.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Delay_2000.maxDurationReached:
            routineTimer.addTime(-Delay_2000.maxDuration)
        elif Delay_2000.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "Manipulate" ---
        # create an object to store info about Routine Manipulate
        Manipulate = data.Routine(
            name='Manipulate',
            components=[manipulate_cue, manipulate_fixation],
        )
        Manipulate.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from cue_position_code
        if cue_position == "left":
            cuepos = (-0.3, 0)
        elif cue_position == "right":
            cuepos = (0.3, 0)
        print("cue_position = ", cue_position)
        manipulate_cue.setPos(cuepos)
        manipulate_cue.setImage(replace_img)
        # store start times for Manipulate
        Manipulate.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Manipulate.tStart = globalClock.getTime(format='float')
        Manipulate.status = STARTED
        thisExp.addData('Manipulate.started', Manipulate.tStart)
        Manipulate.maxDuration = None
        # keep track of which components have finished
        ManipulateComponents = Manipulate.components
        for thisComponent in Manipulate.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Manipulate" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        Manipulate.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *manipulate_cue* updates
            
            # if manipulate_cue is starting this frame...
            if manipulate_cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                manipulate_cue.frameNStart = frameN  # exact frame index
                manipulate_cue.tStart = t  # local t and not account for scr refresh
                manipulate_cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(manipulate_cue, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'manipulate_cue.started')
                # update status
                manipulate_cue.status = STARTED
                manipulate_cue.setAutoDraw(True)
            
            # if manipulate_cue is active this frame...
            if manipulate_cue.status == STARTED:
                # update params
                pass
            
            # if manipulate_cue is stopping this frame...
            if manipulate_cue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > manipulate_cue.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    manipulate_cue.tStop = t  # not accounting for scr refresh
                    manipulate_cue.tStopRefresh = tThisFlipGlobal  # on global time
                    manipulate_cue.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'manipulate_cue.stopped')
                    # update status
                    manipulate_cue.status = FINISHED
                    manipulate_cue.setAutoDraw(False)
            
            # *manipulate_fixation* updates
            
            # if manipulate_fixation is starting this frame...
            if manipulate_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                manipulate_fixation.frameNStart = frameN  # exact frame index
                manipulate_fixation.tStart = t  # local t and not account for scr refresh
                manipulate_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(manipulate_fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'manipulate_fixation.started')
                # update status
                manipulate_fixation.status = STARTED
                manipulate_fixation.setAutoDraw(True)
            
            # if manipulate_fixation is active this frame...
            if manipulate_fixation.status == STARTED:
                # update params
                pass
            
            # if manipulate_fixation is stopping this frame...
            if manipulate_fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > manipulate_fixation.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    manipulate_fixation.tStop = t  # not accounting for scr refresh
                    manipulate_fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    manipulate_fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'manipulate_fixation.stopped')
                    # update status
                    manipulate_fixation.status = FINISHED
                    manipulate_fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Manipulate.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Manipulate.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Manipulate" ---
        for thisComponent in Manipulate.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Manipulate
        Manipulate.tStop = globalClock.getTime(format='float')
        Manipulate.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Manipulate.stopped', Manipulate.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Manipulate.maxDurationReached:
            routineTimer.addTime(-Manipulate.maxDuration)
        elif Manipulate.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "Delay_4000" ---
        # create an object to store info about Routine Delay_4000
        Delay_4000 = data.Routine(
            name='Delay_4000',
            components=[delay_fixation_4000],
        )
        Delay_4000.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for Delay_4000
        Delay_4000.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Delay_4000.tStart = globalClock.getTime(format='float')
        Delay_4000.status = STARTED
        thisExp.addData('Delay_4000.started', Delay_4000.tStart)
        Delay_4000.maxDuration = None
        # keep track of which components have finished
        Delay_4000Components = Delay_4000.components
        for thisComponent in Delay_4000.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Delay_4000" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        Delay_4000.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 4.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *delay_fixation_4000* updates
            
            # if delay_fixation_4000 is starting this frame...
            if delay_fixation_4000.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                delay_fixation_4000.frameNStart = frameN  # exact frame index
                delay_fixation_4000.tStart = t  # local t and not account for scr refresh
                delay_fixation_4000.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(delay_fixation_4000, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'delay_fixation_4000.started')
                # update status
                delay_fixation_4000.status = STARTED
                delay_fixation_4000.setAutoDraw(True)
            
            # if delay_fixation_4000 is active this frame...
            if delay_fixation_4000.status == STARTED:
                # update params
                pass
            
            # if delay_fixation_4000 is stopping this frame...
            if delay_fixation_4000.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > delay_fixation_4000.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    delay_fixation_4000.tStop = t  # not accounting for scr refresh
                    delay_fixation_4000.tStopRefresh = tThisFlipGlobal  # on global time
                    delay_fixation_4000.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'delay_fixation_4000.stopped')
                    # update status
                    delay_fixation_4000.status = FINISHED
                    delay_fixation_4000.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Delay_4000.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Delay_4000.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Delay_4000" ---
        for thisComponent in Delay_4000.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Delay_4000
        Delay_4000.tStop = globalClock.getTime(format='float')
        Delay_4000.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Delay_4000.stopped', Delay_4000.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Delay_4000.maxDurationReached:
            routineTimer.addTime(-Delay_4000.maxDuration)
        elif Delay_4000.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-4.000000)
        
        # --- Prepare to start Routine "Probe" ---
        # create an object to store info about Routine Probe
        Probe = data.Routine(
            name='Probe',
            components=[probe_image, probe_keyResp, yesKey_text, noKey_text],
        )
        Probe.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        print("probesubtype = ", probe_subtype)
        print("trial = ", trial_num)
        
        if probe_subtype in ["cued", "uncued", "replacement"]:
            correct_ans = "f"
        else:
            correct_ans = "j"
        probe_image.setImage(probe_img)
        # create starting attributes for probe_keyResp
        probe_keyResp.keys = []
        probe_keyResp.rt = []
        _probe_keyResp_allKeys = []
        # store start times for Probe
        Probe.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Probe.tStart = globalClock.getTime(format='float')
        Probe.status = STARTED
        thisExp.addData('Probe.started', Probe.tStart)
        Probe.maxDuration = None
        # keep track of which components have finished
        ProbeComponents = Probe.components
        for thisComponent in Probe.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Probe" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        Probe.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *probe_image* updates
            
            # if probe_image is starting this frame...
            if probe_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                probe_image.frameNStart = frameN  # exact frame index
                probe_image.tStart = t  # local t and not account for scr refresh
                probe_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'probe_image.started')
                # update status
                probe_image.status = STARTED
                probe_image.setAutoDraw(True)
            
            # if probe_image is active this frame...
            if probe_image.status == STARTED:
                # update params
                pass
            
            # if probe_image is stopping this frame...
            if probe_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > probe_image.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    probe_image.tStop = t  # not accounting for scr refresh
                    probe_image.tStopRefresh = tThisFlipGlobal  # on global time
                    probe_image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'probe_image.stopped')
                    # update status
                    probe_image.status = FINISHED
                    probe_image.setAutoDraw(False)
            
            # *probe_keyResp* updates
            waitOnFlip = False
            
            # if probe_keyResp is starting this frame...
            if probe_keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                probe_keyResp.frameNStart = frameN  # exact frame index
                probe_keyResp.tStart = t  # local t and not account for scr refresh
                probe_keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe_keyResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'probe_keyResp.started')
                # update status
                probe_keyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(probe_keyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(probe_keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if probe_keyResp is stopping this frame...
            if probe_keyResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > probe_keyResp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    probe_keyResp.tStop = t  # not accounting for scr refresh
                    probe_keyResp.tStopRefresh = tThisFlipGlobal  # on global time
                    probe_keyResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'probe_keyResp.stopped')
                    # update status
                    probe_keyResp.status = FINISHED
                    probe_keyResp.status = FINISHED
            if probe_keyResp.status == STARTED and not waitOnFlip:
                theseKeys = probe_keyResp.getKeys(keyList=['f', 'j'], ignoreKeys=["escape"], waitRelease=False)
                _probe_keyResp_allKeys.extend(theseKeys)
                if len(_probe_keyResp_allKeys):
                    probe_keyResp.keys = _probe_keyResp_allKeys[-1].name  # just the last key pressed
                    probe_keyResp.rt = _probe_keyResp_allKeys[-1].rt
                    probe_keyResp.duration = _probe_keyResp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *yesKey_text* updates
            
            # if yesKey_text is starting this frame...
            if yesKey_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                yesKey_text.frameNStart = frameN  # exact frame index
                yesKey_text.tStart = t  # local t and not account for scr refresh
                yesKey_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(yesKey_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'yesKey_text.started')
                # update status
                yesKey_text.status = STARTED
                yesKey_text.setAutoDraw(True)
            
            # if yesKey_text is active this frame...
            if yesKey_text.status == STARTED:
                # update params
                pass
            
            # if yesKey_text is stopping this frame...
            if yesKey_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > yesKey_text.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    yesKey_text.tStop = t  # not accounting for scr refresh
                    yesKey_text.tStopRefresh = tThisFlipGlobal  # on global time
                    yesKey_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'yesKey_text.stopped')
                    # update status
                    yesKey_text.status = FINISHED
                    yesKey_text.setAutoDraw(False)
            
            # *noKey_text* updates
            
            # if noKey_text is starting this frame...
            if noKey_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                noKey_text.frameNStart = frameN  # exact frame index
                noKey_text.tStart = t  # local t and not account for scr refresh
                noKey_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noKey_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'noKey_text.started')
                # update status
                noKey_text.status = STARTED
                noKey_text.setAutoDraw(True)
            
            # if noKey_text is active this frame...
            if noKey_text.status == STARTED:
                # update params
                pass
            
            # if noKey_text is stopping this frame...
            if noKey_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noKey_text.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    noKey_text.tStop = t  # not accounting for scr refresh
                    noKey_text.tStopRefresh = tThisFlipGlobal  # on global time
                    noKey_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'noKey_text.stopped')
                    # update status
                    noKey_text.status = FINISHED
                    noKey_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Probe.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Probe.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Probe" ---
        for thisComponent in Probe.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Probe
        Probe.tStop = globalClock.getTime(format='float')
        Probe.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Probe.stopped', Probe.tStop)
        # Run 'End Routine' code from code
        keypressed = _probe_keyResp_allKeys[-1].name
        if keypressed == correct_ans:
            print("correct!")
            corr += 1
        # check responses
        if probe_keyResp.keys in ['', [], None]:  # No response was made
            probe_keyResp.keys = None
        trials.addData('probe_keyResp.keys',probe_keyResp.keys)
        if probe_keyResp.keys != None:  # we had a response
            trials.addData('probe_keyResp.rt', probe_keyResp.rt)
            trials.addData('probe_keyResp.duration', probe_keyResp.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Probe.maxDurationReached:
            routineTimer.addTime(-Probe.maxDuration)
        elif Probe.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "ITI" ---
        # create an object to store info about Routine ITI
        ITI = data.Routine(
            name='ITI',
            components=[ITI_text],
        )
        ITI.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ITI
        ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ITI.tStart = globalClock.getTime(format='float')
        ITI.status = STARTED
        thisExp.addData('ITI.started', ITI.tStart)
        ITI.maxDuration = None
        # keep track of which components have finished
        ITIComponents = ITI.components
        for thisComponent in ITI.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ITI" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        ITI.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ITI_text* updates
            
            # if ITI_text is starting this frame...
            if ITI_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ITI_text.frameNStart = frameN  # exact frame index
                ITI_text.tStart = t  # local t and not account for scr refresh
                ITI_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_text.started')
                # update status
                ITI_text.status = STARTED
                ITI_text.setAutoDraw(True)
            
            # if ITI_text is active this frame...
            if ITI_text.status == STARTED:
                # update params
                pass
            
            # if ITI_text is stopping this frame...
            if ITI_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_text.tStartRefresh + jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_text.tStop = t  # not accounting for scr refresh
                    ITI_text.tStopRefresh = tThisFlipGlobal  # on global time
                    ITI_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_text.stopped')
                    # update status
                    ITI_text.status = FINISHED
                    ITI_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                ITI.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITI.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITI.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ITI
        ITI.tStop = globalClock.getTime(format='float')
        ITI.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ITI.stopped', ITI.tStop)
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        rest_loop = data.TrialHandler2(
            name='rest_loop',
            nReps=rest_trigger, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(rest_loop)  # add the loop to the experiment
        thisRest_loop = rest_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisRest_loop.rgb)
        if thisRest_loop != None:
            for paramName in thisRest_loop:
                globals()[paramName] = thisRest_loop[paramName]
        
        for thisRest_loop in rest_loop:
            currentLoop = rest_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisRest_loop.rgb)
            if thisRest_loop != None:
                for paramName in thisRest_loop:
                    globals()[paramName] = thisRest_loop[paramName]
            
            # --- Prepare to start Routine "Rest" ---
            # create an object to store info about Routine Rest
            Rest = data.Routine(
                name='Rest',
                components=[rest_welcome, rest_continue, rest_continue_text],
            )
            Rest.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for rest_continue
            rest_continue.keys = []
            rest_continue.rt = []
            _rest_continue_allKeys = []
            # store start times for Rest
            Rest.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Rest.tStart = globalClock.getTime(format='float')
            Rest.status = STARTED
            thisExp.addData('Rest.started', Rest.tStart)
            Rest.maxDuration = None
            # keep track of which components have finished
            RestComponents = Rest.components
            for thisComponent in Rest.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Rest" ---
            # if trial has changed, end Routine now
            if isinstance(rest_loop, data.TrialHandler2) and thisRest_loop.thisN != rest_loop.thisTrial.thisN:
                continueRoutine = False
            Rest.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 30.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *rest_welcome* updates
                
                # if rest_welcome is starting this frame...
                if rest_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rest_welcome.frameNStart = frameN  # exact frame index
                    rest_welcome.tStart = t  # local t and not account for scr refresh
                    rest_welcome.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rest_welcome, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rest_welcome.started')
                    # update status
                    rest_welcome.status = STARTED
                    rest_welcome.setAutoDraw(True)
                
                # if rest_welcome is active this frame...
                if rest_welcome.status == STARTED:
                    # update params
                    rest_welcome.setText(f"Rest!\n\nGreat job completing the run! You have completed {run_num} out of 6 runs. You may now take a {30 - t:.0f} second break!", log=False)
                
                # if rest_welcome is stopping this frame...
                if rest_welcome.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rest_welcome.tStartRefresh + 30-frameTolerance:
                        # keep track of stop time/frame for later
                        rest_welcome.tStop = t  # not accounting for scr refresh
                        rest_welcome.tStopRefresh = tThisFlipGlobal  # on global time
                        rest_welcome.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'rest_welcome.stopped')
                        # update status
                        rest_welcome.status = FINISHED
                        rest_welcome.setAutoDraw(False)
                
                # *rest_continue* updates
                waitOnFlip = False
                
                # if rest_continue is starting this frame...
                if rest_continue.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
                    # keep track of start time/frame for later
                    rest_continue.frameNStart = frameN  # exact frame index
                    rest_continue.tStart = t  # local t and not account for scr refresh
                    rest_continue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rest_continue, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rest_continue.started')
                    # update status
                    rest_continue.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(rest_continue.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(rest_continue.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if rest_continue is stopping this frame...
                if rest_continue.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 30-frameTolerance:
                        # keep track of stop time/frame for later
                        rest_continue.tStop = t  # not accounting for scr refresh
                        rest_continue.tStopRefresh = tThisFlipGlobal  # on global time
                        rest_continue.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'rest_continue.stopped')
                        # update status
                        rest_continue.status = FINISHED
                        rest_continue.status = FINISHED
                if rest_continue.status == STARTED and not waitOnFlip:
                    theseKeys = rest_continue.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _rest_continue_allKeys.extend(theseKeys)
                    if len(_rest_continue_allKeys):
                        rest_continue.keys = _rest_continue_allKeys[-1].name  # just the last key pressed
                        rest_continue.rt = _rest_continue_allKeys[-1].rt
                        rest_continue.duration = _rest_continue_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # *rest_continue_text* updates
                
                # if rest_continue_text is starting this frame...
                if rest_continue_text.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
                    # keep track of start time/frame for later
                    rest_continue_text.frameNStart = frameN  # exact frame index
                    rest_continue_text.tStart = t  # local t and not account for scr refresh
                    rest_continue_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rest_continue_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'rest_continue_text.started')
                    # update status
                    rest_continue_text.status = STARTED
                    rest_continue_text.setAutoDraw(True)
                
                # if rest_continue_text is active this frame...
                if rest_continue_text.status == STARTED:
                    # update params
                    pass
                
                # if rest_continue_text is stopping this frame...
                if rest_continue_text.status == STARTED:
                    # is it time to stop? (based on local clock)
                    if tThisFlip > 30-frameTolerance:
                        # keep track of stop time/frame for later
                        rest_continue_text.tStop = t  # not accounting for scr refresh
                        rest_continue_text.tStopRefresh = tThisFlipGlobal  # on global time
                        rest_continue_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'rest_continue_text.stopped')
                        # update status
                        rest_continue_text.status = FINISHED
                        rest_continue_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Rest.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Rest.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Rest" ---
            for thisComponent in Rest.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Rest
            Rest.tStop = globalClock.getTime(format='float')
            Rest.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Rest.stopped', Rest.tStop)
            # check responses
            if rest_continue.keys in ['', [], None]:  # No response was made
                rest_continue.keys = None
            rest_loop.addData('rest_continue.keys',rest_continue.keys)
            if rest_continue.keys != None:  # we had a response
                rest_loop.addData('rest_continue.rt', rest_continue.rt)
                rest_loop.addData('rest_continue.duration', rest_continue.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Rest.maxDurationReached:
                routineTimer.addTime(-Rest.maxDuration)
            elif Rest.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-30.000000)
            
            # --- Prepare to start Routine "Trial_prepare" ---
            # create an object to store info about Routine Trial_prepare
            Trial_prepare = data.Routine(
                name='Trial_prepare',
                components=[Trial_prepare_text],
            )
            Trial_prepare.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for Trial_prepare
            Trial_prepare.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Trial_prepare.tStart = globalClock.getTime(format='float')
            Trial_prepare.status = STARTED
            thisExp.addData('Trial_prepare.started', Trial_prepare.tStart)
            Trial_prepare.maxDuration = None
            # keep track of which components have finished
            Trial_prepareComponents = Trial_prepare.components
            for thisComponent in Trial_prepare.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Trial_prepare" ---
            # if trial has changed, end Routine now
            if isinstance(rest_loop, data.TrialHandler2) and thisRest_loop.thisN != rest_loop.thisTrial.thisN:
                continueRoutine = False
            Trial_prepare.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 5.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Trial_prepare_text* updates
                
                # if Trial_prepare_text is starting this frame...
                if Trial_prepare_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Trial_prepare_text.frameNStart = frameN  # exact frame index
                    Trial_prepare_text.tStart = t  # local t and not account for scr refresh
                    Trial_prepare_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Trial_prepare_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Trial_prepare_text.started')
                    # update status
                    Trial_prepare_text.status = STARTED
                    Trial_prepare_text.setAutoDraw(True)
                
                # if Trial_prepare_text is active this frame...
                if Trial_prepare_text.status == STARTED:
                    # update params
                    Trial_prepare_text.setText(f"The trial will begin in {5 - t:.0f} s.", log=False)
                
                # if Trial_prepare_text is stopping this frame...
                if Trial_prepare_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Trial_prepare_text.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        Trial_prepare_text.tStop = t  # not accounting for scr refresh
                        Trial_prepare_text.tStopRefresh = tThisFlipGlobal  # on global time
                        Trial_prepare_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Trial_prepare_text.stopped')
                        # update status
                        Trial_prepare_text.status = FINISHED
                        Trial_prepare_text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Trial_prepare.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Trial_prepare.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Trial_prepare" ---
            for thisComponent in Trial_prepare.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Trial_prepare
            Trial_prepare.tStop = globalClock.getTime(format='float')
            Trial_prepare.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Trial_prepare.stopped', Trial_prepare.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Trial_prepare.maxDurationReached:
                routineTimer.addTime(-Trial_prepare.maxDuration)
            elif Trial_prepare.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-5.000000)
        # completed rest_trigger repeats of 'rest_loop'
        
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "Debrief" ---
    # create an object to store info about Routine Debrief
    Debrief = data.Routine(
        name='Debrief',
        components=[debrief_text],
    )
    Debrief.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for Debrief
    Debrief.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Debrief.tStart = globalClock.getTime(format='float')
    Debrief.status = STARTED
    thisExp.addData('Debrief.started', Debrief.tStart)
    Debrief.maxDuration = None
    # keep track of which components have finished
    DebriefComponents = Debrief.components
    for thisComponent in Debrief.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Debrief" ---
    Debrief.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 180.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *debrief_text* updates
        
        # if debrief_text is starting this frame...
        if debrief_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            debrief_text.frameNStart = frameN  # exact frame index
            debrief_text.tStart = t  # local t and not account for scr refresh
            debrief_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(debrief_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'debrief_text.started')
            # update status
            debrief_text.status = STARTED
            debrief_text.setAutoDraw(True)
        
        # if debrief_text is active this frame...
        if debrief_text.status == STARTED:
            # update params
            pass
        
        # if debrief_text is stopping this frame...
        if debrief_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > debrief_text.tStartRefresh + 180-frameTolerance:
                # keep track of stop time/frame for later
                debrief_text.tStop = t  # not accounting for scr refresh
                debrief_text.tStopRefresh = tThisFlipGlobal  # on global time
                debrief_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'debrief_text.stopped')
                # update status
                debrief_text.status = FINISHED
                debrief_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Debrief.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Debrief.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Debrief" ---
    for thisComponent in Debrief.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Debrief
    Debrief.tStop = globalClock.getTime(format='float')
    Debrief.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Debrief.stopped', Debrief.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Debrief.maxDurationReached:
        routineTimer.addTime(-Debrief.maxDuration)
    elif Debrief.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-180.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
