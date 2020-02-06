def chord(notes):
	chromatic=['a','a#','b','c','c#','d','d#','e','f','f#','g','g#']
	steps=[chromatic.index(note) for note in notes]
	intervals=[steps[i+1]-steps[i] for i in range(len(steps)-1)]
	return intervals

print(chord(['c','e','g']))