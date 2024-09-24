import argparse
import os
import sys

def check_asserts():
    return True


def git_init(repo):
    '''
    Create a .git directory structure.
    '''
    if os.path.exists(repo):
        print(f"Error: The directory '{repo}' already exists.")
        sys.exit(1)
            
    os.mkdir(repo)
    os.mkdir(os.path.join(repo, '.git'))
    os.mkdir(os.path.join(repo, '.git', 'objects'))
    os.mkdir(os.path.join(repo, '.git', 'refs'))
    os.mkdir(os.path.join(repo, '.git', 'refs', 'heads'))
    
    with open(os.path.join(repo, '.git', 'HEAD'), 'wb') as f:
        f.write(b'ref: refs/heads/main')
    
     # Create the main branch file
    with open(os.path.join(repo, '.git', 'refs', 'heads', 'main'), 'wb') as f:
        f.write(b'')  # Initially, the main branch points to nothing (no commits yet)


    print(f"Repository initialized at '{repo}'.")


def main():
    try:
        check_asserts()
    except Exception as e:
        print(e)
        print("git_lite :: Warning checks failing")
        
    parser = argparse.ArgumentParser(
        prog='git_lite',
        description='My own git'
    )

    subparsers = parser.add_subparsers(dest='command', required=True)

    # Initialize command
    init_parser = subparsers.add_parser('init', help='Initialize a new repository')
    init_parser.add_argument('repo', help='Repository name or path')

    args = parser.parse_args()

    if args.command == 'init':
        git_init(args.repo)
        

if __name__ == '__main__':
    main()