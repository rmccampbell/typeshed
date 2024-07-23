from collections.abc import Callable
from typing import Any, ClassVar

from .._distutils.command import install as orig

class install(orig.install):
    user_options: ClassVar[list[tuple[str, str | None, str]]]
    boolean_options: ClassVar[list[str]]
    # Any to work around variance issues
    new_commands: list[tuple[str, Callable[[Any], bool]] | None]
    old_and_unmanageable: Any
    single_version_externally_managed: Any
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    path_file: Any
    extra_dirs: str
    def handle_extra_path(self): ...
    def run(self): ...
    def do_egg_install(self) -> None: ...
