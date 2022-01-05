<div align="center">
  <h1><code>Sledo</code></h1>
  <p>
    <a href="https://github.com/luxbe/sledo" target="_blank">
      <img alt="Stars" src="https://img.shields.io/github/stars/luxbe/sledo">
    </a>
    <a href="https://pypi.org/project/sledo" target="_blank">
      <img alt="PyPI badge" src="https://img.shields.io/pypi/v/sledo">
    </a>
  </p>

<strong>A tool to generate demo data</strong>

<sub>Built with Python</sub>

</div>

## About

Sledo is a tool to automatically generate connected demo data.

## Installation

### pip

```bash
$ pip install sledo
```

### Github

```bash
$ pip install git+https://github.com/luxbe/sledo.git
```

## Quickstart

1. Create a [yaml](https://yaml.org/) file called `config.yaml`. Fill it with schemas and steps.

2. Run the sledo generate command

```
$ sledo generate config.yaml
```

3. Find the generated CSV files in the `out` folder

## Develop

### Install dependencies

```bash
$ git clone https://github.com/luxbe/sledo.git
$ cd sledo
$ pipenv install
```

### Run sledo

```bash
$ pipenv run python sledo/__init__.py generate
```

### Run tests

```bash
$ pytest -v --cov=sledo --cov-report html
```

## License

MIT licensed. See the bundled [LICENSE](https://github.com/luxbe/sledo/blob/master/LICENSE) file for more details.
