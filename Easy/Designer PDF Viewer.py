
#LINK https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true

import string

def designerPdfViewer(h, word):
    list_letters = list(string.ascii_lowercase)
    zipped = dict(zip(list_letters,h))
    tallest_l = 0
    for letter in word:
        if zipped.get(letter) > tallest_l:
            tallest_l = zipped.get(letter)
    area = tallest_l * len(word)
    return area
    
if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(result)
