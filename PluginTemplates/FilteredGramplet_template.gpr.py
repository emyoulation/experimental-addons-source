# encoding:utf-8
#
# Gramps plugin- an addon gramplet for
# the Gramps GTK+/GNOME based genealogy program
#
# Copyright (C) 2024     Kari Kujansuu
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
#    a sidecar to the file idendified below as the fname (filename)
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
        "maintainers": ["Kari Kujansuu",
            "Gramps Bugtracker"],
        "maintainers_email": ["kari.kujansuu@gmail.com",
            "https://gramps-project.org/bugs"],
        "help_url": "https://www.gramps-project.org/wiki/index.php/Gramplets",
#        "requires_mod": ['svgwrite'],
#        "requires_gi": [('GooCanvas', '2.0,3.0')],
#        "requires_exe": ['dot'],
    }

# ------------------------------------------------------------------------
#
# Register Gramplet
#
# ------------------------------------------------------------------------

register(GRAMPLET, # uppercase
         id="SampleGramplet",
         name=_("Sample Gramplet"),
         description=_("sample Gramplet with "
             "filter Configuration options"
         ), # optional
         navtypes=["Person","Families"], # optional
         authors=["Kari Kujansuu"], # optional
         authors_email=["kari.kujansuu@gmail.com"], # optional
         fname="SampleGramplet.py",
         height=300,
         detached_width=250, # optional
         detached_height=400, # optional
         expand=True, # optional
         gramplet='SampleGramplet',
         gramplet_title=_("Sample Gramplet"),
         version = '0.0.0',
         gramps_target_version=major_version,
         **additional_args,
         )
