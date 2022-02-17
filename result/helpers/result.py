import os
import re
from typing import Dict, List

from PyPDF4 import PdfFileReader
from PyPDF4.pdf import PageObject

Result = Dict[str, list]


class ResultParser:
    def __init__(self):
        self.passed_regex = r"(\d{6}) (\(.*?\))"
        self.failed_regex = r"(\d{6}) {(.*?)}"

    def convert_to_result(self, result_string: str):
        result_string = result_string.strip()

        if "T" in result_string or "P" in result_string or "T,P" in result_string or "PF" in result_string:
            results = re.findall(r"\d{4,5}[ ]?[  ]?\(T?,?P?[PF]?\)", result_string)
            if not results:
                results = result_string.replace("withheld_sub- ", "")
                return [[results], True]

            return [results, True]
        else:
            result_string = result_string.strip("()")

        return [[result_string], False]

    def get_content(self, file: PdfFileReader):
        whole_content: str = ""

        for page in file.pages:
            content: str = page.extractText()
            lines: List[str] = content.split("\n")

            for line in lines:
                if line.endswith(","):
                    whole_content += line
                else:
                    whole_content += " " + line

        return whole_content

    def get_result(self, filename):
        file: PdfFileReader = PdfFileReader(filename)
        content: str = self.get_content(file)
        semester = filename.split("_")[1]
        regulation = filename.split("_")[2].split(".")[0]

        all_result = re.findall(self.failed_regex, content) + re.findall(self.passed_regex, content)

        data = dict()

        for roll, result in all_result:
            points, reffered = self.convert_to_result(result)

            formatted_points = []
            for point in points:
                splitted = point.strip(")").split("(")
                subject_code = splitted[0]
                failed_in = ""

                if len(splitted) > 1:
                    failed_in = splitted[1]
                
                formatted_points.append({"subject_code": subject_code, "failed_in": failed_in})

            data[int(roll)] = {
                "roll": roll,
                "points": formatted_points,
                "reffered": reffered,
                "semester": semester,
                "regulation": regulation
            }

        return data

    def get_all_result(self):
        results = dict()

        for folder in sorted(os.listdir("result/static"), reverse=True):
            results[int(folder)] = dict()

            for filename in os.listdir(f"result/static/{folder}"):
                if filename.endswith(".pdf"):
                    full_name = f"result/static/{folder}/{filename}"
                    print(f"Parsing {full_name}")

                    results[int(folder)].update(self.get_result(full_name))

        return results

    @staticmethod
    def get_single_result(all_results, roll):
        all_data = []
        for folder in all_results.keys():
            if roll in all_results[folder]:
                all_data.append(all_results[folder][roll])

        return {"results": all_data}
