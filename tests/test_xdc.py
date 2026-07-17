import re
import tricahue
import unittest
import os
import sys
import requests

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

fj_url = "charmmefj-api.synbiohub.org"
fj_user = None
fj_pass = None

sbh_url = "https://synbiohub.org"
sbh_user = "synbiotest"
sbh_pass = "test123"
sbh_collec = "XDC_package_test"

test_file_path ='tests/test_files'
excel_path = os.path.join(test_file_path, 'Tricahue_v11.6b_Medias.xlsx')

fj_overwrite = 1
sbh_overwrite = 1

# xdc = tricahue.XDC(input_excel_path = excel_path,
#             fj_url = fj_url,
#             fj_user = fj_user, 
#             fj_pass = fj_pass, 
#             sbh_url = sbh_url, 
#             sbh_user = sbh_user, 
#             sbh_pass = sbh_pass, 
#             sbh_collection = sbh_collec, 
#             sbh_collection_description = 'Tricahue XDC package test collection',
#             sbh_overwrite = sbh_overwrite, 
#             fj_overwrite = fj_overwrite, 
#             homespace = homespace,
#             fj_token = None, 
#             sbh_token = None)

class Test_XDC(unittest.TestCase):
    def setup(self, filename, extension):
        # TODO: get file path so it can be run from anywhere
        excel_path = os.path.join(test_file_path, filename+'.'+extension)
        collection_name = re.sub('[^A-Za-z0-9_]', '', filename)
        self.xdc = tricahue.XDC(input_excel_path = excel_path,
            fj_url = fj_url,
            fj_user = fj_user, 
            fj_pass = fj_pass, 
            sbh_url = sbh_url, 
            sbh_user = sbh_user, 
            sbh_pass = sbh_pass, 
            sbh_collection = collection_name + '_test', 
            sbh_collection_description = filename + ' test collection description',
            sbh_overwrite = sbh_overwrite,
            fj_overwrite = fj_overwrite,
            homespace = "https://example.org/", 
            fj_token = None, 
            sbh_token = None)

    def test_medias(self):
        # make this part of the unittest setup method
        self.setup('Tricahue_v11.6b_Medias', 'xlsx')

        sbh_url = self.xdc.run()
        print(sbh_url)
        response = requests.get(sbh_url,
                        headers={
                            'Accept': 'text/plain',
                            'X-authorization': self.xdc.sbh_token},)
        assert response.status_code == 200, f'Got response: {response.status_code}'

    def test_chassis(self):
        self.setup('Tricahue_v11.6b_Chassis', 'xlsx')

        sbh_url = self.xdc.run()
        print(sbh_url)
        response = requests.get(sbh_url,
                        headers={
                            'Accept': 'text/plain',
                            'X-authorization': self.xdc.sbh_token},)
        assert response.status_code == 200, f'Got response: {response.status_code}'

    def test_chemicals(self):
        self.setup('Tricahue_v11.6b_Chemicals', 'xlsm')

        sbh_url = self.xdc.run()
        print(sbh_url)
        response = requests.get(sbh_url,
                        headers={
                            'Accept': 'text/plain',
                            'X-authorization': self.xdc.sbh_token},)
        assert response.status_code == 200, f'Got response: {response.status_code}'

    def test_strain(self):
        self.setup('Tricahue_Strain', 'xlsm')

        sbh_url = self.xdc.run()
        print(sbh_url)
        response = requests.get(sbh_url,
                        headers={
                            'Accept': 'text/plain',
                            'X-authorization': self.xdc.sbh_token},)
        assert response.status_code == 200, f'Got response: {response.status_code}'
        
if __name__ == '__main__':
    unittest.main()
