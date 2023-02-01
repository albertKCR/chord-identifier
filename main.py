notes = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B') #12

tuning =[]
note_index = []

# tuning.append(input()) #E
# tuning.append(input()) #A
# tuning.append(input()) #D
# tuning.append(input()) #G
# tuning.append(input()) #B
# tuning.append(input()) #E

tuning.append('E')
tuning.append('A')
tuning.append('D')
tuning.append('G')
tuning.append('B')
tuning.append('E')

print('Tuning: ', tuning)

for i in range(len(tuning)):
    for j in range(len(notes)):
        if tuning[i]==notes[j]:
            note_index.append(j)

print('Tuning notes index: ', note_index)

string_fret = []
fret_notes = []
fret_notes_index = []

# string_fret.append(input())
# string_fret.append(input())
# string_fret.append(input())
# string_fret.append(input())
# string_fret.append(input())
# string_fret.append(input())

string_fret.append(-1)
string_fret.append(5)
string_fret.append(7)
string_fret.append(7)
string_fret.append(7)
string_fret.append(5)


for i in range(6):
    temp_index = note_index[i]+string_fret[i]
    while temp_index>11:
        temp_index = temp_index-12
    fret_notes_index.append(temp_index)
    fret_notes.append(notes[fret_notes_index[i]])

print('Fret notes: ', fret_notes)
print('Fret notes index in the notes vector: ', fret_notes_index)

#verifies the tonic

if string_fret[0] != -1:
    tonic_index = fret_notes_index[0]
    tonic = fret_notes[0]
elif string_fret[1] != -1:
    tonic_index = fret_notes_index[1]
    tonic = fret_notes[1]
elif string_fret[2] != -1:
    tonic_index = fret_notes_index[2]
    tonic = fret_notes[2]
elif string_fret[3] != -1:
    tonic_index = fret_notes_index[3]
    tonic = fret_notes[3]

print('Tonic: ', tonic)
print('Tonic index in the notes list: ', tonic_index)

#verifies which note is the third (tonic + 2 tone) and the fifth (tonic + 3 1/2 tones)

third = notes[tonic_index+4]
print('Third: ', third)
fifth = notes[tonic_index+7]
print('Fifth: ', fifth)
