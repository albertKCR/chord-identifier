def major_chord():
    for i in strings_to_check:
        if (fret_notes[i]) == tonic or (fret_notes[i]) == third or (fret_notes[i]) == fifth:
            continue
        else:
            return 0
    return tonic
    
def minor_chord():
    for i in strings_to_check:
        if (fret_notes[i]) == tonic or (fret_notes[i]) == minor_third or (fret_notes[i]) == fifth:
            continue
        else:
            return 0
    return tonic + 'm'

def minor_with_seventh_minor():
    for i in strings_to_check:
        if (fret_notes[i]) == tonic or (fret_notes[i]) == minor_third or (fret_notes[i]) == fifth or (fret_notes[i]) == minor_seventh:
            continue
        else:
            return 0
    return tonic + 'm' + '7'

def major_with_seventh_minor():
    for i in strings_to_check:
        if (fret_notes[i]) == tonic or (fret_notes[i]) == third or (fret_notes[i]) == fifth or (fret_notes[i]) == minor_seventh:
            continue
        else:
            return 0
    return tonic + '7'

def minor_with_seventh_major():
    for i in strings_to_check:
        if (fret_notes[i]) == tonic or (fret_notes[i]) == minor_third or (fret_notes[i]) == fifth or (fret_notes[i]) == major_seventh:
            continue
        else:
            return 0
    return tonic + 'm' + '7' + 'M'

def major_with_seventh_major():
    for i in strings_to_check:
        if (fret_notes[i]) == tonic or (fret_notes[i]) == third or (fret_notes[i]) == fifth or (fret_notes[i]) == major_seventh:
            continue
        else:
            return 0
    return tonic + '7' + 'M'

def half_diminished():
    for i in strings_to_check:
        if (fret_notes[i]) == tonic or (fret_notes[i]) == minor_third or (fret_notes[i]) == minor_fifth or (fret_notes[i]) == minor_seventh:
            continue
        else:
            return 0
    return tonic + 'm' + '7' + '(-5)'

def diminished():
    for i in strings_to_check:
        if (fret_notes[i]) == tonic or (fret_notes[i]) == minor_third or (fret_notes[i]) == minor_fifth or (fret_notes[i]) == diminished_seventh:
            continue
        else:
            return 0
    return tonic + '°'

def fourth():
    for i in strings_to_check:
        if (fret_notes[i]) == tonic or (fret_notes[i]) == major_fourth or (fret_notes[i]) == fifth:
            continue
        else:
            return 0
    return tonic + '4'

def sixth():
    for i in strings_to_check:
        if (fret_notes[i]) == tonic or (fret_notes[i]) == third or (fret_notes[i]) == fifth or (fret_notes[i]) == major_sixth:
            continue
        else:
            return 0
    return tonic + '6'

def ninth():
    for i in strings_to_check:
        if (fret_notes[i]) == tonic or (fret_notes[i]) == third or (fret_notes[i]) == fifth or (fret_notes[i]) == minor_seventh or (fret_notes[i]) == major_ninth:
            continue
        else:
            return 0
    return tonic + '9'

def add_ninth():
    for i in strings_to_check:
        if (fret_notes[i]) == tonic or (fret_notes[i]) == third or (fret_notes[i]) == fifth or (fret_notes[i]) == major_ninth:
            continue
        else:
            return 0
    return tonic + 'add9'

#----------------------------------------------------------------------------
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
string_fret.append(0)
string_fret.append(2)
string_fret.append(2)
string_fret.append(3)
string_fret.append(0)


for i in range(6):
    temp_index = note_index[i]+string_fret[i]
    while temp_index>11:
        temp_index = temp_index-12
    fret_notes_index.append(temp_index)
    fret_notes.append(notes[fret_notes_index[i]])

print('Fret notes: ', fret_notes)
print('Fret notes index in the notes vector: ', fret_notes_index)

#verifies the tonic
#in the worst case the tonic will be the fourth string, because need at least 3 notes to form the chord
if string_fret[0] != -1:
    tonic_index = fret_notes_index[0]
    tonic = fret_notes[0]
    tonic_string = 0
elif string_fret[1] != -1:
    tonic_index = fret_notes_index[1]
    tonic = fret_notes[1]
    tonic_string = 1
elif string_fret[2] != -1:
    tonic_index = fret_notes_index[2]
    tonic = fret_notes[2]
    tonic_string = 2
elif string_fret[3] != -1:
    tonic_index = fret_notes_index[3]
    tonic = fret_notes[3]
    tonic_string = 3

print('Tonic: ', tonic)
print('Tonic index in the notes list: ', tonic_index)
print('Tonic string: ', tonic_string)

#identifies which note is the third (tonic + 2 tone) and the fifth (tonic + 3 1/2 tones)
third_index = tonic_index + 4
while third_index > 11:
    third_index = third_index - 12
