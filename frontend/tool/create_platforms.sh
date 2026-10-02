#!/usr/bin/env bash
set -euo pipefail
if [ ! -d android ]; then flutter create --platforms=android,web,ios .; fi
