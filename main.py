def main():
    book_path = "books/frankenstein.txt"
    # file_contents = ""
    def get_text(path):
        with open(path) as f:
            file_contents = f.read()
            return file_contents
            # print(file_contents)
    
    def num_words(file):
        words = file.split()
        # print(words)
        return len(words)
    def num_char(txt):
        lowered = txt.lower().split()
        charactors = {}
        for txt in lowered:
            for char in txt:
                if char in charactors:
                    charactors[char] += 1
                else:
                    charactors[char] = 1
        # print(charactors)
        # print(lowered)
        return charactors
    def reporter(report, num):
        my_dict = list(report_num_char.items())
        report_sort = sorted(my_dict, key=lambda item:item[1], reverse=True)
        print(f"--- Begin report of books/frankenstein.txt --- \n {num} words found in the document")
        for key, value in report_sort:
            print(f"The {key} character was found {value} times")
        print("--- End report ---")
    text = get_text(book_path)
    report_num_char = num_char(text)
    num_of_words = num_words(text)
    reporter(report_num_char, num_of_words )
    # print(num_of_words)






main()