# Asana XT

A Python package to interact with Asana's API and manage tasks efficiently.

## Features
- Create ASANA ticket
- Use JSON profile when creating an ASANA ticket

## Create Distribution
`python setup.py sdist bdist_wheel`

## Installation
```
pip install dist/asana_xt-0.1.0-py3-none-any.whl
```
or
```bash
pip install asana_xt
```

### Install Editable Mode for Development
If you're still developing the package, you can install it in editable mode to avoid rebuilding for every change:
```
pip install -e .
```

## Verify Installation
```bash
pip show asana_xt
```

## Usage Examples

1. Create a task using a profile from the configuration file. Loads `asana_xt.json` by default.

If using from source, from the asana_xt folder
```
python main.py --profile documentation
```

or

If installed
```
asana_xt --profile documentation
```

2. Use a custom configuration file:

```
python main.py --profile documentation --config custom_config.json
```

3. Sample `asana_xt.json` below.

- `profile_name` - The name of the profile. Loaded when using the flag `--profile`
- `project_name` - The name of the project, must be the same name in ASANA.
- `assignee_name` - The name of the assignee, must be the same name in ASANA.
- `subject` - The subject of the task. Subject of the ASANA task.
- `notes` -  The notes of the task. This is a path to a file containing the text notes.

```
{
  "profiles": [
    {
      "profile_name": "documentation",
      "project_name": "Documentation",
      "assignee_name": "Alex Wilson",
      "subject": "Update API Documentation",
      "notes": "docs/api_changes.html"
    }
  ]
}
```

4. Sample `api_changes.html` below.

```
This is a sample content body

@[Virgilio So] This is a sample mention. This is case sensitive
```

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
