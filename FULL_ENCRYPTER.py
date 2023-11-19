from PyPDF2 import PdfReader, PdfWriter

def capture_fingerprint():
    # Implement your fingerprint capturing logic here
    return "YourFingerprintData"  # Replace this with the captured fingerprint data

def capture_face():
    # Implement your face capturing logic here
    pass

def encrypt_pdf_with_biometrics(input_pdf_path, output_pdf_path, fingerprint_data):
    # Open the original PDF using PdfReader
    with open(input_pdf_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)

        # Create a PDF writer object
        pdf_writer = PdfWriter()

        # Add pages from the original PDF to the writer
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        # Set encryption options with a non-empty user_password
        pdf_writer.encrypt(user_password=fingerprint_data, use_128bit=True)

        # Write the encrypted PDF to a file
        with open(output_pdf_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

if __name__ == "__main__":
    fingerprint_data = capture_fingerprint()
    capture_face()
    encrypt_pdf_with_biometrics(r'c:\Users\ANKIT KUMAR\Downloads\CSI_selection_mail[1].pdf', 'encrypted_output.pdf', fingerprint_data)
