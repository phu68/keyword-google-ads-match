


from typing import Counter


def split_line(text):

    # split the text
    words = list(text.split(" "))

    i = 0
    for word in text.split():
        words[i] = "+"+words[i]
        i+=1
    
    str1 = ' '.join(words)
    print(str1)
    # for each word in the line:
    # for word in words:
    #     # print the word
    #     words.append(word)
    #     print("+",words)
if __name__ == "__main__":
    split_line("phạm thanh phú")