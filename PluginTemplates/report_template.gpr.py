# encoding:utf-8
#
# Gramps plugin- an addon gramplet for
# the Gramps GTK+/GNOME based genealogy program
#
# Copyright (C) 2020-2024    Gary Griffin <genealogy@garygriffin.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

# ------------------------------------------------------------------------
#
# Gramps Plugin Registration (metadata and configuration information)
#    a sidecar to the file identified below as the fname (filename)
#    see https://gramps-project.org/wiki/index.php/Gramps_Glossary#addon
#
# ------------------------------------------------------------------------

# See https://www.gramps-project.org/wiki/index.php/Gramplets

from gramps.version import major_version, VERSION_TUPLE

if VERSION_TUPLE < (5, 2, 0):
    additional_args = {
        "status": UNSTABLE, # required
        "help_url": "Gramplets",#secure http not supported in these versions
    }
else:
    additional_args = {
        "status": EXPERIMENTAL, # required
        "audience": EXPERT,
        "maintainers": ["Gary Griffin",
            "Gramps Bugtracker"],
        "maintainers_email": ["genealogy@garygriffin.net",
            "https://gramps-project.org/bugs"],
        "help_url": "https://github.com/emyoulation/experimental-addons-source",
    }

# ------------------------------------------------------------------------
#
# Register Gramplet
#
# ------------------------------------------------------------------------

register(REPORT, # uppercase
        id="sample report", # required to be unique
        name=_("Sample Report"),
        description=_("sample set of reports that "
            "produces a catalog of specified objects."
        ), # optional
        authors=["Gary Griffin"], # optional
        authors_email=["genealogy@garygriffin.net"], # optional
        fname="report_template.py",
        version = '0.6.1',
        gramps_target_version=major_version,
        category = CATEGORY_TEXT,
        reportclass = 'report_template',
        optionclass = 'report_templateOptions',
        report_modes = [REPORT_MODE_GUI, REPORT_MODE_BKI, REPORT_MODE_CLI],
        require_active = False,
        **additional_args,
        )
