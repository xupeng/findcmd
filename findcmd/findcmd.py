#!/usr/bin/env python
#coding=utf8

"""
findcmd.py

Created by Xupeng Yun <xupeng@xupeng.me> on 2011-02-24.
Copyright (c) 2010 xupeng.me. All rights reserved.
"""


import re
import sys
import os
from optparse import OptionParser

from colors import red

def findcmd(cmd, paths=None, case_sensitive=False, exactly_match=False):
    """Find cmds which match given patterns in paths
    """

    if not paths:
        return []

    if case_sensitive:
        flags = 0
    else:
        flags = re.IGNORECASE

    if exactly_match:
        re_cmd = re.compile('^%s$' % cmd, flags)
    else:
        re_cmd = re.compile('%s' % cmd, flags)

    results = []
    for path in paths:
        if not os.path.isdir(path):
            continue

        matches = [os.path.join(path, b) for b in os.listdir(path) if \
                                                            re_cmd.search(b)]
        results.extend(matches)

    return sorted(results)

def main():
    """Entry point
    """

    parser = OptionParser(usage='%prog [options] cmd')
    parser.add_option('-c', '--case-sensitive', action='store_true')
    parser.add_option('-e', '--match-all', action='store_true')
    parser.add_option('--no-color', action='store_true')
    options, args = parser.parse_args()

    if len(args) == 0:
        parser.print_help()
        sys.exit(1)

    cmd = args[0]

    default_path = [
        '/bin',
        '/sbin',
        '/usr/bin',
        '/usr/sbin',
        '/usr/local/bin',
        '/usr/local/sbin',
        '/opt/local/bin',
        '/opt/local/sbin',
        os.path.expanduser('~/bin'),
    ]
    paths = default_path + os.environ['PATH'].split(':')
    paths = sorted(list(set([p.rstrip('/') for p in paths])))

    results = findcmd(cmd, paths, options.case_sensitive, options.match_all)
    if not results:
        return 1

    if options.no_color:
        print '\n'.join(results)
    else:
        def repl(match):
            """Colorize matched text"""
            return red(match.group(), True)
        re_key = re.compile('%s' % cmd, re.IGNORECASE)
        for result in results:
            print re_key.sub(repl, result)

    return 0

if __name__ == '__main__':
    sys.exit(main())

# vim: set ts=4 sw=4 et :
