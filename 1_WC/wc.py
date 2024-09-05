import argparse
import os

def count_bytes(file):
    return os.path.getsize(file)

def count_lines(file):
    try:
        with open(file,'r') as fp:
            return sum([1 for x in fp])
    except Exception as e:
        print(e)
        return -1        

def test_count_bytes():
    assert 342181 == count_bytes('./test.txt')
def test_line_counts():
    assert 7145 == count_bytes('./test.txt')

def check_asserts():
    test_count_bytes()
    test_line_counts()
    
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

    parser.add_argument('file', help='File to process')

    args = parser.parse_args()
    
    if args.c:
        bytes_count = count_bytes(args.file)
        print(f"{bytes_count} {args.file}")
    if args.c:
        print(f"{count_lines(args.file)} {args.file}")
        

if __name__ == '__main__':
    main()
