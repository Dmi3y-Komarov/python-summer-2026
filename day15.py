from pathlib import Path

print('#1')

path = Path("bipki.txt")

print(f'filename {path.name}')
print(f'{path.stem}')
print(f'{path.parent}')
print(f'exists {path.exists()}')
print(f'{path.is_file()}')
print(f'{path.is_dir()}')
print(f'{path.suffix}')

print('#2')

dir_name = str(input('Write name: '))
path = Path(dir_name)
if path.exists():
    print(f'File exists')
else:
    print(f'File not exists')

print('#3')

if path.is_file():
    print('Is file')
elif path.is_dir():
    print('Is directory')
