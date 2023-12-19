import struct


def big_to_little_endian_file(input_file, output_file):
    # Read the content of the input file
    with open(input_file, "rb") as f:
        content = f.read()

    # Convert the content from big-endian to little-endian using struct.pack and struct.unpack
    little_endian_content = b""
    for i in range(0, len(content), 4):
        chunk = content[i : i + 4]
        little_endian_chunk = struct.pack(">I", struct.unpack("<I", chunk)[0])
        little_endian_content += little_endian_chunk

    # Write the converted content to the output file
    with open(output_file, "wb") as f:
        f.write(little_endian_content)


# Example usage:
input_file_path = "a.bin"
output_file_path = "b.bin"

big_to_little_endian_file(input_file_path, output_file_path)
print(f"Conversion complete. Output written to {output_file_path}")
