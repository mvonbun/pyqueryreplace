#!/usr/bin/env python3

import re
import fileinput
import sys
from shutil import copyfile

import pygetch.getch as getch
import pyprintfancy.printFancy as pr

getch = getch.Getch()
pr_old = pr.fancyPrint(fg='orange')
pr_new = pr.fancyPrint(fg='blue')


class Qrr:
    """Query-search-and-replace.

    qrr(re, replace-string | formatter-func-handle)
    the constructor takes two arguments, where the first are is a re-object and
    the second is either a replacement string or a formatter function handle
    which takes a string and outputs another string.
    """

    def __init__(self, re, formatter, getch=getch):
        self.re = re
        self.getch_ack = 'y'
        self.getch_stop = 'q'
        # self.pr_old = pr.fancyPrint(fg='orange')
        # self.pr_new = pr.fancyPrint(fg='blue')

        if isinstance(formatter, str):
            self.use_re_to_sub = True
            self.formatter = lambda x: re.subn(formatter, x)
        else:
            self.use_re_to_sub = False
            self.formatter = formatter

    def qrr_string(self, s, noline=False):
        """Format input string."""
        # match = self.re.match(s)
        # query user only on a match
        query_user = False

        # use re.sub or re.match to detect match
        if self.use_re_to_sub is True:
            [s_new, nof_matches] = self.formatter(s)
            if nof_matches > 0:
                query_user = True
        else:
            if self.re.match(s) is not None:
                s_new = self.formatter(s)
                query_user = True

        # query user and process [y] answer
        if query_user is True:
            if noline is False:
                pr_old.pr(s)
                pr_new.pr(s_new)
            else:
                print('{}'.format(pr_old._str(s)), end='')
                print('{}'.format(pr_new._str(s_new)), end='')
            if getch() is self.getch_ack:
                return s_new
            else:
                return s
        else:
            return s

    def qrr_file(self, filename, output=None, dry=False, bak='.bak'):
        """Read a file line by line and query the user to perform a regexp replace upon
        a match.

        """
        # user info about how to use qrr
        print('query-replace {}'.format(filename))
        print('  type [y] to replace {} by {}'.format(
            pr_old._str('OLD'), pr_new._str('NEW')))

        # query user on lines
        string_buffer = ''
        with open(filename, 'r') as file:
            for line in file:
                string_buffer += self.qrr_string(line, noline=True)

        # replace
        if dry is False:
            if output is None:
                # if not output file is provided, backup the file first
                copyfile(filename, filename + bak)
                output = filename
            with open(output, 'w') as file:
                file.write(string_buffer)


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('regexp', nargs='?', default=None,
                   type=str, help='regexp to search for')
    p.add_argument('sub', nargs='?', default=None, help='regexp substitute')
    p.add_argument('input', nargs='?', default=None,
                   help='input filename to query-search-replace')
    p.add_argument('--output', nargs=1, default=None,
                   help='output filename to store result')
    p.add_argument('--demo', action='store_true',
                   help='show command line demo and exit')
    p.add_argument('--dry', action='store_true',
                   help='dry run (not actually replacing)')
    p.add_argument('--bak', nargs=1, type=str, default='bak',
                   help='backup file extension')
    args = p.parse_args()

    if args.demo is True:
        print("Qrr using re")
        qrr_re = Qrr(re.compile(r'\\'), '|')
        qrr_re.qrr_string('hey\ho\haha')

        print("")
        print("Qrr using formatter")
        rep = re.compile(r'\\')
        qrr_str = Qrr(re.compile(r".+\\.+"),
                      lambda x: "'" + rep.sub(", ", x) + "'")
        qrr_str.qrr_string('hey\ho\haha')

        print("")
        print("Qrr on files (dry run)")
        qrr_re.qrr_file('tb_file.m', dry=True)

        print("")
        print("Qrr on files (serious)")
        qrr_re.qrr_file('tb_doit.m', dry=False)

    else:
        if (args.input is None) or (args.regexp is None) or (args.sub is None):
            p.print_help()
        else:
            qrr_re = Qrr(re.compile(args.regexp), args.sub)
            qrr_re.qrr_file(args.input, output=args.output,
                            dry=args.dry, bak=args.bak)
