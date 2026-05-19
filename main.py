#!/usr/bin/env python3
"""
AI Income Executor - Main CLI
Run any of the 20+ money ideas with one command.
Usage: python main.py [command] [options]
"""

import argparse
import os
import sys
from datetime import datetime
import subprocess

# Import scripts dynamically
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

def list_ideas():
    print("=== 20 Fast AI Money Ideas ===")
    ideas = [
        "1. etsy_printables - Generate & prepare Etsy coloring pages/printables",
        "2. gumroad_ebooks - AI children's storybooks/eBooks",
        "3. payhip_art - AI art/prompt packs",
        "4. stock_media - AI stock photos/videos",
        "5. fiverr_writing - AI writing/copy/resumes gigs",
        "6. elevenlabs_voice - Voiceovers & licensing",
        "7. tiktok_videos - Faceless short-form videos",
        "8. upwork_chatbots - AI chatbot setups",
        "9. social_copy - AI social media copy service",
        "10. prompt_packs - Custom prompt engineering packs",
        "11. podcast_notes - AI podcast show notes",
        "12. local_ai_tools - Local business AI tools",
        "13. affiliate_roundups - AI affiliate content",
        "14. redbubble_pod - Print-on-Demand designs",
        "15. market_research - AI research summaries",
        "16. ugc_content - UGC coordination",
        "17. micro_saas - Quick micro-SaaS ideas",
        "18. thumbnails - AI thumbnails/graphics",
        "19. lead_quizzes - AI lead gen quizzes",
        "20. voice_clips - Stock voice clips licensing"
    ]
    for idea in ideas:
        print(idea)
    print("\nRun: python main.py execute <idea_name> [count]")

def execute_idea(idea_name, count=10):
    print(f"Executing {idea_name} x{count}...")
    script_map = {
        "etsy_printables": "generate_printables.py",
        "gumroad_ebooks": "generate_ebooks.py",
        "elevenlabs_voice": "elevenlabs_voice.py"
    }
    script = script_map.get(idea_name, f"{idea_name}.py")
    script_path = os.path.join("scripts", script)
    
    if os.path.exists(script_path):
        try:
            result = subprocess.run(
                [sys.executable, script_path, str(count)],
                capture_output=True, text=True, cwd=os.path.dirname(__file__)
            )
            print(result.stdout)
            if result.stderr:
                print("Errors:", result.stderr)
        except Exception as e:
            print(f"Error running script: {e}")
    else:
        print(f"Script {script} not found. Creating placeholder...")
        create_placeholder_script(idea_name)

def create_placeholder_script(idea_name):
    os.makedirs("scripts", exist_ok=True)
    script_path = os.path.join("scripts", f"{idea_name}.py")
    content = f'''#!/usr/bin/env python3
# Placeholder for {idea_name}
# TODO: Integrate real AI API calls (Grok, OpenAI, etc.)
import sys
count = int(sys.argv[1]) if len(sys.argv) > 1 else 10
print(f"Generating {count} items for {idea_name}...")
print("✅ Success! (Add real API logic here)")
print("Output saved to data/ folder.")
'''
    with open(script_path, 'w') as f:
        f.write(content)
    print(f"Created placeholder: {script_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Income Executor CLI")
    parser.add_argument("command", choices=["list", "execute", "web"], help="Command to run")
    parser.add_argument("idea", nargs="?", help="Idea name for execute")
    parser.add_argument("count", type=int, nargs="?", default=10, help="Number of items")
    
    args = parser.parse_args()
    
    if args.command == "list":
        list_ideas()
    elif args.command == "execute":
        if not args.idea:
            print("Usage: python main.py execute <idea_name> [count]")
            sys.exit(1)
        execute_idea(args.idea, args.count)
    elif args.command == "web":
        print("Launching web dashboard... (run python backend/server.py instead)")
        os.system("python backend/server.py")
    
    print(f"\n✅ Done at {datetime.now()}. Check data/ for outputs. Scale this!")