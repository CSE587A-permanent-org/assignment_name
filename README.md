# Assignment Template Instructions

## Local software requirements

You'll need [poetry](https://python-poetry.org/) on your local computer.

## Using the template

To use this repository as a template, do the following:

1. Create a new repository through github. After clicking
'new repository', there will be a `template` option at the top
which provides a dropdown. Choose this repository as the template.

1. `git clone` the new repository to your local.
    - Change the name of the `assignment_name` directory to the assignment name.
    This does not need to be the same -- for instance, if you named the repo `dice_posterior_solution`,
    you would name the `assignment_name` subdirectory `dice_posterior`
    - Change the name of the hidden
    `.vscode/assignment_name.code-workspace` to
    `.vscode/<new_name>.code-workspace`
    - Using your favorite text editor, search for all instances of `assignment_name` and replace
      with your actual assignment name. I use the vscode find all/replace all function for this.

1. Run `poetry install`
    - At this point, you can either set the python interpreter in your current
    vscode session, or you can close your current window and re-open. The
    python interpreter is set to the virtual environment by default, as long as
    the `.venv` directory exists, which it does now.

1. Run the tests. There is a simple function in `assignment.py` and
`test_assignment.py`. If there are any problems with the package structure,
names, etc, then it is easiest to deal with it now.
    - Continuous integration is set up to build the package with python 3.9,
    3.10 and 3.11 on pushes to the `main` branch. The .devcontainer directory
    is set up to provide an environment which uses the poetry virtual
    environment and the autograder is configured for use with gradescope. If
    you plan to use any of these features, test them now, also.

1. Once you're convined that the package is set up correctly, start writing.

## Assumptions regarding package structure and filenames

Currently, the assumption is that there will be a directory with the
name of the assignment, eg `assignment_name`, with at least the following
two files: `assignment.py` and `test_assignment.py`. Not all source code
must be in `assignment.py`, for instance you can put source code in other
files. However, it is important, if you are using the autograder without
modification, to write all of your tests in `test_assignment.py`. The
autograder Docker image is written such `test_assignment.py` is placed in the
image at build-time. The students are expected to upload their copy of this
repository. The `test_assignment.py` in the container will be used for the
tests, however, not the student's. This ensures that the students cannot
manipulate the tests. It also means that the students should *not* modify
the tests as they complete the assignment as their modified test file
will not be used (so, no imports, etc).
