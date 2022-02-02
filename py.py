'''
 Бывают ситуации, когда среди огромного количества файлов на вашем компьютере или в отдельной папке вам необходимо найти файлы определенного типа - например, изображения с расширением '.jpg' или документы с расширением '.txt' или файлы, в названии которых есть слово 'butterfly'. Делая это вручную можно потратить слишком много времени. Именно для облегчения подобных задач служит матчинг или паттерны для поиска файлов по определенной маске.
Эта миссия поможет вам разобраться с тем, как это работает.

Ваша задача - определить, соответствует ли заданное имя файла заданному поисковому паттерну.

Вот небольшая таблица, которая показывает, какие символы могут использовать в паттернах.
* 	соответствует всему (любому количеству любых символов)
? 	соответствует любому одному символу
'''



def unix_match(filename: str, pattern: str) -> bool:
    if "*" in pattern and "?" not in pattern:
        if len(pattern.replace("*", "")) == 0:
            return True
        list_file = [i for i in filename]
        list_pattern = [i for i in pattern]
        list_pattern = set(list_pattern)
        list_file = set(list_file)

        for i in list_file:
            list_pattern -= set(i)

        if len(list_pattern) == 1:
            return True
        else:
            return False

    elif "*" not in pattern and "?" in pattern:
        c = pattern.count("?")

        x = [i for i in filename]
        y = [i for i in pattern]

        list1 = []
        list2 = []
        for i in enumerate(x):
            list1.append(i)
        for i in enumerate(y):
            list2.append(i)
        result = set(list1) - set(list2)
        if len(result) == c:
            return True
        else:
            return False

    elif '*' in pattern and "?" in pattern:
        if len(pattern) <= len(filename):
            return True
        else:
            return False

    elif '*' not in pattern and "?" not in pattern:
        pattern = list(set(filename.split('.')) - set(pattern.split('.')))

        if len(pattern) != 0:
            return False
        else:
            return True


if __name__ == '__main__':
    print("Example:")
    print(unix_match("name.exe", "name.???"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")