import sys
from PyPDF2 import PdfReader, PdfWriter

def remove_password(input_pdf, output_pdf, password):
    # Create a PDF reader object
    reader = PdfReader(input_pdf)

    # Check if the PDF is encrypted
    if reader.is_encrypted:
        # Attempt to decrypt the PDF with the provided password
        if reader.decrypt(password):
            print("Password successfully decrypted")
        else:
            print("Incorrect password. Unable to decrypt the PDF.")
            return

    # Create a PDF writer object
    writer = PdfWriter()

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Write the output to a new PDF file
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

    print(f"Password protection removed. New file saved as {output_pdf}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_pdf> <output_pdf> <password>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    password = sys.argv[3]

    remove_password(input_pdf, output_pdf, password)
