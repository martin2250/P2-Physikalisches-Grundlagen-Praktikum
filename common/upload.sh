#!/bin/bash
ID=$(../common/gdrive-linux-x64 list --no-header --query "'0B2OzfW5smQv8MzNyZjlfX2VMTjQ' in parents and name='$1' and trashed=false")
ID=$(echo $ID | awk 'NR==1{print $1; exit}')

if [[ -z $ID ]]
then
	echo "new file"
	../common/gdrive-linux-x64 upload -p 0B2OzfW5smQv8MzNyZjlfX2VMTjQ $1
else
	echo "update"
    ../common/gdrive-linux-x64 update $ID $1
fi


