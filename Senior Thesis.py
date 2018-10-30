# Senior-Thesis-Project

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average, tile,append,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray, repeat, concatenate)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import random


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)) #.decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'Diag Induc'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=1,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "keyboard_start"
keyboard_startClock = core.Clock()
press_space = visual.TextStim(win=win, name='press_space',
    text=u'Hit the spacebar to begin',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

##----------------------------------------------------------------------------##
##--POTENTIAL WORDS-----------------------------------------------------------##
##----------------------------------------------------------------------------##

word_presented_clock = core.Clock()

diagnostic_word = visual.TextStim(
    win=win, name='diagnostic_word', font=u'Arial', pos=(0, 0),
    height=0.2, wrapWidth=None, ori=0, color=(1.0,0.0,0.0), colorSpace='rgb',
    opacity=1, depth=0.0)

inducer_word = visual.TextStim(
    win=win, name='inducer_word', font=u'Arial', pos=(0, 0),
    height=0.2, wrapWidth=None, ori=0, color=(0.0,1.0,0.0), colorSpace='rgb',
    opacity=1, depth=0.0)

#left for upright, right for italics

#==============================================================================#
#       DYNAMIC PARADIGM ELEMENTS                                              #

trialnum = [24]                 #number of trials/ miniblocks
blocknum = [4]                  #number of blocks
stim_options = [[0,0],[1,2],[2,2],[1,4],[2,3]]         #differing number of stimuli per trial
stim_props = [0,0,1,1,2,2,3,4]
word_list = ['word1','word2','word3','word4','word5','word6','word7','word8','word9','word10',
             'word11','word12','word13','word14','word15','word16','word17','word18','word19','word20',
             'word21','word22','word23','word24','word25','word26','word27','word28','word29','word30',
             'word31','word32','word33','word34','word35','word36','word37','word38','word39','word40']
vert_options = [(0,0.2),(0,-0.2)] #if 0 is above fixation, if 1 is below

#   Mapping to values

keypress    = ['d','j']
congruency  = ['cong','inc']
orientation = ['upright','italic']

#==============================================================================#

#keylogging
#response time, accuracy
#save trial matrix info
#record block, trial, and stimulus number for each stimulus
#proportion thing with neutral block (2,2 instead of 1,3)       DONE
#block instruction/ screen (like block 1 of 4 or whatever)      DONE



##########


##-----------------Assume blocks either mostly inc vs not---------------------##
##----------------------------------------------------------------------------##
##-TRIAL MATRIX AND RANDOMIZATION---------------------------------------------##
##----------------------------------------------------------------------------##

random_binary = [0,1]

block_cong = [[1 if x%2==0 else 0 for x in range(blocknum[0])],
                [0 if x%2==0 else 1 for x in range(blocknum[0])]] #pseudorandom option where two subsequent blocks can't be same
np.random.shuffle(random_binary)
block_ord = block_cong[random_binary[0]]        #choose one of two laternating congruency proportion options (block_cong)

word_i = np.repeat(range(0,len(word_list)),1)  #list of all the indices of words to shufftle
np.random.shuffle(word_i)                       #shuffle the indices
word_list_left_full = word_i[:len(word_list)//2]    #index of word r-s mapped to left key
word_list_right_full = word_i[len(word_list)//2:]   #index of word r-s mapped to right key


#trial matrix for number of stimuli in a given trial
#trialmatrix_full = np.repeat(range(len(stim_options)),trialnum[0]/len(stim_options))      #if not divisible?
trialmatrix_full = np.repeat(stim_props,trialnum[0]/len(stim_props))
np.random.shuffle(trialmatrix_full)

trial_by_block = trialnum[0]//blocknum[0]

stim_italics = [0]  #matrix for whether the stimulus is upright or italicized
vert = [0]          #vertical position of the stimulus presentation
for j in trialmatrix_full:
    total = stim_options[trialmatrix_full[j]][0] + stim_options[trialmatrix_full[j]][1]
    if stim_italics[-1] == 0:
        stim_italics += [1 if x%2==0 else 0 for x in range(total)]
        vert += [1 if x%2==0 else 0 for x in range(total + 2)]
    else:
        stim_italics += [0 if x%2==0 else 1 for x in range(total)]
        vert += [0 if x%2==0 else 1 for x in range(total + 2)]
del stim_italics[0]
del vert[0]
np.random.shuffle(vert)


print("Ratio of stimuli for each trial:")
print(trialmatrix_full)


#trial matrix for stimuli within experiment since don't know number of stim a given trial has

##----------------------------------------------------------------------------##
##---DURATIONS FOR STIMULI----------------------------------------------------##

rs_mapping_duration = 5.000
ISI_cross_duration1 = 1.000
                # or 1500ms
ISI_duration = 2.900
stimulus_duration = 0.600
ITI_cross_duration = 2.900


##----------------------------------------------------------------------------##
##-MAKE THE ISI AND ITI CROSSES-----------------------------------------------##
##----------------------------------------------------------------------------##

#Inter-stimulus interval cross
ISI_cross_clock = core.Clock()
ISI_cross1 = visual.TextStim(
    win=win, name='ISI_cross1', text=u'+', font=u'Arial', pos=(0, 0),
    height=0.2, wrapWidth=None, ori=0, color=u'white', colorSpace='rgb',
    opacity=1, depth=0.0)
    
ISI_cross2 = visual.TextStim(
    win=win, name='ISI_cross2', text=u'+', font=u'Arial', pos=(0, 0),
    height=0.2, wrapWidth=None, ori=0, color=u'white', colorSpace='rgb',
    opacity=1, depth=0.0)

#Inter-trial interval cross
ITI_cross_clock = core.Clock()
ITI_cross = visual.TextStim(
    win=win, name='ITI_cross', text=u'+', font=u'Arial', pos=(0, 0),
    height=0.2, wrapWidth=None, ori=0, color=u'white', colorSpace='rgb',
    opacity=1, depth=0.0)


##----------------------------------------------------------------------------##
##-MAKE SOMETHING-----------------------------------------------##
##----------------------------------------------------------------------------##

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine
trial_clock = core.Clock()

# set up handler to look after randomisation of conditions etc
trials_total = data.TrialHandler(nReps=28, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_total')
thisExp.addLoop(trials_total)  # add the loop to the experiment
thisTrial_2 = trials_total.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))
        
##----------------------------------------------------------------------------##
##-INSTRUCTION SCREEN---------------------------------------------------------##
##----------------------------------------------------------------------------##
        
instruction1 = visual.TextStim(
    win=win, font=u'Arial', name = 'instruction1', pos=(0, 0),
    height=0.2, wrapWidth=None, ori=0, color=u'white', colorSpace='rgb',
    opacity=1, depth=0.0)


##----------------------------------------------------------------------------##
##-EXPERIMENT LOOP------------------------------------------------------------##
##----------------------------------------------------------------------------##

for block in range(0,blocknum[0]):
    
    block_prop = block_ord[block]    #proportion of congruent stimuli -- 0 if mostly congruent
    
    print(str(block))
    
    trialmatrix = trialmatrix_full[:trial_by_block]
    trialmatrix_full = trialmatrix_full[trial_by_block:]
    
    word_list_left = word_list_left_full[:trial_by_block]
    word_list_left_full = word_list_left_full[trial_by_block:]
    word_list_right = word_list_right_full[:trial_by_block]
    word_list_right_full = word_list_right_full[trial_by_block:]
    

    ##      Instructions at the beginning of the block
    instruction1.setText(u"Block " + str(block + 1) + " of " + str(blocknum[0]) + ".\n\nPress space when ready.")
        
    continueRoutineInstruct = True
    
    while (continueRoutineInstruct):
        if (instruction1.status == NOT_STARTED):
            instruction1.setAutoDraw(True)
        if (event.getKeys(keyList=["space"])):
            continueRoutineInstruct = False
            instruction1.setAutoDraw(False)
        if continueRoutineInstruct:
                win.flip()
        
    for trial in range(0,trial_by_block):  #trials per run -- 7 trials
        

        time = 0                        #last stimulus is inducer
        frameN = -1
        continueRoutine = True
        searchquit = 0

        currentLoop = trials_total

        #   Proportions of trial -- blocked 0's and 1's separately

        trial_prop = stim_options[trialmatrix[trial]]
        #print("Selected proportion in current trial:")
        #print(trial_prop)

        prop_sep = [[1 if block_prop == 0 else 0 for x in range(trial_prop[0])],[0 if block_prop == 0 else 1 for x in range(trial_prop[1])]]

        proportion = prop_sep[block_prop] + prop_sep[1-block_prop] #first come 1's, then come 0's (i.e. first number inc, then number cong)
        stimnum = len(proportion)
        
        rand_stim = np.repeat(range(0,stimnum),1)
        np.random.shuffle(rand_stim)
        #print("Stimulus combo for trial: ")
        #print(rand_stim)

        stimmatrix = [stim_italics[:stimnum],                   #whether stim is upright (0) or italics (1)
                      np.repeat(proportion,1)]                  #whether stim is congruent (0) or not (1) 
        trial_vert = vert[:(stimnum + 2)]
        
        #print("Upright vs italics")
        #print(stimmatrix[0])
        #print("Congruent vs not")
        #print(stimmatrix[1])
        #print("Selecting which combo")
        #print(rand_stim)
        
        del stim_italics[:stimnum]
        del vert[:(stimnum + 2)]

        ##-CONSTRUCT STIMULUS WORDS-----------------------------------------##
        word_pair = [word_list[word_list_left[trial]],word_list[word_list_right[trial]]]

        rs_mapping = visual.TextStim(
            win=win, name='diagnostic_word_cong', text=u'If ' + word_pair[0] + ' press D\n' + 'If ' + word_pair[1] + ' press J',
            font=u'Arial', pos=(0, 0), height=0.2, wrapWidth=None, ori=0, color=u'white', colorSpace='rgb', opacity=1, depth=0.0)

        #have diagnostics and crosses constructed for whole trial
        if stimnum != 0:
            diagnostic_words = []
            #ISI_crosses = []
            for x in rand_stim:
                diagnostic_words.append(visual.TextStim(
                    win=win, name='diagnostic_word', text=word_pair[not(stimmatrix[0][x] == stimmatrix[1][x])] ,font=u'Arial', 
                    pos=vert_options[trial_vert[x]],
                    height=0.2, wrapWidth=None, ori=0, color=u'red', colorSpace='rgb',
                    opacity=1, depth=0.0, italic=stimmatrix[0][x]))

        inducer_left_word = visual.TextStim(
            win=win, name='inducer_left_word', text=word_pair[0], font=u'Arial', pos=vert_options[trial_vert[-2]],
            height=0.2, wrapWidth=None, ori=0, color=u'green', colorSpace='rgb',
            opacity=1, depth=0.0)
        inducer_right_word = visual.TextStim(
            win=win, name='inducer_right_word', text=word_pair[1], font=u'Arial', pos=vert_options[trial_vert[-1]],
            height=0.2, wrapWidth=None, ori=0, color=u'green', colorSpace='rgb',
            opacity=1, depth=0.0)

        inducer_pair = [inducer_left_word, inducer_right_word]

        np.random.shuffle(inducer_pair)

        #-------------Initialize starttime values---------------------------------#

        rs_mapping_starttime = 0.000
        ISI_cross_starttime1 = 5.000
        inducer1_starttime = ISI_cross_starttime1 + ISI_cross_duration1
        
        #ISI_cross_starttime2 = ISI_cross_starttime1 + ISI_cross_duration1
        #ISI_cross_duration2 = (ISI_duration*(stimnum+1))+stimulus_duration*(stimnum+2)

        if stimnum != 0:
            diagnostic_starttime = [(ISI_cross_starttime1 + ISI_cross_duration1) +
                                        (stimulus_duration + ISI_duration)*i for i in range(stimnum)]
            inducer1_starttime = diagnostic_starttime[-1] + stimulus_duration + ISI_duration       

        inducer2_starttime = inducer1_starttime + stimulus_duration + ISI_duration
        ITI_cross_starttime = inducer2_starttime + stimulus_duration

        #----------------------------------------------------------------------#



        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))


        ##-SET ISI CROSS------------------------------------------------------##
        trial_clock.reset()  # clock

        ##-SET DIAGNOSTIC SCREEN----------------------------------------------##
        word_presented_clock.reset()    # clock

        routineTimer.add(rs_mapping_duration + ISI_cross_duration1 + (stimnum+1)*ISI_duration + 
            (stimnum+2)*stimulus_duration + ITI_cross_duration + win.monitorFramePeriod)

        ##-START TRIAL ROUTINE------------------------------------------------##
        while continueRoutine: # and routineTimer.getTime() > 0:
            t = trial_clock.getTime()
            frameN = frameN + 1

            #--RS MAPPING SCREEN----------------------------------------------##
            if ((t >= rs_mapping_starttime and rs_mapping.status == NOT_STARTED) or
                (searchquit == 1 and rs_mapping.status == NOT_STARTED)):
                rs_mapping.tStart = 1
                rs_mapping.frameNStart = frameN
                rs_mapping.setAutoDraw(True)
                key_list = []
            frameRemains = rs_mapping_starttime + rs_mapping_duration - win.monitorFramePeriod * 0.75  # most of one frame period left
            if (rs_mapping.status == STARTED and t >= frameRemains):
                rs_mapping.setAutoDraw(False)
                event.clearEvents() #to clear the buffer of any button presses

            #--ISI SCREEN BEFORE DIAGNOSTIC-------------------------##
            if t >= ISI_cross_starttime1 and ISI_cross1.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI_cross1.tStart = t
                ISI_cross1.frameNStart = frameN  # exact frame index                    
                ISI_cross1.setAutoDraw(True)
            frameRemains = ISI_cross_starttime1 + ISI_cross_duration1 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if ISI_cross1.status == STARTED and t >= frameRemains:
                ISI_cross1.setAutoDraw(False)
                ISI_cross2.setAutoDraw(True)
                
            if stimnum != 0: 
                for i in range(stimnum):
                    j = rand_stim[i]
                    corr_key = keypress[stimmatrix[0][j]]
                    if (diagnostic_word.status == NOT_STARTED):
                        key = 'none'
                        time = 'no response'
                        rt = 'no response'
                    #--DIAGNOSTIC ITEMS-------------------------------------##
                    diagnostic_word = diagnostic_words[i]
                    #ISI_cross = ISI_crosses[i]
                    if t >= diagnostic_starttime[i] and diagnostic_word.status == NOT_STARTED:
                        #print("Stimulus number: " + str(i) + " -- stimmatrix input number: " + str(j))
                        # keep track of start time/frame for later
                        tStart = t
                        diagnostic_word.frameNStart = frameN  # exact frame index
                        diagnostic_word.setAutoDraw(True)
                    frameRemains = diagnostic_starttime[i] + stimulus_duration - win.monitorFramePeriod * 0.75  # most of one frame period left
                    frameRemains2 = diagnostic_starttime[i] + stimulus_duration + ISI_duration - win.monitorFramePeriod * 0.75
                    key_list_temp = event.getKeys(keyList=keypress)
                    if (len(key_list_temp) > 0 and len(key_list) == 0):
                        #print("Diagnostic " + str(i))
                        key_list = key_list_temp
                        time1 = t
                        key_list.append(time1)
                        key_list.append((time1)-(tStart)*1000)
                    if (diagnostic_word.status == STARTED and t >= frameRemains):# or (diagnostic_word.status == STARTED and (len(key_list)>0)):
                        diagnostic_word.setAutoDraw(False)
                        diagnostic_word.status = PAUSED
                    if (t >= frameRemains2 and diagnostic_word.status == PAUSED):
                        if len(key_list)==3:
                            key = key_list[0]
                            time = key_list[1]
                            rt = key_list[2]
                            del key_list[0:3]  
                        diagnostic_word.status = FINISHED

                        ## RECORD DATA ON THE STIMULUS
                        thisExp.addData('SubjID', expInfo['participant'])
                        thisExp.addData('Block', block+1)
                        thisExp.addData('Miniblock', trial+1)
                        thisExp.addData('Trial', i+1)
                        thisExp.addData('StimulusType', 'diagnostic')
                        thisExp.addData('Word', diagnostic_word.text)
                        thisExp.addData('WordCongruency', congruency[stimmatrix[1][j]])
                        thisExp.addData('Word Orientation', orientation[int(diagnostic_word.italic)])
                        thisExp.addData('WordPTime', tStart)
                        thisExp.addData('ButtonPress', key)
                        thisExp.addData('Accuracy', int(corr_key == key))
                        thisExp.addData('ButtonPressTime', time)
                        thisExp.addData('RT', rt)
                        thisExp.addData('DiagnosticTime',t-tStart)
                        thisExp.nextEntry()   


            inducer1_word = inducer_pair[0]
            inducer2_word = inducer_pair[1]

            if (inducer1_word.name == inducer_left_word):
                corr_key1 = keypress[0]
                corr_key2 = keypress[1]
            else:
                corr_key1 = keypress[1]
                corr_key2 = keypress[0]

            #--INDUCER ITEM------------------------------------## Keep going here
            if (inducer1_word.status == NOT_STARTED):
                key = 'none'
                time = 'no response'
                rt = 'no response'
            if t >= inducer1_starttime and inducer1_word.status == NOT_STARTED:
                # keep track of start time/frame for later
                #print("First inducer word: " + diagnostic_word.text + " at " + str(t))
                tStart = t
                inducer1_word.frameNStart = frameN  # exact frame index
                inducer1_word.setAutoDraw(True)
            frameRemains = inducer1_starttime + stimulus_duration - win.monitorFramePeriod * 0.75  # most of one frame period left
            frameRemains2 = inducer1_starttime + stimulus_duration + ISI_duration - win.monitorFramePeriod * 0.75
            key_list_temp = event.getKeys(keyList=keypress)
            if (len(key_list_temp) > 0 and len(key_list) == 0):
                key_list = key_list_temp
                time1 = t
                key_list.append(time1)
                key_list.append((time1)-(tStart)*1000)
            if (inducer1_word.status == STARTED and t >= frameRemains):# or (diagnostic_word.status == STARTED and (len(key_list)>0)):
                inducer1_word.setAutoDraw(False)
                inducer1_word.status = PAUSED
            if (t >= frameRemains2 and inducer1_word.status == PAUSED):
                if len(key_list)==3:
                    key = key_list[0]
                    time = key_list[1]
                    rt = key_list[2]
                    del key_list[0:3]  
                inducer1_word.status = FINISHED

                ## RECORD DATA ON THE STIMULUS
                thisExp.addData('SubjID', expInfo['participant'])
                thisExp.addData('Block', block+1)
                thisExp.addData('Miniblock', trial+1)
                thisExp.addData('Trial', stimnum+1)
                thisExp.addData('StimulusType', 'inducer')
                thisExp.addData('Word', inducer1_word.text)
                thisExp.addData('WordCongruency', 'none')
                thisExp.addData('Word Orientation', 'none')
                thisExp.addData('WordPTime', tStart)
                thisExp.addData('ButtonPress', key)
                thisExp.addData('Accuracy', int(corr_key1 == key))
                thisExp.addData('ButtonPressTime', time)
                thisExp.addData('RT', rt)
                thisExp.addData('InducerTime',t-tStart)
                thisExp.nextEntry()   

            if (inducer2_word.status == NOT_STARTED):
                key = 'none'
                time = 'no response'
                rt = 'no response'
            if t >= inducer2_starttime and inducer2_word.status == NOT_STARTED:
                tStart = t
                inducer2_word.frameNStart = frameN  # exact frame index
                inducer2_word.setAutoDraw(True)
            frameRemains3 = inducer2_starttime + stimulus_duration - win.monitorFramePeriod * 0.75  # most of one frame period left
           
            if (inducer2_word.status == STARTED and t >= frameRemains3):
                inducer2_word.setAutoDraw(False)
                inducer2_word.status = PAUSED
            #--ITI SCREEN----------------------------------------------##
            if (t >= ITI_cross_starttime and ITI_cross.status == NOT_STARTED):
                # keep track of start time/frame for later
                #ITI_cross.tStart = t
                ITI_cross.frameNStart = frameN  # exact frame index
                ISI_cross2.setAutoDraw(False)
                ITI_cross.setAutoDraw(True)
            key_list_temp = event.getKeys(keyList=keypress)
            if (len(key_list_temp) > 0 and len(key_list) == 0):
                key_list = key_list_temp
                time1 = t
                key_list.append(time1)
                key_list.append((time1)-(tStart)*1000)
            frameRemains4 = ITI_cross_starttime + ITI_cross_duration - win.monitorFramePeriod * 0.75  # most of one frame period left
            
            if (ITI_cross.status == STARTED and t >= frameRemains4 and inducer2_word.status == PAUSED):
                if len(key_list)==3:
                    key = key_list[0]
                    time = key_list[1]
                    rt = key_list[2]
                    del key_list[0:3]  
                inducer2_word.status = FINISHED
                ITI_cross.setAutoDraw(False)
                
                ## RECORD DATA ON THE STIMULUS
                thisExp.addData('SubjID', expInfo['participant'])
                thisExp.addData('Block', block+1)
                thisExp.addData('Miniblock', trial+1)
                thisExp.addData('Trial', stimnum+2)
                thisExp.addData('StimulusType', 'inducer')
                thisExp.addData('Word', inducer2_word.text)
                thisExp.addData('WordCongruency', 'none')
                thisExp.addData('Word Orientation', 'none')
                thisExp.addData('WordPTime', tStart)
                thisExp.addData('ButtonPress', key)
                thisExp.addData('Accuracy', int(corr_key2 == key))
                thisExp.addData('ButtonPressTime', time)
                thisExp.addData('RT', rt)
                thisExp.addData('InducerTime',t-tStart)
                thisExp.nextEntry()
                
                continueRoutine = False

            #--CHECK FOR ESCAPES----------------------------------------------##
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            #--FLIP THE WINDOW------------------------------------------------##
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()


        ##-SET ALL TRIAL COMPONENTS TO 'NOT STARTED'---------------------------###Restarting trial
        
        trialComponents = [ISI_cross1,ITI_cross,ISI_cross2,rs_mapping,instruction1,inducer1_word,inducer2_word]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'setAutoDraw'):
                thisComponent.setAutoDraw(False)
            thisComponent.status = NOT_STARTED

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
