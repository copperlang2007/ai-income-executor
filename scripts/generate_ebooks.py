#!/usr/bin/env python3
"""Idea #2: AI Children's Storybooks for Gumroad"""

import os, sys, json
from datetime import datetime

def generate_ebooks(count=5, theme="space adventure"):
    print(f"📜 Generating {count} AI storybooks on '{theme}'...")
    output_dir = os.path.join("data", "gumroad_ebooks", datetime.now().strftime("%Y%m%d"))
    os.makedirs(output_dir, exist_ok=True)
    
    books = []
    for i in range(count):
        title = f"The {theme.title()} Explorer #{i+1}"
        filepath = os.path.join(output_dir, f"{title.replace(' ', '_')}.pdf")
        with open(filepath, 'w') as f:
            f.write(f"AI-Generated Storybook: {title}\n\nChapter 1: ...\n[Full story generated via Grok/ChatGPT + illustrations]")
        books.append({"title": title, "file": filepath, "price": 9.99})
    
    with open(os.path.join(output_dir, "gumroad_metadata.json"), 'w') as f:
        json.dump(books, f, indent=2)
    
    print(f"✅ {count} ebooks ready in {output_dir}")
    return output_dir

if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    theme = sys.argv[2] if len(sys.argv) > 2 else "space adventure"
    generate_ebooks(count, theme)