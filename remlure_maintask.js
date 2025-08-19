/************************* 
 * Remlure_Maintask *
 *************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.2.2.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'remlure_maintask';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'phase': 'maintask',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from init_code
var set_num, stim_list;

set_num = Math.floor(Math.random() * 10).toString();

stim_list = 'stimuli/csvs/maintask_stimlists/main_stim_list_' + set_num + '.csv';

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WelcomeRoutineBegin());
flowScheduler.add(WelcomeRoutineEachFrame());
flowScheduler.add(WelcomeRoutineEnd());
flowScheduler.add(Encode_instructRoutineBegin());
flowScheduler.add(Encode_instructRoutineEachFrame());
flowScheduler.add(Encode_instructRoutineEnd());
flowScheduler.add(Oper_screen_instructRoutineBegin());
flowScheduler.add(Oper_screen_instructRoutineEachFrame());
flowScheduler.add(Oper_screen_instructRoutineEnd());
flowScheduler.add(Operations_instructRoutineBegin());
flowScheduler.add(Operations_instructRoutineEachFrame());
flowScheduler.add(Operations_instructRoutineEnd());
flowScheduler.add(Probe_screen_instructRoutineBegin());
flowScheduler.add(Probe_screen_instructRoutineEachFrame());
flowScheduler.add(Probe_screen_instructRoutineEnd());
flowScheduler.add(Probe_instructRoutineBegin());
flowScheduler.add(Probe_instructRoutineEachFrame());
flowScheduler.add(Probe_instructRoutineEnd());
flowScheduler.add(Practice_beginRoutineBegin());
flowScheduler.add(Practice_beginRoutineEachFrame());
flowScheduler.add(Practice_beginRoutineEnd());
flowScheduler.add(Trial_prepareRoutineBegin());
flowScheduler.add(Trial_prepareRoutineEachFrame());
flowScheduler.add(Trial_prepareRoutineEnd());
const prac_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(prac_trialsLoopBegin(prac_trialsLoopScheduler));
flowScheduler.add(prac_trialsLoopScheduler);
flowScheduler.add(prac_trialsLoopEnd);







flowScheduler.add(Practice_endRoutineBegin());
flowScheduler.add(Practice_endRoutineEachFrame());
flowScheduler.add(Practice_endRoutineEnd());
flowScheduler.add(Main_exp_beginRoutineBegin());
flowScheduler.add(Main_exp_beginRoutineEachFrame());
flowScheduler.add(Main_exp_beginRoutineEnd());
flowScheduler.add(Trial_prepareRoutineBegin());
flowScheduler.add(Trial_prepareRoutineEachFrame());
flowScheduler.add(Trial_prepareRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);











flowScheduler.add(DebriefRoutineBegin());
flowScheduler.add(DebriefRoutineEachFrame());
flowScheduler.add(DebriefRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'stimuli/csvs/maintask_stimlists/prac_stim_list.csv', 'path': 'stimuli/csvs/maintask_stimlists/prac_stim_list.csv'},
    {'name': 'stimuli/images/faces/michael_phelps.png', 'path': 'stimuli/images/faces/michael_phelps.png'},
    {'name': 'stimuli/images/places/river_bridge.png', 'path': 'stimuli/images/places/river_bridge.png'},
    {'name': 'stimuli/cues/maintain_cue_image.png', 'path': 'stimuli/cues/maintain_cue_image.png'},
    {'name': 'stimuli/images/faces/sandra_bullock.png', 'path': 'stimuli/images/faces/sandra_bullock.png'},
    {'name': 'stimuli/images/fruits/fresh_red_apple.png', 'path': 'stimuli/images/fruits/fresh_red_apple.png'},
    {'name': 'stimuli/images/fruits/pear04.png', 'path': 'stimuli/images/fruits/pear04.png'},
    {'name': 'stimuli/images/places/pink_sand_beach.png', 'path': 'stimuli/images/places/pink_sand_beach.png'},
    {'name': 'stimuli/images/fruits/muskmelon02.png', 'path': 'stimuli/images/fruits/muskmelon02.png'},
    {'name': 'stimuli/cues/suppress_cue_image.png', 'path': 'stimuli/cues/suppress_cue_image.png'},
    {'name': 'stimuli/images/fruits/honeydew.png', 'path': 'stimuli/images/fruits/honeydew.png'},
    {'name': 'stimuli/images/faces/maria_sharapova.png', 'path': 'stimuli/images/faces/maria_sharapova.png'},
    {'name': 'stimuli/images/fruits/sliced_honeydew.png', 'path': 'stimuli/images/fruits/sliced_honeydew.png'},
    {'name': 'stimuli/images/places/supreme_court.png', 'path': 'stimuli/images/places/supreme_court.png'},
    {'name': 'stimuli/images/faces/willie_nelson.png', 'path': 'stimuli/images/faces/willie_nelson.png'},
    {'name': 'stimuli/images/fruits/apple03a.png', 'path': 'stimuli/images/fruits/apple03a.png'},
    {'name': 'stimuli/images/places/japanese_castle.png', 'path': 'stimuli/images/places/japanese_castle.png'},
    {'name': 'stimuli/images/faces/queen_elizabeth_with_crown.png', 'path': 'stimuli/images/faces/queen_elizabeth_with_crown.png'},
    {'name': 'stimuli/images/fruits/half_apple.png', 'path': 'stimuli/images/fruits/half_apple.png'},
    {'name': 'instructions/encode_instructions.png', 'path': 'instructions/encode_instructions.png'},
    {'name': 'instructions/oper_screen_instructions.png', 'path': 'instructions/oper_screen_instructions.png'},
    {'name': 'instructions/operation_instructions.png', 'path': 'instructions/operation_instructions.png'},
    {'name': 'instructions/probe_screen_instructions.png', 'path': 'instructions/probe_screen_instructions.png'},
    {'name': 'instructions/probe_instructions.png', 'path': 'instructions/probe_instructions.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'instructions/probe_instructions.png', 'path': 'instructions/probe_instructions.png'},
    {'name': 'instructions/probe_screen_instructions.png', 'path': 'instructions/probe_screen_instructions.png'},
    {'name': 'instructions/operation_instructions.png', 'path': 'instructions/operation_instructions.png'},
    {'name': 'instructions/oper_screen_instructions.png', 'path': 'instructions/oper_screen_instructions.png'},
    {'name': 'instructions/encode_instructions.png', 'path': 'instructions/encode_instructions.png'},
    {'name': 'stimuli/csvs/maintask_stimlists/prac_stim_list.csv', 'path': 'stimuli/csvs/maintask_stimlists/prac_stim_list.csv'},
    {'name': 'stimuli/csvs/maintask_stimlists/main_stim_list_9.csv', 'path': 'stimuli/csvs/maintask_stimlists/main_stim_list_9.csv'},
    {'name': 'stimuli/csvs/maintask_stimlists/main_stim_list_8.csv', 'path': 'stimuli/csvs/maintask_stimlists/main_stim_list_8.csv'},
    {'name': 'stimuli/csvs/maintask_stimlists/main_stim_list_7.csv', 'path': 'stimuli/csvs/maintask_stimlists/main_stim_list_7.csv'},
    {'name': 'stimuli/csvs/maintask_stimlists/main_stim_list_6.csv', 'path': 'stimuli/csvs/maintask_stimlists/main_stim_list_6.csv'},
    {'name': 'stimuli/csvs/maintask_stimlists/main_stim_list_5.csv', 'path': 'stimuli/csvs/maintask_stimlists/main_stim_list_5.csv'},
    {'name': 'stimuli/csvs/maintask_stimlists/main_stim_list_4.csv', 'path': 'stimuli/csvs/maintask_stimlists/main_stim_list_4.csv'},
    {'name': 'stimuli/csvs/maintask_stimlists/main_stim_list_3.csv', 'path': 'stimuli/csvs/maintask_stimlists/main_stim_list_3.csv'},
    {'name': 'stimuli/csvs/maintask_stimlists/main_stim_list_2.csv', 'path': 'stimuli/csvs/maintask_stimlists/main_stim_list_2.csv'},
    {'name': 'stimuli/csvs/maintask_stimlists/main_stim_list_1.csv', 'path': 'stimuli/csvs/maintask_stimlists/main_stim_list_1.csv'},
    {'name': 'stimuli/csvs/maintask_stimlists/main_stim_list_0.csv', 'path': 'stimuli/csvs/maintask_stimlists/main_stim_list_0.csv'},
    {'name': 'stimuli/images/faces/zoe_saldana.png', 'path': 'stimuli/images/faces/zoe_saldana.png'},
    {'name': 'stimuli/images/faces/willie_nelson.png', 'path': 'stimuli/images/faces/willie_nelson.png'},
    {'name': 'stimuli/images/faces/wendy_davis.png', 'path': 'stimuli/images/faces/wendy_davis.png'},
    {'name': 'stimuli/images/faces/vin_diesel.png', 'path': 'stimuli/images/faces/vin_diesel.png'},
    {'name': 'stimuli/images/faces/venus_williams.png', 'path': 'stimuli/images/faces/venus_williams.png'},
    {'name': 'stimuli/images/faces/usher.png', 'path': 'stimuli/images/faces/usher.png'},
    {'name': 'stimuli/images/faces/tom_hiddleston.png', 'path': 'stimuli/images/faces/tom_hiddleston.png'},
    {'name': 'stimuli/images/faces/tom_brady.png', 'path': 'stimuli/images/faces/tom_brady.png'},
    {'name': 'stimuli/images/faces/tim_tebow.png', 'path': 'stimuli/images/faces/tim_tebow.png'},
    {'name': 'stimuli/images/faces/ted_cruz.png', 'path': 'stimuli/images/faces/ted_cruz.png'},
    {'name': 'stimuli/images/faces/taylor_swift.png', 'path': 'stimuli/images/faces/taylor_swift.png'},
    {'name': 'stimuli/images/faces/shaun_white.png', 'path': 'stimuli/images/faces/shaun_white.png'},
    {'name': 'stimuli/images/faces/seth_rogan.png', 'path': 'stimuli/images/faces/seth_rogan.png'},
    {'name': 'stimuli/images/faces/serena_williams.png', 'path': 'stimuli/images/faces/serena_williams.png'},
    {'name': 'stimuli/images/faces/selena_gomez.png', 'path': 'stimuli/images/faces/selena_gomez.png'},
    {'name': 'stimuli/images/faces/scarlett_johansson.png', 'path': 'stimuli/images/faces/scarlett_johansson.png'},
    {'name': 'stimuli/images/faces/sarah_palin.png', 'path': 'stimuli/images/faces/sarah_palin.png'},
    {'name': 'stimuli/images/faces/sandra_bullock.png', 'path': 'stimuli/images/faces/sandra_bullock.png'},
    {'name': 'stimuli/images/faces/ryan_reynolds.png', 'path': 'stimuli/images/faces/ryan_reynolds.png'},
    {'name': 'stimuli/images/faces/ronda_rousey.png', 'path': 'stimuli/images/faces/ronda_rousey.png'},
    {'name': 'stimuli/images/faces/rihanna.png', 'path': 'stimuli/images/faces/rihanna.png'},
    {'name': 'stimuli/images/faces/rand_paul.png', 'path': 'stimuli/images/faces/rand_paul.png'},
    {'name': 'stimuli/images/faces/queen_elizabeth_with_crown.png', 'path': 'stimuli/images/faces/queen_elizabeth_with_crown.png'},
    {'name': 'stimuli/images/faces/peyton_manning.png', 'path': 'stimuli/images/faces/peyton_manning.png'},
    {'name': 'stimuli/images/faces/penelope_cruz.png', 'path': 'stimuli/images/faces/penelope_cruz.png'},
    {'name': 'stimuli/images/faces/paul_ryan.png', 'path': 'stimuli/images/faces/paul_ryan.png'},
    {'name': 'stimuli/images/faces/olivia_wilde.png', 'path': 'stimuli/images/faces/olivia_wilde.png'},
    {'name': 'stimuli/images/faces/nicki_minaj.png', 'path': 'stimuli/images/faces/nicki_minaj.png'},
    {'name': 'stimuli/images/faces/morgan_freeman.png', 'path': 'stimuli/images/faces/morgan_freeman.png'},
    {'name': 'stimuli/images/faces/miranda_lambert.png', 'path': 'stimuli/images/faces/miranda_lambert.png'},
    {'name': 'stimuli/images/faces/mila_kunis.png', 'path': 'stimuli/images/faces/mila_kunis.png'},
    {'name': 'stimuli/images/faces/michelle_obama.png', 'path': 'stimuli/images/faces/michelle_obama.png'},
    {'name': 'stimuli/images/faces/michele_bachmann.png', 'path': 'stimuli/images/faces/michele_bachmann.png'},
    {'name': 'stimuli/images/faces/michael_phelps.png', 'path': 'stimuli/images/faces/michael_phelps.png'},
    {'name': 'stimuli/images/faces/michael_jordan.png', 'path': 'stimuli/images/faces/michael_jordan.png'},
    {'name': 'stimuli/images/faces/mia_hamm.png', 'path': 'stimuli/images/faces/mia_hamm.png'},
    {'name': 'stimuli/images/faces/martin_omalley.png', 'path': 'stimuli/images/faces/martin_omalley.png'},
    {'name': 'stimuli/images/faces/maria_sharapova.png', 'path': 'stimuli/images/faces/maria_sharapova.png'},
    {'name': 'stimuli/images/faces/marco_rubio.png', 'path': 'stimuli/images/faces/marco_rubio.png'},
    {'name': 'stimuli/images/faces/madonna.png', 'path': 'stimuli/images/faces/madonna.png'},
    {'name': 'stimuli/images/faces/macklemore.png', 'path': 'stimuli/images/faces/macklemore.png'},
    {'name': 'stimuli/images/faces/lucy_liu.png', 'path': 'stimuli/images/faces/lucy_liu.png'},
    {'name': 'stimuli/images/faces/lindsey_vonn.png', 'path': 'stimuli/images/faces/lindsey_vonn.png'},
    {'name': 'stimuli/images/faces/leonardo_dicaprio.png', 'path': 'stimuli/images/faces/leonardo_dicaprio.png'},
    {'name': 'stimuli/images/faces/lebron.png', 'path': 'stimuli/images/faces/lebron.png'},
    {'name': 'stimuli/images/faces/lance_armstrong.png', 'path': 'stimuli/images/faces/lance_armstrong.png'},
    {'name': 'stimuli/images/faces/kobe_bryant.png', 'path': 'stimuli/images/faces/kobe_bryant.png'},
    {'name': 'stimuli/images/faces/keith_urban.png', 'path': 'stimuli/images/faces/keith_urban.png'},
    {'name': 'stimuli/images/faces/katy_perry.png', 'path': 'stimuli/images/faces/katy_perry.png'},
    {'name': 'stimuli/images/faces/justin_bieber.png', 'path': 'stimuli/images/faces/justin_bieber.png'},
    {'name': 'stimuli/images/faces/john_mcain.png', 'path': 'stimuli/images/faces/john_mcain.png'},
    {'name': 'stimuli/images/faces/john_mayer.png', 'path': 'stimuli/images/faces/john_mayer.png'},
    {'name': 'stimuli/images/faces/john_kerry.png', 'path': 'stimuli/images/faces/john_kerry.png'},
    {'name': 'stimuli/images/faces/joe_biden.png', 'path': 'stimuli/images/faces/joe_biden.png'},
    {'name': 'stimuli/images/faces/jj_watt.png', 'path': 'stimuli/images/faces/jj_watt.png'},
    {'name': 'stimuli/images/faces/jennifer_aniston.png', 'path': 'stimuli/images/faces/jennifer_aniston.png'},
    {'name': 'stimuli/images/faces/jeb_bush.png', 'path': 'stimuli/images/faces/jeb_bush.png'},
    {'name': 'stimuli/images/faces/jay_z.png', 'path': 'stimuli/images/faces/jay_z.png'},
    {'name': 'stimuli/images/faces/jason_statham.png', 'path': 'stimuli/images/faces/jason_statham.png'},
    {'name': 'stimuli/images/faces/hope_solo.png', 'path': 'stimuli/images/faces/hope_solo.png'},
    {'name': 'stimuli/images/faces/hillary_clinton.png', 'path': 'stimuli/images/faces/hillary_clinton.png'},
    {'name': 'stimuli/images/faces/gwen_stefani.png', 'path': 'stimuli/images/faces/gwen_stefani.png'},
    {'name': 'stimuli/images/faces/gerard_butler.png', 'path': 'stimuli/images/faces/gerard_butler.png'},
    {'name': 'stimuli/images/faces/george_clooney.png', 'path': 'stimuli/images/faces/george_clooney.png'},
    {'name': 'stimuli/images/faces/george_bush.png', 'path': 'stimuli/images/faces/george_bush.png'},
    {'name': 'stimuli/images/faces/gabby_douglas.png', 'path': 'stimuli/images/faces/gabby_douglas.png'},
    {'name': 'stimuli/images/faces/emma_stone.png', 'path': 'stimuli/images/faces/emma_stone.png'},
    {'name': 'stimuli/images/faces/drake.png', 'path': 'stimuli/images/faces/drake.png'},
    {'name': 'stimuli/images/faces/david_beckham.png', 'path': 'stimuli/images/faces/david_beckham.png'},
    {'name': 'stimuli/images/faces/danica_patrick.png', 'path': 'stimuli/images/faces/danica_patrick.png'},
    {'name': 'stimuli/images/faces/condoleezza_rice.png', 'path': 'stimuli/images/faces/condoleezza_rice.png'},
    {'name': 'stimuli/images/faces/christian_bale.png', 'path': 'stimuli/images/faces/christian_bale.png'},
    {'name': 'stimuli/images/faces/chris_pratt.png', 'path': 'stimuli/images/faces/chris_pratt.png'},
    {'name': 'stimuli/images/faces/chris_hemsworth.png', 'path': 'stimuli/images/faces/chris_hemsworth.png'},
    {'name': 'stimuli/images/faces/chris_christie.png', 'path': 'stimuli/images/faces/chris_christie.png'},
    {'name': 'stimuli/images/faces/carrie_underwood.png', 'path': 'stimuli/images/faces/carrie_underwood.png'},
    {'name': 'stimuli/images/faces/carly_fiorina.png', 'path': 'stimuli/images/faces/carly_fiorina.png'},
    {'name': 'stimuli/images/faces/bruno_mars.png', 'path': 'stimuli/images/faces/bruno_mars.png'},
    {'name': 'stimuli/images/faces/britney_spears.png', 'path': 'stimuli/images/faces/britney_spears.png'},
    {'name': 'stimuli/images/faces/brad_pitt.png', 'path': 'stimuli/images/faces/brad_pitt.png'},
    {'name': 'stimuli/images/faces/blake_shelton.png', 'path': 'stimuli/images/faces/blake_shelton.png'},
    {'name': 'stimuli/images/faces/blake_lively.png', 'path': 'stimuli/images/faces/blake_lively.png'},
    {'name': 'stimuli/images/faces/bill_clinton.png', 'path': 'stimuli/images/faces/bill_clinton.png'},
    {'name': 'stimuli/images/faces/beyonce_knowles.png', 'path': 'stimuli/images/faces/beyonce_knowles.png'},
    {'name': 'stimuli/images/faces/bernie_sanders.png', 'path': 'stimuli/images/faces/bernie_sanders.png'},
    {'name': 'stimuli/images/faces/ben_carson.png', 'path': 'stimuli/images/faces/ben_carson.png'},
    {'name': 'stimuli/images/faces/barack_obama.png', 'path': 'stimuli/images/faces/barack_obama.png'},
    {'name': 'stimuli/images/faces/ariana_grande.png', 'path': 'stimuli/images/faces/ariana_grande.png'},
    {'name': 'stimuli/images/faces/anne_hathaway.png', 'path': 'stimuli/images/faces/anne_hathaway.png'},
    {'name': 'stimuli/images/faces/angela_merkel.png', 'path': 'stimuli/images/faces/angela_merkel.png'},
    {'name': 'stimuli/images/faces/amanda_seyfried.png', 'path': 'stimuli/images/faces/amanda_seyfried.png'},
    {'name': 'stimuli/images/faces/alex_rodriguez.png', 'path': 'stimuli/images/faces/alex_rodriguez.png'},
    {'name': 'stimuli/images/faces/alex_morgan.png', 'path': 'stimuli/images/faces/alex_morgan.png'},
    {'name': 'stimuli/images/faces/adele.png', 'path': 'stimuli/images/faces/adele.png'},
    {'name': 'stimuli/images/faces/adam_levine.png', 'path': 'stimuli/images/faces/adam_levine.png'},
    {'name': 'stimuli/images/faces/abby_wambach.png', 'path': 'stimuli/images/faces/abby_wambach.png'},
    {'name': 'stimuli/images/faces/aaron_rodgers.png', 'path': 'stimuli/images/faces/aaron_rodgers.png'},
    {'name': 'stimuli/images/fruits/yellow_apple.png', 'path': 'stimuli/images/fruits/yellow_apple.png'},
    {'name': 'stimuli/images/fruits/whole_pears.png', 'path': 'stimuli/images/fruits/whole_pears.png'},
    {'name': 'stimuli/images/fruits/whole_pear02.png', 'path': 'stimuli/images/fruits/whole_pear02.png'},
    {'name': 'stimuli/images/fruits/whole_cantaloupe.png', 'path': 'stimuli/images/fruits/whole_cantaloupe.png'},
    {'name': 'stimuli/images/fruits/watermelon.png', 'path': 'stimuli/images/fruits/watermelon.png'},
    {'name': 'stimuli/images/fruits/sliced_watermelon05.png', 'path': 'stimuli/images/fruits/sliced_watermelon05.png'},
    {'name': 'stimuli/images/fruits/sliced_watermelon04.png', 'path': 'stimuli/images/fruits/sliced_watermelon04.png'},
    {'name': 'stimuli/images/fruits/sliced_watermelon03.png', 'path': 'stimuli/images/fruits/sliced_watermelon03.png'},
    {'name': 'stimuli/images/fruits/sliced_watermelon02.png', 'path': 'stimuli/images/fruits/sliced_watermelon02.png'},
    {'name': 'stimuli/images/fruits/sliced_watermelon.png', 'path': 'stimuli/images/fruits/sliced_watermelon.png'},
    {'name': 'stimuli/images/fruits/sliced_pears02.png', 'path': 'stimuli/images/fruits/sliced_pears02.png'},
    {'name': 'stimuli/images/fruits/sliced_pears.png', 'path': 'stimuli/images/fruits/sliced_pears.png'},
    {'name': 'stimuli/images/fruits/sliced_honeydew02.png', 'path': 'stimuli/images/fruits/sliced_honeydew02.png'},
    {'name': 'stimuli/images/fruits/sliced_honeydew.png', 'path': 'stimuli/images/fruits/sliced_honeydew.png'},
    {'name': 'stimuli/images/fruits/sliced_fuji.png', 'path': 'stimuli/images/fruits/sliced_fuji.png'},
    {'name': 'stimuli/images/fruits/red_grapes07.png', 'path': 'stimuli/images/fruits/red_grapes07.png'},
    {'name': 'stimuli/images/fruits/red_grapes06.png', 'path': 'stimuli/images/fruits/red_grapes06.png'},
    {'name': 'stimuli/images/fruits/red_grapes05.png', 'path': 'stimuli/images/fruits/red_grapes05.png'},
    {'name': 'stimuli/images/fruits/red_grapes04.png', 'path': 'stimuli/images/fruits/red_grapes04.png'},
    {'name': 'stimuli/images/fruits/red_grapes03.png', 'path': 'stimuli/images/fruits/red_grapes03.png'},
    {'name': 'stimuli/images/fruits/red_grapes02.png', 'path': 'stimuli/images/fruits/red_grapes02.png'},
    {'name': 'stimuli/images/fruits/red_grapes.png', 'path': 'stimuli/images/fruits/red_grapes.png'},
    {'name': 'stimuli/images/fruits/red_delicious.png', 'path': 'stimuli/images/fruits/red_delicious.png'},
    {'name': 'stimuli/images/fruits/pink_lady.png', 'path': 'stimuli/images/fruits/pink_lady.png'},
    {'name': 'stimuli/images/fruits/pear06.png', 'path': 'stimuli/images/fruits/pear06.png'},
    {'name': 'stimuli/images/fruits/pear05.png', 'path': 'stimuli/images/fruits/pear05.png'},
    {'name': 'stimuli/images/fruits/pear04.png', 'path': 'stimuli/images/fruits/pear04.png'},
    {'name': 'stimuli/images/fruits/pear03.png', 'path': 'stimuli/images/fruits/pear03.png'},
    {'name': 'stimuli/images/fruits/pear02.png', 'path': 'stimuli/images/fruits/pear02.png'},
    {'name': 'stimuli/images/fruits/pear01.png', 'path': 'stimuli/images/fruits/pear01.png'},
    {'name': 'stimuli/images/fruits/pear.png', 'path': 'stimuli/images/fruits/pear.png'},
    {'name': 'stimuli/images/fruits/orange_pear.png', 'path': 'stimuli/images/fruits/orange_pear.png'},
    {'name': 'stimuli/images/fruits/muskmelon02.png', 'path': 'stimuli/images/fruits/muskmelon02.png'},
    {'name': 'stimuli/images/fruits/muskmelon.png', 'path': 'stimuli/images/fruits/muskmelon.png'},
    {'name': 'stimuli/images/fruits/mixed_grapes05.png', 'path': 'stimuli/images/fruits/mixed_grapes05.png'},
    {'name': 'stimuli/images/fruits/mixed_grapes04.png', 'path': 'stimuli/images/fruits/mixed_grapes04.png'},
    {'name': 'stimuli/images/fruits/mixed_grapes03.png', 'path': 'stimuli/images/fruits/mixed_grapes03.png'},
    {'name': 'stimuli/images/fruits/mixed_grapes02.png', 'path': 'stimuli/images/fruits/mixed_grapes02.png'},
    {'name': 'stimuli/images/fruits/mixed_grapes.png', 'path': 'stimuli/images/fruits/mixed_grapes.png'},
    {'name': 'stimuli/images/fruits/leaning_pears03.png', 'path': 'stimuli/images/fruits/leaning_pears03.png'},
    {'name': 'stimuli/images/fruits/leaning_pears02.png', 'path': 'stimuli/images/fruits/leaning_pears02.png'},
    {'name': 'stimuli/images/fruits/leaning_pears.png', 'path': 'stimuli/images/fruits/leaning_pears.png'},
    {'name': 'stimuli/images/fruits/lavaredo.png', 'path': 'stimuli/images/fruits/lavaredo.png'},
    {'name': 'stimuli/images/fruits/kiku_slice.png', 'path': 'stimuli/images/fruits/kiku_slice.png'},
    {'name': 'stimuli/images/fruits/honeydew_melon02.png', 'path': 'stimuli/images/fruits/honeydew_melon02.png'},
    {'name': 'stimuli/images/fruits/honeydew_melon.png', 'path': 'stimuli/images/fruits/honeydew_melon.png'},
    {'name': 'stimuli/images/fruits/honeydew_half.png', 'path': 'stimuli/images/fruits/honeydew_half.png'},
    {'name': 'stimuli/images/fruits/honeydew.png', 'path': 'stimuli/images/fruits/honeydew.png'},
    {'name': 'stimuli/images/fruits/honeycrisp_apple.png', 'path': 'stimuli/images/fruits/honeycrisp_apple.png'},
    {'name': 'stimuli/images/fruits/halved_watermelon02.png', 'path': 'stimuli/images/fruits/halved_watermelon02.png'},
    {'name': 'stimuli/images/fruits/halved_watermelon.png', 'path': 'stimuli/images/fruits/halved_watermelon.png'},
    {'name': 'stimuli/images/fruits/half_apple.png', 'path': 'stimuli/images/fruits/half_apple.png'},
    {'name': 'stimuli/images/fruits/green_pear.png', 'path': 'stimuli/images/fruits/green_pear.png'},
    {'name': 'stimuli/images/fruits/green_grapes06.png', 'path': 'stimuli/images/fruits/green_grapes06.png'},
    {'name': 'stimuli/images/fruits/green_grapes05.png', 'path': 'stimuli/images/fruits/green_grapes05.png'},
    {'name': 'stimuli/images/fruits/green_grapes04.png', 'path': 'stimuli/images/fruits/green_grapes04.png'},
    {'name': 'stimuli/images/fruits/green_grapes03.png', 'path': 'stimuli/images/fruits/green_grapes03.png'},
    {'name': 'stimuli/images/fruits/green_grapes02.png', 'path': 'stimuli/images/fruits/green_grapes02.png'},
    {'name': 'stimuli/images/fruits/green_grapes.png', 'path': 'stimuli/images/fruits/green_grapes.png'},
    {'name': 'stimuli/images/fruits/granny_smith_apples.png', 'path': 'stimuli/images/fruits/granny_smith_apples.png'},
    {'name': 'stimuli/images/fruits/golden_apple.png', 'path': 'stimuli/images/fruits/golden_apple.png'},
    {'name': 'stimuli/images/fruits/gala_apple_leaf.png', 'path': 'stimuli/images/fruits/gala_apple_leaf.png'},
    {'name': 'stimuli/images/fruits/gala_apple.png', 'path': 'stimuli/images/fruits/gala_apple.png'},
    {'name': 'stimuli/images/fruits/fresh_red_apple.png', 'path': 'stimuli/images/fruits/fresh_red_apple.png'},
    {'name': 'stimuli/images/fruits/fresh_pear03.png', 'path': 'stimuli/images/fruits/fresh_pear03.png'},
    {'name': 'stimuli/images/fruits/fresh_pear.png', 'path': 'stimuli/images/fruits/fresh_pear.png'},
    {'name': 'stimuli/images/fruits/fresh_fuji.png', 'path': 'stimuli/images/fruits/fresh_fuji.png'},
    {'name': 'stimuli/images/fruits/finger_grapes.png', 'path': 'stimuli/images/fruits/finger_grapes.png'},
    {'name': 'stimuli/images/fruits/cut_pears05.png', 'path': 'stimuli/images/fruits/cut_pears05.png'},
    {'name': 'stimuli/images/fruits/cut_pears04.png', 'path': 'stimuli/images/fruits/cut_pears04.png'},
    {'name': 'stimuli/images/fruits/cut_pears03.png', 'path': 'stimuli/images/fruits/cut_pears03.png'},
    {'name': 'stimuli/images/fruits/cut_pears02.png', 'path': 'stimuli/images/fruits/cut_pears02.png'},
    {'name': 'stimuli/images/fruits/cut_pears.png', 'path': 'stimuli/images/fruits/cut_pears.png'},
    {'name': 'stimuli/images/fruits/cut_cantaloupe.png', 'path': 'stimuli/images/fruits/cut_cantaloupe.png'},
    {'name': 'stimuli/images/fruits/casaba_melon.png', 'path': 'stimuli/images/fruits/casaba_melon.png'},
    {'name': 'stimuli/images/fruits/canteloupe_sliced04.png', 'path': 'stimuli/images/fruits/canteloupe_sliced04.png'},
    {'name': 'stimuli/images/fruits/cantaloupe_sliced03.png', 'path': 'stimuli/images/fruits/cantaloupe_sliced03.png'},
    {'name': 'stimuli/images/fruits/cantaloupe_sliced.png', 'path': 'stimuli/images/fruits/cantaloupe_sliced.png'},
    {'name': 'stimuli/images/fruits/cantaloupe02.png', 'path': 'stimuli/images/fruits/cantaloupe02.png'},
    {'name': 'stimuli/images/fruits/cantaloupe.png', 'path': 'stimuli/images/fruits/cantaloupe.png'},
    {'name': 'stimuli/images/fruits/bosc_pear.png', 'path': 'stimuli/images/fruits/bosc_pear.png'},
    {'name': 'stimuli/images/fruits/black_grapes05.png', 'path': 'stimuli/images/fruits/black_grapes05.png'},
    {'name': 'stimuli/images/fruits/black_grapes04.png', 'path': 'stimuli/images/fruits/black_grapes04.png'},
    {'name': 'stimuli/images/fruits/black_grapes03.png', 'path': 'stimuli/images/fruits/black_grapes03.png'},
    {'name': 'stimuli/images/fruits/black_grapes02.png', 'path': 'stimuli/images/fruits/black_grapes02.png'},
    {'name': 'stimuli/images/fruits/black_grapes.png', 'path': 'stimuli/images/fruits/black_grapes.png'},
    {'name': 'stimuli/images/fruits/apple_slice2.png', 'path': 'stimuli/images/fruits/apple_slice2.png'},
    {'name': 'stimuli/images/fruits/apple_green.png', 'path': 'stimuli/images/fruits/apple_green.png'},
    {'name': 'stimuli/images/fruits/apple07.png', 'path': 'stimuli/images/fruits/apple07.png'},
    {'name': 'stimuli/images/fruits/apple06.png', 'path': 'stimuli/images/fruits/apple06.png'},
    {'name': 'stimuli/images/fruits/apple05b.png', 'path': 'stimuli/images/fruits/apple05b.png'},
    {'name': 'stimuli/images/fruits/apple05a.png', 'path': 'stimuli/images/fruits/apple05a.png'},
    {'name': 'stimuli/images/fruits/apple04.png', 'path': 'stimuli/images/fruits/apple04.png'},
    {'name': 'stimuli/images/fruits/apple03c.png', 'path': 'stimuli/images/fruits/apple03c.png'},
    {'name': 'stimuli/images/fruits/apple03b.png', 'path': 'stimuli/images/fruits/apple03b.png'},
    {'name': 'stimuli/images/fruits/apple03a.png', 'path': 'stimuli/images/fruits/apple03a.png'},
    {'name': 'stimuli/images/fruits/apple01 2.png', 'path': 'stimuli/images/fruits/apple01 2.png'},
    {'name': 'stimuli/images/places/yellow_sand_kauai.png', 'path': 'stimuli/images/places/yellow_sand_kauai.png'},
    {'name': 'stimuli/images/places/yellow_sand_beach.png', 'path': 'stimuli/images/places/yellow_sand_beach.png'},
    {'name': 'stimuli/images/places/white_sand_beach.png', 'path': 'stimuli/images/places/white_sand_beach.png'},
    {'name': 'stimuli/images/places/unique_mountains.png', 'path': 'stimuli/images/places/unique_mountains.png'},
    {'name': 'stimuli/images/places/tree_beach.png', 'path': 'stimuli/images/places/tree_beach.png'},
    {'name': 'stimuli/images/places/tower_bridge.png', 'path': 'stimuli/images/places/tower_bridge.png'},
    {'name': 'stimuli/images/places/texas_beach.png', 'path': 'stimuli/images/places/texas_beach.png'},
    {'name': 'stimuli/images/places/taj_mahal.png', 'path': 'stimuli/images/places/taj_mahal.png'},
    {'name': 'stimuli/images/places/sydney_bridge.png', 'path': 'stimuli/images/places/sydney_bridge.png'},
    {'name': 'stimuli/images/places/swedish_bridge.png', 'path': 'stimuli/images/places/swedish_bridge.png'},
    {'name': 'stimuli/images/places/supreme_court.png', 'path': 'stimuli/images/places/supreme_court.png'},
    {'name': 'stimuli/images/places/sunset_beach.png', 'path': 'stimuli/images/places/sunset_beach.png'},
    {'name': 'stimuli/images/places/stbasils.png', 'path': 'stimuli/images/places/stbasils.png'},
    {'name': 'stimuli/images/places/space_needle.png', 'path': 'stimuli/images/places/space_needle.png'},
    {'name': 'stimuli/images/places/skyway_bridge.png', 'path': 'stimuli/images/places/skyway_bridge.png'},
    {'name': 'stimuli/images/places/sioseh_bridge.png', 'path': 'stimuli/images/places/sioseh_bridge.png'},
    {'name': 'stimuli/images/places/shell_beach.png', 'path': 'stimuli/images/places/shell_beach.png'},
    {'name': 'stimuli/images/places/sandy_beach.png', 'path': 'stimuli/images/places/sandy_beach.png'},
    {'name': 'stimuli/images/places/sajama.png', 'path': 'stimuli/images/places/sajama.png'},
    {'name': 'stimuli/images/places/sagrada_familia.png', 'path': 'stimuli/images/places/sagrada_familia.png'},
    {'name': 'stimuli/images/places/royal_albert_hall.png', 'path': 'stimuli/images/places/royal_albert_hall.png'},
    {'name': 'stimuli/images/places/river_bridge.png', 'path': 'stimuli/images/places/river_bridge.png'},
    {'name': 'stimuli/images/places/ripple_beach.png', 'path': 'stimuli/images/places/ripple_beach.png'},
    {'name': 'stimuli/images/places/red_sand_beach.png', 'path': 'stimuli/images/places/red_sand_beach.png'},
    {'name': 'stimuli/images/places/python_bridge.png', 'path': 'stimuli/images/places/python_bridge.png'},
    {'name': 'stimuli/images/places/pont_du_gard.png', 'path': 'stimuli/images/places/pont_du_gard.png'},
    {'name': 'stimuli/images/places/piza.png', 'path': 'stimuli/images/places/piza.png'},
    {'name': 'stimuli/images/places/pink_sand_beach.png', 'path': 'stimuli/images/places/pink_sand_beach.png'},
    {'name': 'stimuli/images/places/pink_beach.png', 'path': 'stimuli/images/places/pink_beach.png'},
    {'name': 'stimuli/images/places/petronas_towers.png', 'path': 'stimuli/images/places/petronas_towers.png'},
    {'name': 'stimuli/images/places/palm_beach.png', 'path': 'stimuli/images/places/palm_beach.png'},
    {'name': 'stimuli/images/places/outer_banks_beach.png', 'path': 'stimuli/images/places/outer_banks_beach.png'},
    {'name': 'stimuli/images/places/natchez_bridge.png', 'path': 'stimuli/images/places/natchez_bridge.png'},
    {'name': 'stimuli/images/places/mountains1.png', 'path': 'stimuli/images/places/mountains1.png'},
    {'name': 'stimuli/images/places/mountain_range.png', 'path': 'stimuli/images/places/mountain_range.png'},
    {'name': 'stimuli/images/places/mount_huang.png', 'path': 'stimuli/images/places/mount_huang.png'},
    {'name': 'stimuli/images/places/mount_hood.png', 'path': 'stimuli/images/places/mount_hood.png'},
    {'name': 'stimuli/images/places/mount_fuji.png', 'path': 'stimuli/images/places/mount_fuji.png'},
    {'name': 'stimuli/images/places/mount_everest.png', 'path': 'stimuli/images/places/mount_everest.png'},
    {'name': 'stimuli/images/places/millau_bridge.png', 'path': 'stimuli/images/places/millau_bridge.png'},
    {'name': 'stimuli/images/places/meijigallery_tokyo.png', 'path': 'stimuli/images/places/meijigallery_tokyo.png'},
    {'name': 'stimuli/images/places/mediterranean_beach.png', 'path': 'stimuli/images/places/mediterranean_beach.png'},
    {'name': 'stimuli/images/places/matterhorn.png', 'path': 'stimuli/images/places/matterhorn.png'},
    {'name': 'stimuli/images/places/long_bridge.png', 'path': 'stimuli/images/places/long_bridge.png'},
    {'name': 'stimuli/images/places/light_pink_beach.png', 'path': 'stimuli/images/places/light_pink_beach.png'},
    {'name': 'stimuli/images/places/licancabur.png', 'path': 'stimuli/images/places/licancabur.png'},
    {'name': 'stimuli/images/places/kilimanjaro.png', 'path': 'stimuli/images/places/kilimanjaro.png'},
    {'name': 'stimuli/images/places/kailash.png', 'path': 'stimuli/images/places/kailash.png'},
    {'name': 'stimuli/images/places/k2.png', 'path': 'stimuli/images/places/k2.png'},
    {'name': 'stimuli/images/places/japanese_castle.png', 'path': 'stimuli/images/places/japanese_castle.png'},
    {'name': 'stimuli/images/places/jacques_bridge.png', 'path': 'stimuli/images/places/jacques_bridge.png'},
    {'name': 'stimuli/images/places/independence_hall.png', 'path': 'stimuli/images/places/independence_hall.png'},
    {'name': 'stimuli/images/places/himalayas.png', 'path': 'stimuli/images/places/himalayas.png'},
    {'name': 'stimuli/images/places/harvard.png', 'path': 'stimuli/images/places/harvard.png'},
    {'name': 'stimuli/images/places/half_dome.png', 'path': 'stimuli/images/places/half_dome.png'},
    {'name': 'stimuli/images/places/hagia_sophia.png', 'path': 'stimuli/images/places/hagia_sophia.png'},
    {'name': 'stimuli/images/places/gray_beach.png', 'path': 'stimuli/images/places/gray_beach.png'},
    {'name': 'stimuli/images/places/grand_teton.png', 'path': 'stimuli/images/places/grand_teton.png'},
    {'name': 'stimuli/images/places/golden_gate_bridge.png', 'path': 'stimuli/images/places/golden_gate_bridge.png'},
    {'name': 'stimuli/images/places/glass_bridge.png', 'path': 'stimuli/images/places/glass_bridge.png'},
    {'name': 'stimuli/images/places/gherkin.png', 'path': 'stimuli/images/places/gherkin.png'},
    {'name': 'stimuli/images/places/freedom_beach.png', 'path': 'stimuli/images/places/freedom_beach.png'},
    {'name': 'stimuli/images/places/forth_bridge.png', 'path': 'stimuli/images/places/forth_bridge.png'},
    {'name': 'stimuli/images/places/fort_knox.png', 'path': 'stimuli/images/places/fort_knox.png'},
    {'name': 'stimuli/images/places/flatiron_building.png', 'path': 'stimuli/images/places/flatiron_building.png'},
    {'name': 'stimuli/images/places/fitz_roy.png', 'path': 'stimuli/images/places/fitz_roy.png'},
    {'name': 'stimuli/images/places/empire_state_building.png', 'path': 'stimuli/images/places/empire_state_building.png'},
    {'name': 'stimuli/images/places/eiger.png', 'path': 'stimuli/images/places/eiger.png'},
    {'name': 'stimuli/images/places/donghai_bridge.png', 'path': 'stimuli/images/places/donghai_bridge.png'},
    {'name': 'stimuli/images/places/dome_of_the_rock.png', 'path': 'stimuli/images/places/dome_of_the_rock.png'},
    {'name': 'stimuli/images/places/distant_mountains.png', 'path': 'stimuli/images/places/distant_mountains.png'},
    {'name': 'stimuli/images/places/denali.png', 'path': 'stimuli/images/places/denali.png'},
    {'name': 'stimuli/images/places/danyang_bridge.png', 'path': 'stimuli/images/places/danyang_bridge.png'},
    {'name': 'stimuli/images/places/covered_bridge.png', 'path': 'stimuli/images/places/covered_bridge.png'},
    {'name': 'stimuli/images/places/costa_rica_mountain.png', 'path': 'stimuli/images/places/costa_rica_mountain.png'},
    {'name': 'stimuli/images/places/cn_tower.png', 'path': 'stimuli/images/places/cn_tower.png'},
    {'name': 'stimuli/images/places/cinderella_castle.png', 'path': 'stimuli/images/places/cinderella_castle.png'},
    {'name': 'stimuli/images/places/chengyang_bridge.png', 'path': 'stimuli/images/places/chengyang_bridge.png'},
    {'name': 'stimuli/images/places/castle.png', 'path': 'stimuli/images/places/castle.png'},
    {'name': 'stimuli/images/places/capitol.png', 'path': 'stimuli/images/places/capitol.png'},
    {'name': 'stimuli/images/places/capilano_bridge.png', 'path': 'stimuli/images/places/capilano_bridge.png'},
    {'name': 'stimuli/images/places/california_beach.png', 'path': 'stimuli/images/places/california_beach.png'},
    {'name': 'stimuli/images/places/brooklyn_bridge.png', 'path': 'stimuli/images/places/brooklyn_bridge.png'},
    {'name': 'stimuli/images/places/black_sand_maui.png', 'path': 'stimuli/images/places/black_sand_maui.png'},
    {'name': 'stimuli/images/places/black_sand.png', 'path': 'stimuli/images/places/black_sand.png'},
    {'name': 'stimuli/images/places/black_beach_surf.png', 'path': 'stimuli/images/places/black_beach_surf.png'},
    {'name': 'stimuli/images/places/black_beach_iceland.png', 'path': 'stimuli/images/places/black_beach_iceland.png'},
    {'name': 'stimuli/images/places/beautiful_beach.png', 'path': 'stimuli/images/places/beautiful_beach.png'},
    {'name': 'stimuli/images/places/azadi_monument.png', 'path': 'stimuli/images/places/azadi_monument.png'},
    {'name': 'stimuli/images/places/aoraki.png', 'path': 'stimuli/images/places/aoraki.png'},
    {'name': 'stimuli/images/places/alpamayo.png', 'path': 'stimuli/images/places/alpamayo.png'},
    {'name': 'stimuli/images/places/alcantara_bridge.png', 'path': 'stimuli/images/places/alcantara_bridge.png'},
    {'name': 'stimuli/images/places/alamo.png', 'path': 'stimuli/images/places/alamo.png'},
    {'name': 'stimuli/images/places/akashi_bridge.png', 'path': 'stimuli/images/places/akashi_bridge.png'},
    {'name': 'stimuli/images/places/360_bridge.png', 'path': 'stimuli/images/places/360_bridge.png'},
    {'name': 'stimuli/cues/suppress_cue_image.png', 'path': 'stimuli/cues/suppress_cue_image.png'},
    {'name': 'stimuli/cues/maintain_cue_image.png', 'path': 'stimuli/cues/maintain_cue_image.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.2';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var WelcomeClock;
var welcome_text;
var welcome_keyResp;
var Encode_instructClock;
var encode_instruct_img;
var encode_instruct_cont_text;
var encode_instruct_keyResp;
var Oper_screen_instructClock;
var operscreen_instruct_img;
var operscreen_instruct_cont_text;
var operscreen_instruct_keyResp;
var Operations_instructClock;
var operations_instruct_img;
var operations_instruct_conttext;
var operations_instruct_keyResp;
var Probe_screen_instructClock;
var probescreen_instruct_img;
var probescreen_instruct_conttext;
var probescreen_instruct_keyResp;
var Probe_instructClock;
var probe_instructions_img;
var probe_instructions_conttext;
var probe_instructions_keyResp;
var Practice_beginClock;
var prac_begin_text;
var prac_begin_keyResp;
var corr;
var Trial_prepareClock;
var Trial_prepare_text;
var EncodeClock;
var encode_fixation;
var img_1_left;
var img_2_right;
var Delay_2000Clock;
var delay_fixation_2000;
var ManipulateClock;
var manipulate_cue;
var manipulate_fixation;
var Delay_4000Clock;
var delay_fixation_4000;
var ProbeClock;
var probe_image;
var probe_keyResp;
var yesKey_text;
var noKey_text;
var ITIClock;
var ITI_text;
var Practice_endClock;
var practice_continue_text;
var pracend_keyResp;
var Main_exp_beginClock;
var mainexp_begin_text;
var main_exp_begin;
var RestClock;
var rest_exclaim_text;
var rest_welcome;
var rest_continue;
var rest_continue_text;
var DebriefClock;
var debrief_text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Welcome"
  WelcomeClock = new util.Clock();
  welcome_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcome_text',
    text: 'Welcome to an experiment by the ... Lab!\n\nThis experiment is meant to be run in full-screen mode. DO NOT escape out of the full-screen. Otherwise you will have to restart the entire experiment from the beginning.\n\n\nPress <SPACE> to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  welcome_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Encode_instruct"
  Encode_instructClock = new util.Clock();
  encode_instruct_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'encode_instruct_img', units : undefined, 
    image : 'instructions/encode_instructions.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 0.075)], 
    draggable: false,
    size : [1.53, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  encode_instruct_cont_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'encode_instruct_cont_text',
    text: 'Press <SPACE> to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  encode_instruct_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Oper_screen_instruct"
  Oper_screen_instructClock = new util.Clock();
  operscreen_instruct_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'operscreen_instruct_img', units : undefined, 
    image : 'instructions/oper_screen_instructions.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 0.075)], 
    draggable: false,
    size : [1.53, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  operscreen_instruct_cont_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'operscreen_instruct_cont_text',
    text: 'Press <SPACE> to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  operscreen_instruct_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Operations_instruct"
  Operations_instructClock = new util.Clock();
  operations_instruct_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'operations_instruct_img', units : undefined, 
    image : 'instructions/operation_instructions.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [1.53, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  operations_instruct_conttext = new visual.TextStim({
    win: psychoJS.window,
    name: 'operations_instruct_conttext',
    text: 'Press <SPACE> to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.43)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  operations_instruct_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Probe_screen_instruct"
  Probe_screen_instructClock = new util.Clock();
  probescreen_instruct_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'probescreen_instruct_img', units : undefined, 
    image : 'instructions/probe_screen_instructions.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [1.47, 0.95],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  probescreen_instruct_conttext = new visual.TextStim({
    win: psychoJS.window,
    name: 'probescreen_instruct_conttext',
    text: 'Press <SPACE> to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.45)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  probescreen_instruct_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Probe_instruct"
  Probe_instructClock = new util.Clock();
  probe_instructions_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'probe_instructions_img', units : undefined, 
    image : 'instructions/probe_instructions.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [1.47, 0.9],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  probe_instructions_conttext = new visual.TextStim({
    win: psychoJS.window,
    name: 'probe_instructions_conttext',
    text: 'Press <SPACE> to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.45)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  probe_instructions_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Practice_begin"
  Practice_beginClock = new util.Clock();
  prac_begin_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'prac_begin_text',
    text: "Let's do a couple of practice trials!\n\n\n\nPress <RETURN> to continue.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  prac_begin_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from corrinit_code
  corr = 0;
  
  // Initialize components for Routine "Trial_prepare"
  Trial_prepareClock = new util.Clock();
  Trial_prepare_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Trial_prepare_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Encode"
  EncodeClock = new util.Clock();
  encode_fixation = new visual.Polygon({
    win: psychoJS.window, name: 'encode_fixation', 
    edges: 100, size:[0.03, 0.03],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('dimgray'),
    fillColor: new util.Color('dimgray'),
    fillColor: 'dimgray',
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  img_1_left = new visual.ImageStim({
    win : psychoJS.window,
    name : 'img_1_left', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [(- 0.3), 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  img_2_right = new visual.ImageStim({
    win : psychoJS.window,
    name : 'img_2_right', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.3, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "Delay_2000"
  Delay_2000Clock = new util.Clock();
  delay_fixation_2000 = new visual.Polygon({
    win: psychoJS.window, name: 'delay_fixation_2000', 
    edges: 100, size:[0.03, 0.03],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('dimgray'),
    fillColor: new util.Color('dimgray'),
    fillColor: 'dimgray',
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "Manipulate"
  ManipulateClock = new util.Clock();
  manipulate_cue = new visual.ImageStim({
    win : psychoJS.window,
    name : 'manipulate_cue', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  manipulate_fixation = new visual.Polygon({
    win: psychoJS.window, name: 'manipulate_fixation', 
    edges: 100, size:[0.03, 0.03],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('dimgray'),
    fillColor: new util.Color('dimgray'),
    fillColor: 'dimgray',
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  // Initialize components for Routine "Delay_4000"
  Delay_4000Clock = new util.Clock();
  delay_fixation_4000 = new visual.Polygon({
    win: psychoJS.window, name: 'delay_fixation_4000', 
    edges: 100, size:[0.03, 0.03],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('dimgray'),
    fillColor: new util.Color('dimgray'),
    fillColor: 'dimgray',
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "Probe"
  ProbeClock = new util.Clock();
  var keyPressed_probe;
  
  probe_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'probe_image', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  probe_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  yesKey_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'yesKey_text',
    text: '[F]\nYES',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), (- 0.35)], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  noKey_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'noKey_text',
    text: '[J]\nNO',
    font: 'Arial',
    units: undefined, 
    pos: [0.2, (- 0.35)], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "ITI"
  ITIClock = new util.Clock();
  ITI_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'ITI_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Practice_end"
  Practice_endClock = new util.Clock();
  practice_continue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_continue_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  pracend_keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Main_exp_begin"
  Main_exp_beginClock = new util.Clock();
  mainexp_begin_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'mainexp_begin_text',
    text: 'The main experiment is about to begin.\n\n\n\nPress <ENTER> to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  main_exp_begin = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Rest"
  RestClock = new util.Clock();
  rest_exclaim_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rest_exclaim_text',
    text: 'Rest!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  rest_welcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'rest_welcome',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  rest_continue = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  rest_continue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'rest_continue_text',
    text: 'Press <SPACE> if you would like to end the break early!',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "Debrief"
  DebriefClock = new util.Clock();
  debrief_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'debrief_text',
    text: "In the experiment, you were asked to encode two items on each trial. You were then cued to manipulate one of the items in your working memory by either maintaining it, suppressing it, or replacing it. We then probed your memory of one item's position. The aim of this study is to test if semantic activation reduces your ability to suppress the individual items in that list. The results of this study will improve our understanding of when people are good at controlling their thoughts and when they are not, which in its extreme could result in symptoms of psychological disorders such as rumination and thought intrusions.\n\nYour participation is greatly appreciated! If you have any questions, please feel free to email me at {edjoeleung@utexas.edu}. THANK YOU!!",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.035,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var WelcomeMaxDurationReached;
var _welcome_keyResp_allKeys;
var WelcomeMaxDuration;
var WelcomeComponents;
function WelcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Welcome' ---
    t = 0;
    WelcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    WelcomeMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData("stim_set", set_num);
    
    welcome_keyResp.keys = undefined;
    welcome_keyResp.rt = undefined;
    _welcome_keyResp_allKeys = [];
    psychoJS.experiment.addData('Welcome.started', globalClock.getTime());
    WelcomeMaxDuration = null
    // keep track of which components have finished
    WelcomeComponents = [];
    WelcomeComponents.push(welcome_text);
    WelcomeComponents.push(welcome_keyResp);
    
    for (const thisComponent of WelcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function WelcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Welcome' ---
    // get current time
    t = WelcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcome_text* updates
    if (t >= 0.0 && welcome_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_text.tStart = t;  // (not accounting for frame time here)
      welcome_text.frameNStart = frameN;  // exact frame index
      
      welcome_text.setAutoDraw(true);
    }
    
    
    // *welcome_keyResp* updates
    if (t >= 0.0 && welcome_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_keyResp.tStart = t;  // (not accounting for frame time here)
      welcome_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { welcome_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { welcome_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { welcome_keyResp.clearEvents(); });
    }
    
    if (welcome_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = welcome_keyResp.getKeys({keyList: ['space'], waitRelease: false});
      _welcome_keyResp_allKeys = _welcome_keyResp_allKeys.concat(theseKeys);
      if (_welcome_keyResp_allKeys.length > 0) {
        welcome_keyResp.keys = _welcome_keyResp_allKeys[_welcome_keyResp_allKeys.length - 1].name;  // just the last key pressed
        welcome_keyResp.rt = _welcome_keyResp_allKeys[_welcome_keyResp_allKeys.length - 1].rt;
        welcome_keyResp.duration = _welcome_keyResp_allKeys[_welcome_keyResp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of WelcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WelcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Welcome' ---
    for (const thisComponent of WelcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Welcome.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(welcome_keyResp.corr, level);
    }
    psychoJS.experiment.addData('welcome_keyResp.keys', welcome_keyResp.keys);
    if (typeof welcome_keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('welcome_keyResp.rt', welcome_keyResp.rt);
        psychoJS.experiment.addData('welcome_keyResp.duration', welcome_keyResp.duration);
        routineTimer.reset();
        }
    
    welcome_keyResp.stop();
    // the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Encode_instructMaxDurationReached;
var _encode_instruct_keyResp_allKeys;
var Encode_instructMaxDuration;
var Encode_instructComponents;
function Encode_instructRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Encode_instruct' ---
    t = 0;
    Encode_instructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Encode_instructMaxDurationReached = false;
    // update component parameters for each repeat
    encode_instruct_keyResp.keys = undefined;
    encode_instruct_keyResp.rt = undefined;
    _encode_instruct_keyResp_allKeys = [];
    psychoJS.experiment.addData('Encode_instruct.started', globalClock.getTime());
    Encode_instructMaxDuration = null
    // keep track of which components have finished
    Encode_instructComponents = [];
    Encode_instructComponents.push(encode_instruct_img);
    Encode_instructComponents.push(encode_instruct_cont_text);
    Encode_instructComponents.push(encode_instruct_keyResp);
    
    for (const thisComponent of Encode_instructComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Encode_instructRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Encode_instruct' ---
    // get current time
    t = Encode_instructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *encode_instruct_img* updates
    if (t >= 0.0 && encode_instruct_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      encode_instruct_img.tStart = t;  // (not accounting for frame time here)
      encode_instruct_img.frameNStart = frameN;  // exact frame index
      
      encode_instruct_img.setAutoDraw(true);
    }
    
    
    // *encode_instruct_cont_text* updates
    if (t >= 0.0 && encode_instruct_cont_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      encode_instruct_cont_text.tStart = t;  // (not accounting for frame time here)
      encode_instruct_cont_text.frameNStart = frameN;  // exact frame index
      
      encode_instruct_cont_text.setAutoDraw(true);
    }
    
    
    // *encode_instruct_keyResp* updates
    if (t >= 0.0 && encode_instruct_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      encode_instruct_keyResp.tStart = t;  // (not accounting for frame time here)
      encode_instruct_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { encode_instruct_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { encode_instruct_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { encode_instruct_keyResp.clearEvents(); });
    }
    
    if (encode_instruct_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = encode_instruct_keyResp.getKeys({keyList: ['space'], waitRelease: false});
      _encode_instruct_keyResp_allKeys = _encode_instruct_keyResp_allKeys.concat(theseKeys);
      if (_encode_instruct_keyResp_allKeys.length > 0) {
        encode_instruct_keyResp.keys = _encode_instruct_keyResp_allKeys[_encode_instruct_keyResp_allKeys.length - 1].name;  // just the last key pressed
        encode_instruct_keyResp.rt = _encode_instruct_keyResp_allKeys[_encode_instruct_keyResp_allKeys.length - 1].rt;
        encode_instruct_keyResp.duration = _encode_instruct_keyResp_allKeys[_encode_instruct_keyResp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Encode_instructComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Encode_instructRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Encode_instruct' ---
    for (const thisComponent of Encode_instructComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Encode_instruct.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(encode_instruct_keyResp.corr, level);
    }
    psychoJS.experiment.addData('encode_instruct_keyResp.keys', encode_instruct_keyResp.keys);
    if (typeof encode_instruct_keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('encode_instruct_keyResp.rt', encode_instruct_keyResp.rt);
        psychoJS.experiment.addData('encode_instruct_keyResp.duration', encode_instruct_keyResp.duration);
        routineTimer.reset();
        }
    
    encode_instruct_keyResp.stop();
    // the Routine "Encode_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Oper_screen_instructMaxDurationReached;
var _operscreen_instruct_keyResp_allKeys;
var Oper_screen_instructMaxDuration;
var Oper_screen_instructComponents;
function Oper_screen_instructRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Oper_screen_instruct' ---
    t = 0;
    Oper_screen_instructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Oper_screen_instructMaxDurationReached = false;
    // update component parameters for each repeat
    operscreen_instruct_keyResp.keys = undefined;
    operscreen_instruct_keyResp.rt = undefined;
    _operscreen_instruct_keyResp_allKeys = [];
    psychoJS.experiment.addData('Oper_screen_instruct.started', globalClock.getTime());
    Oper_screen_instructMaxDuration = null
    // keep track of which components have finished
    Oper_screen_instructComponents = [];
    Oper_screen_instructComponents.push(operscreen_instruct_img);
    Oper_screen_instructComponents.push(operscreen_instruct_cont_text);
    Oper_screen_instructComponents.push(operscreen_instruct_keyResp);
    
    for (const thisComponent of Oper_screen_instructComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Oper_screen_instructRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Oper_screen_instruct' ---
    // get current time
    t = Oper_screen_instructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *operscreen_instruct_img* updates
    if (t >= 0.0 && operscreen_instruct_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      operscreen_instruct_img.tStart = t;  // (not accounting for frame time here)
      operscreen_instruct_img.frameNStart = frameN;  // exact frame index
      
      operscreen_instruct_img.setAutoDraw(true);
    }
    
    
    // *operscreen_instruct_cont_text* updates
    if (t >= 0.0 && operscreen_instruct_cont_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      operscreen_instruct_cont_text.tStart = t;  // (not accounting for frame time here)
      operscreen_instruct_cont_text.frameNStart = frameN;  // exact frame index
      
      operscreen_instruct_cont_text.setAutoDraw(true);
    }
    
    
    // *operscreen_instruct_keyResp* updates
    if (t >= 0.0 && operscreen_instruct_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      operscreen_instruct_keyResp.tStart = t;  // (not accounting for frame time here)
      operscreen_instruct_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { operscreen_instruct_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { operscreen_instruct_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { operscreen_instruct_keyResp.clearEvents(); });
    }
    
    if (operscreen_instruct_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = operscreen_instruct_keyResp.getKeys({keyList: ['space'], waitRelease: false});
      _operscreen_instruct_keyResp_allKeys = _operscreen_instruct_keyResp_allKeys.concat(theseKeys);
      if (_operscreen_instruct_keyResp_allKeys.length > 0) {
        operscreen_instruct_keyResp.keys = _operscreen_instruct_keyResp_allKeys[_operscreen_instruct_keyResp_allKeys.length - 1].name;  // just the last key pressed
        operscreen_instruct_keyResp.rt = _operscreen_instruct_keyResp_allKeys[_operscreen_instruct_keyResp_allKeys.length - 1].rt;
        operscreen_instruct_keyResp.duration = _operscreen_instruct_keyResp_allKeys[_operscreen_instruct_keyResp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Oper_screen_instructComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Oper_screen_instructRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Oper_screen_instruct' ---
    for (const thisComponent of Oper_screen_instructComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Oper_screen_instruct.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(operscreen_instruct_keyResp.corr, level);
    }
    psychoJS.experiment.addData('operscreen_instruct_keyResp.keys', operscreen_instruct_keyResp.keys);
    if (typeof operscreen_instruct_keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('operscreen_instruct_keyResp.rt', operscreen_instruct_keyResp.rt);
        psychoJS.experiment.addData('operscreen_instruct_keyResp.duration', operscreen_instruct_keyResp.duration);
        routineTimer.reset();
        }
    
    operscreen_instruct_keyResp.stop();
    // the Routine "Oper_screen_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Operations_instructMaxDurationReached;
var _operations_instruct_keyResp_allKeys;
var Operations_instructMaxDuration;
var Operations_instructComponents;
function Operations_instructRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Operations_instruct' ---
    t = 0;
    Operations_instructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Operations_instructMaxDurationReached = false;
    // update component parameters for each repeat
    operations_instruct_keyResp.keys = undefined;
    operations_instruct_keyResp.rt = undefined;
    _operations_instruct_keyResp_allKeys = [];
    psychoJS.experiment.addData('Operations_instruct.started', globalClock.getTime());
    Operations_instructMaxDuration = null
    // keep track of which components have finished
    Operations_instructComponents = [];
    Operations_instructComponents.push(operations_instruct_img);
    Operations_instructComponents.push(operations_instruct_conttext);
    Operations_instructComponents.push(operations_instruct_keyResp);
    
    for (const thisComponent of Operations_instructComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Operations_instructRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Operations_instruct' ---
    // get current time
    t = Operations_instructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *operations_instruct_img* updates
    if (t >= 0.0 && operations_instruct_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      operations_instruct_img.tStart = t;  // (not accounting for frame time here)
      operations_instruct_img.frameNStart = frameN;  // exact frame index
      
      operations_instruct_img.setAutoDraw(true);
    }
    
    
    // *operations_instruct_conttext* updates
    if (t >= 0.0 && operations_instruct_conttext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      operations_instruct_conttext.tStart = t;  // (not accounting for frame time here)
      operations_instruct_conttext.frameNStart = frameN;  // exact frame index
      
      operations_instruct_conttext.setAutoDraw(true);
    }
    
    
    // *operations_instruct_keyResp* updates
    if (t >= 0.0 && operations_instruct_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      operations_instruct_keyResp.tStart = t;  // (not accounting for frame time here)
      operations_instruct_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { operations_instruct_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { operations_instruct_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { operations_instruct_keyResp.clearEvents(); });
    }
    
    if (operations_instruct_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = operations_instruct_keyResp.getKeys({keyList: ['space'], waitRelease: false});
      _operations_instruct_keyResp_allKeys = _operations_instruct_keyResp_allKeys.concat(theseKeys);
      if (_operations_instruct_keyResp_allKeys.length > 0) {
        operations_instruct_keyResp.keys = _operations_instruct_keyResp_allKeys[_operations_instruct_keyResp_allKeys.length - 1].name;  // just the last key pressed
        operations_instruct_keyResp.rt = _operations_instruct_keyResp_allKeys[_operations_instruct_keyResp_allKeys.length - 1].rt;
        operations_instruct_keyResp.duration = _operations_instruct_keyResp_allKeys[_operations_instruct_keyResp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Operations_instructComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Operations_instructRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Operations_instruct' ---
    for (const thisComponent of Operations_instructComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Operations_instruct.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(operations_instruct_keyResp.corr, level);
    }
    psychoJS.experiment.addData('operations_instruct_keyResp.keys', operations_instruct_keyResp.keys);
    if (typeof operations_instruct_keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('operations_instruct_keyResp.rt', operations_instruct_keyResp.rt);
        psychoJS.experiment.addData('operations_instruct_keyResp.duration', operations_instruct_keyResp.duration);
        routineTimer.reset();
        }
    
    operations_instruct_keyResp.stop();
    // the Routine "Operations_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Probe_screen_instructMaxDurationReached;
var _probescreen_instruct_keyResp_allKeys;
var Probe_screen_instructMaxDuration;
var Probe_screen_instructComponents;
function Probe_screen_instructRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Probe_screen_instruct' ---
    t = 0;
    Probe_screen_instructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Probe_screen_instructMaxDurationReached = false;
    // update component parameters for each repeat
    probescreen_instruct_keyResp.keys = undefined;
    probescreen_instruct_keyResp.rt = undefined;
    _probescreen_instruct_keyResp_allKeys = [];
    psychoJS.experiment.addData('Probe_screen_instruct.started', globalClock.getTime());
    Probe_screen_instructMaxDuration = null
    // keep track of which components have finished
    Probe_screen_instructComponents = [];
    Probe_screen_instructComponents.push(probescreen_instruct_img);
    Probe_screen_instructComponents.push(probescreen_instruct_conttext);
    Probe_screen_instructComponents.push(probescreen_instruct_keyResp);
    
    for (const thisComponent of Probe_screen_instructComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Probe_screen_instructRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Probe_screen_instruct' ---
    // get current time
    t = Probe_screen_instructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *probescreen_instruct_img* updates
    if (t >= 0.0 && probescreen_instruct_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      probescreen_instruct_img.tStart = t;  // (not accounting for frame time here)
      probescreen_instruct_img.frameNStart = frameN;  // exact frame index
      
      probescreen_instruct_img.setAutoDraw(true);
    }
    
    
    // *probescreen_instruct_conttext* updates
    if (t >= 0.0 && probescreen_instruct_conttext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      probescreen_instruct_conttext.tStart = t;  // (not accounting for frame time here)
      probescreen_instruct_conttext.frameNStart = frameN;  // exact frame index
      
      probescreen_instruct_conttext.setAutoDraw(true);
    }
    
    
    // *probescreen_instruct_keyResp* updates
    if (t >= 0.0 && probescreen_instruct_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      probescreen_instruct_keyResp.tStart = t;  // (not accounting for frame time here)
      probescreen_instruct_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { probescreen_instruct_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { probescreen_instruct_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { probescreen_instruct_keyResp.clearEvents(); });
    }
    
    if (probescreen_instruct_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = probescreen_instruct_keyResp.getKeys({keyList: ['space'], waitRelease: false});
      _probescreen_instruct_keyResp_allKeys = _probescreen_instruct_keyResp_allKeys.concat(theseKeys);
      if (_probescreen_instruct_keyResp_allKeys.length > 0) {
        probescreen_instruct_keyResp.keys = _probescreen_instruct_keyResp_allKeys[_probescreen_instruct_keyResp_allKeys.length - 1].name;  // just the last key pressed
        probescreen_instruct_keyResp.rt = _probescreen_instruct_keyResp_allKeys[_probescreen_instruct_keyResp_allKeys.length - 1].rt;
        probescreen_instruct_keyResp.duration = _probescreen_instruct_keyResp_allKeys[_probescreen_instruct_keyResp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Probe_screen_instructComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Probe_screen_instructRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Probe_screen_instruct' ---
    for (const thisComponent of Probe_screen_instructComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Probe_screen_instruct.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(probescreen_instruct_keyResp.corr, level);
    }
    psychoJS.experiment.addData('probescreen_instruct_keyResp.keys', probescreen_instruct_keyResp.keys);
    if (typeof probescreen_instruct_keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('probescreen_instruct_keyResp.rt', probescreen_instruct_keyResp.rt);
        psychoJS.experiment.addData('probescreen_instruct_keyResp.duration', probescreen_instruct_keyResp.duration);
        routineTimer.reset();
        }
    
    probescreen_instruct_keyResp.stop();
    // the Routine "Probe_screen_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Probe_instructMaxDurationReached;
var _probe_instructions_keyResp_allKeys;
var Probe_instructMaxDuration;
var Probe_instructComponents;
function Probe_instructRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Probe_instruct' ---
    t = 0;
    Probe_instructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Probe_instructMaxDurationReached = false;
    // update component parameters for each repeat
    probe_instructions_keyResp.keys = undefined;
    probe_instructions_keyResp.rt = undefined;
    _probe_instructions_keyResp_allKeys = [];
    psychoJS.experiment.addData('Probe_instruct.started', globalClock.getTime());
    Probe_instructMaxDuration = null
    // keep track of which components have finished
    Probe_instructComponents = [];
    Probe_instructComponents.push(probe_instructions_img);
    Probe_instructComponents.push(probe_instructions_conttext);
    Probe_instructComponents.push(probe_instructions_keyResp);
    
    for (const thisComponent of Probe_instructComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Probe_instructRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Probe_instruct' ---
    // get current time
    t = Probe_instructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *probe_instructions_img* updates
    if (t >= 0.0 && probe_instructions_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      probe_instructions_img.tStart = t;  // (not accounting for frame time here)
      probe_instructions_img.frameNStart = frameN;  // exact frame index
      
      probe_instructions_img.setAutoDraw(true);
    }
    
    
    // *probe_instructions_conttext* updates
    if (t >= 0.0 && probe_instructions_conttext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      probe_instructions_conttext.tStart = t;  // (not accounting for frame time here)
      probe_instructions_conttext.frameNStart = frameN;  // exact frame index
      
      probe_instructions_conttext.setAutoDraw(true);
    }
    
    
    // *probe_instructions_keyResp* updates
    if (t >= 0.0 && probe_instructions_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      probe_instructions_keyResp.tStart = t;  // (not accounting for frame time here)
      probe_instructions_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { probe_instructions_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { probe_instructions_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { probe_instructions_keyResp.clearEvents(); });
    }
    
    if (probe_instructions_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = probe_instructions_keyResp.getKeys({keyList: ['space'], waitRelease: false});
      _probe_instructions_keyResp_allKeys = _probe_instructions_keyResp_allKeys.concat(theseKeys);
      if (_probe_instructions_keyResp_allKeys.length > 0) {
        probe_instructions_keyResp.keys = _probe_instructions_keyResp_allKeys[_probe_instructions_keyResp_allKeys.length - 1].name;  // just the last key pressed
        probe_instructions_keyResp.rt = _probe_instructions_keyResp_allKeys[_probe_instructions_keyResp_allKeys.length - 1].rt;
        probe_instructions_keyResp.duration = _probe_instructions_keyResp_allKeys[_probe_instructions_keyResp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Probe_instructComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Probe_instructRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Probe_instruct' ---
    for (const thisComponent of Probe_instructComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Probe_instruct.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(probe_instructions_keyResp.corr, level);
    }
    psychoJS.experiment.addData('probe_instructions_keyResp.keys', probe_instructions_keyResp.keys);
    if (typeof probe_instructions_keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('probe_instructions_keyResp.rt', probe_instructions_keyResp.rt);
        psychoJS.experiment.addData('probe_instructions_keyResp.duration', probe_instructions_keyResp.duration);
        routineTimer.reset();
        }
    
    probe_instructions_keyResp.stop();
    // the Routine "Probe_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Practice_beginMaxDurationReached;
var _prac_begin_keyResp_allKeys;
var Practice_beginMaxDuration;
var Practice_beginComponents;
function Practice_beginRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Practice_begin' ---
    t = 0;
    Practice_beginClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Practice_beginMaxDurationReached = false;
    // update component parameters for each repeat
    prac_begin_keyResp.keys = undefined;
    prac_begin_keyResp.rt = undefined;
    _prac_begin_keyResp_allKeys = [];
    // Run 'Begin Routine' code from corrinit_code
    corr = 0;
    
    psychoJS.experiment.addData('Practice_begin.started', globalClock.getTime());
    Practice_beginMaxDuration = null
    // keep track of which components have finished
    Practice_beginComponents = [];
    Practice_beginComponents.push(prac_begin_text);
    Practice_beginComponents.push(prac_begin_keyResp);
    
    for (const thisComponent of Practice_beginComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Practice_beginRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Practice_begin' ---
    // get current time
    t = Practice_beginClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prac_begin_text* updates
    if (t >= 0.0 && prac_begin_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_begin_text.tStart = t;  // (not accounting for frame time here)
      prac_begin_text.frameNStart = frameN;  // exact frame index
      
      prac_begin_text.setAutoDraw(true);
    }
    
    
    // *prac_begin_keyResp* updates
    if (t >= 0.0 && prac_begin_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_begin_keyResp.tStart = t;  // (not accounting for frame time here)
      prac_begin_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { prac_begin_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { prac_begin_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { prac_begin_keyResp.clearEvents(); });
    }
    
    if (prac_begin_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = prac_begin_keyResp.getKeys({keyList: ['return'], waitRelease: false});
      _prac_begin_keyResp_allKeys = _prac_begin_keyResp_allKeys.concat(theseKeys);
      if (_prac_begin_keyResp_allKeys.length > 0) {
        prac_begin_keyResp.keys = _prac_begin_keyResp_allKeys[_prac_begin_keyResp_allKeys.length - 1].name;  // just the last key pressed
        prac_begin_keyResp.rt = _prac_begin_keyResp_allKeys[_prac_begin_keyResp_allKeys.length - 1].rt;
        prac_begin_keyResp.duration = _prac_begin_keyResp_allKeys[_prac_begin_keyResp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Practice_beginComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Practice_beginRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Practice_begin' ---
    for (const thisComponent of Practice_beginComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Practice_begin.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(prac_begin_keyResp.corr, level);
    }
    psychoJS.experiment.addData('prac_begin_keyResp.keys', prac_begin_keyResp.keys);
    if (typeof prac_begin_keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('prac_begin_keyResp.rt', prac_begin_keyResp.rt);
        psychoJS.experiment.addData('prac_begin_keyResp.duration', prac_begin_keyResp.duration);
        routineTimer.reset();
        }
    
    prac_begin_keyResp.stop();
    // the Routine "Practice_begin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Trial_prepareMaxDurationReached;
var Trial_prepareMaxDuration;
var Trial_prepareComponents;
function Trial_prepareRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Trial_prepare' ---
    t = 0;
    Trial_prepareClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    Trial_prepareMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('Trial_prepare.started', globalClock.getTime());
    Trial_prepareMaxDuration = null
    // keep track of which components have finished
    Trial_prepareComponents = [];
    Trial_prepareComponents.push(Trial_prepare_text);
    
    for (const thisComponent of Trial_prepareComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function Trial_prepareRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Trial_prepare' ---
    // get current time
    t = Trial_prepareClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    if (Trial_prepare_text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      Trial_prepare_text.setText(`The trial will begin in ${util.pad(Number.parseFloat((5 - t)).toFixed(0), 1)} s.`, false);
    }
    
    // *Trial_prepare_text* updates
    if (t >= 0.0 && Trial_prepare_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Trial_prepare_text.tStart = t;  // (not accounting for frame time here)
      Trial_prepare_text.frameNStart = frameN;  // exact frame index
      
      Trial_prepare_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Trial_prepare_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Trial_prepare_text.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Trial_prepareComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Trial_prepareRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Trial_prepare' ---
    for (const thisComponent of Trial_prepareComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Trial_prepare.stopped', globalClock.getTime());
    if (Trial_prepareMaxDurationReached) {
        routineTimer.add(Trial_prepareMaxDuration);
    } else {
        routineTimer.add(-5.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var prac_trials;
function prac_trialsLoopBegin(prac_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    prac_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'stimuli/csvs/maintask_stimlists/prac_stim_list.csv',
      seed: undefined, name: 'prac_trials'
    });
    psychoJS.experiment.addLoop(prac_trials); // add the loop to the experiment
    currentLoop = prac_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPrac_trial of prac_trials) {
      snapshot = prac_trials.getSnapshot();
      prac_trialsLoopScheduler.add(importConditions(snapshot));
      prac_trialsLoopScheduler.add(EncodeRoutineBegin(snapshot));
      prac_trialsLoopScheduler.add(EncodeRoutineEachFrame());
      prac_trialsLoopScheduler.add(EncodeRoutineEnd(snapshot));
      prac_trialsLoopScheduler.add(Delay_2000RoutineBegin(snapshot));
      prac_trialsLoopScheduler.add(Delay_2000RoutineEachFrame());
      prac_trialsLoopScheduler.add(Delay_2000RoutineEnd(snapshot));
      prac_trialsLoopScheduler.add(ManipulateRoutineBegin(snapshot));
      prac_trialsLoopScheduler.add(ManipulateRoutineEachFrame());
      prac_trialsLoopScheduler.add(ManipulateRoutineEnd(snapshot));
      prac_trialsLoopScheduler.add(Delay_4000RoutineBegin(snapshot));
      prac_trialsLoopScheduler.add(Delay_4000RoutineEachFrame());
      prac_trialsLoopScheduler.add(Delay_4000RoutineEnd(snapshot));
      prac_trialsLoopScheduler.add(ProbeRoutineBegin(snapshot));
      prac_trialsLoopScheduler.add(ProbeRoutineEachFrame());
      prac_trialsLoopScheduler.add(ProbeRoutineEnd(snapshot));
      prac_trialsLoopScheduler.add(ITIRoutineBegin(snapshot));
      prac_trialsLoopScheduler.add(ITIRoutineEachFrame());
      prac_trialsLoopScheduler.add(ITIRoutineEnd(snapshot));
      prac_trialsLoopScheduler.add(prac_trialsLoopEndIteration(prac_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function prac_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(prac_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function prac_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: stim_list,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(EncodeRoutineBegin(snapshot));
      trialsLoopScheduler.add(EncodeRoutineEachFrame());
      trialsLoopScheduler.add(EncodeRoutineEnd(snapshot));
      trialsLoopScheduler.add(Delay_2000RoutineBegin(snapshot));
      trialsLoopScheduler.add(Delay_2000RoutineEachFrame());
      trialsLoopScheduler.add(Delay_2000RoutineEnd(snapshot));
      trialsLoopScheduler.add(ManipulateRoutineBegin(snapshot));
      trialsLoopScheduler.add(ManipulateRoutineEachFrame());
      trialsLoopScheduler.add(ManipulateRoutineEnd(snapshot));
      trialsLoopScheduler.add(Delay_4000RoutineBegin(snapshot));
      trialsLoopScheduler.add(Delay_4000RoutineEachFrame());
      trialsLoopScheduler.add(Delay_4000RoutineEnd(snapshot));
      trialsLoopScheduler.add(ProbeRoutineBegin(snapshot));
      trialsLoopScheduler.add(ProbeRoutineEachFrame());
      trialsLoopScheduler.add(ProbeRoutineEnd(snapshot));
      trialsLoopScheduler.add(ITIRoutineBegin(snapshot));
      trialsLoopScheduler.add(ITIRoutineEachFrame());
      trialsLoopScheduler.add(ITIRoutineEnd(snapshot));
      const rest_loopLoopScheduler = new Scheduler(psychoJS);
      trialsLoopScheduler.add(rest_loopLoopBegin(rest_loopLoopScheduler, snapshot));
      trialsLoopScheduler.add(rest_loopLoopScheduler);
      trialsLoopScheduler.add(rest_loopLoopEnd);
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var rest_loop;
function rest_loopLoopBegin(rest_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    rest_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: rest_trigger, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'rest_loop'
    });
    psychoJS.experiment.addLoop(rest_loop); // add the loop to the experiment
    currentLoop = rest_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisRest_loop of rest_loop) {
      snapshot = rest_loop.getSnapshot();
      rest_loopLoopScheduler.add(importConditions(snapshot));
      rest_loopLoopScheduler.add(RestRoutineBegin(snapshot));
      rest_loopLoopScheduler.add(RestRoutineEachFrame());
      rest_loopLoopScheduler.add(RestRoutineEnd(snapshot));
      rest_loopLoopScheduler.add(Trial_prepareRoutineBegin(snapshot));
      rest_loopLoopScheduler.add(Trial_prepareRoutineEachFrame());
      rest_loopLoopScheduler.add(Trial_prepareRoutineEnd(snapshot));
      rest_loopLoopScheduler.add(rest_loopLoopEndIteration(rest_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function rest_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(rest_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function rest_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var EncodeMaxDurationReached;
var EncodeMaxDuration;
var EncodeComponents;
function EncodeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Encode' ---
    t = 0;
    EncodeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    EncodeMaxDurationReached = false;
    // update component parameters for each repeat
    img_1_left.setImage(encode_1_img);
    img_2_right.setImage(encode_2_img);
    psychoJS.experiment.addData('Encode.started', globalClock.getTime());
    EncodeMaxDuration = null
    // keep track of which components have finished
    EncodeComponents = [];
    EncodeComponents.push(encode_fixation);
    EncodeComponents.push(img_1_left);
    EncodeComponents.push(img_2_right);
    
    for (const thisComponent of EncodeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EncodeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Encode' ---
    // get current time
    t = EncodeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *encode_fixation* updates
    if (t >= 0.0 && encode_fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      encode_fixation.tStart = t;  // (not accounting for frame time here)
      encode_fixation.frameNStart = frameN;  // exact frame index
      
      encode_fixation.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (encode_fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      encode_fixation.setAutoDraw(false);
    }
    
    
    // *img_1_left* updates
    if (t >= 0.0 && img_1_left.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      img_1_left.tStart = t;  // (not accounting for frame time here)
      img_1_left.frameNStart = frameN;  // exact frame index
      
      img_1_left.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (img_1_left.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      img_1_left.setAutoDraw(false);
    }
    
    
    // *img_2_right* updates
    if (t >= 0.0 && img_2_right.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      img_2_right.tStart = t;  // (not accounting for frame time here)
      img_2_right.frameNStart = frameN;  // exact frame index
      
      img_2_right.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (img_2_right.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      img_2_right.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EncodeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EncodeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Encode' ---
    for (const thisComponent of EncodeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Encode.stopped', globalClock.getTime());
    if (EncodeMaxDurationReached) {
        routineTimer.add(EncodeMaxDuration);
    } else {
        routineTimer.add(-2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Delay_2000MaxDurationReached;
var Delay_2000MaxDuration;
var Delay_2000Components;
function Delay_2000RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Delay_2000' ---
    t = 0;
    Delay_2000Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    Delay_2000MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('Delay_2000.started', globalClock.getTime());
    Delay_2000MaxDuration = null
    // keep track of which components have finished
    Delay_2000Components = [];
    Delay_2000Components.push(delay_fixation_2000);
    
    for (const thisComponent of Delay_2000Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Delay_2000RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Delay_2000' ---
    // get current time
    t = Delay_2000Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *delay_fixation_2000* updates
    if (t >= 0.0 && delay_fixation_2000.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      delay_fixation_2000.tStart = t;  // (not accounting for frame time here)
      delay_fixation_2000.frameNStart = frameN;  // exact frame index
      
      delay_fixation_2000.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (delay_fixation_2000.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      delay_fixation_2000.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Delay_2000Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Delay_2000RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Delay_2000' ---
    for (const thisComponent of Delay_2000Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Delay_2000.stopped', globalClock.getTime());
    if (Delay_2000MaxDurationReached) {
        routineTimer.add(Delay_2000MaxDuration);
    } else {
        routineTimer.add(-2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ManipulateMaxDurationReached;
var cuepos;
var ManipulateMaxDuration;
var ManipulateComponents;
function ManipulateRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Manipulate' ---
    t = 0;
    ManipulateClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    ManipulateMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from cue_position_code
    if ((cue_position === "left")) {
        cuepos = [(- 0.3), 0];
    } else {
        if ((cue_position === "right")) {
            cuepos = [0.3, 0];
        }
    }
    console.log("cue_position = ", cue_position);
    
    manipulate_cue.setPos(cuepos);
    manipulate_cue.setImage(replace_img);
    psychoJS.experiment.addData('Manipulate.started', globalClock.getTime());
    ManipulateMaxDuration = null
    // keep track of which components have finished
    ManipulateComponents = [];
    ManipulateComponents.push(manipulate_cue);
    ManipulateComponents.push(manipulate_fixation);
    
    for (const thisComponent of ManipulateComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ManipulateRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Manipulate' ---
    // get current time
    t = ManipulateClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *manipulate_cue* updates
    if (t >= 0.0 && manipulate_cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      manipulate_cue.tStart = t;  // (not accounting for frame time here)
      manipulate_cue.frameNStart = frameN;  // exact frame index
      
      manipulate_cue.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (manipulate_cue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      manipulate_cue.setAutoDraw(false);
    }
    
    
    // *manipulate_fixation* updates
    if (t >= 0.0 && manipulate_fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      manipulate_fixation.tStart = t;  // (not accounting for frame time here)
      manipulate_fixation.frameNStart = frameN;  // exact frame index
      
      manipulate_fixation.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (manipulate_fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      manipulate_fixation.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ManipulateComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ManipulateRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Manipulate' ---
    for (const thisComponent of ManipulateComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Manipulate.stopped', globalClock.getTime());
    if (ManipulateMaxDurationReached) {
        routineTimer.add(ManipulateMaxDuration);
    } else {
        routineTimer.add(-2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Delay_4000MaxDurationReached;
var Delay_4000MaxDuration;
var Delay_4000Components;
function Delay_4000RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Delay_4000' ---
    t = 0;
    Delay_4000Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    Delay_4000MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('Delay_4000.started', globalClock.getTime());
    Delay_4000MaxDuration = null
    // keep track of which components have finished
    Delay_4000Components = [];
    Delay_4000Components.push(delay_fixation_4000);
    
    for (const thisComponent of Delay_4000Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Delay_4000RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Delay_4000' ---
    // get current time
    t = Delay_4000Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *delay_fixation_4000* updates
    if (t >= 0.0 && delay_fixation_4000.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      delay_fixation_4000.tStart = t;  // (not accounting for frame time here)
      delay_fixation_4000.frameNStart = frameN;  // exact frame index
      
      delay_fixation_4000.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (delay_fixation_4000.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      delay_fixation_4000.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Delay_4000Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Delay_4000RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Delay_4000' ---
    for (const thisComponent of Delay_4000Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Delay_4000.stopped', globalClock.getTime());
    if (Delay_4000MaxDurationReached) {
        routineTimer.add(Delay_4000MaxDuration);
    } else {
        routineTimer.add(-4.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ProbeMaxDurationReached;
var correct_ans;
var keyPressed_probe;
var _probe_keyResp_allKeys;
var ProbeMaxDuration;
var ProbeComponents;
function ProbeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Probe' ---
    t = 0;
    ProbeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    ProbeMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from probe_code
    let correct_ans;
    if (["cued", "uncued", "replacement"].includes(probe_subtype)) {
        correct_ans = "f";
    } else {
        correct_ans = "j";
    }
    keyPressed_probe = undefined;
    probe_image.setImage(probe_img);
    probe_keyResp.keys = undefined;
    probe_keyResp.rt = undefined;
    _probe_keyResp_allKeys = [];
    psychoJS.experiment.addData('Probe.started', globalClock.getTime());
    ProbeMaxDuration = null
    // keep track of which components have finished
    ProbeComponents = [];
    ProbeComponents.push(probe_image);
    ProbeComponents.push(probe_keyResp);
    ProbeComponents.push(yesKey_text);
    ProbeComponents.push(noKey_text);
    
    for (const thisComponent of ProbeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ProbeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Probe' ---
    // get current time
    t = ProbeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *probe_image* updates
    if (t >= 0.0 && probe_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      probe_image.tStart = t;  // (not accounting for frame time here)
      probe_image.frameNStart = frameN;  // exact frame index
      
      probe_image.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (probe_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      probe_image.setAutoDraw(false);
    }
    
    
    // *probe_keyResp* updates
    if (t >= 0.0 && probe_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      probe_keyResp.tStart = t;  // (not accounting for frame time here)
      probe_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { probe_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { probe_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { probe_keyResp.clearEvents(); });
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (probe_keyResp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      probe_keyResp.status = PsychoJS.Status.FINISHED;
        }
      
    if (probe_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = probe_keyResp.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _probe_keyResp_allKeys = _probe_keyResp_allKeys.concat(theseKeys);
      if (_probe_keyResp_allKeys.length > 0) {
        probe_keyResp.keys = _probe_keyResp_allKeys[_probe_keyResp_allKeys.length - 1].name;  // just the last key pressed
        probe_keyResp.rt = _probe_keyResp_allKeys[_probe_keyResp_allKeys.length - 1].rt;
        probe_keyResp.duration = _probe_keyResp_allKeys[_probe_keyResp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *yesKey_text* updates
    if (t >= 0.0 && yesKey_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      yesKey_text.tStart = t;  // (not accounting for frame time here)
      yesKey_text.frameNStart = frameN;  // exact frame index
      
      yesKey_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (yesKey_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      yesKey_text.setAutoDraw(false);
    }
    
    
    // *noKey_text* updates
    if (t >= 0.0 && noKey_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      noKey_text.tStart = t;  // (not accounting for frame time here)
      noKey_text.frameNStart = frameN;  // exact frame index
      
      noKey_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (noKey_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      noKey_text.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ProbeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ProbeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Probe' ---
    for (const thisComponent of ProbeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Probe.stopped', globalClock.getTime());
    // Run 'End Routine' code from probe_code
    try {
        keyPressed_probe = _probe_keyResp_allKeys[_probe_keyResp_allKeys.length - 1].name;
    } catch (e) {
    }
    console.log(keyPressed_probe)
    if ((keyPressed_probe !== undefined) && (keyPressed_probe === correct_ans)) {
        console.log("correct!");
        corr += 1;
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(probe_keyResp.corr, level);
    }
    psychoJS.experiment.addData('probe_keyResp.keys', probe_keyResp.keys);
    if (typeof probe_keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('probe_keyResp.rt', probe_keyResp.rt);
        psychoJS.experiment.addData('probe_keyResp.duration', probe_keyResp.duration);
        routineTimer.reset();
        }
    
    probe_keyResp.stop();
    if (ProbeMaxDurationReached) {
        routineTimer.add(ProbeMaxDuration);
    } else {
        routineTimer.add(-2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ITIMaxDurationReached;
var ITIMaxDuration;
var ITIComponents;
function ITIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ITI' ---
    t = 0;
    ITIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    ITIMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('ITI.started', globalClock.getTime());
    ITIMaxDuration = null
    // keep track of which components have finished
    ITIComponents = [];
    ITIComponents.push(ITI_text);
    
    for (const thisComponent of ITIComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ITIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ITI' ---
    // get current time
    t = ITIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ITI_text* updates
    if (t >= 0.0 && ITI_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ITI_text.tStart = t;  // (not accounting for frame time here)
      ITI_text.frameNStart = frameN;  // exact frame index
      
      ITI_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + jitter - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (ITI_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ITI_text.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ITIComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ITIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ITI' ---
    for (const thisComponent of ITIComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ITI.stopped', globalClock.getTime());
    // the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Practice_endMaxDurationReached;
var _pracend_keyResp_allKeys;
var Practice_endMaxDuration;
var Practice_endComponents;
function Practice_endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Practice_end' ---
    t = 0;
    Practice_endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Practice_endMaxDurationReached = false;
    // update component parameters for each repeat
    practice_continue_text.setText((("That is the end of the practice! Your accuracy was " + corr.toString()) + "/6.\n\nPress <SPACE> to continue!"));
    pracend_keyResp.keys = undefined;
    pracend_keyResp.rt = undefined;
    _pracend_keyResp_allKeys = [];
    psychoJS.experiment.addData('Practice_end.started', globalClock.getTime());
    Practice_endMaxDuration = null
    // keep track of which components have finished
    Practice_endComponents = [];
    Practice_endComponents.push(practice_continue_text);
    Practice_endComponents.push(pracend_keyResp);
    
    for (const thisComponent of Practice_endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Practice_endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Practice_end' ---
    // get current time
    t = Practice_endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practice_continue_text* updates
    if (t >= 0.0 && practice_continue_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_continue_text.tStart = t;  // (not accounting for frame time here)
      practice_continue_text.frameNStart = frameN;  // exact frame index
      
      practice_continue_text.setAutoDraw(true);
    }
    
    
    // *pracend_keyResp* updates
    if (t >= 0.0 && pracend_keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pracend_keyResp.tStart = t;  // (not accounting for frame time here)
      pracend_keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { pracend_keyResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { pracend_keyResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { pracend_keyResp.clearEvents(); });
    }
    
    if (pracend_keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = pracend_keyResp.getKeys({keyList: ['space'], waitRelease: false});
      _pracend_keyResp_allKeys = _pracend_keyResp_allKeys.concat(theseKeys);
      if (_pracend_keyResp_allKeys.length > 0) {
        pracend_keyResp.keys = _pracend_keyResp_allKeys[_pracend_keyResp_allKeys.length - 1].name;  // just the last key pressed
        pracend_keyResp.rt = _pracend_keyResp_allKeys[_pracend_keyResp_allKeys.length - 1].rt;
        pracend_keyResp.duration = _pracend_keyResp_allKeys[_pracend_keyResp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Practice_endComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Practice_endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Practice_end' ---
    for (const thisComponent of Practice_endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Practice_end.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(pracend_keyResp.corr, level);
    }
    psychoJS.experiment.addData('pracend_keyResp.keys', pracend_keyResp.keys);
    if (typeof pracend_keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('pracend_keyResp.rt', pracend_keyResp.rt);
        psychoJS.experiment.addData('pracend_keyResp.duration', pracend_keyResp.duration);
        routineTimer.reset();
        }
    
    pracend_keyResp.stop();
    // the Routine "Practice_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Main_exp_beginMaxDurationReached;
var _main_exp_begin_allKeys;
var Main_exp_beginMaxDuration;
var Main_exp_beginComponents;
function Main_exp_beginRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Main_exp_begin' ---
    t = 0;
    Main_exp_beginClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    Main_exp_beginMaxDurationReached = false;
    // update component parameters for each repeat
    main_exp_begin.keys = undefined;
    main_exp_begin.rt = undefined;
    _main_exp_begin_allKeys = [];
    psychoJS.experiment.addData('Main_exp_begin.started', globalClock.getTime());
    Main_exp_beginMaxDuration = null
    // keep track of which components have finished
    Main_exp_beginComponents = [];
    Main_exp_beginComponents.push(mainexp_begin_text);
    Main_exp_beginComponents.push(main_exp_begin);
    
    for (const thisComponent of Main_exp_beginComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Main_exp_beginRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Main_exp_begin' ---
    // get current time
    t = Main_exp_beginClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *mainexp_begin_text* updates
    if (t >= 0.0 && mainexp_begin_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mainexp_begin_text.tStart = t;  // (not accounting for frame time here)
      mainexp_begin_text.frameNStart = frameN;  // exact frame index
      
      mainexp_begin_text.setAutoDraw(true);
    }
    
    
    // *main_exp_begin* updates
    if (t >= 0.0 && main_exp_begin.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      main_exp_begin.tStart = t;  // (not accounting for frame time here)
      main_exp_begin.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { main_exp_begin.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { main_exp_begin.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { main_exp_begin.clearEvents(); });
    }
    
    if (main_exp_begin.status === PsychoJS.Status.STARTED) {
      let theseKeys = main_exp_begin.getKeys({keyList: ['return'], waitRelease: false});
      _main_exp_begin_allKeys = _main_exp_begin_allKeys.concat(theseKeys);
      if (_main_exp_begin_allKeys.length > 0) {
        main_exp_begin.keys = _main_exp_begin_allKeys[_main_exp_begin_allKeys.length - 1].name;  // just the last key pressed
        main_exp_begin.rt = _main_exp_begin_allKeys[_main_exp_begin_allKeys.length - 1].rt;
        main_exp_begin.duration = _main_exp_begin_allKeys[_main_exp_begin_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Main_exp_beginComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Main_exp_beginRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Main_exp_begin' ---
    for (const thisComponent of Main_exp_beginComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Main_exp_begin.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(main_exp_begin.corr, level);
    }
    psychoJS.experiment.addData('main_exp_begin.keys', main_exp_begin.keys);
    if (typeof main_exp_begin.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('main_exp_begin.rt', main_exp_begin.rt);
        psychoJS.experiment.addData('main_exp_begin.duration', main_exp_begin.duration);
        routineTimer.reset();
        }
    
    main_exp_begin.stop();
    // the Routine "Main_exp_begin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var RestMaxDurationReached;
var _rest_continue_allKeys;
var RestMaxDuration;
var RestComponents;
function RestRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Rest' ---
    t = 0;
    RestClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(30.000000);
    RestMaxDurationReached = false;
    // update component parameters for each repeat
    rest_continue.keys = undefined;
    rest_continue.rt = undefined;
    _rest_continue_allKeys = [];
    psychoJS.experiment.addData('Rest.started', globalClock.getTime());
    RestMaxDuration = null
    // keep track of which components have finished
    RestComponents = [];
    RestComponents.push(rest_exclaim_text);
    RestComponents.push(rest_welcome);
    RestComponents.push(rest_continue);
    RestComponents.push(rest_continue_text);
    
    for (const thisComponent of RestComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function RestRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Rest' ---
    // get current time
    t = RestClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rest_exclaim_text* updates
    if (t >= 0.0 && rest_exclaim_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rest_exclaim_text.tStart = t;  // (not accounting for frame time here)
      rest_exclaim_text.frameNStart = frameN;  // exact frame index
      
      rest_exclaim_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rest_exclaim_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rest_exclaim_text.setAutoDraw(false);
    }
    
    
    if (rest_welcome.status === PsychoJS.Status.STARTED){ // only update if being drawn
      rest_welcome.setText(`Great job completing the run! You have completed ${run_num} out of 6 runs. You may now take a ${util.pad(Number.parseFloat((30 - t)).toFixed(0), 1)} second break!`, false);
    }
    
    // *rest_welcome* updates
    if (t >= 0.0 && rest_welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rest_welcome.tStart = t;  // (not accounting for frame time here)
      rest_welcome.frameNStart = frameN;  // exact frame index
      
      rest_welcome.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rest_welcome.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rest_welcome.setAutoDraw(false);
    }
    
    
    // *rest_continue* updates
    if (t >= 20 && rest_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rest_continue.tStart = t;  // (not accounting for frame time here)
      rest_continue.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rest_continue.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rest_continue.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rest_continue.clearEvents(); });
    }
    
    frameRemains = 30 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if ((rest_continue.status === PsychoJS.Status.STARTED || rest_continue.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      rest_continue.status = PsychoJS.Status.FINISHED;
        }
      
    if (rest_continue.status === PsychoJS.Status.STARTED) {
      let theseKeys = rest_continue.getKeys({keyList: ['space'], waitRelease: false});
      _rest_continue_allKeys = _rest_continue_allKeys.concat(theseKeys);
      if (_rest_continue_allKeys.length > 0) {
        rest_continue.keys = _rest_continue_allKeys[_rest_continue_allKeys.length - 1].name;  // just the last key pressed
        rest_continue.rt = _rest_continue_allKeys[_rest_continue_allKeys.length - 1].rt;
        rest_continue.duration = _rest_continue_allKeys[_rest_continue_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *rest_continue_text* updates
    if (t >= 20 && rest_continue_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rest_continue_text.tStart = t;  // (not accounting for frame time here)
      rest_continue_text.frameNStart = frameN;  // exact frame index
      
      rest_continue_text.setAutoDraw(true);
    }
    
    frameRemains = 30 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if ((rest_continue_text.status === PsychoJS.Status.STARTED || rest_continue_text.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      rest_continue_text.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RestComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function RestRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Rest' ---
    for (const thisComponent of RestComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Rest.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(rest_continue.corr, level);
    }
    psychoJS.experiment.addData('rest_continue.keys', rest_continue.keys);
    if (typeof rest_continue.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rest_continue.rt', rest_continue.rt);
        psychoJS.experiment.addData('rest_continue.duration', rest_continue.duration);
        routineTimer.reset();
        }
    
    rest_continue.stop();
    if (RestMaxDurationReached) {
        routineTimer.add(RestMaxDuration);
    } else {
        routineTimer.add(-30.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var DebriefMaxDurationReached;
var DebriefMaxDuration;
var DebriefComponents;
function DebriefRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Debrief' ---
    t = 0;
    DebriefClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(180.000000);
    DebriefMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('Debrief.started', globalClock.getTime());
    DebriefMaxDuration = null
    // keep track of which components have finished
    DebriefComponents = [];
    DebriefComponents.push(debrief_text);
    
    for (const thisComponent of DebriefComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function DebriefRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Debrief' ---
    // get current time
    t = DebriefClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *debrief_text* updates
    if (t >= 0.0 && debrief_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debrief_text.tStart = t;  // (not accounting for frame time here)
      debrief_text.frameNStart = frameN;  // exact frame index
      
      debrief_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 180 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (debrief_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      debrief_text.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of DebriefComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function DebriefRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Debrief' ---
    for (const thisComponent of DebriefComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Debrief.stopped', globalClock.getTime());
    if (DebriefMaxDurationReached) {
        routineTimer.add(DebriefMaxDuration);
    } else {
        routineTimer.add(-180.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
