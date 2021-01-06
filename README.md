# Robotframework-FlaUI Library

## Introduction

Robotframework-FlaUI is a keyword based user interface automation testing library for Windows applications like Win32, WinForms, WPF or Store Apps.
It's based on the [FlaUI](https://github.com/FlaUI/FlaUI) user interface automation library.

## Documentation

*  [Keyword documentation](https://gdatasoftwareag.github.io/robotframework-flaui)

## Local usage

### Linux

```
  sudo apt install ruby-bundler ruby-full
```

### Windows

Install Ruby+Devkit from [RubyInstaller for Windows](https://rubyinstaller.org/downloads/)

### Execution

Install ruby+dev environment and execute in docs

```
bundle install
bundle exec jekyll server
```

Open browser and surf to [http://127.0.0.1:4000](http://127.0.0.1:4000)

## Docker usage

Build docker image and run it

```
docker-compose up -d --build
docker-compose up
```

Open browser and surf to [http://127.0.0.1:4000](http://127.0.0.1:4000)

### Information about docker usage

File not changing inside docker container after updating from 2.1.0.5 to 2.2.0.0
  --> https://github.com/docker/for-win/issues/5530

Modification from any files in mounted volume will not be tracked and not updated.
