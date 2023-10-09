#!/bin/bash

conan create . --build=missing && \
  conan upload -c "type_erasure" --check --all --remote staconan
