from adif_file import adi
import argparse
from pprint import pformat
from heapq import merge


def arg_parser():
    parser = argparse.ArgumentParser(
        description="Merge two ADIF files into one. Message order is preserved.")
    parser.add_argument("file1", help="First .adi file to merge.", type=str)
    parser.add_argument("file2", help="Second .adi file to merge.", type=str)
    parser.add_argument("out", help="Merged file output. Defaults to merged.adi",
                        type=str, default="merged.adi", nargs="?")
    args = parser.parse_args()
    print(args.file1)
    print(args.file2)
    print(args.out)
    return args


args = arg_parser()
adif_1 = adi.load(args.file1)
adif_2 = adi.load(args.file2)

# print(type(adif_1))
# print(pformat(adif_1.keys()))
# print(pformat(adif_1.get('HEADER')))
# print(type(adif_1.get('RECORDS')))
# print(pformat(adif_2.get('HEADER')))
# print(pformat(adif_1.get('RECORDS')[-4:]))
# print(pformat(adif_2.get('RECORDS')[-4:]))

merged = merge(adif_1.get('RECORDS'), adif_2.get('RECORDS'), key=lambda x: (x['QSO_DATE_OFF'], x['TIME_OFF']))
# print(pformat(list(merged)[-10:]))
adif_1['RECORDS'] = list(merged)
# print(pformat(adif_1.get('RECORDS')[-20:]))
adi.dump(args.out, adif_1, linebreaks=False)
