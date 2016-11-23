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
# Program 6: Writing out to TXT file
# ------------------------------------------------------------------------

import SimpleProgramUtilities as Utils

def getNextLine():
    line = input("> ")
    return line

def shouldQuit(str):
    result = False
     
    if str == "end":
        result = True
    
    return result

def main():
    filename = "Program6_Data.txt"
    filePath = Utils.getDataFile(filename, False)
    file = open(filePath, 'w')

    print("Enter text to be written. When done writing, enter 'end'\n")

    nextLine = getNextLine()

    while not shouldQuit(nextLine):
        file.write(nextLine + "\n")
        nextLine = getNextLine()

    print("\nFinished writing to TXT file '{}'".format(filePath))