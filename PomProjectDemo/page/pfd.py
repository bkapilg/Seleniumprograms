import os
import pdfkit

pdfkit.from_url("http://www.gutenberg.org/files/1112/1112.txt", "romeoandjuliet.pdf")

os.startfile("romeoandjuliet.pdf")