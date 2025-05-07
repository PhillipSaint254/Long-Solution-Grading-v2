from twenty import get_all_frets

note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
base_midi = 64  # E4

def get_note_counts():
    note_counts = {}
    all_frets = get_all_frets()
    for fret in all_frets:
        midi = base_midi + fret
        name = note_names[midi % 12]
        note_counts[name] = note_counts.get(name, 0) + 1

    return note_counts

if __name__ == "__main__":
    print(get_note_counts())
