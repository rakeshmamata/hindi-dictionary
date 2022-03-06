import sys
sys.path.append("brahmic")

import cmu

def main():
    old = read_old()
    f = open("10k.txt")

    result = (process(row, old) for row in f.readlines())
    result = [r for r in result if r]
    print "\n\n\n".join(result).encode("utf-8")


def process(row, old):
    word = row.split()[1].strip()
    if word in old:
        return

    # import pdb; pdb.set_trace()
    arpa = cmu.lookup(word.lower())
    american = cmu.trans(arpa)


    return """
-- lib.word: %s
american: %s
arpabet: %s
    """ % (word, american, arpa)



def read_old():
    f = open("index.ftd")
    # import pdb; pdb.set_trace()
    o = dict()
    for l in f.readlines():
        if not l.startswith("-- lib.word:"):
            continue
        word = l.split(":")[1].strip()
        o[word.lower()] = 1
    return o


if __name__ == "__main__":
    main()
