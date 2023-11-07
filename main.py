from Ram.Base.GUI import CipherCLI

if __name__ == "__main__":
    cli = CipherCLI()
    cli.output.print_message()
    cli.run()
    cli.output.print_end()