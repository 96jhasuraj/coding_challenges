import argparse
import os

def count_bytes(file):
    return os.path.getsize(file)

def test_count_bytes():
    assert 342181 == count_bytes('./test.txt')

def check_asserts():
    test_count_bytes()

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
    parser.add_argument('file', help='File to process')

    args = parser.parse_args()
    
    if args.c:
        bytes_count = count_bytes(args.file)
        print(f"{bytes_count} {args.file}")

if __name__ == '__main__':
    main()
