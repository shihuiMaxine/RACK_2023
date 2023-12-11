import urllib.parse
import requests
import GitHubClient
from GitHubResponseDecoder import GitHubResponseDecoder
from CodeDownloader import CodeDownloader
from CodeFile import CodeFile  # Assuming you have the CodeFile class in a "core" module

class GitHubThread:
    def __init__(self, target_repo, search_query):
        self.code_files = []
        self.target_repo = target_repo
        self.search_query = search_query
        self.MAXIMUM_EXAMPLES = 5

    def collect_results_from_repo(self):
        try:
            call_url = self.develop_search_url()
            api_response = GitHubClient.execute_github_call(call_url)
            # print("API response:", api_response)
            self.code_files = GitHubResponseDecoder.extract_results_from_json(api_response)
            # print(self.target_repo, len(self.code_files))
            # self.code_files = self.get_page_content()
            # self.code_files = self.refine_code_results()
        except Exception as exc:
            # Handle the exception
            pass

    def refine_code_results(self):
        # Code for refining the results
        limit = min(len(self.code_files), self.MAXIMUM_EXAMPLES)
        if len(self.code_files) > self.MAXIMUM_EXAMPLES:
            for i in range(limit, len(self.code_files)):
                self.code_files.pop(i)
        return self.code_files

    def get_page_content(self):
        # Code for downloading the content
        limit = min(len(self.code_files), self.MAXIMUM_EXAMPLES)
        if len(self.code_files) > self.MAXIMUM_EXAMPLES:
            for i in range(limit, len(self.code_files)):
                self.code_files.pop(i)
        # Now download the contents
        downloader = CodeDownloader(self.code_files)  # You'll need to implement the CodeDownloader class
        self.code_files = downloader.download_code_contents()
        return self.code_files

    def get_collected_results(self):
        # Returning the collected fragments
        return self.code_files

    def develop_search_url(self):
        # Code for developing the base query
        call_url = ""
        try:
            encoded_item = urllib.parse.quote(self.search_query, safe='')
            call_url = f"https://github.com/search?q=python+language%3A+parse&type=repositories"
            call_url = f"https://github.com/search?q={encoded_item}&type=code"
            call_url = f"https://github.com/search?q={encoded_item}&type=code+in:file+user:{self.target_repo}+extension:python"
            call_url = f"https://github.com/huggingface/transformers/blob/bf7cfac20a08fa401d35d5a3d14246f4119d1f52/src/transformers/trainer.py#L2424"
    
            # call_url = f"https://api.github.com/search/code?q=send+email+language:python"
            # call_url = f"https://github.com/search?q=parse&type=code+in:file+user:google+extension:python"

            # https://github.com/search?q=python+language%3APython&type=repositories&l=Python
            # https://github.com/search/code?q=Document%20Jsoup%20Element%20Elements+in:file+user:apache+extension:java
            # call_url = f"https://api.github.com/search/code?q={encoded_item}+in:file+user:{self.target_repo}+extension:java"
        except Exception as exc:
            # Handle the exception
            pass
        print(call_url)
        return call_url

    def run(self):
        # Code for downloading the code files
        try:
            self.collect_results_from_repo()
        except Exception as exc:
            # Handle the exception
            exc.print_stack()

# Assuming you have implemented the GitHubClient and GitHubResponseDecoder classes
