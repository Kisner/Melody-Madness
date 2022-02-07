"""
Iteration 3
Diya and Nozima worked on it together because voting and generate bracket linked together
This is a skeleton file with the basic generate bracket and voting component of our app. Currently it only works with
command line user input and does not work with web development.
"""

from datetime import datetime, timedelta
import math


class Bracket:

    def __init__(self, num_artist, artists, time_created):
        self.num_artist = num_artist
        self.artists = artists
        self.winners = []
        self.time_created = time_created
        self.finish = False

    def add_artist(self, artist):
        # add artist to the bracket if bracket is not full
        if len(self.artists) < self.num_artist:
            self.artists.append(artist)
        else:
            print("The bracket is full.")

    def convert_pairs(self):
        new_list = []
        index = 0

        # puts two competing artists into a list and creates a 2D list with all pairs
        while index < (len(self.artists) - 1):
            new_list.append([self.artists[index], self.artists[index + 1]])
            index += 2
        return new_list

    def print_bracket(self):
        # prints only the valid tournament brackets
        # in a valid tournament the number of artist matches the bracket size and makes sure
        # the number of artists is even
        if len(self.artists) == self.num_artist:
            if self.num_artist % 2 == 0:
                half = int(len(self.artists) / 2)

                for i in range(half):
                    print(f"Artist {i + 1}: {self.artists[i]:40}  Artist {i + half + 1}: {self.artists[i + half]}")
            else:
                print("Number of artists must be even to create a proper bracket.")
        else:
            print("Number of artist not aligned with the bracket.")

    def get_winners(self):
        if self.finish:
            print("Here are the winners of this round.")

        # asks for votes and adds them to a list of winners
        temp = self.convert_pairs()
        for pair in temp:
            print(f"Option 1: {pair[0]} \n Option 2: {pair[1]}")
            choice = int(input("Which artist? "))
            self.winners.append(pair[choice - 1])

    def check_time(self):
        # (does not work at the moment)
        # suppose to keep track of the time limit on the bracket voting
        if (datetime.now() - self.time_created) > timedelta(1):
            self.finish = True
            print("This bracket is over.")
        else:
            self.finish = False
            print("The bracket is still running.")


def run_bracket():
    max_voting = 16
    artist_list = []

    # gets the artists
    for i in range(int(max_voting)):
        artist = input("Enter the artists: ")
        artist_list.append(artist)

    time = input("Enter time: ")
    all_brackets_list = []

    # run the loop for each bracket voting round
    while max_voting > 1:

        my_bracket = Bracket(max_voting, artist_list, time)

        # prints the bracket
        my_bracket.convert_pairs()
        my_bracket.print_bracket()

        # gets the winners of the bracket
        my_bracket.get_winners()
        artist_list = my_bracket.winners

        # keep track of all the brackets
        all_brackets_list.append(my_bracket)
        max_voting //= 2
        # my_bracket.check_time()

    print("The Winner is: ", all_brackets_list[len(all_brackets_list)-1].winners[0], " !!!!!!!")


def test_cases():
    test_1 = Bracket(3, [1, 2, 3], "2121-11-15")
    test_2 = Bracket(4, ['a', 'b', 'c', 'd'], "2121-11-15")

    # Test 1: Even and Odd convert pairs
    odd_pair = test_1.convert_pairs()
    even_pair = test_2.convert_pairs()

    if len(odd_pair) == int(3/2):
        print("Odd pair correctly made")
        print(odd_pair)
    else:
        print("Odd pair not created successfully")

    if len(even_pair) == int(4/2):
        print("Even pair correctly made")
        print(even_pair)
    else:
        print("Even pair not created successfully")

    # Test 2: Print Bracket
    test_3 = Bracket(3, [1, 2, 3, 4], "2121-11-15")

    print("printing test 3 bracket:")
    test_3.print_bracket()
    print("printing test 2 bracket:")
    test_2.print_bracket()
    print("printing test 1 bracket:")
    test_1.print_bracket()


if __name__ == "__main__":
    run_bracket()
    test_cases()