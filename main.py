import argparse
import sys
import pathlib

import pygit2


class GitTuiError(Exception):
    """
    Generic Error for git-tui script
    """

class GitTui:
    def __init__(self, repo_path: str | pathlib.Path = "."):
        self.repo = self.__init_repo(repo_path=repo_path)

    def __init_repo(self, repo_path: str | pathlib.Path) -> pygit2.Repository:
        try:
            # When directory is not a git repo: _pygit2.GitError: Repository not found at /home
            # When directory doesn't exist: _pygit2.GitError: Repository not found at /home/bumbum
            # When user doesn't have permission to the directory: OSError: /root/git-tui: failed to resolve path '/root/git-tui': Permission denied
            return pygit2.Repository(path=repo_path)
        except (OSError, pygit2.GitError) as exc:
            raise GitTuiError(f'Failed to load repository: {exc}') from exc

def main(repo_path: str | pathlib.Path):
    try:
        GitTui(repo_path=repo_path)
    except GitTuiError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--repo-path", default=".", help="Path to the GIT repository, default is the current directory")
    args = parser.parse_args()

    main(
        repo_path=pathlib.Path(args.repo_path),
    )
