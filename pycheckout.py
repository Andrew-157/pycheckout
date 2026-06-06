import sys
from pathlib import Path

from pygit2 import init_repository
from pygit2.enums import BranchType
from prompt_toolkit.shortcuts import choice
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style


class PyCheckoutError(Exception):
    """
    Exception to be raised by PyCheckout class
    """

class PyCheckout:
    def __init__(
        self,
        repo_path: str | None = None,
        use_tui: bool = True
    ):
        self.repository = repo_path
        self.use_tui = use_tui

    @property
    def repository(self) -> str | None:
        if self._repository:
            return str(Path(self._repository.path).parent.absolute())
        return None

    @repository.setter
    def repository(self, repo_path: str | None):
        if not repo_path:
            self._repository = None
        else:
            try:
                self._repository = init_repository(repo_path)
            except Exception as exc:
                raise PyCheckoutError(f'Failed to initialize repository under path "{repo_path}"') from exc

    @property
    def local_branches(self) -> list[str]:
        if not self._repository:
            raise PyCheckoutError('Cannot list local branches without initialized repository')
        return list(self._repository.branches.local)

    @property
    def checked_out_branch(self) -> str:
        if not self._repository:
            raise PyCheckoutError('Cannot get currently checked out branch without initialized repository')
        return self._repository.head.shorthand

    def _get_branch_name_from_tui(self) -> str:
        if not self.use_tui:
            raise PyCheckoutError('Cannot get branch from user with TUI mode disabled')
        if not self._repository:
            raise PyCheckoutError('Cannot use TUI mode without initialized repository')
        try:
            style = Style.from_dict({
                'current-branch': 'fg:#2ecc71 bold'
            })
            branch_name = choice(
                message="Choose a branch:",
                options = [
                    (br, HTML(f'<current-branch>* {br}</current-branch>'))
                    if br == self.checked_out_branch
                    else (br, br)
                    for br in self.local_branches
                ],
                style=style,
            )
            return branch_name
        except KeyboardInterrupt:
            sys.exit(0)

    def checkout(self, branch_name: str | None = None):
        if not self._repository:
            raise PyCheckoutError('Cannot checkout to a branch without iniatialized repository')
        if not branch_name and self.use_tui is False:
            raise PyCheckoutError('Branch name must be provided for checkout if TUI mode is disabled')
        branch_name = branch_name if branch_name else self._get_branch_name_from_tui()
        branch_obj = self._repository.lookup_branch(
            branch_name,
            BranchType.LOCAL,
        )
        if not branch_obj:
            raise PyCheckoutError(f'Branch "{branch_name}" was not found locally for the repository "{self.repository}"')
        self._repository.checkout(branch_obj)

    def delete_branch(self, branch_name: str | None = None):
        if not self._repository:
            raise PyCheckoutError('Cannot delete branch without initialized repository')
        if not branch_name and self.use_tui is False:
            raise PyCheckoutError('Branch name must be provided for delete if TUI mode is disabled')
        branch_name = branch_name if branch_name else self._get_branch_name_from_tui()
        if branch_name == self.checked_out_branch:
            raise PyCheckoutError('Cannot delete branch from which the repository is currently checked out')
        branch_obj = self._repository.lookup_branch(
            branch_name,
            BranchType.LOCAL,
        )
        if not branch_obj:
            raise PyCheckoutError(f'Branch "{branch_name}" was not found locally for the repository "{self.repository}"')
        branch_obj.delete()
