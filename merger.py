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
            redis_code = int(s[5:9])
            prefix_length = 11
            if redis_code > 6:
                prefix_length = 80
            if not prefix or redis_code > 6:
                prefix = s[:prefix_length]

            if not suffix:
                suffix = s[-9:]
            data.append(s[prefix_length:-9])

    with open(out_file, 'wb') as f:
        f.write(b'{}{}{}'.format(prefix, b''.join(data), suffix))

parser = argparse.ArgumentParser(description='merge redis rdb files')
parser.add_argument('--out', dest='out_file', help='set output file name')
parser.add_argument('rdbs', type=str, nargs='+', help='redis rdb files')

args = parser.parse_args()

merge(args.rdbs, args.out_file)
