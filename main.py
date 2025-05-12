from stats import num_words, num_char, reporter
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    # file_contents = ""
    def get_book_text(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            file_contents = file.read()
        return file_contents
    

    # def reporter(report, num):
    #     my_dict = list(report_num_char.items())
    #     report_sort = sorted(my_dict, key=lambda item:item[1], reverse=True)
    #     print(f"--- Begin report of books/frankenstein.txt --- \n {num} words found in the document")
    #     for key, value in report_sort:
    #         print(f"The {key} character was found {value} times")
    #     print("--- End report ---")
    text = get_book_text(book_path)
    report_num_char = num_char(text)
    num_of_words = num_words(text)
    reporter(report_num_char, num_of_words )
    print(num_of_words, report_num_char)





main()