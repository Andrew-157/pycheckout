from git import Repo

repo = Repo(path=".")


for b in repo.branches:
    if b == repo.active_branch:
        print(f"Active branch: {b}")
    else:
        print(f"Non-active branch: {b}")
        repo.delete_head(b)
