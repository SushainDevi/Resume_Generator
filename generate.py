from weasyprint import HTML

# Input HTML file path and output PDF file path
input_html = 'resume_sample.html'
output_pdf = 'resume_sample.pdf'

# Convert HTML to PDF
HTML(file_uri=input_html).write_pdf(output_pdf)
