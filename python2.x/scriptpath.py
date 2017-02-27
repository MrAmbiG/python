
'''
.SYNOPSIS
    powershell's $scriptroot equivalent
.DESCRIPTION
    powershell's $scriptroot equivalent
.NOTES
    File Name      : scriptpath.py
    Author         : gajendra d ambi
    Date           : September 2016
    Prerequisite   : python 2.7.x, 
    Copyright      - None
.LINK
    Script posted over: https://github.com/MrAmbiG/python
'''
def get_script_dir(follow_symlinks=True):
    import sys, os, inspect
    if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)
    scriptpath = get_script_dir()
