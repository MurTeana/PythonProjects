import json
import base64


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


def decode_base64_from_json_to_pdf(json_file_path, output_pdf_path):
    try:
        # Read the JSON content from the input file
        with open(json_file_path, "r") as json_file:
            json_data = json.load(json_file)

        # Extract the base64-encoded string from the JSON
        base64_string = json_data.get("Value", "")

        # Decode and save as a PDF file
        decode_base64_to_pdf(base64_string, output_pdf_path)

    except Exception as e:
        print(f"Error: {e}")


# Example usage
input_json_file_path = "D:/Coding/PYTHON/PythonProjects/BASE64toPDF/data/input.json"
output_pdf_file_path = "D:/Coding/PYTHON/PythonProjects/BASE64toPDF/data/file.pdf"

decode_base64_from_json_to_pdf(input_json_file_path, output_pdf_file_path)
