import os

my_dir = os.path.dirname(os.path.realpath(__file__))
home_dir = os.path.expanduser('~')

# vim
dot_vim_dir = os.path.join(home_dir, '.vim')
if os.path.isdir(dot_vim_dir):
    os.rename(dot_vim_dir, dot_vim_dir + '_bak')
os.symlink(
        os.path.join(my_dir, '.vim'), dot_vim_dir)
dot_vimrc = os.path.join(home_dir, '.vimrc')
if os.path.isfile(dot_vimrc):
    os.rename(dot_vimrc, dot_vimrc + '_bak')

