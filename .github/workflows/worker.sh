#!/usr/bin/env bash


rawurlencode() {
  local string="${1}"
  local strlen=${#string}
  local encoded=""
  local pos c o

  for (( pos=0 ; pos<strlen ; pos++ )); do
     c=${string:$pos:1}
     case "$c" in
        [-_.~a-zA-Z0-9] ) o="${c}" ;;
        * )               printf -v o '%%%02x' "'$c"
     esac
     encoded+="${o}"
  done
  echo "${encoded}"    # You can either set a return variable (FASTER)
  REPLY="${encoded}"   #+or echo the result (EASIER)... or both... :p
}


rm README.md
filenames=$(ls)
echo "## leetcode" >> README.md
echo >> README.md
echo >> README.md


while IFS= read -r line; do
    echo "[$line]($( rawurlencode "$line" ))" >> README.md
    echo >> README.md
done <<< "$filenames"

echo '```' >> README.md
echo "note: readme format stolen from @MuhammadNaqi03" >> README.md
echo '```' >> README.md
