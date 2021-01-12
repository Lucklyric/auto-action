import argparse

parser= argparse.ArgumentParser(description='dummy_app')
parser.add_argument('pos1', type=int)
parser.add_argument('pos2', type=int)
parser.add_argument('--arg1', type=int)
parser.add_argument('--arg2', type=str)

args = parser.parse_args()

if __name__ == '__main__':
    sum_result = args.pos1 + args.pos2
    print("{}.{}".format(sum_result**args.arg1, args.arg2))


