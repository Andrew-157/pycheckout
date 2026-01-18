from git import Repo

repo = Repo(".")

print(repo.__dict__)
print(repo.is_dirty())
