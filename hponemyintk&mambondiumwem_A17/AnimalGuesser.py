######################################################################
# Names: Kyaw Hpone Myint and Marima Andrew Mambondiumwe
# username: hponemyintk and mambondiumwem
# Program: AnimalGuesser.py
#
# Assignment number: A17
# Purpose: This is the driver class which will store and access data from binarytree class
######################################################################

from BinaryTree import binarytree

def main():
    print "\n\
    This is the Animal Guessing Game. To start, think of a real animal \n\
    and the computer will try to guess the animal you have in mind by asking you questions. \n\
    You will answer honestly. The AI wins if it guess right, if its guess is wrong then you have to\n\
    input what animal you were thinking of and then the question that would lead to that animal.\n\
    This way it can learn from its mistake.\n"

    game = raw_input("Press enter to start the game")

    tree = binarytree() # Make an object of the class type binarytree
    tree.gen_list() # function call to class metho gen_list

    game_on = 'yes' # This is a flag to check whether the is over or not

    while game_on.lower() == 'yes':
        # Start traversing the tree from the root until the game is lost
        tree.cur_ind = 0
        while tree.is_game(tree.cur_ind) != 0:
            pass
        game_on = raw_input('Do you want to start over?')

    tree.write_file() #write file


main()
