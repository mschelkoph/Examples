'''
Notes:

middle C = 48
Last note (to keep things smaller) = 72

'''
import MusicChoices
import numpy as np
from mingus.containers import Bar, Track, Note
import mingus.core.value as value
from mingus.midi import midi_file_out
import mingus.extra.lilypond as LP
import pickle
import time
import subprocess
import tkinter as tk
import pygame

#Handles the "Play music" click
def handle_click2(event):
    pygame.mixer.music.load("QLMusic.mid")
    pygame.mixer.music.play()

#GUI for user to vote on the song
def Event_Window():
    window = tk.Tk()
    window.title("dropdown test")

    img = tk.PhotoImage(file="QLSMusic.png")
    img1 = img.subsample(2,2)

    mainframe = tk.Frame(window)
    mainframe.grid(column=0, row=0, sticky="N,W,E,S")
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx = 100)

    vote = tk.IntVar(window)

    choices = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    vote.set(0)

    popupMenu = tk.OptionMenu(mainframe, vote, *choices)
    tk.Label(mainframe, image=img1).grid(row=1, column=1, columnspan=2, rowspan=2, padx=5, pady=5)
    tk.Label(mainframe, text="Rate the Song").grid(row=5, column=2)
    popupMenu.grid(row=6, column=2)

    button = tk.Button(mainframe, text="Play song", width=10, height=5)
    button.grid(row=6, column=1)

    def change_dropdown(*args):
        global creator
        creator = vote.get()
        window.destroy()

    vote.trace('w', change_dropdown)
    button.bind("<Button-1>", handle_click2)

    window.mainloop()


t = Track()
pygame.init()

size = 10
goalReward = 1

epsilon = 0.9
epsDecay = 0.09

start_q_table = None
runAmount = 1

learningRate = 1
discount = 0.95

creator = 0
goal = 10

#converts the voting scale from 1-10 to decimal
def DecideReward(score):
    if score == 0:
        return 0
    else:
        return score / 10

# checking to see if a file exists, if not, it will create a new q-table
if start_q_table is None:
    q_table = np.random.uniform(low=-1, high=0, size=(10,126))
else:
    with open(start_q_table, "rb") as f:
        q_table = pickle.load(f)

episode_rewards = []
actionList = []
count = 0
#Start of the training session
for episode in range(runAmount):
    episode_reward = 0
    #length of the training group
    for x in range(5):
        obs = creator - goal
        trackTime = 0
        action = 0
        #tracks how long the song can be and stores the actions in a list
        while trackTime <= 10:
            if np.random.random_sample() > epsilon:
                action = np.argmax(q_table[obs])
                actionList.append(action)
            else:
                action = np.random.randint(0, 126)
                actionList.append(action)
            #Creates the note using mingus
            trackTime += MusicChoices.CreateNoteAction(t, action)
        #creates the midi file and png image of the music created
        midi_file_out.write_Track("QLMusic.mid", t)
        T = LP.from_Track(t)
        LP.to_png(T, "QLSMusic")

        #engages the GUI for user to vote
        Event_Window()

        #takes user vote and translates that into meaningful reward
        reward = DecideReward(creator)
        if creator == goal:
            reward = goalReward
        for act in actionList:
            newObs = creator - goal
            max_future_q = np.max(q_table[newObs, act])
            current_q = q_table[obs][act]

            #q-learning
            if reward == goalReward:
                new_q = max_future_q
            else:
                new_q = (1 - learningRate) * current_q + learningRate * (reward + discount * max_future_q)

            q_table[obs][act] = new_q

        actionList.clear()
        t = 0
        t = Track()
        print(q_table)
        episode_reward += reward
    
    episode_rewards.append(episode_reward)
    epsilon *= epsDecay
#Creates file at the end of the training session
with open(f"qtable-{int(time.time())}.pickle", "wb") as f:
    pickle.dump(q_table, f)
