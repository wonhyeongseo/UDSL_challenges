# v0.0.1

def code_logger():
    """
    Get a python file, and strip strings and comments from code:
    to return a dictionary of methods and unique variable names as keys-
    with their number of occurances as values
    AND including the comment operator and its occurances
    """
    from collections import defaultdict
    from re import sub
    dd = defaultdict(lambda: 0)
    remove_strings = r'"[^"]*"|\'[^\']*\''
    remove_comments = r'#.*' # different for every prog.lang.
    remove_args = r'[(][^)]*[)]'
    # abstract_comprehension = r'[]'
    filename = input('파일 경로를 입력하십시오...: ')
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            line = sub(remove_strings, '', line)
            if '#' in line: dd['#(주석)'] += 1
            line = sub(remove_comments, '', line)
            line = sub(remove_args, '()', line)
            for word in line.split():
                if len(word) == 0: continue
                word = word.strip('[](),')
                dd[word] += 1

    for word in sorted(dd):
        print('<{word}> : {num_of_occurances}번 출현'.format(
            word=word, num_of_occurances=dd[word]))
code_logger()
