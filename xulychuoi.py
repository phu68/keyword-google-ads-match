


from typing import Counter

def tach_chuoi(chuoi):
    chuoi_moi = list(chuoi.split(" "))
    return chuoi_moi

def doi_sanh_rong_co_dk(chuoi):
    chuoi_moi = list(chuoi.split(" "))
    i = 0
    for tu in chuoi.split():
        chuoi_moi[i] = "+"+chuoi_moi[i]
        i += 1
    str1 = ' '.join(chuoi_moi)
    # print(str1)
    return str1


def chuyen_str(chuoi):
    str1 = ' '.join(chuoi)
    return str1


# def split_line(text):

#     # split the text
#     words = list(text.split(" "))

#     i = 0
#     for word in text.split():
#         words[i] = "+"+words[i]
#         i+=1
    
#     str1 = ' '.join(words)
#     print(str1)
    # for each word in the line:
    # for word in words:
    #     # print the word
    #     words.append(word)
    #     print("+",words)
if __name__ == "__main__":
    #split_line("phạm thanh phú")
    phu = "phạm thanh phú"
    # tach_chuoi(phu)
    kq = doi_sanh_rong_co_dk(phu)
    # chuyen_str(phu)
    print(kq)