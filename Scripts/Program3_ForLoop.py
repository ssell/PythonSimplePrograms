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
# Program 3: For-loop, built-in enumerate function, new style formatting
# ------------------------------------------------------------------------

friends = ["John", "Pat", "Gary", "Michael"]

print("Printing contents of 'friends' in order:")

for i, name in enumerate(friends):
    print("\tfriends[{iter}] = {name}".format(iter=i, name=name))

# ------------------------------------------------------------------------
# Print names in reverse-order using different format style
# ------------------------------------------------------------------------

print("Printing contents of 'friends' in reverse-order:")

numFriends = len(friends)

for i in range((numFriends - 1), -1, -1): 
    print("\tfriends[{}] = {}".format(i, friends[i]))
    
# ------------------------------------------------------------------------
# Print names containing only the letter 'a' using different format style
# ------------------------------------------------------------------------

print("Printing contents of 'friends' that contains the letter 'a':")

for i, name in enumerate(friends):
    if 'a' in name:
        print("\tfriends[{1}] = {0}".format(friends[i], i))