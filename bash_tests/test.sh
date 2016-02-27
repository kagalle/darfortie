#!/bin/bash
echo "$OPTIND"
while getopts ":P:" opt; do
  case $opt in
    P)  echo \"${OPTARG}\";;
    \?)  echo wrong;;
  esac
  echo "$OPTIND"
done
echo "$OPTIND"
shift $(($OPTIND - 1))
echo "$OPTIND"
if ! [ -z "$1" ]; then
  abc="ABC \"$1\""
fi
echo $abc

