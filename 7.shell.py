import os
import subprocess

class PythonShell:
    def __init__(self):
        self.current_dir = os.getcwd()

    def run_command(self, command):
        # split the command string into a list of arguments
        args = command.split()

        # check for IO redirection operators
        input_redirect = None
        output_redirect = None
        append_redirect = None
        if "<" in args:
            input_redirect = args[args.index("<") + 1]
            args.remove("<")
            args.remove(input_redirect)
        if ">" in args:
            output_redirect = args[args.index(">") + 1]
            args.remove(">")
            args.remove(output_redirect)
        if ">>" in args:
            append_redirect = args[args.index(">>") + 1]
            args.remove(">>")
            args.remove(append_redirect)

        # execute the command with subprocess.Popen()
        process = subprocess.Popen(args,
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   cwd=self.current_dir)

        # handle input redirection
        if input_redirect:
            with open(input_redirect, "r") as input_file:
                input_data = input_file.read()
                process.stdin.write(input_data.encode())
                process.stdin.close()

        # handle output redirection
        if output_redirect:
            with open(output_redirect, "w") as output_file:
                output = process.stdout.read()
                output_file.write(output.decode())
        elif append_redirect:
            with open(append_redirect, "a") as append_file:
                output = process.stdout.read()
                append_file.write(output.decode())
        else:
            # print the output to the console
            output = process.stdout.read()
            print(output.decode())

        # close the file descriptors and wait for the process to terminate
        process.stdin.close()
        process.stdout.close()
        process.stderr.close()
        process.wait()

    def change_dir(self, path):
        os.chdir(path)
        self.current_dir = os.getcwd()

    def get_current_dir(self):
        return self.current_dir

if __name__ == "__main__":
    shell = PythonShell()
    while True:
        user_input = input(f"{shell.get_current_dir()} $ ")

        if user_input == "":
            continue

        if user_input == "clear":
            os.system("clear")
            continue

        if user_input == "exit":
            break

        if user_input.startswith("cd"):
            path = user_input.split()[1]
            if path == "~":
                path = os.path.expanduser("~")
            shell.change_dir(path)
            continue
        else:
            shell.run_command(user_input)
