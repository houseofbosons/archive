import os

# askFor asks for user input
def askFor(label):
  return input(label)

# getPostname recursively gets a non-empty postname from teh user
def getPostname(name):
  if name.strip() != "":
    return name

  sn = askFor("Enter a postname : ")
  return getPostname(sn)

# checkFormat checks for spaces in postname,
# and confirms if the user wants to use it or not
def checkFormat(sn):
  resp = askFor("Sure about using spaces (\" \") in name [Yes/No/Rename] : ")
  if resp[:1].lower() == "y":
    return sn

  elif resp[:1].lower() == "n":
    print("Removing spaces (\" \") ..")
    return sn.replace(' ', '-')

  elif resp[:1].lower() == "r":
    new = getPostname("")
    if len(new.split(" ")) > 1:
      new = checkFormat(new)
    return new

  return checkFormat(sn)


# Getting Post Name from user
seriesname = getPostname("")

if len(seriesname.split(" ")) > 1:
  seriesname = checkFormat(seriesname)

# creating directories
rootdir = os.path.join(".", "content", seriesname)

dirnames = [
  os.path.join(rootdir, "New-Post"),
  os.path.join(rootdir, "Another-Post")
]

filenames = [
  os.path.join(dirnames[0], "New-Post-0.md"),
  os.path.join(dirnames[1], "Another-Post-0.html")
]

conflict =  os.path.exists(rootdir)

if conflict:
  quit("Directory \""+rootdir+"\" is already exist")

# creating directory
print("Creating post directory..")
for dn in dirnames:
  os.makedirs(os.path.join(dn, "Assets"))

# creating document file
print("Creating document files..")
for fn in filenames:
  file = open(fn, "w")
  file.write("Automatically generated content\n"+fn)
  file.close()

# indicating that the directory is a series
file = open(os.path.join(rootdir, ".metadata"), "w")
file.write("0")
file.close()