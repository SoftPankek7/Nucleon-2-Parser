try:
    import sys
    import os
except ModuleNotFoundError:
    print("Please fix the SYS and/or OS module.")
    exit(1)

try:
    import random
    import time
except ModuleNotFoundError:
    print("Please fix the RANDOM and/or TIME module.")

charset = ["","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"," ","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

variables = {
    # User Variables Below

    "00": "b", # Variable A - all set to be binary beforehand
    "01": "b", # Variable B
    "10": "b", # Variable C
    "11": "b", # Variable D

    # System Variables Below

    "copy_set": "",
    "append_set": "", # Append set
    "Index": 0, # How far down instructions it is
    "Version": "Nucleon (Primarily ST) 2.00D" # Version / Name
}

def error(string):
    print("\033[0m\033[0m\033[1m\033[41m\033[2m\033[30m ERROR \033[0m :  " + str(string) + "\033[0m")

def unmodeled(string):
    print("[ INFO ] Command \""+string+"\" Unmodelled.")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def flick_through_file(file):
    global flicked
    try:
        file = open(file, "rt")
        global run_list
        run_list = file.readlines()
        file.close()
        flicked = True
        return True
    except FileNotFoundError:
        #error("Runfile could not be found.")
        return False
    except:
        error("Error flicking through runfile.")
        flicked = False
        return False
    
def convert_to_st1c61_charset(string):
    bits_per_char = 6
    result = []
    # Using the ST1C61 Charset
    for i in range(0, len(string), bits_per_char):
        chunk = string[i:i+bits_per_char]
        if len(chunk) < bits_per_char:
            continue
        index = int(chunk, 2)
        result.append(charset[index])
    return "".join(result)

def convert_from_st1c61_charset(string):
    bits_per_char = 6
    binary_string = ""
    # Using the ST1C61 Charset
    for char in string:
        if char in charset:
            index = charset.index(char)
            binary_string += format(index, f"0{bits_per_char}b")
        else:
            pass
    return binary_string

def string_editor():
    print(variables["Version"]+ " String Easy-Editor")
    print("-"*len(variables["Version"]+ " String Easy-Editor"))
    print("00  -  Var A")
    print("01  -  Var B")
    print("10  -  Var C")
    print("11  -  Var D")
    _a = input("What var do you want to set it to?  ")
    _b = input("What do you want it to output?  ")
    clear()
    binary_string = convert_to_st1c61_charset(_b)
    chunks = [binary_string[i:i+2] for i in range(0, len(binary_string), 2)]
    commands = []
    commands.append("000011" + _a)
    for chunk in chunks:
        if len(chunk) < 2:
            chunk = chunk.ljust(2, "0")
        commands.append("000111" + chunk)
        commands.append("000101" + _a)
    commands.append("001000" + _a)
    for cmd in commands:
        print(cmd)
    del _a
    del _b
    del cmd
    del commands
    del binary_string
    exit()

def parse_code(command, argument):
    if command == "000000":
        exit(0)
    elif command == "000001":
        if argument == "00":
            exit(2)
        elif variables[argument] == variables["00"]:
            exit(0)
    elif command == "000010":
        variables[argument] = ""
    elif command == "000011":
        variables[argument] = "s"
    elif command == "000100":
        variables[argument] = "b"
    elif command == "000101":
        variables[argument] += variables["append_set"]
    elif command == "000110":
        variables[argument] = variables[argument][:-1]
    elif command == "000111":
        variables["append_set"] = argument
    elif command == "001000":
        val = variables.get(argument, "b")
        mode = val[0]
        data = val[1:]
        if mode == "b":
            print(data)
        elif mode == "s":
            try:
                print(convert_to_st1c61_charset(data))
            except ValueError:
                pass
        else:
            print(val)
    elif command == "001001":
        unmodeled("GOTO")
    elif command == "001010":
        variables[argument] = variables["copy_set"]
    elif command == "001011":
        variables["copy_set"] = variables[argument]
    elif command == "001100":
        variables["Index"] += 2
    elif command == "001101":
        variables["Index"] -= 2
    elif command == "001110":
        user_input = input("User Input :  ")
        variables[argument] = "s"+convert_from_st1c61_charset(user_input)
        del user_input
    elif command == "001111":
        print(variables[argument])
        print(variables["00"])
        if variables[argument][1:] == variables["00"][1:]:
            variables["Index"] += 4
    elif command == "010000":
        if variables[argument] != variables["00"]:
            variables["Index"] += 4
        else: 
            pass
    elif command == "010001":
        unmodeled("CONVERT_FORMAT")
    elif command == "010010":
        clear()
    elif command == "010011":
        variables[argument] = random.choice(["0", "1"])
    elif command == "010100":
        try:
            time.sleep(1)
        except ModuleNotFoundError:
            pass
    elif command == "010101":
        try:
            time.sleep(5)
        except ModuleNotFoundError:
            pass
    elif command == "010110":
        input("[ ENTER TO CONTINUE ]")
    elif command == "010111":
        variables["Index"] = 0
    elif command == "011000":
        unmodeled("EXCECUTE_NEXT_IF")
    elif command == "011001":
        unmodeled("EXCECUTE_LAST_IF")
    elif command == "011010":
        try:
            print(convert_to_st1c61_charset(data))
        except ValueError:
            pass
    elif command == "011011":
        print(data)
    elif command == "011100":
        print()
    elif command == "011101":
        variables[argument] = random.choice(["0", "1"])+random.choice(["0", "1"])
    elif command == "011110":
        # "Secret" plaintext REM / COMMENT command
        pass
    elif command == "011111":
        pass
    elif command == "100000":
        pass
    elif command == "100001":
        pass
    elif command == "100010":
        pass
    elif command == "100011":
        pass
    elif command == "100100":
        pass
    elif command == "100101":
        pass
    elif command == "100110":
        pass
    elif command == "100111":
        pass
    elif command == "101000":
        pass
    elif command == "101001":
        pass
    elif command == "101010":
        pass
    elif command == "101011":
        pass
    elif command == "101100":
        pass
    elif command == "101101":
        pass
    elif command == "101110":
        pass
    elif command == "101111":
        pass
    elif command == "110000":
        pass
    elif command == "110001":
        pass
    elif command == "110010":
        pass
    elif command == "110011":
        pass
    elif command == "110100":
        pass
    elif command == "110101":
        pass
    elif command == "110110":
        pass
    elif command == "110111":
        pass
    elif command == "111000":
        pass
    elif command == "111001":
        pass
    elif command == "111010":
        pass
    elif command == "111011":
        pass
    elif command == "111100":
        pass
    elif command == "111101":
        pass
    elif command == "111110":
        pass
    elif command == "111111":
        pass
    elif command[0] == ";":
        # treat comments as comments.. not code!
        pass
    else:
        error("Command: "+command+" could not be found, in line/index "+ str(variables["Index"]) )

def file_pick_mode():
    try:
        print(variables["Version"] + " Runfile Picker")
        while True:
            if flick_through_file(input("Input a path. :  ")):
                break
    except KeyboardInterrupt:
        clear()
        exit(0)

def parse_line(item):
    global command
    global argument
    try:
        command = item[0:6]
        argument = item[6:8]
        return True
    except TypeError:
        return False

def cli_parse():
    print(variables["Version"]+" Shell")
    try:
        while True:
            requested_command = input(" >>>>  ")
            parse_line(requested_command)
            parse_code(command, argument)
    except KeyboardInterrupt:
        clear()

if __name__ == "__main__":
    #clear() # Tidy up the shell.. Maybe not...

    # Detect whether any command line arguments have been parsed. If so, Run IT!
    try:
        if sys.argv[1] == "-v" or sys.argv[1].lower() == "--version":
            print(variables["Version"])
            exit(0)
        elif sys.argv[1] == "-h" or sys.argv[1].lower() == "--help" or sys.argv[1] == "/?":
            print(variables["Version"] + " Integrated Help")
            print("-"* len(variables["Version"] + " Integrated Help"))
            print("Script Usage: ( * = Optional )\n\n")
            print("nucleon.py [*-v][*-h][*-c][*-f][*-s][*/path/to/your/runfile.st2]")
            print("\n-v, --version :  Show Version & Quit")
            print("-h, --help, /? :  Show This Menu")
            print("-c, --cli :  Force CLI mode.")
            print("-f, --file :  Force File Mode. (If no file was given, enter the file selector mode.)")
            print("-s, --string :  Simple string creation tool aimed to help developers.")
            exit(0)
        elif sys.argv[1] == "-c" or sys.argv[1].lower() == "--cli":
            cli_parse()
        elif sys.argv[1].endswith(".st2"):
            flick_through_file(sys.argv[1])
        elif sys.argv[1] == "-s" or sys.argv[1].lower() == "--string":
            string_editor()
        elif sys.argv[1] == "-f" or sys.argv[1].lower() == "--file":
            try:
                if sys.argv[2].endswith(".st2"):
                    flick_through_file(sys.argv[2])
                else:
                    raise IndexError
            except IndexError:
                file_pick_mode()
        else:
            error("Uknown command-line switch.")
    except IndexError:
        pass
    # Detect whether a runfile has been specified.

    try:
        # User did specify CLI arguments. Enter the Nucleon/ST parser.
        if not flick_through_file(sys.argv[1]):
            error("Runfile could not be loaded.")
        else:
            while variables["Index"] < len(run_list):
                line = run_list[variables["Index"]].strip()
                if line:
                    parse_line(line)
                    parse_code(command, argument)
                variables["Index"] += 1
    except IndexError:
        # User did not specify CLI arguments. Enter the Nucleon/ST run shell.
        try:
            cli_parse()
        except KeyboardInterrupt:
            clear()
            exit()