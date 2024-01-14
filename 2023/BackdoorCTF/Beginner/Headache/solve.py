file_path = "chal.png"

with open(file_path, "rb") as file:
    file_content = file.read()

bytes_data = file_content
png_header = [0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]
header = bytes(png_header)

new_data = header + bytes_data[len(png_header) :]

with open("solve.png", "wb") as file:
    file.write(new_data)
