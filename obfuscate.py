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

    # 3. CSS -> JS
    import base64
    import re
    
    for css in CSS_FILES:
        src_path = os.path.join(SRC_DIR, css)
        temp_css = os.path.join(OUT_DIR, "temp_" + css)
        out_js = os.path.join(OUT_DIR, css + ".js")
        if os.path.exists(src_path):
            print(f"Obfuscating CSS {css} via JS wrapper...")
            cmd = f"npx clean-css-cli -o {temp_css} {src_path}"
            run_command(cmd)
            with open(temp_css, "r", encoding="utf-8") as f:
                min_css = f.read()
            os.remove(temp_css)
            # Encode in base64
            b64_css = base64.b64encode(min_css.encode('utf-8')).decode('utf-8')
            js_content = f"var s=document.createElement('style');s.innerHTML=decodeURIComponent(escape(window.atob('{b64_css}')));document.head.appendChild(s);"
            temp_js = os.path.join(OUT_DIR, "temp_" + css + ".js")
            with open(temp_js, "w", encoding="utf-8") as f:
                f.write(js_content)
            run_command(f"npx javascript-obfuscator {temp_js} --output {out_js} --compact true")
            os.remove(temp_js)

    # 4. Obfuscate HTML
    for html in HTML_FILES:
        src_path = os.path.join(SRC_DIR, html)
        out_path = os.path.join(OUT_DIR, html)
        if os.path.exists(src_path):
            print(f"Minifying and Obfuscating HTML {html}...")
            # Run minifier
            cmd = (
                f"npx html-minifier-terser {src_path} "
                f"-o {out_path} "
                f"--collapse-whitespace --remove-comments "
                f"--minify-js true --remove-attribute-quotes"
            )
            run_command(cmd)
            
            with open(out_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Replace CSS links with JS script tags
            for css in CSS_FILES:
                pattern = re.compile(rf'<link[^>]*href=["\']?{css}["\']?[^>]*>', re.IGNORECASE)
                content = pattern.sub(f"<script src='{css}.js'></script>", content)

            # Extract body and remove it from main html
            body_match = re.search(r'(<body.*</body>)', content, flags=re.IGNORECASE|re.DOTALL)
            head_match = re.search(r'(<head>.*</head>)', content, flags=re.IGNORECASE|re.DOTALL)
            
            if body_match and head_match:
                head = head_match.group(1)
                body = body_match.group(1)
                
                # Encode body
                b64_body = base64.b64encode(body.encode('utf-8')).decode('utf-8')
                body_js = f"document.write(decodeURIComponent(escape(window.atob('{b64_body}'))));"
                
                temp_js = os.path.join(OUT_DIR, "html_body.js")
                with open(temp_js, "w", encoding="utf-8") as f:
                    f.write(body_js)
                    
                body_obf_name = f"body_{html}.js"
                out_js = os.path.join(OUT_DIR, body_obf_name)
                run_command(f"npx javascript-obfuscator {temp_js} --output {out_js} --compact true")
                os.remove(temp_js)
                
                # Final HTML
                new_html = f"<!DOCTYPE html><html lang='it'>{head}<script src='{body_obf_name}'></script></html>"
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(new_html)
            else:
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(content)
              
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
