import os
import subprocess
import shutil
import sys

# --- CONFIGURATION ---
# Folder where your original, readable code will live
SRC_DIR = "src"
# Folder for protected/deployed code
OUT_DIR = "obfuscated"

# Files to protect
JS_FILES = ["script.js", "i18n.js", "bsw_template.js"]
CSS_FILES = ["styles.css", "new_card_styles.css", "clean_styles.css", "docs_styles.css"]
HTML_FILES = ["index.html"]
# Other assets to copy (logos, etc.)
COPY_DIRS = ["logos", "Rockwell", "simens"]

def run_command(cmd):
    print(f"Executing: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    return True

def setup_src():
    if not os.path.exists(SRC_DIR):
        print(f"Creating {SRC_DIR} and moving source files...")
        os.makedirs(SRC_DIR, exist_ok=True)
        # Move files if they are in root
        for f in JS_FILES + CSS_FILES + HTML_FILES:
            if os.path.exists(f):
                shutil.move(f, os.path.join(SRC_DIR, f))
                print(f"Moved {f} to {SRC_DIR}")

def build():
    print("--- Starting Build & Obfuscation ---")
    
    # 1. Prepare OUT_DIR
    if not os.path.exists(OUT_DIR):
        os.makedirs(OUT_DIR)
    
    if not os.path.exists(SRC_DIR):
        print(f"Error: {SRC_DIR} folder not found. Run with --setup first.")
        return

    # 2. Obfuscate JS
    for js in JS_FILES:
        src_path = os.path.join(SRC_DIR, js)
        out_path = os.path.join(OUT_DIR, js)
        if os.path.exists(src_path):
            print(f"Obfuscating {js}...")
            cmd = (
                f"npx javascript-obfuscator {src_path} "
                f"--output {out_path} "
                f"--compact true "
                f"--identifier-names-generator hexadecimal "
                f"--string-array true "
                f"--string-array-encoding base64 "
                f"--unicode-escape-sequence false"
            )
            run_command(cmd)

    # 3. Minify CSS
    for css in CSS_FILES:
        src_path = os.path.join(SRC_DIR, css)
        out_path = os.path.join(OUT_DIR, css)
        if os.path.exists(src_path):
            print(f"Minifying CSS {css}...")
            cmd = f"npx clean-css-cli -o {out_path} {src_path}"
            run_command(cmd)

    # 4. Obfuscate HTML
    for html in HTML_FILES:
        src_path = os.path.join(SRC_DIR, html)
        out_path = os.path.join(OUT_DIR, html)
        if os.path.exists(src_path):
            print(f"Minifying HTML {html}...")
            # Advanced HTML Minification removes comments, collapses whitespace, 
            # minifies inline JS/CSS, and removes optional tags
            cmd = (
                f"npx html-minifier-terser {src_path} "
                f"-o {out_path} "
                f"--collapse-whitespace "
                f"--remove-comments "
                f"--minify-css true "
                f"--minify-js true "
                f"--remove-script-type-attributes "
                f"--remove-style-link-type-attributes "
                f"--remove-attribute-quotes"
            )
            run_command(cmd)
                
    # 5. Copy extra directories
    for d in COPY_DIRS:
        if os.path.exists(d):
            dest = os.path.join(OUT_DIR, d)
            if os.path.exists(dest):
                shutil.rmtree(dest)
            print(f"Copying directory {d}...")
            shutil.copytree(d, dest)

    print("--- Build Complete! ---")
    print(f"Production files are now in the '{OUT_DIR}' folder.")
    print("Original files are safe in the 'src' folder.")

if __name__ == "__main__":
    if "--setup" in sys.argv:
        setup_src()
    else:
        build()
