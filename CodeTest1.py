def main():
    chosen_function = ""
    while chosen_function != "E":
        chosen_function = input("\nEnter P for Pangram Detector, A for Animation or E to exit: ")
        chosen_function = chosen_function.upper()
        if chosen_function == "P":
            pangram_detector()
        elif chosen_function == "A":
            animation()
        elif chosen_function == "E":
            print("Exiting the program now.")
        else:
            print(chosen_function + " is not a valid function call.")
        
def pangram_detector():
    phrase = input("Enter a string to test: ")
    phrase = phrase.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newPhrase = ""
    for char in alphabet:
        if not char in phrase:
            newPhrase += char
        if len(newPhrase) == 26: 
            #Once all 26 letters are found, for loop ends so it can end early on in a file
            break
    print(newPhrase)

def animation():
    particle_sim = input("Enter a speed and a string to test separated by a comma: ")
    split_particle = []
    #Getting rid of spaces between inputs to make it harder for the user to break the code.
    particle_sim = ''.join(particle_sim.split())
    split_particle = particle_sim.split(',')

    #Splitting up the input given of speed and initial conditions
    speed = int(split_particle[0])
    animation_string = split_particle[1]
    animation_string = animation_string.upper()

    #Creating a final state in which the animation is completed
    final_state = len(animation_string) * '.'
    current_state = ""

    left_list = list(final_state)
    right_list = list(final_state)
    #Once the final string is equal to final state the program while loop ends
    while animation_string != final_state:
        animation_list = list(final_state)

        current_state = animation_string.replace('B', 'X')
        current_state = current_state.replace('L', 'X')
        current_state = current_state.replace('R', 'X')
        print(current_state)

        index = 0
        index2 = 0      
        for x in animation_string:
            if x == "L":
                left_list[index] = "."
                if (index-speed) >= 0:
                    left_list[index-speed] = "L"
            elif x == "R":
                if animation_string[index - speed] != "R" and animation_string[index - speed] != "B":
                    right_list[index] = "."
                if (index+speed) < len(left_list):
                    right_list[index+speed] = "R"
            elif x == "B":
                left_list[index] = "."
                if (index-speed) >= 0:
                    left_list[index-speed] = "L"
                if animation_string[index - speed] != "R" and animation_string[index - speed] != "B":
                    right_list[index] = "."        
                if (index+speed) < len(left_list):
                    right_list[index+speed] = "R"

            index += 1

        for x in animation_list:
            if left_list[index2] == "L" and right_list[index2] == "R":
                animation_list[index2] = "B"
            elif left_list[index2] == "L":
                animation_list[index2] = "L"
            elif right_list[index2] == "R":
                animation_list[index2] = "R"
            index2 += 1

        animation_string = "".join(animation_list)

    print(animation_string)

if __name__ == '__main__':
    main()