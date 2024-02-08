import random
import subprocess

def main():
    with open("randomfile.txt", "w") as file:
        file.write("")

    num_iterations = random.randint(2, 10)

    for i in range(num_iterations):
        with open("randomfile.txt", "a") as file:
            file.write(".")
        subprocess.run(["git", "add", "randomfile.txt"])
        subprocess.run(["git", "commit", "-m", "Auto-commit: #" + str(i) + ""])

    subprocess.run(["git", "push", "origin", "master"])

if __name__ == "__main__":
    main()
