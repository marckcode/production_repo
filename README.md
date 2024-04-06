<h1 style="color:cyan;"> GIT </h1>

CONFIG:

- git config --global user.email \<email>
- git config --global user.name \<name>


CONCEPTS:

- Repositories: Folders for files, managed by git.
- Commits: Set of changes in a repository.
- Branches
- Merging
- Tags

COMMANDS:

- git init
- git add \<file>
- git pull [origin xxxx]
- git push [origin xxxx]
- git branch
- git branch -d 
- git checkout | git switch
- git checkout -b \<branch name>
- git log
- git merge
- git rebase
- git diff
- git tag
- git stash pop | recovers the last deleted commit
- git reset
- HEAD

WORK FLOW:

- git init
- git add .
- git commit -m "message"
- \<create repo in web>
- git remote add origin \<link>
- git branch -M main
- git push -u origin main


# TEST CHANGE