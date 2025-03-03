import os

file_path = "artifacts\proprocessor.pkl"

if os.path.exists(file_path):
    print("✅ File exists:", file_path)
else:
    print("❌ File NOT found:", file_path)
    print("🔎 Current working directory:", os.getcwd())
