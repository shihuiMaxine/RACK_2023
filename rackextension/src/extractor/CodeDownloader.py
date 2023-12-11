from CodeFile import CodeFile
import requests

class CodeDownloader:
    def __init__(self, code_files=None):
        self.CodeFiles = code_files if code_files is not None else []

    def get_raw_content(self, code_file_url):
        # Code for downloading the content
        code = ""
        try:
            response = requests.get(code_file_url, timeout=(2, 5))
            response.raise_for_status()  # Raise an exception for HTTP errors

            code = response.text
        except requests.exceptions.RequestException as exc:
            # Handle the exception
            pass

        return code

    def download_code_contents(self):
        # Code for downloading the codes
        try:
            for code_file in self.CodeFiles:
                raw_content = self.get_raw_content(code_file.rawFileURL)
                code_file.CompleteCode = raw_content
        except Exception as exc:
            # Handle the exception
            pass

        return self.CodeFiles

if __name__ == "__main__":
    # Example usage:
    code_files = [CodeFile(), CodeFile()]  # Create CodeFile objects
    downloader = CodeDownloader(code_files)
    downloaded_files = downloader.download_code_contents()
    for code_file in downloaded_files:
        print(code_file.CompleteCode)
