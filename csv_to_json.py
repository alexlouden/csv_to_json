import csv
import json
import sys
from collections import OrderedDict


def csv_to_json(input_f, output_f):
    """ Convert CSV to JSON """

    dr = csv.DictReader(input_f)
    rows = list(dr)
    keys = dr.fieldnames

    data = OrderedDict()
    for k in keys:

        # TODO empty strings?

        # Determine row type
        try:
            # try float
            parsed_row = [float(r[k]) for r in rows]
            # but check if ints are more appropriate

            if all(int(r) == r for r in parsed_row):
                raise ValueError('Use ints instead')
        except ValueError:
            try:
                # try int
                parsed_row = [int(r[k]) for r in rows]
            except ValueError:
                # strings it is
                parsed_row = [r[k] for r in rows]

        data[k] = parsed_row

    json.dump(data, output_f, indent=2)


def test_csv_to_json():
    """ Test using nosetests """

    try:
        from nose.tools import assert_equals
    except ImportError:
        raise ImportError('Need nose to run tests')

    from cStringIO import StringIO

    f_input = StringIO("""\
ints,floats,strings
1,1.5,test
5,5.2,thing""")
    f_output = StringIO()

    # Convert
    csv_to_json(f_input, f_output)

    f_output.seek(0)
    print f_output.read()

    expected = """\
{
  "ints": [
    1, 
    5
  ], 
  "floats": [
    1.5, 
    5.2
  ], 
  "strings": [
    "test", 
    "thing"
  ]
}"""
    f_output.seek(0)
    assert_equals(f_output.read(), expected)


if __name__ == '__main__':
    csv_to_json(sys.stdin, sys.stdout)
