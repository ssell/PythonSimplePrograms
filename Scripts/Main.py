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
    regex = re.compile("Program(\d)+_[a-zA-Z]+\.py")
    path = os.path.dirname(os.path.realpath(__file__))
    simplePrograms = []

    for file in os.listdir(path):
        fullFilePath = os.path.join(path, file)
        if (os.path.isfile(fullFilePath) and (regex.match(file))):
            simplePrograms.append((fullFilePath, file))

    return simplePrograms

# ------------------------------------------------------------------------
# Converts a list of program names/path to module names to import.
# \param programs
# \return List of module names
# ------------------------------------------------------------------------

def getModuleNames(programs):
    # Source: http://www.diveintopython.net/functional_programming/all_together.html
    programToModule = lambda program: os.path.splitext(program[1])[0]
    moduleNames = map(programToModule, programs)
    return moduleNames

# ------------------------------------------------------------------------
# Retrieves and imports a map of modules
# ------------------------------------------------------------------------

def getModules(programs):
    # Source: http://stackoverflow.com/a/301146
    moduleNames = getModuleNames(programs)
    modules = map(__import__, moduleNames)
    return modules

# ------------------------------------------------------------------------
# Runs the specified program.
# \param program Program tuple to run.
# \return None.
# ------------------------------------------------------------------------

# ! Note ! This function is no longer used. It is kept here for future
# reference and to also serve as a reminder of what does not work.
# Exec was not sufficient as it did not allow for the use of `input` 
# within the external scripts. 

# def runProgram(program):
#     with open(program[0]) as file:
#         code = compile(file.read(), program[0], "exec")
#         exec(code)

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
# Loops continuously and runs selected sample programs.
# \return None.
# ------------------------------------------------------------------------

def main():

    # Gather all of the sample programs all dynamically imported modules.
    # We then run the desired module via it's main function when selected.

    # This approach is used instead of directly running the external script
    # (for example through exec) since it allows for us to receive user 
    # input which the other approaches do not.

    programs = getPrograms()
    modules = list(getModules(programs))

    while True:
        programIndex = getProgramToRun(programs)
        program = programs[programIndex]

        print("\n! ---------------------------------------------------------------")
        print("! Start Running {}".format(program[1]))
        print("! ---------------------------------------------------------------\n")
        
        modules[programIndex].main()

        print("\n! ---------------------------------------------------------------")
        print("! Finish Running {}".format(program[1]))
        print("! ---------------------------------------------------------------\n")

# ------------------------------------------------------------------------

main()