import unittest
import enchant


d = enchant.Dict('en')


def find_word_ladder(source, dest, current_ladder = [], deadends = [], depth=0):
    if len(source) != len(dest):
        return None

    if source == dest:
        return current_ladder
    if current_ladder == []:
        current_ladder.append(source)

    ladders = []

    for i in range(len(source)):
        for l in range(ord('a'), ord('z')+1):
            l = chr(l)
            if l == source[i]:
                continue

            word = source[:i]+l+source[i+1:]
            if word == dest:
                current_ladder.append(dest)
                return [current_ladder]

            if word in current_ladder or word in deadends:
                continue

            if d.check(word):
                ladders.append(current_ladder + [word])

    result = []
    if ladders == []:
        deadends.append(current_ladder[-1])

    for ladder in ladders:
        for l in find_word_ladder(ladder[-1], dest, ladder, deadends, depth+1):
            if l[-1] == dest:
                result.append(l)
    print(result)
    return result



class TestWordLadder(unittest.TestCase):

    def test_word_ladder(self):
        print(find_word_ladder('hit', 'cog'))
        #find_word_ladder('test', 'cost')



if __name__=='__main__':
    unittest.main()
