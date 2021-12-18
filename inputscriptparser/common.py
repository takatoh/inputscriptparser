class Keyword():
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f'Keyword<{self.val}>'

    def __repr__(self):
        return f'Keyword<{self.val}>'


def _flatten(lis):
    result = []
    for elem in lis:
        if isinstance(elem, list):
            result += _flatten(elem)
        else:
            result.append(elem)
    return result
