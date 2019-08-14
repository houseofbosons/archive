import os

print("Reading valid directories..\n")

blogs = []
series = []
unidentified = []

# for root, subdirs, files in os.walk(os.path.join(".","content")):
#   print(subdirs)

rootdir = os.path.join(".", "content")

# print(os.listdir(os.path.join(".","content")))

for each in os.listdir(rootdir):
  dn = os.path.join(rootdir, each)
  
  if os.path.isdir(dn):
    with open(os.path.join(dn, ".metadata")) as f:
      isBlog = f.readlines()

      if len(isBlog) > 0 and isBlog[0] == "0":
        blogs.append(each)
      elif len(isBlog) > 0 and isBlog[0] == "1":
        series.append(each)
      else:
        unidentified.append(each)

print("**", len(blogs), "Blogs **")
for b in blogs:
  print("\t--", b)

print("**", len(series), "Series **")
for s in series:
  print("\t--", s)

print("**", len(unidentified), "Unidentified **")
for u in unidentified:
  print("\t--", u)
  
print("")