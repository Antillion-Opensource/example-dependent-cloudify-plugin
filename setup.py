# coding=utf-8
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import setuptools

setuptools.setup(

    name='dummy-cloudify-plugin',
    version='0.1.1',
    author='Oliver Tupman',
    author_email='otupman@antillion.com',
    description='Dummy plugin as part of the plugin example repo',
    license='LICENCE',
    install_requires=[
        'cloudify-plugins-common>=3.4',
        'cloudify-dsl-parser>=3.4'
    ],
    packages=['ant_dummy']
)
