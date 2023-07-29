import os
import subprocess


def get_dir_name(path):
    return os.path.dirname(path)


def run():
    cur_file_path = os.path.abspath(__file__)
    dir_path = get_dir_name(cur_file_path)

    # getting list of all folder in current directory
    question_categories = os.listdir(dir_path)

    for category in question_categories:
        path = os.path.join(dir_path, category)
        # checking if path is directory or not
        if os.path.isdir(path):
            # listing all the files from the path
            files = os.listdir(path)
            for question in files:
                question_path = os.path.join(path, question)
                # checking if the type if file and its a python file
                if os.path.isfile(question_path) and question_path.endswith(".py"):
                    print("current question: ", question)
                    subprocess.run(["python", question_path], check=True)
                    print()


if __name__ == "__main__":
    """runs all the questions solutions at once"""
    print("running all questions solution...")
    run()
