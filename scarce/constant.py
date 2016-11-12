import os

import scarce

# Silicon constants
epsilon_s = 1.04e-10  # Permittivity of silicon [F/m]
density = 2.3290  # Density of silicon [g cm^-3], wikipedia

# Software constants
# Get package path
package_path = os.path.dirname(scarce.__file__)  # Get the absolute path of this software
FIXTURE_FOLDER = os.path.join(package_path, 'testing/fixtures')
DATA_FOLDER = os.path.join(package_path, 'scarce/scarce')