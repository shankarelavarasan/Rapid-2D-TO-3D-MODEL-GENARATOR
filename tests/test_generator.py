import unittest
import os
from src.generator import create_3d_model_from_dxf

class TestGenerator(unittest.TestCase):

    def setUp(self):
        # The sample.dxf file should already exist from the previous steps.
        self.test_dxf_path = "sample.dxf"
        self.test_output_path = "test_output.stl"

    def tearDown(self):
        # Clean up the created file
        if os.path.exists(self.test_output_path):
            os.remove(self.test_output_path)

    def test_create_3d_model_from_dxf(self):
        # Test the full pipeline from DXF to STL
        create_3d_model_from_dxf(self.test_dxf_path, amount=20, output_path=self.test_output_path)

        # Check if the output file was created
        self.assertTrue(os.path.exists(self.test_output_path))

        # Check if the file is a valid STL file (binary format)
        with open(self.test_output_path, 'rb') as f:
            # A binary STL file starts with 80 bytes of header.
            # The content starts with "solid" in ASCII STL, but not necessarily in binary.
            # For a simple check, we'll just verify that the file is not empty
            # and has a reasonable size.
            file_size = os.path.getsize(self.test_output_path)
            self.assertGreater(file_size, 84) # 80 bytes for header + 4 bytes for num triangles

            # A more robust check would be to try and read the STL file
            # with a library like numpy-stl, but for now, this is sufficient.

if __name__ == '__main__':
    unittest.main()
