# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == '__main__':
    with open('./data/APPLING1DAT.643', 'r') as file:
        lines = file.readlines()
        for l in lines:
            print(l.split())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
