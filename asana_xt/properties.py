# Copyright 2024 Virgilio "Jan" So
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
class ReleaseProperties:
    @staticmethod
    def load_properties(file_path):
        properties = {}
        with open(file_path) as prop_file:
            for line in prop_file:
                key, value = line.strip().split("=", 1)
                properties[key] = value
        return properties
