import subprocess

def generate_manim_file(filename, code):
    try:
        with open(filename, "w") as file:
            file.write(code)
        print(f"\nFile '{filename}' created successfully.\n")

    except Exception as e:
        print(f"\nAn error occurred while creating the file: {e}\n")

def run_manim(path):
    print("\n Running File\n")
    cmd = 'python -m manim -pql ' + path + " Demo"
    returned_value = subprocess.call(cmd,shell=True)
    print('returned vale:', returned_value)


def edit_manim(path):
    with open(path,"r+") as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        file.writelines(lines[1:-1])

    print("\nFile Edited\n")