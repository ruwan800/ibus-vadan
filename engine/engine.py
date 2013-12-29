# vim:set et sts=4 sw=4:
#
# ibus-vadan - Input method for Sinhala based on I-Bus
# 
# Copyright (C) 2012 ruwan Jayasinghe <ruwan800@gmail.com>
#               2012 Kasun Madhusanka <kasunmbx@gmail.com>
# 
# ibus-vadan is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# ibus-vadan is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import gobject
#import pango
import ibus
from ibus import keysyms
from ibus import modifier
from db import Db


class Engine(ibus.EngineBase):


    def __init__(self, bus, object_path):
        super(Engine, self).__init__(bus, object_path)
        self.__is_invalidate = False
        self.__preedit_string = u""
        self.__preedit_word   = u""
        self.__atEnglish = False
        self.__lookup_table = ibus.LookupTable()
        self.__lookup_table.set_orientation(1)
        self.__prop_list = ibus.PropList()
        self.__prop_list.append(ibus.Property(u"test", icon = u"ibus-locale"))

    def process_key_event(self, keyval, keycode, state):
        # ignore key release events
        is_press = ((state & modifier.RELEASE_MASK) == 0)
        if not is_press:
            return False

        if self.__preedit_string:
            if keyval == keysyms.Return:
                self.commit_current_string()
                return True
            elif keyval == keysyms.Escape:
                self.__preedit_string = u""
                self.__update()
                return True
            elif keyval == keysyms.BackSpace:
                self.__preedit_string = self.__preedit_string[:-1]
                self.__invalidate()
                return True
            elif keyval == keysyms.space:
                self.commit_current_string()
                return False
            elif keyval >= keysyms._0 and keyval <= keysyms._9:
                index = keyval - keysyms._1
                if index == -1:
                    index = 9
                if index < self.__lookup_table.get_number_of_candidates():
                    self.__commit_string( self.__lookup_table.get_candidate(index).text+" ")
                return True
            elif keyval == keysyms.Page_Up or keyval == keysyms.KP_Page_Up:
                self.page_up()
                return True
            elif keyval == keysyms.Page_Down or keyval == keysyms.KP_Page_Down:
                self.page_down()
                return True
            elif keyval == keysyms.Up:
                self.cursor_up()
                return True
            elif keyval == keysyms.Down:
                self.cursor_down()
                return True
            elif keyval == keysyms.Left or keyval == keysyms.Right:
                return True
        if keyval in xrange(keysyms.a, keysyms.z + 1) or \
            keyval in xrange(keysyms.A, keysyms.Z + 1):
            if state & (modifier.CONTROL_MASK | modifier.ALT_MASK) == 0:
                self.__preedit_string += unichr(keyval)
                self.__invalidate()
                return True
        else:
            if keyval < 128 and self.__preedit_string:
                self.__commit_string(self.__preedit_string)
        return False

    def __invalidate(self):
        if self.__is_invalidate:
            return
        self.__is_invalidate = True
        gobject.idle_add(self.__update, priority = gobject.PRIORITY_LOW)

    def show_cursor(self):
        if not self.__lookup_table.is_cursor_visible():
            self.__lookup_table.show_cursor(True)
            self.__update_lookup_table()

    def hide_cursor(self):
        if  self.__lookup_table.is_cursor_visible():
            self.__lookup_table.show_cursor(False)
            self.__update_lookup_table()

    def commit_current_string(self):
        if self.__lookup_table.is_cursor_visible():
            if self.__lookup_table.get_number_of_candidates() > 0:
                self.__commit_string(self.__lookup_table.get_current_candidate().text)
        else:
            if self.__atEnglish:
                self.__commit_string(self.__preedit_string)
            else:
                self.__commit_string(self.__preedit_word)

    def __update_preedit_text(self,text):
        self.update_preedit_text(ibus.Text(text), len(text), len(text) > 0)
        self.__update_lookup_table()
        return True

    def cursor_up(self):
        if self.__lookup_table.is_cursor_visible():
            if self.__lookup_table.cursor_up():
                self.cursor_up_lookup_table()
            else:
                self.hide_cursor()
        else:
            self.__atEnglish = True
            self.__update_preedit_text(self.__preedit_string)
        return True

    def cursor_down(self):
        if self.__lookup_table.is_cursor_visible():
            if self.__lookup_table.cursor_down():
                self.cursor_down_lookup_table()
        else:
            if self.__atEnglish:
                self.__atEnglish = False
                self.__update_preedit_text(self.__preedit_word)
            else:
                self.show_cursor()
        return True

    def __commit_string(self, text):
        self.commit_text(ibus.Text(text))
        status = text != self.__preedit_string
        self.__preedit_string = u""
        self.__preedit_word   = u""
        self.__atEnglish      = False
        self.__update()
        if status:
            Db.updateDb(text)

    def __update(self):
        self.__lookup_table.clean()
        self.__lookup_table.show_cursor(False)
        if len(self.__preedit_string) > 0:
            suggestions = Db.suggest(self.__preedit_string)
            if suggestions:
                self.__preedit_word = suggestions[0]
            else:
                self.__preedit_word = self.__preedit_string
            for text in suggestions[1:]:
                self.__lookup_table.append_candidate(ibus.Text(text))
        else:
            self.__preedit_word   = u""
        self.update_auxiliary_text(ibus.Text(self.__preedit_string), len(self.__preedit_string) > 0)
        self.__update_preedit_text(self.__preedit_word)
        self.__is_invalidate = False

    def __update_lookup_table(self):
        visible = self.__lookup_table.get_number_of_candidates() > 0
        self.update_lookup_table(self.__lookup_table, visible)


    def focus_in(self):
        self.register_properties(self.__prop_list)

    def focus_out(self):
        pass

    def reset(self):
        pass

    def property_activate(self, prop_name):
        print "PropertyActivate(%s)" % prop_name

