#! /usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake


class Interview360(ConanFile):
    name = 'Interview360'

    settings = [
        'os',
        'build_type',
        'arch',
        'build_type',
    ]

    generators = [
        'cmake',
    ]

    def config_options(self) -> None:
        self.options['qt'].shared = True

    def requirements(self) -> None:
        self.requires('qt/6.4.2')

    def build(self) -> None:
        cmake: CMake = CMake(self)

        cmake.configure()
        cmake.build()

    def imports(self) -> None:
        self.copy('*.dll', dst='bin', src='bin')
        self.copy('*.so', dst='lib', src='lib')
        self.copy('*.dylib', dst='lib', src='lib')
        self.copy('platforms/*', dst='bin', src='res/archdatadir/plugins')
