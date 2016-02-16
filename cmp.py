""" Commit hook for pylint """
import decimal
import os
import re
import sys
import subprocess
import collections
import ConfigParser
import py_compile, compileall


ExecutionResult = collections.namedtuple(
    'ExecutionResult',
    'status, stdout, stderr'
)


def _execute(cmd):
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    status = process.poll()
    return ExecutionResult(status, stdout, stderr)


def _current_commit():
    if _execute('git rev-parse --verify HEAD'.split()).status:
        return '4b825dc642cb6eb9a060e54bf8d69288fbee4904'
    else:
        return 'HEAD'


def _get_list_of_committed_files():
    """ Returns a list of files about to be commited. """
    files = []
    # pylint: disable=E1103
    diff_index_cmd = 'git diff-index --cached %s' % _current_commit()
    output = subprocess.check_output(
        diff_index_cmd.split()
    )
    for result in output.split('\n'):
        if result != '':
            result = result.split()
            if result[4] in ['A', 'M']:
                files.append(result[5])

    return files


def _is_python_file(filename):
    """Check if the input file looks like a Python script

    Returns True if the filename ends in ".py" or if the first line
    contains "python" and "#!", returns False otherwise.

    """
    if filename.endswith('.py'):
        return True
    else:
        with open(filename, 'r') as file_handle:
            first_line = file_handle.readline()
        return 'python' in first_line and '#!' in first_line


def check_repo():
    """ Main function doing the checks
    """
    # List of checked files and their results
    python_files = []

    dfile = 'source_cp'
    # Set the exit code
    all_filed_passed = True

    # Find Python files
    import pdb;pdb.set_trace()
    for filename in _get_list_of_committed_files():
        try:
            if _is_python_file(filename):
                python_files.append((filename))
        except IOError:
            print 'File not found (probably deleted): {}\t\tSKIPPED'.format(
                filename)

    # Don't do anything if there are no Python files
    if len(python_files) == 0:
        sys.exit(0)
    if compile_files(python_files, force=1):
        all_filed_passed = True

    return all_filed_passed


def compile_files(files, ddir=None, force=0, rx=None, quiet=0, ignore=0):
    """Byte-compile all file.
    file:      the file to byte-compile
    ddir:      if given, purported directory name (this is the
               directory name that will show up in error messages)
    force:     if 1, force compilation, even if timestamps are up-to-date
    quiet:     if 1, be quiet during compilation

    """

    success = 1
    dfile = None
    for fullname in files:
        if rx is not None:
            mo = rx.search(fullname)
            if mo:
                continue
        if os.path.isdir(fullname):
            continue
        elif not os.path.isfile(fullname):
            print "file does not exist:", fullname
            success = 0
        elif fullname[-3:] == '.py':
            cfile = fullname + (__debug__ and 'c' or 'o')
            ftime = os.stat(fullname).st_mtime
            try: ctime = os.stat(cfile).st_mtime
            except os.error: ctime = 0
            if (ctime > ftime) and not force: continue
            if not quiet:
                print 'Compiling', fullname, '...'
            try:
                ok = py_compile.compile(fullname, None, dfile, True)
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except py_compile.PyCompileError,err:
                if quiet:
                    print 'Compiling', fullname, '...'
                print err.msg
                success = 0
            except (MemoryError, SyntaxError),err:
                if quiet:
                    print 'Compiling', fullname, '...'
                print err.msg
                success = 0
            except IOError, e:
                print "Sorry", e
                success = 0
            else:
                if ok == 0:
                    success = 0
    if not success and ignore:
        print "Errors were ignored."
    return success or ignore


if __name__=='__main__':
    check_repo()