import docx

doc = docx.Document()

list_tuples = [('João',19)('Maria',25)('Pedro',30)]

table = doc.add_table(1,2,3)

heading_cells = table.rows[0].cells
heading_cells[0].text = 'Name'
heading_cells[1].text = 'Age'

for index,tuple in enumerate(list_tuples):
  cells = table.add_row().cells
  cells[0].text = tuple[0]
  cells[1].text = str(tuple[1])



doc.save('Example_doc') 