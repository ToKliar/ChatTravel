import math
import argparse
from travel_promt import get_travel_tips

parser = argparse.ArgumentParser(description="travel assistant")
# 为功能 6 添加子命令行 
sub_parsers = parser.add_subparsers(help='sub command help')
parser_travel_tips = sub_parsers.add_parser('tips', help='give travel tips according to travel information')
parser_travel_tips.add_argument('-d', '--date', type=str, required=True, nargs='+', help='travel start date',metavar='June 3rd')
parser_travel_tips.add_argument('-l', '--location', type=str, required=True, nargs='+', help='travel location',metavar='New York')
parser_travel_tips.add_argument('-s', '--duration', type=int, default=3,required=True, help='travel duration (day)', metavar='3')
parser_travel_tips.add_argument('-b', '--budget', type=int, default=2000, required=True, help='travel budget', metavar='2000')
parser_travel_tips.set_defaults(func=get_travel_tips)


args = parser.parse_args()
args.func(args)