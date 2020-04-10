count identifiers / words

```
$ echo camelCaseVariable | ./main.py
identifier ranking
camelCaseVariable	1

word ranking
camel	1
case	1
variable	1
```

output sample: https://gist.github.com/nishio/409c59f850542905f599d2dd830ad394


## in single folder
```
$ cat project_dir/src/* | ./main.py

```

## with subfolders
```
$ find project_dir/regroup/src/* | xargs cat | ./main.py
```
