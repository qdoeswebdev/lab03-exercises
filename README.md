# Lab 03: Git and GitHub
This repository documents my practice with 
local Git, GitHub, branches, and pull requests.

## README Responses

### 1.1 After initialization
```text
ls -la
total 0
drwxr-xr-x 1 sthoma12 sthoma12 4096 Sep  3 10:09 .
drwxr-xr-x 1 sthoma12 sthoma12 4096 Sep  3 10:09 ..
drwxr-xr-x 1 sthoma12 sthoma12 4096 Sep  3 10:09 .git
```

### 1.2 First git status
```text
git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)
```

### 1.3 After the first commit
```
git status
On branch main
nothing to commit, working tree clean
```

### 1.4 git log
```text
git log --oneline
609f94b (HEAD -> main) Create lab README
```

### 1.5 git diff
Paste the `git status` and `git diff` commands and their output.

```text
git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

~~~text
git diff
diff --git a/README.md b/README.md
index 4b56a46..825971e 100644
--- a/README.md
+++ b/README.md
@@ -1,4 +1,6 @@
 # Lab 03: Git and GitHub
+This repository documents my practice with
+local Git, GitHub, branches, and pull requests.

 ## README Responses

@@ -26,8 +28,17 @@ nothing added to commit but untracked files present (use "git add" to track)
 ```

 ### 1.3 After the first commit
+```
+git status
+On branch main
+nothing to commit, working tree clean
+```

 ### 1.4 git log
+```text
+git log --oneline
+609f94b (HEAD -> main) Create lab README
+```

 ### 1.5 git diff
~~~

How does this `git status` differ from the one in **1.2**?  
In the `git status` from **1.2**, there are no commits and `README.md` is not being tracked.
In this `git status`, `README.md` is being tracked, but changes to the file have not been staged for commit.

### 1.6 Git command reflections
In one or two sentences each, what does each command do?

- `git init` - initializes a Git repository in the current directory
- `git status` - shows the status of the working tree, including the current branch,
which files are being tracked, and which changes have been staged
- `git add` - adds one or more files to the staging area
- `git commit` - commits all files in the staging area to the current branch
- `git log` - lists all commits made to the current repository
- `git diff` - lists all differences between files in the working tree and
files in the staging area (or most recent commit) 

### 1.7 Repository link
https://github.com/qdoeswebdev/lab03-exercises

### 1.8 Comparing approaches
In your own words:

- How does the nested-loop approach check for a duplicate?
  - For each item in the array, check for equality with every other item in the array.
In other words, check every possible pair and return true if any pair contains matching items.
- How does the set-based approach check for a duplicate?
  - Create an empty set and iterate through the array, adding each item to the set if it is not already there
and returning true if it is. The set will already contain an item only if that item is a duplicate.
- What is the runtime and memory trade-off of each?
  - The set-based approach has a much better runtime than the nested-loop approach,
but the nested-loop approach uses less memory because it does not need a set.

### 1.9 Pull request merge options
In your own words, what does each GitHub merge option do?

- Create a merge commit
  - Uses `git merge` to move the changes from one branch to another while preserving commit history
- Squash and merge
  - Uses `git merge --squash` to combine all changes from one branch into a single commit before
moving them to another branch
- Rebase and merge
  - Uses `git rebase` to reapply the changes from one branch onto the end of another, rewriting commit history
