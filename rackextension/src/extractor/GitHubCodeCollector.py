import os
from GitHubThread import GitHubThread
from StaticData import StaticData
from CodeFile import CodeFile  # Assuming you have the CodeFile class in a "core" module
import threading
class GitHubCodeCollector:
    def __init__(self, search_query=None):
        self.CodeFiles = []
        self.search_query = search_query
        self.TOPK = 5
        self.repos = ["apache", "eclipse", "google", "facebook"]

    def collect_github_results(self):
        try:
            rcollection = []
            tcollection = []

            for repo in self.repos:
                rthread = GitHubThread(repo, self.search_query)
                rcollection.append(rthread)
                t = threading.Thread(target=rthread.run)
                tcollection.append(t)
                t.start()

            total_repo = len(self.repos)
            completed = 0
            while completed < total_repo:
                for i in range(len(tcollection)):
                    t = tcollection[i]
                    if not t.is_alive():
                        gthread = rcollection[i]
                        tresults = gthread.get_collected_results()
                        count = 0
                        for cf in tresults:
                            self.CodeFiles.append(cf)
                            count += 1
                            if count == self.TOPK:
                                break
                        tcollection.pop(i)
                        rcollection.pop(i)
                        completed += 1

        except Exception as exc:
            # Handle the exception
            pass

        print("Total results collected:", len(self.CodeFiles))
        return self.CodeFiles

    def collect_from_local_repo(self, exception_id):
        # Collecting code from a local repository
        try:
            code_folder = os.path.join(StaticData.Surf_Data_Base, "codes", str(exception_id))
            f_dir = os.path.join(code_folder)
            if os.path.exists(f_dir):
                file_count = len(os.listdir(f_dir))
                for i in range(file_count):
                    code_file_path = os.path.join(f_dir, f"{i}.java")
                    code_file = CodeFile()
                    try:
                        with open(code_file_path, 'r') as file:
                            content = file.read()
                        # Collecting the complete codes
                        code_file.CompleteCode = content
                        self.CodeFiles.append(code_file)
                    except Exception as exc:
                        # Handle the exception
                        pass
        except Exception as exc:
            pass

        return self.CodeFiles

    def save_code_contents(self, code_files):
        # Code for showing the code contents
        try:
            count = 0
            for code_file in code_files:
                file_url = os.path.join(StaticData.Surf_Data_Base, "codes", f"{count}.java")
                with open(file_url, 'w') as f:
                    f.write(code_file.CompleteCode)
                count += 1
        except Exception as exc:
            # Handle the exception
            pass

    def save_code_contents_by_exception_id(self, exception_id, code_files):
        # Code for saving the code contents
        try:
            count = 0
            dir_path = os.path.join(StaticData.Surf_Data_Base, "codes", str(exception_id))
            os.makedirs(dir_path, exist_ok=True)

            for code_file in code_files:
                file_url = os.path.join(dir_path, f"{count}.java")
                with open(file_url, 'w') as f:
                    f.write(code_file.CompleteCode)
                count += 1
        except Exception as exc:
            # Handle the exception
            pass

    @staticmethod
    def main():
        # search_query = "Document Jsoup Element Elements"
        search_query = "parse"
        git_code_collector = GitHubCodeCollector(search_query)
        git_code_collector.collect_github_results()

if __name__ == "__main__":
    GitHubCodeCollector.main()
