

def custom_write(file_name, strings: list[str]):
    f = open(file_name, 'a', encoding='utf-8')
    strings_positions = {}
    index = 1
    for i in strings:
        strings_positions[ (index, f.tell()) ] = i
        f.write('\n' + i)
        index += 1
    f.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)