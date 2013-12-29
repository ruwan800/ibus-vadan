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
                  (os.path.join(installDir, 'share', 'pixmaps' ), ['data/ibus-vadan.png'])]
     )
