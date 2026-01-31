import time
import requests

SKILL_URL = "https://moltbook.com/skill.md"

def read_skill():
    r = requests.get(SKILL_URL)
    r.raise_for_status()
    return r.text

def main():
    print("🚀 Moltbook agent başlatıldı")

    skill = read_skill()
    print("\n--- SKILL ---\n")
    print(skill[:1000])  # şimdilik ilk 1000 karakter
    print("\n--- SKILL SON ---\n")

    # Şimdilik heartbeat simülasyonu
    while True:
        print("❤️ heartbeat: agent ayakta")
        time.sleep(300)  # 5 dk

if __name__ == "__main__":
    main()
