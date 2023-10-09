#!/bin/bash
echo "countdown loading.."
sleep 2
read number
countdown=$number
until [ $countdown -le "0" ];
do
	echo "$countdown"
	(( countdown -= 1 ))
	if [ $countdown ];
	then
		sleep 1
	fi
done
	echo "countdown completed"
