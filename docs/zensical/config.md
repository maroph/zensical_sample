---
icon: lucide/cog
---

# Config

## Debian Packages

```
sudo apt install python3-pip
sudo apt install python3-venv
```

## Python Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
python -m pip install --upgrade wheel
python -m pip install zensical
```

### Needed for direct deployment to branch gh-pages

```
python -m pip install ghp-import
```

## Create a new template project

```
$ zensical new zensical_sample
$ cd zensical_sample
$ ls -AR
.:
docs  .github  zensical.toml

./docs:
index.md  markdown.md

./.github:
workflows

./.github/workflows:
docs.yml
```

