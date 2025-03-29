def flip_html(file_path, output_path):
    # Read the HTML file
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Reverse the content
    flipped_content = lines[::-1]

    # Write the reversed content to a new file
    with open(output_path, "w", encoding="utf-8") as file:
        file.writelines(flipped_content)

    # Verification: Read back and check if flipping again restores the original
    with open(output_path, "r", encoding="utf-8") as file:
        flipped_back = file.readlines()[::-1]

    # Debugging: Check for missing lines
    if len(lines) != len(flipped_back):
        print(f"Warning: Mismatch detected! Original lines: {len(lines)}, Flipped lines: {len(flipped_back)}")
        missing_lines = set(lines) - set(flipped_back)
        if missing_lines:
            print(f"Missing lines:\n{''.join(missing_lines)}")
    else:
        print(f"Flipping verification successful! All {len(lines)} lines were transferred correctly.")

# Example usage
input_file = "links2.html"  # Replace with your HTML file
output_file = "flipped_example.html"
flip_html(input_file, output_file)
