import os

# askFor asks for user input
def askFor(label):
  return input(label)

# getPostname recursively gets a non-empty postname from teh user
def getPostname(name):
  if name.strip() != "":
    return name

  pn = askFor("Enter a postname : ")
  return getPostname(pn)

# checkFormat checks for spaces in postname,
# and confirms if the user wants to use it or not
def checkFormat(pn):
  resp = askFor("Sure about using spaces (\" \") in name [Yes/No/Rename] : ")
  if resp[:1].lower() == "y":
    return pn

  elif resp[:1].lower() == "n":
    print("Removing spaces (\" \") ..")
    return pn.replace(' ', '-')

  elif resp[:1].lower() == "r":
    new = getPostname("")
    if len(new.split(" ")) > 1:
      new = checkFormat(new)
    return new

  return checkFormat(pn)


# Getting Post Name from user
postname = getPostname("")

if len(postname.split(" ")) > 1:
  postname = checkFormat(postname)

# creating directories
dirname = os.path.join(".", "content", postname)

filenames = [
  os.path.join(dirname, postname.replace(' ', '-')+"-0.md"),
  os.path.join(dirname, postname.replace(' ', '-')+"-0.html")
]

conflict = os.path.exists(dirname)

if conflict:
  quit("Directory \""+dirname+"\" is already exist")

# creating directory
print("Creating post directory..")
os.makedirs(os.path.join(dirname, "Assets"))

# creating document file
print("Creating document files..")

for fn in filenames:
  file = open(fn, "w")
  file.write("Automatically generated content\n"+fn)
  file.close()

# indicating that the directory is a blog
file = open(os.path.join(dirname, ".metadata"), "w")
file.write("1")
file.close()