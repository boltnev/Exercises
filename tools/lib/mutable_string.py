class MutableString:

    def __init__(self, string):
        self._string = list(string)

    def __getitem__(self, index):
        return self._string[index]

    def __setitem__(self, index, value):
        self._string[index] = value

    def __str__(self):
        return "".join(self._string)

    def __eq__(self, another):
        return str(self) == str(another)

    def __len__(self):
        return len(self._string)

    def __repr__(self):
        return "".join(self._string)

    def __reversed__(self):
        return MutableString(reversed(self._string))