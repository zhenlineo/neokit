#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright (c) 2002-2016 "Neo Technology,"
# Network Engine for Objects in Lund AB [http://neotechnology.com]
#
# This file is part of Neo4j.
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

"""
Usage:   neoctl.py <cmd=arg>
         --start=path/to/neo4j/home: start neo4j
         --stop=path/to/neo4j/home : stop neo4j
         -h                        : show this help message

Example: neoctl.py --start=./neo4j-enterprise-3.0.0-M01
         neoctl.py -h
"""

from __future__ import print_function
from sys import argv, exit
from os import name
from getopt import getopt
from subprocess import call, Popen, PIPE

is_windows = (name == 'nt')
neo4j_home = '.'


def main():
    global neo4j_home
    if len(argv) <= 1:
        print_help()
        exit()
    try:
        opts, args = getopt(argv[1:], "h", ["start=", "stop="])
    except getopt.GetoptError as err:
        print(str(err))
        print_help()
        exit_code = 2
    else:
        exit_code = 0
        for opt, arg in opts:
            if opt == '-h':
                print_help()
            elif opt == "--start":
                neo4j_home = arg
                exit_code = neo4j_start() or 0
            elif opt == "--stop":
                neo4j_home = arg
                exit_code = neo4j_stop() or 0
            else:
                print("Bad option %s" % opt)
                exit_code = 1
            if exit_code != 0:
                break
    exit(exit_code)


def neo4j_start():
    if is_windows:
        return powershell([ neo4j_home + '/bin/neo4j.bat install-service;', neo4j_home + '/bin/neo4j.bat start'])
    else:
        call([neo4j_home + "/bin/neo4j", "start"])


def neo4j_stop():
    if is_windows:
        return powershell([neo4j_home + '/bin/neo4j.bat stop;', neo4j_home + '/bin/neo4j.bat uninstall-service'])
    else:
        call([neo4j_home+"/bin/neo4j", "stop"])


def powershell(cmd):

    cmd = ['powershell.exe'] + cmd
    p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    return_code = p.wait()
    print(out)
    print(err)
    return return_code


def print_help():
    print(__doc__)

if __name__ == "__main__":
    main()