def main():
    words = dict()  # aa -> [words starting with aa]

    for p in open("index.ftd").read().split("-- lib.word:"):
        if not p.strip(): continue
        word = p.split("\n")[0].strip()
        k = word.lower().replace("'", "").replace(".", "")[:2]
        for i in range(10):
            if str(i) in k:
                k = "numerals"
        if k not in words:
            words[k] = []
        words[k].append(p)

    for k in words:
        f = open("%s.ftd" % k, "w")
        f.write("-- import: rakeshmamata.github.io/hindi-dictionary/lib\n\n")
        for i in words[k]:
            f.write("-- lib.word:%s" % i)

    f = open("iiii.ftd", "w")
    keys = words.keys()
    keys.sort()
    for k in keys:
        f.write("-- ftd.text: %s\nlink: %s/\n\n\n" % (k, k))

if __name__ == "__main__":
    main()
