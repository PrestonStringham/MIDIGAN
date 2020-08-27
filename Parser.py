import mido
import csv
import os
if not os.path.exists('parsed_songs'):
    os.makedirs('parsed_songs')

'''
The goal of this class is to use TensorFlow's research project Magenta to read MIDI files and extract the relevant data that will be used to train the model. In my case, I am particularly interested to see how the model will interpret the velocity paramter of MIDI notes as this is responsible for much of the emotion in music. This class should generate a csv file for every input containing the start time, end time note, and velocity.
'''
class Parser:
    
    path = ''
    files = []

    def __init__(self, path):
                self.path = path
                self.files = os.listdir(self.path)
                if len(self.files) == 0:
                    raise Exception('No files in path directory. Please add files.')
            
    def parse(self):
        for file in self.files:
            messages = []
            for message in mido.MidiFile(self.path + file).tracks[0]:
                messages.append(message)
            print(messages)        
            #I only care about note_on and note_off
            cleansed = [x for x in messages if x.type == 'note_on' or x.type == 'note_off']
            messages = cleansed

            #Only get the values that matter
            parsed = []
            parsed.append(['note_status', 'note', 'velocity', 'time'])
            for i in range(len(messages)):

                parsed.append([messages[i].type, messages[i].note, messages[i].velocity, messages[i].time])
                if parsed[i][0] == 'note_on':
                    parsed[i][0] = 1
                if parsed[i][0] == 'note_off':
                    parsed[i][0] = 0
            
            with open('parsed_songs/' + file[:len(file) - 4] + '.csv','w+') as my_csv:
                csvWriter = csv.writer(my_csv,delimiter=',')
                csvWriter.writerows(parsed)
