import numpy as np
import pandas as pd
from datetime import datetime
import os
import seaborn as sns
import matplotlib.pyplot as plt


class ParticipantData(object):
    def __init__(self, path, num_trials=144, participant=None):
        df = pd.read_csv(path)
        # Capture participant identifier information
        self.participant = participant or int(df['participant'].unique()[0])
        # Capture design iteration
        self.date = self.extract_date(df)
        # Save the number of trials
        self.num_trials = num_trials
        # Initiate the check attribute
        self.pass_check = True
        # Extract only the relevant data
        self.wm_df = self.filter_wm(df)
        self.wm_df = self.wm_df.rename(columns={"probe_keyResp.keys": "response", "probe_keyResp.rt": "rt"})
        # Process the wm_df, adding helper columns and extracting metrics
        self.wm_df["correct_ans"] = ["f" if r.probe_subtype in ["uncued", "cued", "replacement"] else "j" for _, r in self.wm_df.iterrows()]
        self.wm_df["correct"] = self.wm_df["response"] == self.wm_df["correct_ans"]

    def __len__(self):
        return self.wm_df.shape[0]

    def extract_date(self, df):
        date_str = df.date.unique().item()
        return datetime.strptime(date_str, "%Y-%m-%d_%Hh%M.%S.%f")

    def filter_wm(self, df):
        try:
            return df[(df.run_num != "practice") & (~df["Encode.started"].isna())].copy(deep=True).reset_index(drop=True)
        except:
            print(f"WARNING: could not filter wm for participant {self.participant}")
            self.pass_check = False
            return

    def extract_wm(self, save_data=False):
        self.wm_df["participant"] = self.participant
        ret_list = ["participant",
                    "encode_1_cat", "encode_2_cat", "operation", "replace_cat",
                    "cue_position", "probe_subtype",
                    "correct_ans", "correct",
                    "response", "rt",
                    "encode_1_img", "encode_2_img", "replace_img", "probe_img",
                    "run_num", "jitter",
                    ]
        extracted_wm = self.wm_df[ret_list].copy(deep=True)
        # if save_data:
        #     extracted_wm.to_csv(os.path.join(self.subdirectory_path, f"{self.participant}_main_beh_data.csv"))
        return extracted_wm

    def incomplete(self):
        return self.__len__() < self.num_trials if self.pass_check else True

    def p_omissions(self):
        return self.wm_df.response.isna().sum() / self.num_trials if self.pass_check else 1

    def tot_accuracy(self):
        return np.mean(self.wm_df["correct"]) if self.pass_check else 0


class MasterDF(object):
    operation_conditions = ["maintain", "suppress", "replace"]
    probe_conditions = ["cued", "uncued", "replacement", "lure", "novel"]
    def __init__(self, p_data_list: list, excl_criteria: dict = None):
        """
        :param p_data_list: a list of ParticipantData objects
        :param excl_criteria: criteria to exclude from the analysis. Must include:
                    - "o-threshold": omission threshold out of 1
                    - "a-threshold": accuracy threshold out of 1
        """
        self.p_data_list = p_data_list
        self.excluded_list = []
        # extract the master dataframe
        self.mdf = self.extract_mdf(self.p_data_list, excl_criteria=excl_criteria)

    def n_participants(self):
        return self.mdf["participant"].nunique()

    def mean_accuracy(self):
        return np.mean([data.tot_accuracy() for data in self.p_data_list if data.participant not in self.excluded_list])

    def corr(self):
        return self.mdf[self.mdf.correct == True]

    def check_participant(self, data: ParticipantData, excl_criteria=None, save_ID=True):
        if excl_criteria is None:
            excl_criteria = {"o_threshold": 0.15, "a_threshold": 0.7}
        criteria = [data.p_omissions() > excl_criteria["o_threshold"],
                    data.tot_accuracy() < excl_criteria["a_threshold"],
                    data.incomplete(),
                    ]
        if (not data.pass_check) or any(criteria):
            if save_ID and data.participant not in self.excluded_list:
                self.excluded_list.append(data.participant)
            return None
        else:
            return data.extract_wm()

    def extract_mdf(self, p_data_list: list, excl_criteria: dict = None):
        mdf_list = []
        if excl_criteria is None:
            excl_criteria = {"o_threshold": 0.15, "a_threshold": 0.7}
        for data in p_data_list:
            mdf_list.append(self.check_participant(data, excl_criteria=excl_criteria, save_ID=True)) #, **version_criteria[data.version]))
        return pd.concat(mdf_list, ignore_index=True)

    # def subselect(self, semantic_cond, operation, probe_cond, n):
    #     t_df = pd.DataFrame()
    #     df = self.mdf[(self.mdf.semantic_cond == semantic_cond) & \
    #                   (self.mdf.operation == operation) & \
    #                   (self.mdf.probe_cond == probe_cond)
    #                   ]
    #     for participant in df.participant.unique():
    #         t_df = pd.concat([t_df, df[df.participant == participant].sample(n=n)])
    #     return t_df
    #
    # def balance_corr(self):
    #     corr_df = self.mdf[self.mdf.correct]
    #     corr_df = corr_df.groupby(["participant", "semantic_cond", "operation", "probe_cond"]).count().reset_index()
    #     p_list = self.find_unbalanced(corr_df)
    #     return self.mdf[~self.mdf.participant.isin(p_list)]


