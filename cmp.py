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
    for fl in python_files:
        py_compile.compile(fl, './t1.txt')
    return all_filed_passed

if __name__=='__main__':
    check_repo()