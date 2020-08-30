import magenta
import note_seq
import os
import csv
if not os.path.exists('parsed_songs'):
    os.makedirs('parsed_songs')

class MagentaParser:

    path = ''
    files = []

    def __init__(self, path):
        self.path = path
        self.files = os.listdir(self.path)
        if len(self.files) == 0:
            raise Exception('No files in path directory. Please add MIDI files.')

    def parse(self):
        for fil in self.files:
            seq = note_seq.midi_file_to_note_sequence(self.path + fil)
            notes = seq.notes
            messages = []
            messages.append(['pitch', 'velocity', 'start_time', 'end_time', 'tempo'])
            for i in range(len(notes)):
                messages.append([notes[i].pitch, notes[i].velocity, notes[i].start_time, notes[i].end_time, seq.tempos[0].qpm])
            with open('parsed_songs/' + fil[:len(fil) - 4] + '.csv','w+') as my_csv:
                csvWriter = csv.writer(my_csv,delimiter=',')
                csvWriter.writerows(messages)
