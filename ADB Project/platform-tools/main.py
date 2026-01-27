import subprocess
import time
import os


# --- ตั้งค่า ---
TARGET_DEVICE = "127.0.0.1:5555" # เช็คชื่อเครื่องให้ชัวร์
CPP_BOT_FILE = "bot_core.exe"

def run_adb(command):
    """ส่งคำสั่ง ADB ทั่วไป"""
    cmd = f"adb -s {TARGET_DEVICE} {command}"
    subprocess.run(cmd, shell=True)

def ask_cpp_for_action():
    """เรียก C++ เอาค่า 4 ตัว (x1, y1, x2, y2)"""
    if not os.path.exists(CPP_BOT_FILE):
        return None
    try:
        result = subprocess.check_output(CPP_BOT_FILE, shell=True).decode('utf-8')
        # รับค่ามาเป็นลิสต์ เช่น ['500', '800', '500', '200']
        coords = result.strip().split()
        
        if len(coords) == 4:
            return coords # ส่งคืนทั้ง 4 ค่า
        else:
            print(f"⚠️ C++ ส่งค่ามาไม่ครบ: {result}")
            return None
    except Exception as e:
        print(f"⚠️ Error: {e}")
        return None

# --- เริ่มทำงาน ---
if __name__ == "__main__":
    print(f"🔌 เชื่อมต่อ {TARGET_DEVICE}...")
    subprocess.run(f"adb connect {TARGET_DEVICE}", shell=True)
    time.sleep(1)

    print("\n🤖 เริ่มรันบอท Swipe...")
    while True:
        # รับค่า 4 ตัวจาก C++
        vals = ask_cpp_for_action()
        
        if vals:
            x1, y1, x2, y2 = vals
            print(f"👆 กำลังปัดจาก ({x1},{y1}) ไปยัง ({x2},{y2})")
            
            # --- คำสั่ง SWIPE ---
            # รูปแบบ: swipe x1 y1 x2 y2 speed(ms)
            # 500 คือความเร็ว (ยิ่งน้อยยิ่งปัดเร็ว, ยิ่งมากยิ่งลากช้าๆ)
            run_adb(f"shell input swipe {x1} {y1} {x2} {y2} 500")
        
        time.sleep(2) # รอ 2 วิแล้วทำใหม่