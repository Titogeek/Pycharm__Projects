from pathlib import Path

path = Path("maths")
print(path.exists)
# creating a new directory in project file
path2 = Path("Trialdir1")
path2.mkdir()
# Deleting a existing directory
# path2.rmdir()



