import csv

def main():
    f = open("e.csv")
    r = csv.reader(f)
    # r.next()

    result = (process(row) for row in r)
    result = [r for r in result if r]
    print("\n\n\n".join(result))


def process(row):
    if "ARPABet" in row[1]:
        return
    if not row[1].strip():
        return
    (word, rest) = row[1].split(":", 1)
    word = word.strip()
    (arpa, american) = rest.split("=>")
    arpa = arpa.strip()
    american = american.strip()

    indian = row[2]
    meaning = row[3]
    explanation = row[4]

    if indian.strip().lower() != "same":
        indian = f"\nindian: {indian}"
    else:
        indian = ""

    if meaning.strip():
        meaning = f"\nmeaning: {meaning}"
    else:
        meaning = ""

    return f"""
-- lib.word: {word}
american: {american}
arpabet: {arpa}{indian}{meaning}

{explanation}
    """.strip()




if __name__ == "__main__":
    main()
