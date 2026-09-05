# SPDX-License-Identifier: MPL-2.0 OR BSD-3-Clause
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#
# Alternatively, this file may be used and redistributed under the terms
# of the 3-Clause BSD License as published in the repository's LICENSE-BSD file.
#
# Copyright (c) 2026 Benny Dreamly. All rights reserved.

from pathlib import Path

import settings

class Sims4Settings(settings.Group):
    class ModsFolder(settings.UserFolderPath):
        """Path to the Sims 4 Mods folder"""
        description = "the folder your Sims 4 mods are installed to"

    mods_folder: ModsFolder = ModsFolder(Path.home() / "Documents" / "Electronic Arts" / "The Sims 4" / "Mods")