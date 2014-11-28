csv_to_json
===========

Converts CSV files to JSON files

```bash
python csv_to_json.py < input.csv > output.json
```

### Example

```csv
name,age
Alex,25
Steve,45
```

Converts to

```json
{
	"name": ["Alex", "Steve"],
	"age": [25, 45]
}
```

### Tests

```bash
$ nosetests csv_to_json.py 
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```