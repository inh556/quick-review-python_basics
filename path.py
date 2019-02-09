import os

path = os.path.abspath('.')  # current
print(path)
print(os.path.exists('/Users/yanbinjin/coding'))
print(os.path.isfile('/Users'))
print(os.path.isdir('/Users'))
os.path.join('/path2', '/path2') # join pathes


from pathlib import Path
p = Path('.')
print(p.resolve())


q = Path('/User/a/b/c')
Path.mkdir(q.parent=True)