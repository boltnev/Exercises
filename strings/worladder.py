import unittest
import enchant


d = enchant.Dict('en')


def find_word_ladder(source, dest, current_ladder = []):
    if len(source) != len(dest):
        return None

    if source == dest:
        return current_ladder

    ladders = []

    for i in range(len(source)):
        if source[i] == dest[i]:
            continue

        word = source[:i]+dest[i]+source[i+1:]

        if d.check(word):
            ladders.append(current_ladder + [word])

    for ladder in ladders:
        print(ladder)
        print(find_word_ladder(ladder[-1], dest, ladder))

    return ladders



class TestWordLadder(unittest.TestCase):

    def test_word_ladder(self):
        find_word_ladder('hit', 'cog')
        pass



if __name__=='__main__':
    unittest.main()
