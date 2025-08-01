target "docker-metadata-action" {}

variable "APP" {
  default = "mathesar"
}

variable "VERSION" {
  // renovate: datasource=github-releases depName=mathesar-foundation/mathesar
  default = "0.2.5"
}

variable "SOURCE" {
  default = "https://github.com/mathesar-foundation/mathesar"
}

group "default" {
  targets = ["image-local"]
}

target "image" {
  inherits = ["docker-metadata-action"]
  args = {
    VERSION = "${VERSION}"
  }
  labels = {
    "org.opencontainers.image.source" = "${SOURCE}"
  }
}

target "image-local" {
  inherits = ["image"]
  output = ["type=docker"]
  tags = ["${APP}:${VERSION}"]
}

target "image-all" {
  inherits = ["image"]
  platforms = [
    "linux/amd64",
    "linux/arm64"
  ]
}