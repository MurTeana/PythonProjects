import json
import base64
import os


def decode_base64_to_pdf(base64_string, output_pdf_path):
    try:
        # Decode the base64 string
        decoded_data = base64.b64decode(base64_string)

        # Write the decoded data to a PDF file
        with open(output_pdf_path, "wb") as pdf_file:
            pdf_file.write(decoded_data)

        print(f"Decoding successful. PDF file saved at: {output_pdf_path}")

    except Exception as e:
        print(f"Error: {e}")


def decode_base64_values_from_json_to_pdfs(json_file_path, output_directory):
    try:
        # Read the JSON content from the input file
        with open(json_file_path, "r") as json_file:
            json_data = json.load(json_file)

        # Ensure the output directory exists
        os.makedirs(output_directory, exist_ok=True)

        # Iterate over each object in the JSON array
        for i, data_entry in enumerate(json_data):
            # Extract the base64-encoded string from the "Value" field
            base64_string = data_entry.get("Value", "")

            # Create a unique output PDF file path based on the index
            output_pdf_path = f"{output_directory}/parcel_{i + 1}.pdf"  #

            # Decode and save as a PDF file
            decode_base64_to_pdf(base64_string, output_pdf_path)

    except Exception as e:
        print(f"Error: {e}")


# Example usage
input_json_file_path = "D:/Coding/PYTHON/PythonProjects/BASE64toPDF/data/input.json"
output_directory = "D:/Coding/PYTHON/PythonProjects/BASE64toPDF/data"

decode_base64_values_from_json_to_pdfs(input_json_file_path, output_directory)
