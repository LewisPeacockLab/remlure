# Creates practice list
import pandas as pd
import numpy as np
import random

########################################################################
### The following code subselects practice stimuli from the novel stims for use in the practice list ###
# faces_filename = f"stimuli/csvs/main_task/faces_novelorig.csv"
# fruits_filename = f"stimuli/csvs/main_task/fruits_novelorig.csv"
# places_filename = f"stimuli/csvs/main_task/places_novelorig.csv"
#
# facesdf = pd.read_csv(faces_filename, header=None)
# fruitsdf = pd.read_csv(fruits_filename, header=None)
# placesdf = pd.read_csv(places_filename, header=None)
#
# faces_practice = []
# fruits_practice = []
# places_practice = []
#
# for n in range(3):
#     origl = [facesdf, fruitsdf, placesdf][n]
#     newl = [faces_practice, fruits_practice, places_practice][n]
#     shuffledl = np.random.permutation(origl[0].tolist()).tolist()
#     numpics = len(shuffledl) - 70
#     for i in range(numpics):
#         newl.append(shuffledl.pop())
#
# faces_limdf = pd.DataFrame([l for l in facesdf[0] if l not in faces_practice])
# fruits_limdf = pd.DataFrame([l for l in fruitsdf[0] if l not in fruits_practice])
# places_limdf = pd.DataFrame([l for l in placesdf[0] if l not in places_practice])
#
# faces_filename = f"stimuli/csvs/main_task/faces_novel.csv"
# fruits_filename = f"stimuli/csvs/main_task/fruits_novel.csv"
# places_filename = f"stimuli/csvs/main_task/places_novel.csv"
#
# faces_limdf.to_csv(faces_filename, header=False, index=False)
# fruits_limdf.to_csv(fruits_filename, header=False, index=False)
# places_limdf.to_csv(places_filename, header=False, index=False)
#
# pd.DataFrame(faces_practice).to_csv("stimuli/csvs/main_task/faces_practice.csv", header=False, index=False)
# pd.DataFrame(fruits_practice).to_csv("stimuli/csvs/main_task/fruits_practice.csv", header=False, index=False)
# pd.DataFrame(places_practice).to_csv("stimuli/csvs/main_task/places_practice.csv", header=False, index=False)
#
# Check to ensure that the stimlists do not utilize practice stimuli
# faces_filename = f"stimuli/csvs/main_task/faces_practice.csv"
# fruits_filename = f"stimuli/csvs/main_task/fruits_practice.csv"
# places_filename = f"stimuli/csvs/main_task/places_practice.csv"
# facesdf = pd.read_csv(faces_filename, header=None)
# fruitsdf = pd.read_csv(fruits_filename, header=None)
# placesdf = pd.read_csv(places_filename, header=None)
# praclist = []
# for l in [facesdf, fruitsdf, placesdf]:
#     praclist += l[0].tolist()
# for il in range(10):
#     mainTask_df_infile = f"stimuli/csvs/maintask_stimlists/main_stim_list_{il}.csv"
#     df = pd.read_csv(mainTask_df_infile)
#     print("filenum = ", il)
#     print("probesinprac = ", bool([l for l in df["probe_img"] if l in praclist]))
#     print([l for l in df["probe_img"] if l in praclist])

########################################################################
pracStims_df = pd.read_csv("archive/stimulus setup code/prac_stim_template.csv")

faces_praclist = pd.read_csv("archive/stim_csvs/faces_practice.csv", header=None)[0].tolist()
places_praclist = pd.read_csv("archive/stim_csvs/places_practice.csv", header=None)[0].tolist()
fruits_praclist = pd.read_csv("archive/stim_csvs/fruits_practice.csv", header=None)[0].tolist()

stims_dict = {"faces": np.random.permutation(faces_praclist).tolist(),
              "places": np.random.permutation(places_praclist).tolist(),
              "fruits": np.random.permutation(fruits_praclist).tolist(),}

opcue_dict = {"maintain": "stimuli/cues/maintain_cue_image.png",
              "suppress": "stimuli/cues/suppress_cue_image.png",}
# initiate the image list
image_list = []
# Perform the build chunked by run
for i, r in pracStims_df.iterrows():
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
        # Save the image into the dict
        images_dict[imgnum] = stims_dict[imgcat].pop()
    # Select a probe image
    if probe_pos is not None:
        probe_img = images_dict[probe_pos]
    else:
        probecat = np.random.choice([r.encode_1_cat, r.encode_2_cat])
        probe_img = stims_dict[probecat].pop()
    # Save the probe image
    images_dict["probe"] = probe_img
    # Save the image dict into the run image list
    image_list.append(images_dict)

# Add stims to df
pracStims_df["encode_1_img"] = [i["left"] for i in image_list]
pracStims_df["encode_2_img"] = [i["right"] for i in image_list]
pracStims_df["replace_img"] = [i["replacement"] for i in image_list]
pracStims_df["probe_img"] = [i["probe"] for i in image_list]

pracdf_infile = f"stimuli/csvs/maintask_stimlists/prac_stim_list.csv"
# Save to maintask folder
pracStims_df.to_csv(
    pracdf_infile , index=False
)


