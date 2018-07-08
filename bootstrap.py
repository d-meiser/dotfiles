import os

my_dir = os.path.dirname(os.path.realpath(__file__))
home_dir = os.path.expanduser('~')

os.symlink(
        os.path.join(my_dir, '.vim'),
        os.path.join(home_dir, '.vim'))

