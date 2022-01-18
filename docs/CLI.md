# CLI

To interact with the sledo CLI, open a new terminal and type following commands into it:

```bash
$ sledo --help
```

`--help` Shows options for interaction with sledo CLI

```bash
$ sledo generate [FILE]
```

The `generate` command creates CSV files out of given configuration YAML file.

```bash
$ sledo generate [FILE] -O [DIRECTORY]
$ sledo generate [FILE] --outdir [DIRECTORY]
```

With the `-O` / `--outdir` option, the out directory for the generated CSV files can be chosen.

## Example Command:

```bash
$ sledo generate config.yaml -O dist

```

This generates CSV files out of `config.yaml` into the folder `dist`
