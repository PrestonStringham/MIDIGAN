'''The purpose of the file is to make sure that midi files can be recreated using from the csv exported from the readm.py file. I want to make sure that the data that the model will be presented will be able to be readable such that the model's generated messages will properly be able to be converted back into a midi file.'''
import pandas as pd
import numpy as np
import mido
from mido import Message, MidiFile, MidiTrack

directory = 'parsed_songs'

df = pd.read_csv(directory + '/Time.csv')

print(df.head)

length = len(list(df['note_status']))

df['note_status'].loc[df.note_status == '1'] = 'note_on'
df['note_status'].loc[df.note_status == '0'] = 'note_off'

messages = []
for i in range(length):
    messages.append(mido.Message(df.at[i, 'note_status'], 
        note = df.at[i, 'note'], velocity = df.at[i, 'velocity'], time = int(df.at[i, 'time'])))

print(messages)

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track) 
for message in messages:
    track.append(message)
mid.save('Time_reconstruct.mid')
