# macjustice-recipes
Autopkg recipes

## AzureCLI

Downloads the official Azure CLI macOS tarball from [GitHub releases](https://github.com/Azure/azure-cli/releases) and packages it to `/usr/local/azure-cli`, with `/usr/local/bin/az` symlinked to the launcher. Set the `ARCH` input to `arm64` (default) or `x86_64`.

| Recipe | Does |
|---|---|
| `AzureCLI.download` | Downloads the tarball and verifies Microsoft's code signature on a bundled library |
| `AzureCLI.pkg` | Builds `AzureCLI-<arch>-<version>.pkg` |
| `AzureCLI.munki` | Imports into Munki (`testing` catalog), with `supported_architectures` set from `ARCH` |
| `AzureCLI.jamf` | Creates the category and uploads the package to Jamf Pro (no policy or groups) |

Requires the [homebysix-recipes](https://github.com/autopkg/homebysix-recipes) repo (`autopkg repo-add homebysix-recipes`) for the `VersionSplitter` processor. The Jamf recipe also requires [grahampugh/jamf-upload](https://github.com/grahampugh/jamf-upload) (`autopkg repo-add grahampugh/jamf-upload`).

**Python is not included.** The tarball contains only the Azure CLI Python packages. To run, `az` requires a Python 3.14 interpreter set in the `AZ_PYTHON` environment variable.

## Development

Checks run with [prek](https://github.com/j178/prek) (configured in `prek.toml`) on commit and in GitHub Actions. Run `prek install` once after cloning to enable the git hook, or `prek run --all-files` to check everything.
