#!/bin/bash
set -e
PYBIND_VER=$1

git feature pybind-bump-${PYBIND_VER}
wget -c https://github.com/pybind/pybind11/archive/refs/tags/v${PYBIND_VER}.tar.gz
tar xzvf v${PYBIND_VER}.tar.gz
git rm -rf pybind11
mv pybind11-${PYBIND_VER} pybind11
git add pybind11
git commit -a -m "pybind: update to ${PYBIND_VER}"
rm v${PYBIND_VER}.tar.gz
