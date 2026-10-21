# macjustice-recipes
Autopkg recipes

## AzureCLI

> [!IMPORTANT]
> **This package does not include Python, and `az` will not run without it.** You must separately deploy Python 3.14 and set `AZ_PYTHON` to it on every Mac. See [Python dependency](#python-dependency) below.

Downloads the official Azure CLI macOS tarball from [GitHub releases](https://github.com/Azure/azure-cli/releases) and packages it to `/usr/local/azure-cli`, with `/usr/local/bin/az` symlinked to the launcher. Set the `ARCH` input to `arm64` (default) or `x86_64`.

| Recipe | Does |
|---|---|
| `AzureCLI.download` | Downloads the tarball and verifies Microsoft's code signature on a bundled library |
| `AzureCLI.pkg` | Builds `AzureCLI-<arch>-<version>.pkg` |
| `AzureCLI.munki` | Imports into Munki (`testing` catalog), with `supported_architectures` set from `ARCH` |
| `AzureCLI.jamf` | Creates the category and uploads the package to Jamf Pro (no policy or groups) |

Requires the [homebysix-recipes](https://github.com/autopkg/homebysix-recipes) repo (`autopkg repo-add homebysix-recipes`) for the `VersionSplitter` processor. The Jamf recipe also requires [grahampugh/jamf-upload](https://github.com/grahampugh/jamf-upload) (`autopkg repo-add grahampugh/jamf-upload`).

### Python dependency

Microsoft's macOS tarball contains only the Azure CLI Python packages, not a Python interpreter. These recipes package it as-is. On its own, the installed `az` fails immediately:

```
$ az --version
Error: AZ_PYTHON not set.
For offline/tarball installs, set AZ_PYTHON to a Python 3.14 path.
```

To make `az` work, you need both of the following on each Mac:

1. **Python 3.14, exactly.** The tarball's compiled modules are built for one Python version (see `/usr/local/azure-cli/libexec/lib/python3.*`). A different version may appear to work, but anything that depends on a version-specific compiled module breaks. For example, Microsoft's macOS sign-in broker (`pymsalruntime`) fails to load. Possible sources include [python.org](https://www.python.org/downloads/macos/), [MacAdmins Python](https://github.com/macadmins/python) (if it provides 3.14) or Homebrew (`python@3.14`).
2. **`AZ_PYTHON` set to that interpreter** in each user's environment, for example in `/etc/zshrc` or a configuration profile:

   ```sh
   export AZ_PYTHON=/Library/Frameworks/Python.framework/Versions/3.14/bin/python3.14
   ```

Microsoft can move to a newer Python version in any release. When that happens, deploy the new Python version and update `AZ_PYTHON` before rolling out that Azure CLI release. In Munki, consider adding your Python item to `requires` in an override of the `AzureCLI.munki` recipe.

## Development

Checks run with [prek](https://github.com/j178/prek) (configured in `prek.toml`) on commit and in GitHub Actions. Run `prek install` once after cloning to enable the git hook, or `prek run --all-files` to check everything.
