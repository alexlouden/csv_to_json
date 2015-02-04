import csv
import json
import sys
from collections import OrderedDict


def json_to_csv(input_f, output_f):
    """ Convert JSON to CSV """

    input_data = json.load(input_f, object_pairs_hook=OrderedDict)

    if isinstance(input_data, list):
        list_of_dicts = input_data
        fieldnames = list_of_dicts[0].keys()

    elif isinstance(input_data, dict):
        dict_of_lists = input_data
        fieldnames = dict_of_lists.keys()

        # Dict of lists to list of dicts
        # Assume all lists are same length
        list_len = len(dict_of_lists.values()[0])
        list_of_dicts = [
            {k: v[i] for k, v in dict_of_lists.items()}
            for i in range(list_len)
        ]

    w = csv.DictWriter(output_f, fieldnames, lineterminator='\n')
    w.writeheader()
    w.writerows(list_of_dicts)


def test_json_to_csv():
    """ Test using nosetests """

    try:
        from nose.tools import assert_equals
    except ImportError:
        raise ImportError('Need nose to run tests')

    from cStringIO import StringIO

    f_input = StringIO("""\
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
}""")
    f_output = StringIO()

    # Convert
    json_to_csv(f_input, f_output)

    f_output.seek(0)
    print f_output.read()

    expected = """\
ints,floats,strings
1,1.5,test
5,5.2,thing
"""
    f_output.seek(0)
    assert_equals(f_output.read(), expected)


if __name__ == '__main__':
    json_to_csv(sys.stdin, sys.stdout)
