import os

from conans import ConanFile, tools


class TE(ConanFile):
    name = "type_erasure"
    version = "latest"
    url = "https://github.com/systrading/type-erasure"
    license = "Boost"
    description = "[Boost::ext].TE: C++17 Type Erasure Library"
    settings = "os", "compiler", "arch", "build_type"
    exports_sources = "include/*"
    no_copy_source = True

    def package(self):
        self.copy("*.hpp")


