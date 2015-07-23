############
# SETTING UP #
############
# import this
def print_download_links():
    """Open links to download pip, and then to download IPython"""
    download_pip_link = 'http://pip.readthedocs.org/en/latest/installing.html'
    print "pip ({0}) is the package manager for Python packages".format(download_pip_link)

    print "when you know the name of a package that pip can get you, you type this into your terminal:",
    # that comma means the next time we print something, it will print on the same line.
    print "'pip install <package_name>'"
    print "or, if it tells you 'Permission Denied': sudo pip install <package_name>"
    awesome_sauce = 'IPython'
    print "you will pip this to download {0}!".format(awesome_sauce)

def matters_of_opinion():
    favorite_editors = dict()
    favorite_editors['zack'] = 'Sublime Text 3'
    favorite_editors['some_other_people'] = 'PyCharm'

    editor_links = dict()
    editor_links['Sublime Text 3'] = 'http://www.sublimetext.com/3'
    pycharm_url = 'https://www.jetbrains.com/student/'
    editor_links['PyCharm'] = pycharm_url


    for key, value in favorite_editors.items():
        print "{0}'s favorite editor for writing python programs is {1}, found at: {2}".format(key, value, editor_links[value])
    print #prints a blank line
    the_only_terminal_you_should_use = 'IPython'
    print "The terminal you see when you type 'python' into the terminal is really horrible."
    print "There might be an entire ACM talk about {0}, the only terminal you should use".format(the_only_terminal_you_should_use)


def get_started():
    print_download_links()
    matters_of_opinion()
    #  count_to_ten()
    # count_to_ten_slightly_faster()


def print_zen():
    import this

# get_started()


print_zen()
# def count_to_ten():
#     """ Count to a thousand"""
#     for x in range(1,11):  # for every number in [1,11)
#         print x

# def count_to_ten_slightly_faster():
#     for x in xrange(1,11):
#         print x


