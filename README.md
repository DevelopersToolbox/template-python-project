<p align="center">
    <a href="https://github.com/OffSecToolbox/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/offsectoolbox/black-and-white-circle-256.png" alt="OffSecToolbox logo" />
    </a>
    <br />
    <a href="https://github.com/OffSecToolbox/baseline-project/actions/workflows/cicd-pipeline-local.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/offsectoolbox/baseline-project/cicd-pipeline-local.yml?branch=master&label=local%20pipeline&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/OffSecToolbox/baseline-project/actions/workflows/cicd-pipeline-shared.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/offsectoolbox/baseline-project/cicd-pipeline-shared.yml?branch=master&label=shared%20pipeline&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://codecov.io/gh/OffSecToolbox/baseline-project">
        <img src="https://img.shields.io/codecov/c/gh/OffSecToolbox/baseline-project?label=code%20coverage&style=for-the-badge" alt="code coverage" />
    </a>
    <br />
    <a href="https://github.com/OffSecToolbox/baseline-project/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/OffSecToolbox/baseline-project/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/OffSecToolbox/baseline-project/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/OffSecToolbox/baseline-project/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

This is the baseline template that we use internally when creating new python tools for the Offensive Security Toolbox. It has all of the basic functionality
that we need.

Base functionality:

1. Command line processing with examples parameters
2. Wrappers for information, warning, error, success and system messages (and associated colours)
3. A global configuration namespace with example configuration
4. Custom exceptions with examples
5. Clear documentation for each function
6. Minimal dependency on external modules

We decided to make this available along with our other tools to allow people to use a well engineered starting point when creating their own tools.

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
