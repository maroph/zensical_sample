# Plugin: Markdown Exec
* [PyPi](https://pypi.org/project/markdown-exec/)
* [GitHub](https://github.com/pawamoy/markdown-exec/)
* [Documentation](https://pawamoy.github.io/markdown-exec/)
* [Zensical Documentation](https://zensical.org/docs/setup/extensions/markdown-exec/)

Supported with Zensical >= 0.0.47

## Plugin Installation
```
pip install "markdown-exec[ansi]"
```


## zensical.toml
```
[project.plugins.markdown-exec]
```

## Markdown Exec Sample Call
<!--
 https://zensical.org/docs/setup/extensions/markdown-exec/
 python exec="on" source="above" : show also the source code
 https://zensical.org/docs/authoring/data-tables/#column-alignment
 :---     align left
 :---:    align center
 ---:     align right
 -->
```python exec="on"
print("Markdown Exec: simple table  ")
print("  ")
print("| First Header  | Second Header |")
print("| ------------- | ------------- |")
print("| Content Cell  | Content Cell |")
print("| Content Cell  | Content Cell |")
print("  ")
```

<!--
 https://zensical.org/docs/authoring/data-tables/#usage
 https://zensical.org/docs/authoring/icons-emojis/
 -->
```python exec="on"
print("Markdown Exec: simple table with icons  ")
print("  ")
print("| Method      | Description                          |")
print("| ----------- | ------------------------------------ |")
print("| `GET`       | :lucide-check:       Fetch resource  |")
print("| `PUT`       | :lucide-check-check: Update resource |")
print("| `DELETE`    | :lucide-x:           Delete resource |")
print("  ")
```

