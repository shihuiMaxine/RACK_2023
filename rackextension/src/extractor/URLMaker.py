class URLMaker:
    @staticmethod
    def get_raw_url(html_url):
        # Code for getting RAW URL
        raw_file_url = ""
        # Example htmlURL: "https://github.com/jquery/jquery/blob/c8c32f1d0583711355c593fb4c84332bfba18254/speed/benchmarker.js"
        try:
            # Find the "blob" path
            blob_str_index = html_url.find("blob/")

            # Extracting repo info
            git_index = html_url.find("github.com")
            brace_index = git_index + 10
            repo_info = html_url[brace_index + 1:blob_str_index - 1]

            # Extracting the "blob" part
            blob_index = blob_str_index + 5
            rest_part = html_url[blob_index:]
            next_slash = rest_part.find("/")
            blob = rest_part[:next_slash]

            # Extracting the file path
            file_path = rest_part[next_slash + 1:]

            # Form the raw path
            raw_file_url = f"https://raw.github.com/{repo_info}/{blob}/{file_path}"
            print(raw_file_url)

        except Exception as exc:
            pass

        return raw_file_url
if __name__ == "__main__":
    # call_url = "https://api.github.com/some_endpoint"
    # call_url ="https://github.com/search?q=python+language%3A+parse&type=repositories"
    result =URLMaker.get_raw_url("https://github.com/jquery/jquery/blob/c8c32f1d0583711355c593fb4c84332bfba18254/speed/benchmarker.js")
    print(result)
