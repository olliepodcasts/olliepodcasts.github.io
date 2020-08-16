#!/usr/bin/python3

""" Build index from directory listing for each directory in dirs. """
import os

# May need to do "pip install mako"
from mako.template import Template

INDEX_TEMPLATE = r""" ${header}

% for name in names:
* [${name}](${name})
% endfor
"""

EXCLUDED = ['index.md', 'generate_index.py']


def write(filename, content):
    """ Writes content to the file filename. """
    file = open(filename, 'w')
    file.write(content)
    file.close()


def generate_index():
    """ Generates an index.md file for the current working directory. """
    filenames = [filename for filename in sorted(os.listdir('.'))
                 if filename not in EXCLUDED]
    header = os.path.split(os.getcwd())[1] + '/'
    write('index.md', '##' + Template(INDEX_TEMPLATE).render(names=filenames, header=header))


def get_dirs(superdirectory):
    """ Returns a list of dirs in a given directory. """
    return next(os.walk(superdirectory))[1]


def get_dirs_with_superdirectory(superdirectory):
    """ Returns a list of dirs in a given directory, in the form ["superdirectory/dir", ...]. """
    return [superdirectory + "/" + filename for filename in get_dirs(superdirectory)]


def main():
    dirs = []
    dirs_and_subdirs = ['.', 'jbs', 'jbs/2019', 'dmr']

    for superdir in dirs_and_subdirs:
        dirs += [superdir] + get_dirs_with_superdirectory(superdir)

    home_dir = os.getcwd()
    for directory in dirs:
        os.chdir(directory)
        generate_index()
        os.chdir(home_dir)


if __name__ == '__main__':
    main()
