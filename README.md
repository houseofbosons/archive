# House-of-Bosons Content Archive
All the public blog posts are hosted here!

# Instructions (un-understandable :p)
1. Create a new directory for every new blog post.
2. For series, created nested directory trees for each of the sub-post document.
3. Store all the releted assets (ex. images), in a directory called `assets` for each blog.

# Clone Repository
```
git clone git@github.com:houseofbosons/archive.git
```

# Scripts

To create directories and files for a new Post:
```
python3 ./scripts/new_blog.py
```

To create directories and files for a new Series:
```
python3 ./scripts/new_series.py
```

To list out all the content
```
python3 ./scripts/list_all.py
```

To commit content (git):
```
bash ./scripts/update_content.sh
```
