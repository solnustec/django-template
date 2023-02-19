#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
RESET='\033[0m'

function no_log_if_successful {
  set +e
  COMMAND=$@
  printf "Running $COMMAND ... "

  OUTPUT=$($@ 2>&1)
  EXIT_CODE=$?
  if [[ $EXIT_CODE -gt 0 ]]; then
    printf "${RED}Failed${RESET} 😢\n"
    printf "%s\n\n" "${OUTPUT}"
  else
    printf "${GREEN}Success!${RESET}\n"
  fi
  set -e
  return $EXIT_CODE
}
