def num_words(file):
        words = file.split()
        return len(words)
def num_char(txt):
        lower = txt.lower().split()
        charactors = {}
        for txt in lower:
                for char in txt:        
                        if char in charactors:
                                charactors[char] += 1
                        else:
                                charactors[char] = 1
        return charactors
def reporter(report, num_char):
        lists = []
        print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {num_char} total words\n--------- Character Count -------\n")
        for key, value in report.items():
                print(f"{key}: {value}")
                lists.append({"char": key, "num": value})
        lists.sort(key=lambda x: x["num"], reverse=True)
        return lists
