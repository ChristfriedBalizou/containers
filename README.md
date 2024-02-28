<!---
NOTE: AUTO-GENERATED FILE
to edit this file, instead edit its template at: ./github/scripts/templates/README.md.j2
-->
<div align="center">


## Containers

_A personal collection of container images_

</div>

<div align="center">

![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/ChristfriedBalizou/containers/release-scheduled.yaml?style=for-the-badge&label=Scheduled%20Release)

</div>

Welcome to my container images, if looking for a container start by [browsing the GitHub Packages page for this repo's packages](https://github.com/ChristfriedBalizou?tab=packages&repo_name=containers).

## Versionning

This project support [semantically versioned](https://semver.org/), [rootless](https://rootlesscontaine.rs/), and [multiple architecture](https://www.docker.com/blog/multi-arch-build-and-images-the-simple-way/) containers for various applications.


## Passing arguments to a application

Some applications do not support defining configuration via environment variables and instead only allow certain config to be set in the command line arguments for the app. To circumvent this, for applications that have an `entrypoint.sh` read below.

1. First read the Kubernetes docs on [defining command and arguments for a Container](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/).
2. Look up the documentation for the application and find a argument you would like to set.
3. Set the argument in the `args` section, be sure to include `entrypoint.sh` as the first arg and any application specific arguments thereafter.

    ```yaml
    args:
      - /entrypoint.sh
      - --port
      - "8080"
    ```

## Configuration volume

For applications that need to have persistent configuration data the config volume is hardcoded to `/config` inside the container. This is not able to be changed in most cases.

## Available Images

Each Image will be built with a `rolling` tag, along with tags specific to it's version. Available Images Below

Container | Channel | Image | Latest Tags
--- | --- | --- | ---


## Contributing

1. Install [Docker](https://docs.docker.com/get-docker/), [Taskfile](https://taskfile.dev/) & [Cuelang](https://cuelang.org/)
2. Get familiar with the structure of the repositroy
3. Find a similar application in the apps directory
4. Copy & Paste an application and update the directory name
5. Update `metadata.json`, `Dockerfile`, `ci/latest.sh`, `ci/goss.yaml` and make it suit the application build
6. Include any additional files if required
7. Use Taskfile to build and test your image

    ```ruby
    task APP=trackatrr CHANNEL=main test
    ```

### Automated tags

Here's an example of how tags are created in the GitHub workflows, be careful with `metadata.json` as it does affect the outcome of how the tags will be created when the application is built.

| Application    | Channel   | Stable  | Base    | Generated Tag                  |
|----------------|-----------|---------|---------|--------------------------------|
| `ubuntu`       | `focal`   | `true`  | `true`  | `ubuntu:focal-rolling`         |
| `ubuntu`       | `focal`   | `true`  | `true`  | `ubuntu:focal-19880312`        |
| `alpine`       | `3.16`    | `true`  | `true`  | `alpine:rolling`               |
| `alpine`       | `3.16`    | `true`  | `true`  | `alpine:3.16.0`                |
| `tracktarr`    | `develop` | `false` | `false` | `tracktarr-develop:3.0.8.1538` |
| `tracktarr`    | `develop` | `false` | `false` | `tracktarr-develop:rolling`    |
| `tracktarr`    | `main`    | `true`  | `false` | `tracktarr:3.0.8.1507`         |
| `tracktarr`    | `main`    | `true`  | `false` | `tracktarr:rolling`            |

## Credits

Huge appreciation to [onedr0p/containers](https://github.com/onedr0p/containers) where the inspiration came for this repositroy.