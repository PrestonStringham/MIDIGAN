#The purpose of this file is to test whether the parsed data from magentaparser.py can be
#converted back into a midi sequence and exported as a midi file. This is purely to make sure
#that notes predicted by the model can be properly formatted such that it can also be 
#converted back into a midi file.

import pandas as pd
import magenta
import note_seq
import os

directory = 'parsed_songs'

df = pd.read_csv(directory + '/Time.csv')

seq = note_seq.NoteSequence()

for i in range(len(list(df['velocity']))):
    seq.notes.add(pitch=df.at[i, 'pitch'], velocity=df.at[i, 'velocity'],
            start_time=df.at[i, 'start_time'], end_time=df.at[i, 'end_time'])
tempo = df['tempo'].iloc[0]
seq.tempos.add(qpm=tempo)
note_seq.sequence_proto_to_midi_file(seq, 'songs_test/Tim_reconstruct.mid')
