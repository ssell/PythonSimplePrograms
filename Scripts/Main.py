# ------------------------------------------------------------------------
# Copyright 2016 Steven T Sell (ssell@vertexfragment.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------

import os
import re
import subprocess
import SimpleProgramUtilities as Utils

# ------------------------------------------------------------------------
# Finds and returns a list of all Python programs in the local directory.
# \return List of tuples of all programs. Tuple of {FullPath, FileName}
# ------------------------------------------------------------------------

def getPrograms():
    regex = re.compile("Program(\d)+_[a-zA-Z]+.py")
    path = os.path.dirname(os.path.realpath(__file__))
    simplePrograms = []

    for file in os.listdir(path):
        fullFilePath = os.path.join(path, file)
        if (os.path.isfile(fullFilePath) and (regex.match(file))):
            simplePrograms.append((fullFilePath, file))

    return simplePrograms

# ------------------------------------------------------------------------
# Queries the user for which program to run from a displayed list.
# \param programs List of all programs available to run.
# \return Index into the input list for the program to run.
# ------------------------------------------------------------------------

def getProgramToRun(programs):
    print("Choose which sample program to run:\n")

    for i, program in enumerate(programs):
        print("  {})\t{}".format((i + 1), program[1]))

    programIndex = Utils.toInt(input("\n> Run program: "), 0)

    if (programIndex == 0) or (programIndex > len(programs)):
        print("{} Invalid Selection\n".format(Utils.errorMessage()))
        return getProgramToRun(programs)

    return programIndex - 1

# ------------------------------------------------------------------------
# Runs the specified program.
# \param program Program tuple to run.
# \return None.
# ------------------------------------------------------------------------

def runProgram(program):
    with open(program[0]) as file:
        code = compile(file.read(), program[0], "exec")
        exec(code)

# ------------------------------------------------------------------------
# Loops continuously and runs selected sample programs.
# \return None.
# ------------------------------------------------------------------------

def main():

    # Regex to match our sample program file names of 'Program#_Name.py'
    programs = getPrograms()

    while True:
        programIndex = getProgramToRun(programs)
        program = programs[programIndex]

        print("\n! ---------------------------------------------------------------")
        print("! Start Running {}".format(program[1]))
        print("! ---------------------------------------------------------------\n")

        runProgram(program)

        print("\n! ---------------------------------------------------------------")
        print("! Finish Running {}".format(program[1]))
        print("! ---------------------------------------------------------------\n")

# ------------------------------------------------------------------------

main()