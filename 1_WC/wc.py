import argparse
import os

def count_bytes(file):
    try:
        return os.path.getsize(file)
    except Exception as e:
        print(e)
        return -1

def count_lines(file):
    try:
        with open(file,'r',encoding='utf-8') as fp:
            return sum([1 for x in fp])
    except Exception as e:
        print(e)
        return -1        

def count_words(file,):
    try:
        with open(file,'r',encoding='utf-8') as fp:
            return sum([len(line.split(' ')) for line in fp])
    except Exception as e:
        print(e)
        return -1   
    
def test_count_bytes():
    actual = count_bytes('./test.txt')
    expected = 342181  
    assert actual == expected, f"Byte count test failed: expected {expected}, got {actual}"

def test_line_counts():
    actual = count_lines('./test.txt')
    expected = 7143  
    assert actual == expected, f"Line count test failed: expected {expected}, got {actual}"

def test_word_counts():
    actual = count_words('./test.txt')
    expected = 60176  
    assert actual == expected, f"Word count test failed: expected {expected}, got {actual}"


def check_asserts():
    test_count_bytes()
    test_line_counts()
    test_word_counts()
    
def main():
    try:
        check_asserts()
    except Exception as e:
        print(e)
        print("ccwc :: Warning checks failing")
        
    parser = argparse.ArgumentParser(
        prog='ccwc',
        description='Counts bytes in a file.'
    )
    parser.add_argument('-c', action='store_true', help='Print byte count of a file')
    parser.add_argument('-l', action='store_true', help='Print lines count of a file')
    parser.add_argument('-w', action='store_true', help='Print words count of a file')

    parser.add_argument('file', help='File to process')

    args = parser.parse_args()
    
    if args.c:
        bytes_count = count_bytes(args.file)
        print(f"{bytes_count} {args.file}")
    if args.l:
        print(f"{count_lines(args.file)} {args.file}")
    if args.w:
        print(f"{count_words(args.file)} {args.file}")
        

if __name__ == '__main__':
    main()
