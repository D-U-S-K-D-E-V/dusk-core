import unittest

if __name__ == "__main__":
    # Discover and run all tests in the 'tests' directory
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=".", pattern="test_*.py")
    
    runner = unittest.TextTestRunner()
    runner.run(suite)