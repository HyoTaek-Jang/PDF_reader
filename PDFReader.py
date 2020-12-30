from tika import parser

pdf_path = 'software17.pdf'
raw = parser.from_file(pdf_path)
content = raw['content']

print(content.strip())