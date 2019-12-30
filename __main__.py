# QR Code Generator
# Copyright (C) 2019 Vũ Đắc Hoàng Ân
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import argparse
import datetime
from pathlib import Path


def convert_date(date, input_format, output_format, i=0):
    try:
        output = datetime.datetime.strptime(date, input_format).strftime(output_format)
        if i:
            return output
        else:
            print(output)
    except (ValueError, TypeError):
        if i:
            print(f'There is an error on line {i}: {date}')
            return date
        else:
            print(f'There is an error while converting {date}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser('date-format-conveter', description='Date Format Converter')
    parser.add_argument('data', help='Input data (string or file)')
    parser.add_argument('-i', '--input-format', help='input format (default %%d/%%m/%%Y)', default='%d/%m/%Y')
    parser.add_argument('-o', '--output-format', help='output format (default %%m/%%d/%%Y)', default='%m/%d/%Y')
    parser.add_argument('-f', '--output-file', help='output file (default output.txt)', default='output.txt')
    parser.add_argument('-v', '--version', action='version', version='1.0')

    args = parser.parse_args()
    data = args.data
    in_format = args.input_format
    out_format = args.output_format
    out_file = args.output_file

    if Path(data).is_file():
        with open(data) as file:
            with open(out_file, 'w') as f:
                for idx, day in enumerate(file, 1):
                    line = convert_date(day.rstrip(), in_format, out_format, idx)
                    f.write(f'{line}\n')
    else:
        convert_date(data, in_format, out_format)
