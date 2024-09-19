# encoding:utf-8
#
# Gramps plugin- a template to create an filtered addon gramplet for
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
# Gramps modules
#
# ------------------------------------------------------------------------

# See https://www.gramps-project.org/wiki/index.php/Gramplets

import inspect  # debug library
from gramps.gen.filters import CustomFilters
from gramps.gen.plug.menu import FilterOption
from gramps.gen.plug import Gramplet


class SampleGramplet(Gramplet):

    def init(self):
        self.filter_list = CustomFilters.get_filters("Person")
        self.filter_index = 0

    def build_options(self):
        self.filter_option = FilterOption("Filter", self.filter_index)
        self.filter_option.set_filters(self.filter_list)
        self.add_option(self.filter_option)
        self.print_filter_name()  # debug

    def on_load(self):
        if len(self.gui.data) > 0:
            self.filter_index = int(self.gui.data[0])

    def save_options(self):
        self.filter_index = self.filter_option.get_value()
        self.gui.data = [self.filter_index]
        self.print_filter_name()  # debug

    def print_filter_name(self):
        selected_filter = self.filter_option.get_filter()
        self.append_text(
            f"Called from: {inspect.currentframe().f_back.f_code.co_name}\n"
        )  # debug: ID the function's name which calls this function
        self.append_text(f"Filter =  {selected_filter.name}\n")
