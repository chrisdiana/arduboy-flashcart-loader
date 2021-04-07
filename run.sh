#!/bin/bash


HELP=$(cat <<EOF
	\n
	ARDUBOY FLASHCART LOADER\n
	Run with argument <index build write all>:
	\n\n
	\t./run.sh <arg>\n\n
	\tExample: ./run.sh index example-flashcart/\n\n
EOF
)

CMD=$1
DIR_PATH=$2


check_flashcart_dir() {
	if [ -z $DIR_PATH ]; then
		echo "ERROR: missing flashcart directory path (./run.sh build ./example-flashcart/)"
		exit 1
	fi
}

index() {
	check_flashcart_dir
	python3 ./src/generate_flashcart_bin.py $1
}

build() {
	check_flashcart_dir
	python3 ./Arduboy-Python-Utilities/flashcart-builder.py "$1/flashcart-index.csv"
}

write() {
	check_flashcart_dir
	python3 ./Arduboy-Python-Utilities/flashcart-writer.py "$1/flashcart-image.bin"
}

all() {
	index $DIR_PATH
	build $DIR_PATH
	write $DIR_PATH
}

case $CMD in
	index 	| -i ) index $DIR_PATH ;;
	build 	| -b ) build $DIR_PATH ;;
	write 	| -w ) write $DIR_PATH ;;
	all 	| -a ) all $DIR_PATH ;;
	*) echo $HELP ;;
esac