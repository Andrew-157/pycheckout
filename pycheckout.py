import argparse
import sys
import pathlib

from pygit2 import Repository, GitError
from pygit2.enums import BranchType

class GitTuiError(Exception):
    """
    Generic Error for git-tui script
    """

class GitTui:
    # NOTE: consider using os.getcwd instead of "."
    def __init__(self, repo_path: str | pathlib.Path = "."):
        self.repo = self.__init_repo(repo_path=repo_path)

    def _init_repo(self, repo_path: str | pathlib.Path) -> Repository:
        try:
            # When directory is not a git repo: _pygit2.GitError: Repository not found at /home
            # When directory doesn't exist: _pygit2.GitError: Repository not found at /home/bumbum
            # When user doesn't have permission to the directory: OSError: /root/git-tui: failed to resolve path '/root/git-tui': Permission denied
            return Repository(path=repo_path)
        except (OSError, GitError) as exc:
            raise GitTuiError(f'Failed to load repository: {exc}') from exc

    def checkout(self, branch: str | None):
        pass

    def delete(self, branch: str | None):
        if branch:
            branch_object = self.repo.lookup_branch(branch, BranchType.LOCAL)
            if not branch_object:
                raise GitTuiError(f'Branch "{branch}" was not found')
            if branch_object.is_checked_out():
                raise GitTuiError(f'Cannot delete branch "{branch}" as we are currently checked out from it')

def main(
    branch: str | None,
    repo_path: str | pathlib.Path,
    delete: bool,
):
    try:
        gt = GitTui(repo_path=repo_path)
        if delete:
            gt.delete(branch=branch)
        else:
            gt.checkout(branch=branch)
    except GitTuiError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("branch", nargs="?", default=None, help="Branch which either should be deleted or checked out to, if not provided, the user will be able to choose the branch")
    parser.add_argument("-r", "--repo-path", default=".", help="Path to the GIT repository, default is the current directory")
    parser.add_argument("-d", "--delete", action="store_true", help="Should provided branch be deleted")
    args = parser.parse_args()

    main(
        branch=args.branch,
        repo_path=pathlib.Path(args.repo_path),
        delete=args.delete,
    )
