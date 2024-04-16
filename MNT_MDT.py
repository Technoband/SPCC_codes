def display_MNT_and_MDT(ALP):
    MNT = {}  # Macro Name Table
    MDT = {}  # Macro Definition Table
    current_macro_name = None  # Track current macro being defined

    for line_index, line in enumerate(ALP):
        if line.startswith("MACRO"):
            parts = line.split()
            macro_name = parts[1]
            parameters = parts[2:]
            current_macro_name = macro_name
            MNT[macro_name] = line_index  # Index of MDT entry for this macro
            MDT[macro_name] = {'parameters': parameters, 'definition': []}
        elif line == "MEND":
            current_macro_name = None
        else:
            if current_macro_name is not None:
                MDT[current_macro_name]['definition'].append(line)

    # Print MNT
    print("Macro Name Table (MNT):")
    for macro_name, index in MNT.items():
        print(f"{macro_name}: {index}")

    # Print MDT
    print("\nMacro Definition Table (MDT):")
    for macro_name, data in MDT.items():
        print(f"{macro_name}:")
        print("Parameters:", data['parameters'])
        print("Definition:")
        for line in data['definition']:
            print(line)

# Example usage:
ALP = [
    "MACRO ADD A, B",
    "LDA A",
    "ADD B",
    "STA RESULT",
    "MEND",
    "MACRO SUB A, B",
    "LDA A",
    "SUB B",
    "STA RESULT",
    "MEND",
    "ADD 5, 10",
    "SUB 20, 7"
]

display_MNT_and_MDT(ALP)
