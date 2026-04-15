import os

def merge(source_folder, output_filename):
    with open(output_filename, 'ab' ) as outfile:
        for num, filename in enumerate(sorted(os.listdir(source_folder))):
            if (num % 10) == 0:
                print(num)
            file_path = os.path.join(source_folder, filename)
            
            try:
                with open(file_path, 'rb') as infile:
                    outfile.write(infile.read())
                print(f"Successfully appended: {filename}")
            except Exception as e:
                print(f"Could not read {filename}: {e}")

if __name__ == "__main__":
    merge(r'Analysis\runs', r'Analysis\total.txt')
    print("DONE")