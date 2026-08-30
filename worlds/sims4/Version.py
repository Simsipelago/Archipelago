# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#
# Alternatively, this file may be used and redistributed under the terms
# of the 3-Clause BSD License as published in the repository's LICENSE-BSD file.
#
# Copyright (c) 2026 Benny Dreamly. All rights reserved.

VERSION: tuple[int, int, int] | tuple[int, int, int, str] = (2, 0, 1)


class Sims4Version:

    @staticmethod
    def tuple_to_str(version: tuple[int, int, int] | tuple[int, int, int, str]) -> str:
        if len(version) == 3:
            return f"{version[0]}.{version[1]}.{version[2]}"
        else:
            major, minor, patch, suffix = version
            return f"{major}.{minor}.{patch}-{suffix}"

    @staticmethod
    def str_to_tuple(version: str) -> tuple[int, int, int] | tuple[int, int, int, str]:
        if "-" in version:
            base, suffix = version.split("-", 1)  # only split on first dash
            major, minor, patch = map(int, base.split("."))
            return major, minor, patch, suffix
        else:
            major, minor, patch = map(int, version.split("."))
            return major, minor, patch

    @staticmethod
    def is_rc(version: tuple[int, int, int] | tuple[int, int, int, str]) -> bool:
        return len(version) == 4

    @staticmethod
    def does_major_version_mismatch(
            client_version: tuple[int, int, int] | tuple[int, int, int, str],
            server_version: tuple[int, int, int] | tuple[int, int, int, str]
    ) -> bool:
        return client_version[0] != server_version[0]
