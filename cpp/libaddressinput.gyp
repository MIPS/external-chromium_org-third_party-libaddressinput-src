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
    'libaddressinput_gtest_dir':      '/usr/include',
    'libaddressinput_gtest_src_dir':  '/usr/src/gtest/src',
  },
  'target_defaults': {
    'cflags': [
      '-fpic',
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
        '<(DEPTH)',
        '<(libaddressinput_gtest_dir)',
        '<(INTERMEDIATE_DIR)',
        '<(SHARED_INTERMEDIATE_DIR)',
      ],
      'copies': [
        {
          'destination': '<(INTERMEDIATE_DIR)/src',
          'files': [
            '<(libaddressinput_gtest_src_dir)/gtest-all.cc',
            '<(libaddressinput_gtest_src_dir)/gtest.cc',
            '<(libaddressinput_gtest_src_dir)/gtest-death-test.cc',
            '<(libaddressinput_gtest_src_dir)/gtest-filepath.cc',
            '<(libaddressinput_gtest_src_dir)/gtest-internal-inl.h',
            '<(libaddressinput_gtest_src_dir)/gtest_main.cc',
            '<(libaddressinput_gtest_src_dir)/gtest-port.cc',
            '<(libaddressinput_gtest_src_dir)/gtest-printers.cc',
            '<(libaddressinput_gtest_src_dir)/gtest-test-part.cc',
            '<(libaddressinput_gtest_src_dir)/gtest-typed-test.cc',
          ],
        },
      ],
      'conditions': [
        ['OS == "linux"', {
          'ldflags': [
            '-pthread',
          ],
        }],
      ],
    },
  ],
}
