import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, 'user.json')

print(f"Checking DB_FILE: {DB_FILE}")

if not os.path.exists(DB_FILE):
    print("❌ File not found!")
else:
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"File content length: {len(content)}")
            print("--- CONTENT START ---")
            print(content)
            print("--- CONTENT END ---")
            
            f.seek(0)
            data = json.load(f)
            print(f"✅ JSON Loaded Successfully. Items: {len(data)}")
            for item in data:
                print(f" - User: {item.get('username')}, Role: {item.get('role')}")
    except json.JSONDecodeError as e:
        print(f"❌ JSON Decode Error: {e}")
    except Exception as e:
        print(f"❌ Other Error: {e}")
