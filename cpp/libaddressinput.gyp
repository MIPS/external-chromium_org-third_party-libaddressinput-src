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

    # Default include directories. Override with your system's include paths or
    # paths to your own implementations.
    'gtest_dir':     '/usr/include',
    'gtest_src_dir': '/usr/src/gtest',
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
        '<(INTERMEDIATE_DIR)/src/gtest-all.cc',
        '<(INTERMEDIATE_DIR)/src/gtest_main.cc',
      ],
      'dependencies': [
        'libaddressinput',
      ],
      'include_dirs': [
        '<(gtest_src_dir)',
      ],
      'copies': [
        {
          'destination': '<(INTERMEDIATE_DIR)/src',
          'files': [
            '<(gtest_src_dir)/src/gtest-all.cc',
            '<(gtest_src_dir)/src/gtest_main.cc',
          ],
        },
      ],
      'conditions': [
        ['OS == "linux"', {
          'ldflags': [
            # GTest needs to link to pthread.
            '-pthread',
          ],
        }],
      ],
    },
  ],
}
