#!/usr/bin/python
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


from distutils.core import setup
import glob
import os

installDir = "/usr"
dataDir = "/var"
package = "ibus-vadan"
setup(name='ibus-vadan',
      version='1.0',
      description='Input method for Sinhala based on I-Bus',
      author='ruwan Jayasinghe, Kasun Madhusnka',
      author_email='ruwan800@gmail.com, kasunmbx@gmail.com',
      long_description = 'Input method for Sinhala based on I-Bus',
      license = 'GPL',
      data_files=[(os.path.join(installDir, 'lib', package ), ['ibus-vadan']),
                  (os.path.join(installDir, 'share', package ), glob.glob('engine/*.py') ),
                  (os.path.join(installDir, 'share', 'ibus', 'component' ), ['data/ibus-vadan.xml']),
                  (os.path.join(dataDir, 'lib', package ), ['data/vadan.sqlite']),
                  (os.path.join(installDir, 'share', 'pixmaps' ), ['data/ibus-vadan.svg'])]
     )
