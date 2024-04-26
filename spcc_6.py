# Implementation of Pass1 Macro Output

class MacroProcessor:
    def __init__(self):
        self.MNT={}
        self.MDT=[]
        self.ALA=[]
        self.output=[]

    def process(self, lines):
        in_macro=False
        macro_name=''

        for line in lines:
            strip_line=line.strip()
            if "MACRO" in strip_line:
                in_macro=True
                parts=strip_line.split()
                macro_name=parts[0]
                self.MNT[macro_name]=len(self.MDT)
                self.ALA=parts[1:]
                self.MDT.append((macro_name,parts[1:]))
            elif "MEND" in strip_line:
                in_macro=False
                self.MDT.append(("MEND",))
            elif in_macro:
                self.MDT.append((strip_line,))
            else:
                self.output.append(strip_line)

    def display_results(self):
        print("Pass 1 Output")
        for line in self.output:
            print(line)
        print("MDT TABLE\n")
        for index,entry in enumerate(self.MDT,1):
            print(f"{index} : {entry}")
        print("MNT TABLE\n")
        for name,i in self.MNT.items():
            print(f"{name} : {i}")
        print("ALA\n")
        for arg in self.ALA:
            print(arg)

# Sample input
input_lines = [
    "PRG START 0",
    "INCR MACRO &ARG1, &ARG2, &ARG3",
    "A 1, &ARG1",
    "A 2, &ARG2",
    "A 3, &ARG3",
    "MEND",
    "LOOP1 INCR DATA1, DATA2, DATA3",
    "DATA1 DC F'5'",
    "DATA2 DC F'10'",
    "DATA3 DC F'15'"
]

# Processing the input
macro_processor = MacroProcessor()
macro_processor.process(input_lines)

# Displaying the results
macro_processor.display_results()
