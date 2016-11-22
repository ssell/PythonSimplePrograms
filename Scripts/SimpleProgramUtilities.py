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

import os

# ------------------------------------------------------------------------
# 
# ------------------------------------------------------------------------

def errorMessage():
    return "! Error !"

# ------------------------------------------------------------------------
# Used for declaring static function variables.
# Credit: http://stackoverflow.com/a/279586
# ------------------------------------------------------------------------

def staticVars(**args):
    def decorate(func):
        for arg in args:
            setattr(func, arg, args[arg])
        return func
    return decorate

# ------------------------------------------------------------------------
# A simple function to convert a string to an int. If the conversion fails,
# then the specified fallback value is returned.
#
# \param str The string to attempt to convert.
# \param fallback The fallback value to return if conversion fails.
#
# \return The converted string value.
# ------------------------------------------------------------------------

def toInt(str, fallback):
    try:
        return int(str)
    except ValueError:
        return fallback

# ------------------------------------------------------------------------
#
# ------------------------------------------------------------------------

def getDataPath():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), (".." + os.sep + "Data"))

# ------------------------------------------------------------------------
#
# ------------------------------------------------------------------------

@staticVars(dataPath=getDataPath())
def getDataFile(filename):
    file = (getDataFile.dataPath + os.sep + filename)

    if not os.path.isfile(file):
        print("{} Failed to find Data file '{}'".format(errorMessage(), file))
        file = ""

    return file
