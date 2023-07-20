import pytest
import os
import sys
sys.path.append(os.path.abspath('../'))
print(sys.path)
import worker

# Test the worker's granural functions

def test_get_random_bytes():
    assert "result" == worker.get_random_bytes()

def test_hash_bytes():
    assert "result" == worker.hash_bytes("input")

if __name__ == "__main__":
    test_get_random_bytes()
