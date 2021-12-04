# input is a list of chords(str)
# concatenate (tack on) the string "7" to each chord in the list
# if "7" already exists at the end of the chord, don't add another

def concatSeven(chords):
    sevens = []
    # loop through chords, at each index, find the end of the string
    # [chord + "7" for chord in chords if chord[len(chord) - 1] != "7"]
    for chord in chords:
        # if the last character == "7" return the orginal
        if chord[len(chord) - 1] == "7":
            sevens.append(chord)
        # else not tack "7" onto the end
        else:
            seven = chord + "7"
            sevens.append(seven)
    return sevens

print(concatSeven(["G", "F", "C"]))
print(concatSeven(["G", "F7", "C"]))
print(concatSeven(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]))
print(concatSeven(["Dm", "G", "E", "A"]))
print(concatSeven([]))