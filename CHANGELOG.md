# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [In development] - Unreleased


## [1.6.0] - 2023-04-20

### Changed

- Templates to match `fittings>=2.0.0`


## [1.5.0] - 2022-07-31

### Fixed

- HTML and JS syntax
- Templates for `mumbletemps`

### Added

- evetime-js to `mumbletemps` public-facing template

### Changed

- Static files to their AA3 versions
- Minimum requirements
  - Alliance Auth v2.15.0


## [1.4.0] - 2022-03-03

### Added

- Test suite for AA 3.x and Django 4

### Changed

- Switched to `setup.cfg` as config file, since `setup.py` is deprecated now

### Removed

- Deprecated settings


## [1.3.0] - 2022-01-12

### Added

- Tests for Python 3.11

### Changed

- JavaScript: `const` instead of `let` where appropriate
- Minimum requirements
  - Alliance Auth v2.9.4


## [1.2.0] - 2021-11-30

### Changed

- Minimum requirements
  - Python 3.7
  - Alliance Auth v2.9.3


## [1.1.1] - 2021-10-19

### Changes

- Use SITE_NAME variable instead of a static site name


## [1.1.0] - 2021-10-17

### Added

- Basic test suite

### Changed

- AA templates for AA 2.9.x

### Removed

- Unused files and code


## [1.0.5] - 2021-07-02

### Changed

- base template for new message layout


## [1.0.4] - 2021-06-29

### Added

- Favicons


## [1.0.3] - 2021-05-17

### Fixed

- Define function before use in javascript


## [1.0.2] - 2021-04-23

### Added

- Eve time to top menu bar


## [1.0.1] - 2021-04-22

### Fixed

- Alliance name for Pypi


## [1.0.0] - 2021-04-22

### Fixed

- GDPR issues with templates for "Fittings and Doctrines" and "Mumble Templinks" module
