# -*- coding: utf-8 -*-
import argparse


def merge(rdbs, out_file):
    if len(rdbs) <= 1:
        print 'at least 2 rdb files. no need to merge.'
        return

    prefix = None
    suffix = None
    data = []

    for rdb in rdbs:
        with open(rdb, 'rb') as f:
            s = f.read()
            if not prefix:
                prefix = s[:11]
            if not suffix:
                suffix = s[-9:]
            data.append(s[11:-9])

    with open(out_file, 'wb') as f:
        f.write(b'{}{}{}'.format(prefix, b''.join(data), suffix))

parser = argparse.ArgumentParser(description='merge redis rdb files')
parser.add_argument('--out', dest='out_file', help='set output file name')
parser.add_argument('rdbs', type=str, nargs='+', help='redis rdb files')

args = parser.parse_args()

merge(args.rdbs, args.out_file)
