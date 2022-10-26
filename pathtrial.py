from pathlib import Path

path3 = Path()

for file in path3.glob('*.py'):
    print(file)

path = Path("maths")
print(path.exists)
# creating a new directory in project file
path2 = Path("Trialdir2")
path2.mkdir()
# Deleting a existing directory
# path2.rmdir()



