import random

# Take in Multiline Str & Assigns it to var. called poem.
poem = """If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer…
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!"""


#Split Poem Str & Assigns it var. called lines_list.
lines_list = poem.split("\n")


#Define (L.P.B) func that Takes in lines_list as parameter.
def lines_printed_backwards(lines_list):
    lines_list.reverse()

# Run For Loop & Print Each Line in lines_list(poem).
    index = len(lines_list)
    for line in lines_list:
        print(str(index)+ " " + line)
        index -= 1

# Calling (L.P.B) func.
lines_printed_backwards(lines_list)
print(" ")


# Define (L.P.R) func 
def lines_printed_random(lines_list):
    random.shuffle(lines_list)
    print(lines_list)

# Calling (L.P.R) func
lines_printed_random(lines_list)
print(" ")


# Define (L.P.S) func)
def lines_printed_sorted(lines_list):
    lines_list.sort(reverse=True)
    print('lines_list(in Descending):', lines_list)
    print(" ")

lines_printed_sorted(lines_list)