from pathlib import Path, PureWindowsPath

dir_name = Path("/home/wender/Desktop/Projects/Python")
path_on_windows = PureWindowsPath(dir_name)

list_of_files = []

def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*.map')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        list_of_files.append(str(path));
        print(f'{spacer}+ {path.name}')


tree(dir_name)
print(len(list_of_files))
print(list_of_files)
num_file = 0
for myfile in list_of_files:
    num_file += 1
    print('{}. {}'.format(num_file,myfile))
print('Enter the number of files you want to move:')
input()