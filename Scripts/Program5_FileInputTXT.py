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

# ------------------------------------------------------------------------
# Program 5: Opening and Reading TXT File
# ------------------------------------------------------------------------

import SimpleProgramUtilities as Utils

# ------------------------------------------------------------------------
# Prints the contents of the TXT file at the specified path
# \return None.
# ------------------------------------------------------------------------

def printFile(path):
    result = True

    try:
        file = open(path, 'r')
        lineNumber = 1

        for line in file:
            # Note that we change the line ending from '\n' to '' as
            # the incoming TXT line already has a newline at the end.
            print("{}:\t{}".format(lineNumber, line), end="")
            lineNumber += 1

    except OSError:
        print("{} failed to read Data file '{}'".format(Utils.errorMessage(), path))
        result = False

    return result 

# ------------------------------------------------------------------------

fileName = "Program5_Data.txt"
filePath = Utils.getDataFile(fileName)

if len(filePath) > 0:
    if printFile(filePath):
        print("\n\nSuccessfully read TXT file '{}'".format(filePath))
    else:
        print("\n\nFailed to read TXT file '{}'".format(filePath))