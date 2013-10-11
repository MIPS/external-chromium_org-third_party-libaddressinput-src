# Copyright (C) 2013 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
{
  'variables': {
    'component%': 'shared_library',
  },
  'target_defaults': {
    'cflags': [
      '-std=c++03',
    ],
    'configurations': {
      'Debug': {
        'cflags': [
          '-O0',
          '-g',
        ],
      },
      'Release': {
        'cflags': [
          '-O3',
        ],
      },
    },
  },
  'targets': [
    {
      'target_name': 'libaddressinput',
      'type': '<(component)',
      'cflags': [
        '-fvisibility=hidden',
      ],
    },
    {
      'target_name': 'libaddressinput_unittests',
      'type': 'executable',
      'sources': [
        'test/main.cc',
      ],
      'dependencies': [
        'libaddressinput',
        'gtest.gyp:main',
      ],
    },
  ],
}
