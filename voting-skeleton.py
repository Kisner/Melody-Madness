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
        if len(self.artists) < self.num_artist:
            self.artists.append(artist)
        else:
            print("The bracket is full.")

    def convert_pairs(self):
        new_list = []
        index = 0
        while index < (len(self.artists) - 1):
            new_list.append([self.artists[index], self.artists[index + 1]])
            index += 2
        return new_list

    def print_bracket(self):
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

    def check_time(self):
        if (datetime.now() - self.time_created) > timedelta(1):
            self.finish = True
            print("This bracket is over.")
        else:
            self.finish = False
            print("The bracket is still running.")


def run_bracket():
    print(type(datetime.now()))
    mem = 16
    while mem > 1:

        artist_list = []

        for i in range(int(mem)):
            artist = input("Enter the artists: ")
            artist_list.append(artist)
        # 2021-11-14 22:42:55.043259
        time = input("Enter time: ")

        my_bracket = Bracket(mem, artist_list, time)

        print(my_bracket.convert_pairs())
        my_bracket.print_bracket()

        my_bracket.get_winners()

        mem /= 2
        # my_bracket.check_time()

def run_voting(my_bracket):
    # use loop based on num_artists
    # keep winners list with winners of each round
    full_list = []
    full_list.append(my_bracket.artists)
    temp_list = []
    round = 0
    index = 0
    max_voting = my_bracket.num_artist
    while (index < max_voting) and (max_voting > 1):
        user_vote = input("Vote 1 for " + full_list[round][index] + " or 2 for " + full_list[round][index + 1] + "\n")
        if user_vote == "1":
            print("You voted for ", full_list[round][index])
            temp_list.append(full_list[round][index])
        else:
            print("You voted for ", full_list[round][index + 1])
            temp_list.append(full_list[round][index + 1])
        index += 2
        if index >= max_voting:
            round +=1
            index = 0
            full_list.append(temp_list)
            temp_list = []
            max_voting //= 2

    # print full list
    print("All artists and then the winners of each round are printed below")
    for i in range(len(full_list)):
        print("[", end='')
        for j in range(len(full_list[i])):
            print(full_list[i][j], end=" ")
        print("]")

    return full_list


def test_vote():
    artist_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    my_time = "2021-11-16"
    my_bracket = Bracket(16, artist_list, my_time)
    artist_list_pairs = my_bracket.convert_pairs()

    my_bracket.winners = run_voting(my_bracket)


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
    # run_bracket()
    # test_cases()
    test_vote()


