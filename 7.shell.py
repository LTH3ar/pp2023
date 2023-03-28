#!/usr/bin/python
import subprocess
import os

class command_struct:
    def __init__(self, command_string):
        self.command_string = command_string.split()
        self.command = self.command_string[0]
        self.args = self.command_string[1:]


class UserInput:
    def __init__(self):
        self.input = None

    def get_input(self):
        self.input = input("myshell> ")
        if self.input == "":
            return
        else:
            self.input = self.input.split("|")
            command_count = len(self.input)
            for i in range(command_count):
                self.input[i] = command_struct(self.input[i])

    def print_input(self):
        for i in self.input:
            print(i.command + " " + str(i.args))


class Shell:
    def __init__(self):
        self.user_input = UserInput()

    def run(self):
        while True:
            self.user_input.get_input()
            self.user_input.print_input()
            self.run_command_check()

    def change_dir(self):
        if self.user_input.input[0].args[0] == '~':
            os.chdir(os.path.expanduser("~"))
        else:
            os.chdir(self.user_input.input[0].args[0])

    def run_command_check(self):
        if len(self.user_input.input) == 0:
            return

        if self.user_input.input[0].command == "cd":
            self.change_dir()
        elif self.user_input.input[0].command == "exit":
            exit()
        else:
            if len(self.user_input.input) == 1:
                self.execute_command_single()
            else:
                self.execute_command_pipe()

    def io_redirection(self, command_raw):
        output_file = None
        input_file = None
        sign_io = [">", "<", ">>"]

        # if command_raw not in sign_io:
        #    return command_raw, None, None

        for token in command_raw:

            if token == "<":
                input_file = command_raw[command_raw.index(token) + 1]
                command_raw.remove(token)
                command_raw.remove(input_file)
                # print(command_raw)

        for token in command_raw:
            if token == ">":
                output_file = command_raw[command_raw.index(token) + 1]
                command_raw.remove(token)
                command_raw.remove(output_file)
                # print(command_raw)

            elif token == ">>":
                output_file = command_raw[command_raw.index(token) + 1]
                command_raw.remove(token)
                command_raw.remove(output_file)
                # print(command_raw)

        # print(command_raw)

        return command_raw, input_file, output_file

    def execute_command_single(self):
        command, input_file, output_file = self.io_redirection(self.user_input.input[0].command_string)
        # print(command, input_file, output_file)

        if input_file and not output_file:
            with open(input_file, "r") as input_file:
                input_file = input_file
                exec_command = subprocess.Popen(command, stdin=input_file, stdout=subprocess.PIPE, shell=False)

        elif output_file and not input_file:
            with open(output_file, "w") as output_file:
                output_file = output_file
                exec_command = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=output_file, shell=False)

        elif input_file and output_file:
            with open(input_file, "r") as input_file:
                input_file = input_file
                with open(output_file, "w") as output_file:
                    exec_command = subprocess.Popen(command, stdin=input_file, stdout=output_file, shell=False)
                    output_file = output_file
        else:
            exec_command = subprocess.Popen(command, shell=False)

        exec_command.wait()
        output, error = exec_command.communicate()
        if output:
            output_lst = (output.decode().split("\n"))
            for i in output_lst:
                print(i)
        if error:
            print(error.decode())

    def execute_command_pipe(self):
        command_lst = []
        input_file_lst = []
        output_file_lst = []
        for i in range(len(self.user_input.input)):
            command, input_file, output_file = self.io_redirection(self.user_input.input[i].command_string)
            input_file_lst.append(input_file)
            output_file_lst.append(output_file)
            command_raw = command_struct(" ".join(command))
            command_lst.append(command_raw)
        if any(input_file_lst) and not any(output_file_lst):
            with open(input_file_lst[0], "r") as input_file:
                input_file = input_file
                exec_command = subprocess.Popen(command_lst[0].command_string, stdin=input_file, stdout=subprocess.PIPE,
                                                shell=False)
                for i in range(1, len(self.user_input.input)):
                    exec_command = subprocess.Popen(command_lst[i].command_string, stdin=exec_command.stdout,
                                                    stdout=subprocess.PIPE, shell=False)

        elif any(output_file_lst) and not any(input_file_lst):
            for i in output_file_lst:
                if i != None:
                    with open(i, "w") as output_file:
                        output_file = output_file
                        exec_command = subprocess.Popen(command_lst[0].command_string, stdin=subprocess.PIPE,
                                                        stdout=subprocess.PIPE, shell=False)
                        for i in range(1, len(self.user_input.input)):
                            exec_command = subprocess.Popen(command_lst[i].command_string, stdin=exec_command.stdout,
                                                            stdout=output_file, shell=False)

        elif any(input_file_lst) and any(output_file_lst):
            with open(input_file_lst[0], "r") as input_file:
                input_file = input_file
                for i in output_file_lst:
                    if i != None:
                        with open(i, "w") as output_file:
                            output_file = output_file
                            exec_command = subprocess.Popen(command_lst[0].command_string, stdin=input_file,
                                                            stdout=subprocess.PIPE, shell=False)
                            for i in range(1, len(self.user_input.input)):
                                exec_command = subprocess.Popen(command_lst[i].command_string,
                                                                stdin=exec_command.stdout, stdout=output_file,
                                                                shell=False)
        else:
            exec_command = subprocess.Popen(self.user_input.input[0].command_string, stdout=subprocess.PIPE,
                                            shell=False)
            for i in range(1, len(self.user_input.input)):
                exec_command = subprocess.Popen(self.user_input.input[i].command_string, stdin=exec_command.stdout,
                                                stdout=subprocess.PIPE, shell=False)

        exec_command.wait()

        output, error = exec_command.communicate()
        # exec_command.stdout.close()

        if output:
            output_lst = (output.decode().split("\n"))
            for i in output_lst:
                print(i)

        if error:
            print(error.decode())


if __name__ == "__main__":
    shell = Shell()
    shell.run()