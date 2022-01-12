# CLI

To interact with the sledo CLI, open a new terminal and type following commands into it:

```bash

$ sledo --help

```

<code>--help</code> Shows options for interaction with sledo CLI

```bash

$ sledo generate [FILE]

```

<code>generate [FILE] </code>Creates .csv files out of given configuration YAML (config.yaml) file. Enter name of file into [FILE], without braces.

```bash

$ sledo generate [FILE] -O [TEXT]
$ sledo generate [FILE] --outdir [TEXT]

```

<code>-O / --outdir </code>Generates .csv files out of given YAML file into folder [TEXT], which will be created during runtime. Enter name of folder into [TEXT], without braces.
<br>
<br>

## Example Command:
```bash
$ sledo generate config.yaml -O dist

````
This generates .csv files out of _config.yaml_ into the folder _dist_
