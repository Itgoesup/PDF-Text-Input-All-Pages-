

# PDF Merger Script


This program merges all PDF files in the current directory and adds a watermark of "Hello world" to each page of each PDF file.

The main goal is to watermark each of the PDF pages.






## Installation

Fork or download the repository.

You will need:

* PyPDF2
* reportlab

    
## Usage

1. The program reads all the PDF files in the current directory and creates a watermark with the text "Hello world" using reportlab.
2. For each page of each PDF file, the program merges the watermark with the page using PyPDF2.
3. The resulting PDF files with the watermark are saved temporarily and then merged into a final PDF file using PyPDF2.
4. The temporary PDF files are then deleted.

## Note

- The order of the merged PDF files depends on the order in which they appear in the directory.
- The program assumes that all the PDF files in the directory need to be merged. If you want to merge only specific files, you can modify the code to include only those files.