def vis_compare(data=None, y=None, x="operation", hue="probe_subtype", cut=0,
                type="box", swarm=False, order=None, hue_order=None, ylim=None,
                custom_colors=False,
                **kwargs):
        """
        Visualizes comparison df
        y: default=None. {"RT", "accuracy"}
        """
        sns.set_theme(style="dark")
        if custom_colors:
            colors = {"maintain": "forestgreen", "suppress": "firebrick", "replace": "navy",
                      "cued": "darkblue", "uncued": "darkorange", "uncued_diff_category": "saddlebrown",
                      "manipulated": "royalblue", "unmanipulated": "skyblue",}
            dark_colors = {"manipulated": "darkblue", "unmanipulated": "deepskyblue",
                           "maintain": "springgreen", "suppress": "lightcoral",}
        else:
            colors = sns.color_palette("deep")
            dark_colors = sns.color_palette("dark")
        if swarm:
            ax = sns.swarmplot(data=data.groupby(["participant", "semantic_cond", "operation", "probe_cond", "cuc"]).mean(y).reset_index(),
                               x=x, y=y, hue=hue, dodge=True, size=2, palette=dark_colors, hue_order=hue_order)
        else:
            ax = None
        if type == "box":
            plot = sns.boxplot(data=data, x=x, y=y, hue=hue, whis=(5, 95), ax=ax, palette=colors, hue_order=hue_order)
        elif type == "violin":
            plot = sns.violinplot(data=data, x=x, y=y, hue=hue,
                                  split=True, fill=True, cut=cut, inner="quart", dodge=True,
                                  ax=ax, palette=colors)
        elif type == "bar":
            plot = sns.barplot(data=data, x=x, y=y, hue=hue, errorbar="ci", order=order, hue_order=hue_order, palette=colors)
            if y == "correct":
                plot.set(ylim=(ylim or(data.correct.min() - 0.1, 1)))
            elif y == "RT":
                plot.set(ylim=(ylim or (data.RT.mean() - 0.5, data.RT.mean() + 0.2)))
            else:
                plot.set(ylim=ylim)
        plot.set(xlabel=x, ylabel=y)
        return plot

data_dir = "data/online_pilot"
fig_dir = "figures/online_pilot"

# Initiate a list to store ParticipantData objects
p_data_list = []
for file in os.listdir(data_dir):
    if file.endswith(".csv"):
        p_data_list.append(ParticipantData(os.path.join(data_dir, file)))
# Load the participant data list into a MasterDF object
master = MasterDF(p_data_list)

# Get mean accuracy
print("N =", master.n_participants())
print("mean accuracy =", np.round(master.mean_accuracy(), 2))
print("N_excluded =", len(master.excluded_list))

# Visualize prelim
vis_compare(master.mdf,
            y="correct",
            ylim=(0.4, 1),
            type="bar",
            )
plt.title(f"Accuracy across different probes N={master.n_participants()}")
plt.savefig(f"{fig_dir}/acc.png")
plt.show()

vis_compare(master.corr(),
            y="rt",
            type="bar",
            ylim=(0.55, 1.2)
            )
plt.title(f"RT across different probes (correct responses only) N={master.n_participants()}")
plt.savefig(f"{fig_dir}/rt.png")
plt.show()