third = notes[third_index]
print('Third: ', third)
fifth_index = tonic_index + 7
while fifth_index > 11:
    fifth_index = fifth_index - 12
fifth = notes[fifth_index]
print('Fifth: ', fifth)

#identifies the minor third
minor_third_index = tonic_index + 3
while minor_third_index > 11:
    minor_third_index = minor_third_index - 12
minor_third = notes[minor_third_index]
print('Minor third: ', minor_third)

#identifies the major fourth
major_fourth_index = tonic_index + 5
while major_fourth_index > 11:
    major_fourth_index = major_fourth_index - 12
major_fourth = notes[major_fourth_index]
print('Major fourth: ', major_fourth)

#identifies the minor fifth
minor_fifth_index = tonic_index + 6
while minor_fifth_index > 11:
    minor_fifth_index = minor_fifth_index - 12
minor_fifth = notes[minor_fifth_index]
print('Minor fifth: ', minor_fifth)

#identifies the major sixth
major_sixth_index = tonic_index + 9
while major_sixth_index > 11:
    major_sixth_index = major_sixth_index - 12
major_sixth = notes[major_sixth_index]
print('Major sixth: ', major_sixth)

#identifies the minor, major and diminished seventh
minor_seventh_index = tonic_index + 10
while minor_seventh_index > 11:
    minor_seventh_index = minor_seventh_index - 12
minor_seventh = notes[minor_seventh_index]
print('Minor seventh: ', minor_seventh)

major_seventh_index = tonic_index + 11
while major_seventh_index > 11:
    major_seventh_index = major_seventh_index - 12
major_seventh = notes[major_seventh_index]
print('Major seventh: ', major_seventh)

diminished_seventh_index = tonic_index + 9
while diminished_seventh_index > 11:
    diminished_seventh_index = diminished_seventh_index - 12
diminished_seventh = notes[diminished_seventh_index]
print('Diminished seventh: ', diminished_seventh)

#identifies the major ninth
major_ninth_index = tonic_index + 2
while major_ninth_index > 11:
    major_ninth_index = major_ninth_index - 12
major_ninth = notes[major_ninth_index]
print('Major ninth: ', major_ninth)

#verifies which strings are played in the chord
strings_to_check = []
for i in range(6):
    if string_fret[i]!=-1:
        strings_to_check.append(i)
#print(strings_to_check)

print(tonic, 'scale: ', tonic, major_ninth, third, major_fourth, fifth, major_sixth, major_seventh)

if major_chord()!=0:
    print('Used notes: Tonic:', tonic, '; Third:', third, '; Fifth:', fifth)
    print(major_chord())
elif minor_chord()!=0:
    print('Used notes: Tonic:', tonic, '; Minor third:', minor_third, '; Fifth:', fifth)
    print(minor_chord())
elif minor_with_seventh_major()!=0:
    print('Used notes: Tonic:', tonic, '; Minor third:', minor_third, '; Fifth:', fifth, '; Minor seventh:', minor_seventh)
    print(minor_with_seventh_major())
elif major_with_seventh_major()!=0:
    print('Used notes: Tonic:', tonic, '; Third:', third, '; Fifth:', fifth, '; Minor seventh:', minor_seventh)
    print(major_with_seventh_major())
elif minor_with_seventh_minor()!=0:
    print('Used notes: Tonic:', tonic, '; Minor third:', minor_third, '; Fifth:', fifth, '; Seventh:', major_seventh)
    print(minor_with_seventh_minor())
elif major_with_seventh_minor()!=0:
    print('Used notes: Tonic:', tonic, '; Third:', third, '; Fifth:', fifth, '; Seventh:', major_seventh)
    print(major_with_seventh_minor())
elif half_diminished()!=0:
    print('Used notes: Tonic:', tonic, '; Minor third:', minor_third, '; Minor Fifth:', minor_fifth, '; Minor seventh:', minor_seventh)
    print(half_diminished())
elif diminished()!=0:
    print('Used notes: Tonic:', tonic, '; Minor third:', minor_third, '; Minor Fifth:', minor_fifth, '; Diminished seventh:', diminished_seventh)
    print(diminished())
elif fourth()!=0:
    print('Used notes: Tonic:', tonic, '; Fourth:', major_fourth, '; Fifth:', fifth)
    print(fourth())
elif sixth()!=0:
    print('Used notes: Tonic:', tonic, '; Third:', third, '; Fifth:', fifth, '; Sixth:', major_sixth)
    print(sixth())
elif add_ninth()!=0:
    print('Used notes: Tonic:', tonic, '; Third:', third, '; Fifth:', fifth, '; Ninth:', major_ninth)
    print(add_ninth())
elif ninth()!=0:
    print('Used notes: Tonic:', tonic, '; Third:', third, '; Fifth:', fifth, '; Ninth:', major_ninth, '; Minor seventh:', minor_seventh)
    print(ninth())