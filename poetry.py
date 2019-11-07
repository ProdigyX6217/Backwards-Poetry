poem = """If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer…
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!"""
# Take in Multiline Str & Assigns it to var. called poem.

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


def lines_printed_random():
    pass
# Testing Code