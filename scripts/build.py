import subprocess


def main():
    # Run the cx_Freeze build command
    subprocess.run(["poetry", "run", "python", "setup.py", "build"], check=True)


if __name__ == "__main__":
    main()
