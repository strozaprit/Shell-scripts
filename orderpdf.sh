#!/bin/bash
#For each pdf file in a folder declared in array,
#extract the first 8 filename digits,
#check if a folder with the same name exists and copy files inside it.
#If the folder doesn't exist, it creates the folder and copy files.
#lungo is the file name and path
#nomefile is the filename with extension
#corto are 8 digits from the filename

a=/script/docks
b=/script/setramar
dir=( "$a" "$b" )
for i in ${dir[@]};
do
for lungo in $i/*.pdf;
do
#echo $lungo
nomefile=${lungo##*/}
#echo $nomefile
corto=${nomefile:0:8}
#echo $corto
if [ -d $i/$corto ];
then
  cp $i/$nomefile $i/$corto
  rm -f $i/$nomefile
else
 mkdir $i/$corto
 cp $i/$nomefile $i/$corto
 rm -f $i/$nomefile
fi
done
done
