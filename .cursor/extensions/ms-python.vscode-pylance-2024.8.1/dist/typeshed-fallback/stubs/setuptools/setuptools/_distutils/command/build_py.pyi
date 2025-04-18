from _typeshed import Incomplete

from ..cmd import Command

class build_py(Command):
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    negative_opt: Incomplete
    build_lib: Incomplete
    py_modules: Incomplete
    package: Incomplete
    package_data: Incomplete
    package_dir: Incomplete
    compile: int
    optimize: int
    force: Incomplete
    def initialize_options(self) -> None: ...
    packages: Incomplete
    data_files: Incomplete
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def get_data_files(self): ...
    def find_data_files(self, package, src_dir): ...
    def build_package_data(self) -> None: ...
    def get_package_dir(self, package): ...
    def check_package(self, package, package_dir): ...
    def check_module(self, module, module_file): ...
    def find_package_modules(self, package, package_dir): ...
    def find_modules(self): ...
    def find_all_modules(self): ...
    def get_source_files(self): ...
    def get_module_outfile(self, build_dir, package, module): ...
    def get_outputs(self, include_bytecode: bool = True): ...
    def build_module(self, module, module_file, package): ...
    def build_modules(self) -> None: ...
    def build_packages(self) -> None: ...
    def byte_compile(self, files) -> None: ...
