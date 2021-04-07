default:
	python3 manage/generate_flashcart_bin.py custom-flashcart/
	python3 manage/flashcart-builder.py custom-flashcart/flashcart-index.csv
	python3 manage/flashcart-writer.py custom-flashcart/flashcart-image.bin
