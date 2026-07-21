import os
import re
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import requests
import tricahue

sbh_url = "https://api.synbiohub.org" #"https://synbiohub.org"
sbh_user = "synbiotest"
sbh_pass = "test123"
sbh_overwrite = True

test_file_path = "tests/test_files"


class XDC_SBH_tests(unittest.TestCase):
    def setup(self, filename, extension):
        excel_path = os.path.join(test_file_path, f"{filename}.{extension}")
        collection_name = re.sub("[^A-Za-z0-9_]", "", filename)
        self.xdc = tricahue.XDC(
            input_excel_path=excel_path,
            homespace="https://example.org/",
        )
        self.sbh_collection_name = f"{collection_name}_test"
        self.sbh_description = f"{filename} test collection description"

    def upload_to_sbh(self):
        collection_url, _ = self.xdc.upload_to_new_collection(
            sbh_url=sbh_url,
            sbh_collection_name=self.sbh_collection_name,
            sbh_overwrite=sbh_overwrite,
            sbh_description=self.sbh_description,
            sbh_user=sbh_user,
            sbh_pass=sbh_pass,
        )
        return collection_url

    def assert_collection_available(self, collection_url):
        response = requests.get(
            collection_url,
            headers={
                "Accept": "text/plain",
                "X-authorization": self.xdc.sbh_token,
            },
        )
        self.assertEqual(response.status_code, 200, f"Got response: {response.status_code}")

    def test_medias(self):
        self.setup("Tricahue_v11.6b_Medias", "xlsx")
        self.assert_collection_available(self.upload_to_sbh())

    def test_chassis(self):
        self.setup("Tricahue_v11.6b_Chassis", "xlsx")
        self.assert_collection_available(self.upload_to_sbh())

    def test_chemicals(self):
        self.setup("Tricahue_v11.6b_Chemicals", "xlsm")
        self.assert_collection_available(self.upload_to_sbh())

    def test_strain(self):
        self.setup("Tricahue_Strain", "xlsm")
        self.assert_collection_available(self.upload_to_sbh())


if __name__ == "__main__":
    unittest.main()
