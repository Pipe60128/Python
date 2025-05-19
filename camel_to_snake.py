def snakecode(word):
    snake = " "
    for char in word:
        if char.isupper():
            snake += "_" + char.lower()
        else:
             snake += char
    return snake
def main():
    w = input()
    print(f'{snakecode(w)}')
main()