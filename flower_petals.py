"""
1. "I love you"
2. "a little"
3. "a lot"
4. "passionately"
5. "madly"
6. "not at all"
If there are more than 6 petals, you start over with "I love you" for 7 petals, "a little" for 8 petals and so on.

When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

Your goal is to determine which phrase the girls would say at the last petal for a flower of a given number of petals. The number of petals is always greater than 0.
"""

"""
def how_much_i_love_you(nb_petals):
    # your code
    if nb_petals == 1 and nb_petals > 7:
        return "I love you"
    elif nb_petals == 2 and nb_petals > 8:
        return "a little"
    elif nb_petals == 3 and nb_petals > 9:
        return "a lot"
    elif nb_petals == 4 and nb_petals > 10:
        return "passionately"
    elif nb_petals == 5 and nb_petals > 11:
        return "madly"
    elif nb_petals == 6 and nb_petals > 12:
        return "not at all"
"""

def how_much_i_love_you(nb_petals):
    phrases = [
        "I love you",
        "a little",
        "a lot",
        "passionately",
        "madly",
        "not at all"
    ]
    
    return phrases[(nb_petals - 1) % 6] # Use modulo to cycle through the phrases

"""
SOLUTION

Modulo Operation: For any given number of petals nb_petals, the phrase is determined by the position (nb_petals - 1) % 6. This adjustment ensures:

When nb_petals is 1, the index is 0 ("I love you").

When nb_petals is 2, the index is 1 ("a little").

...

When nb_petals is 6, the index is 5 ("not at all").

When nb_petals is 7, the index wraps around to 0 ("I love you") again, and so on.

This approach efficiently handles any positive integer input for nb_petals, ensuring the correct phrase is returned based on the cyclic nature of the phrases.
"""

print(how_much_i_love_you(1))  # "I love you"
print(how_much_i_love_you(2))  # "a little"