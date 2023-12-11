import json
from CodeFile import CodeFile
from URLMaker import URLMaker

class GitHubResponseDecoder:
    @staticmethod
    def extract_results_from_json(api_response):
        # Code for extracting the source file URLs
        code_files = []
        try:
            data = json.loads(api_response)
            code_items = data.get("items", [])
            for code_item in code_items:
                # Extracting necessary elements
                html_url = code_item.get("html_url", "")
                raw_file_url = URLMaker.get_raw_url(html_url)
                score = code_item.get("score", 0.0)

                # Creating code file
                code_file = CodeFile()
                code_file.htmlFileURL = html_url
                code_file.rawFileURL = raw_file_url
                code_file.GitHubScore = score

                # Adding to the collection
                code_files.append(code_file)
        except Exception as exc:
            # Handle the exception
            pass
        return code_files
