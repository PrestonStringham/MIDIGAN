import magenta
import note_seq
import os
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
        seq = note_seq.midi_file_to_note_sequence(self.path + self.files[0])
        print(seq.notes)
