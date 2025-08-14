"""
เครื่องวิเคราะห์อัตราการเต้นหัวใจ (Heart Rate Analyzer)
ตัวอย่าง AI ทางการแพทย์อย่างง่ายสำหรับนักเรียนมัธยม
"""

import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime, timedelta

class HeartRateAnalyzer:
    def __init__(self):
        # เกณฑ์อัตราการเต้นหัวใจตามอายุ (ครั้งต่อนาที)
        self.heart_rate_zones = {
            "เด็ก (6-12 ปี)": {
                "resting": {"min": 70, "max": 120},
                "normal": {"min": 80, "max": 115},
                "exercise": {"min": 150, "max": 190}
            },
            "วัยรุ่น (13-18 ปี)": {
                "resting": {"min": 60, "max": 100},
                "normal": {"min": 70, "max": 95},
                "exercise": {"min": 140, "max": 180}
            },
            "ผู้ใหญ่ (19-64 ปี)": {
                "resting": {"min": 60, "max": 100},
                "normal": {"min": 65, "max": 85},
                "exercise": {"min": 120, "max": 170}
            },
            "ผู้สูงอายุ (65+ ปี)": {
                "resting": {"min": 60, "max": 100},
                "normal": {"min": 65, "max": 85},
                "exercise": {"min": 100, "max": 140}
            }
        }
        
        # การจำแนกสถานะ
        self.status_categories = {
            "ช้ามาก": {"color": "#87CEEB", "advice": "อาจมีปัญหาระบบหัวใจ ควรพบแพทย์"},
            "ช้า": {"color": "#90EE90", "advice": "ปกติสำหรับนักกีฬาหรือคนออกกำลังกายเป็นประจำ"},
            "ปกติ": {"color": "#98FB98", "advice": "อัตราการเต้นหัวใจปกติดี"},
            "เร็วเล็กน้อย": {"color": "#FFD700", "advice": "อาจเกิดจากความเครียด กาแฟ หรือการออกกำลังกาย"},
            "เร็ว": {"color": "#FFA500", "advice": "ควรพักผ่อน หลีกเลี่ยงสิ่งกระตุ้น"},
            "เร็วมาก": {"color": "#FF6347", "advice": "ควรพบแพทย์ทันที อาจเป็นอันตราย"}
        }
    
    def get_age_group(self, age):
        """กำหนดกลุ่มอายุ"""
        if 6 <= age <= 12:
            return "เด็ก (6-12 ปี)"
        elif 13 <= age <= 18:
            return "วัยรุ่น (13-18 ปี)"
        elif 19 <= age <= 64:
            return "ผู้ใหญ่ (19-64 ปี)"
        else:
            return "ผู้สูงอายุ (65+ ปี)"
    
    def analyze_heart_rate(self, heart_rate, age, activity_level="resting"):
        """วิเคราะห์อัตราการเต้นหัวใจ"""
        age_group = self.get_age_group(age)
        normal_range = self.heart_rate_zones[age_group][activity_level]
        
        # จำแนกสถานะ
        if heart_rate < normal_range["min"] - 20:
            status = "ช้ามาก"
        elif heart_rate < normal_range["min"]:
            status = "ช้า"
        elif normal_range["min"] <= heart_rate <= normal_range["max"]:
            status = "ปกติ"
        elif heart_rate <= normal_range["max"] + 20:
            status = "เร็วเล็กน้อย"
        elif heart_rate <= normal_range["max"] + 40:
            status = "เร็ว"
        else:
            status = "เร็วมาก"
        
        # คำนวณ Max Heart Rate ตามสูตร 220 - อายุ
        max_hr = 220 - age
        target_zone_low = int(max_hr * 0.5)  # 50% ของ Max HR
        target_zone_high = int(max_hr * 0.85)  # 85% ของ Max HR
        
        return {
            "status": status,
            "age_group": age_group,
            "normal_range": normal_range,
            "max_hr": max_hr,
            "target_zone": {"low": target_zone_low, "high": target_zone_high},
            "advice": self.status_categories[status]["advice"],
            "color": self.status_categories[status]["color"]
        }
    
    def generate_sample_data(self, duration_hours=24):
        """สร้างข้อมูลตัวอย่างอัตราการเต้นหัวใจ 24 ชั่วโมง"""
        times = []
        heart_rates = []
        
        base_time = datetime.now() - timedelta(hours=duration_hours)
        
        for i in range(duration_hours * 4):  # ทุก 15 นาที
            time = base_time + timedelta(minutes=i * 15)
            times.append(time)
            
            # จำลองรูปแบบการเต้นหัวใจตามเวลา
            hour = time.hour
            
            if 0 <= hour <= 6:  # นอนหลับ
                hr = random.randint(55, 70)
            elif 7 <= hour <= 8:  # ตื่นนอน
                hr = random.randint(70, 85)
            elif 9 <= hour <= 11:  # ทำงาน/เรียน
                hr = random.randint(75, 90)
            elif 12 <= hour <= 13:  # พักเที่ยง
                hr = random.randint(80, 95)
            elif 14 <= hour <= 17:  # ทำงาน/เรียนต่อ
                hr = random.randint(75, 90)
            elif 18 <= hour <= 19:  # ออกกำลังกาย
                hr = random.randint(120, 160)
            elif 20 <= hour <= 22:  # พักผ่อน
                hr = random.randint(70, 85)
            else:  # เตรียมนอน
                hr = random.randint(65, 80)
            
            # เพิ่มความสุ่มเล็กน้อย
            hr += random.randint(-5, 5)
            heart_rates.append(max(50, min(200, hr)))  # จำกัดค่าให้อยู่ในช่วงที่เป็นไปได้
        
        return times, heart_rates
    
    def plot_heart_rate_trend(self, times, heart_rates, age):
        """สร้างกราฟแนวโน้มอัตราการเต้นหัวใจ"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # กราฟแนวโน้ม 24 ชั่วโมง
        ax1.plot(times, heart_rates, color='red', linewidth=2, marker='o', markersize=3)
        ax1.set_title('อัตราการเต้นหัวใจใน 24 ชั่วโมง', fontsize=14, fontweight='bold')
        ax1.set_xlabel('เวลา')
        ax1.set_ylabel('อัตราการเต้นหัวใจ (ครั้ง/นาที)')
        ax1.grid(True, alpha=0.3)
        
        # เส้นแสดงโซนปกติ
        age_group = self.get_age_group(age)
        normal_range = self.heart_rate_zones[age_group]["resting"]
        ax1.axhline(y=normal_range["min"], color='green', linestyle='--', alpha=0.7, label='ขีดจำกัดล่าง')
        ax1.axhline(y=normal_range["max"], color='green', linestyle='--', alpha=0.7, label='ขีดจำกัดบน')
        ax1.fill_between(times, normal_range["min"], normal_range["max"], alpha=0.2, color='green', label='โซนปกติ')
        ax1.legend()
        
        # ฮิสโตแกรมการกระจายของข้อมูล
        ax2.hist(heart_rates, bins=20, color='skyblue', alpha=0.7, edgecolor='black')
        ax2.set_title('การกระจายของอัตราการเต้นหัวใจ', fontsize=14, fontweight='bold')
        ax2.set_xlabel('อัตราการเต้นหัวใจ (ครั้ง/นาที)')
        ax2.set_ylabel('จำนวนครั้ง')
        ax2.axvline(x=np.mean(heart_rates), color='red', linestyle='-', linewidth=2, label=f'ค่าเฉลี่ย: {np.mean(heart_rates):.1f}')
        ax2.axvline(x=normal_range["min"], color='green', linestyle='--', alpha=0.7)
        ax2.axvline(x=normal_range["max"], color='green', linestyle='--', alpha=0.7)
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
    
    def create_heart_rate_zones_chart(self, age):
        """สร้างกราฟแสดงโซนการเต้นหัวใจ"""
        max_hr = 220 - age
        zones = {
            "โซนฟื้นฟู (50-60%)": {"min": max_hr * 0.5, "max": max_hr * 0.6, "color": "#87CEEB"},
            "โซนเผาผลาญไขมัน (60-70%)": {"min": max_hr * 0.6, "max": max_hr * 0.7, "color": "#90EE90"},
            "โซนแอโรบิก (70-80%)": {"min": max_hr * 0.7, "max": max_hr * 0.8, "color": "#FFD700"},
            "โซนแอนแอโรบิก (80-90%)": {"min": max_hr * 0.8, "max": max_hr * 0.9, "color": "#FFA500"},
            "โซนขีดจำกัด (90-100%)": {"min": max_hr * 0.9, "max": max_hr, "color": "#FF6347"}
        }
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # วาดแถบสี
        for i, (zone_name, zone_data) in enumerate(zones.items()):
            width = zone_data["max"] - zone_data["min"]
            ax.barh(i, width, left=zone_data["min"], height=0.6, 
                   color=zone_data["color"], alpha=0.8, label=zone_name)
            
            # ใส่ข้อความในแถบ
            center = (zone_data["min"] + zone_data["max"]) / 2
            ax.text(center, i, f'{int(zone_data["min"])}-{int(zone_data["max"])}', 
                   ha='center', va='center', fontweight='bold')
        
        ax.set_xlim(0, max_hr + 20)
        ax.set_ylim(-0.5, len(zones) - 0.5)
        ax.set_xlabel('อัตราการเต้นหัวใจ (ครั้ง/นาที)', fontsize=12)
        ax.set_title(f'โซนการเต้นหัวใจสำหรับอายุ {age} ปี (Max HR: {max_hr})', fontsize=14, fontweight='bold')
        ax.set_yticks(range(len(zones)))
        ax.set_yticklabels(list(zones.keys()))
        ax.grid(True, alpha=0.3, axis='x')
        
        plt.tight_layout()
        plt.show()

def main():
    print("\n❤️  เครื่องวิเคราะห์อัตราการเต้นหัวใจ (Heart Rate Analyzer)")
    print("    ระบบ AI ตรวจสอบสุขภาพหัวใจอย่างง่าย")
    print("-" * 60)
    
    analyzer = HeartRateAnalyzer()
    
    try:
        print("\n📝 เลือกโหมดการใช้งาน:")
        print("   1. วิเคราะห์อัตราการเต้นหัวใจปัจจุบัน")
        print("   2. ดูข้อมูลตัวอย่าง 24 ชั่วโมง")
        print("   3. ดูโซนการเต้นหัวใจตามอายุ")
        
        mode = input("\n   เลือกโหมด (1-3): ").strip()
        
        if mode == "1":
            # วิเคราะห์อัตราการเต้นหัวใจปัจจุบัน
            print("\n📝 กรุณากรอกข้อมูล:")
            heart_rate = int(input("   อัตราการเต้นหัวใจปัจจุบัน (ครั้ง/นาที): "))
            age = int(input("   อายุ (ปี): "))
            
            print("\n   สถานะกิจกรรม:")
            print("   1. พักผ่อน (resting)")
            print("   2. กิจกรรมปกติ (normal)")
            print("   3. ออกกำลังกาย (exercise)")
            
            activity_choice = input("   เลือกสถานะ (1-3): ").strip()
            activity_map = {"1": "resting", "2": "normal", "3": "exercise"}
            activity_level = activity_map.get(activity_choice, "resting")
            
            # วิเคราะห์ผล
            result = analyzer.analyze_heart_rate(heart_rate, age, activity_level)
            
            # แสดงผล
            print("\n" + "="*50)
            print("📊 ผลการวิเคราะห์อัตราการเต้นหัวใจ")
            print("="*50)
            
            print(f"\n👤 ข้อมูลพื้นฐาน:")
            print(f"   อายุ: {age} ปี")
            print(f"   กลุ่มอายุ: {result['age_group']}")
            print(f"   อัตราการเต้นหัวใจสูงสุด: {result['max_hr']} ครั้ง/นาที")
            
            print(f"\n💓 ผลการวิเคราะห์:")
            print(f"   อัตราการเต้นหัวใจ: {heart_rate} ครั้ง/นาที")
            print(f"   สถานะ: {result['status']}")
            print(f"   ช่วงปกติ: {result['normal_range']['min']}-{result['normal_range']['max']} ครั้ง/นาที")
            print(f"   โซนเป้าหมายการออกกำลังกาย: {result['target_zone']['low']}-{result['target_zone']['high']} ครั้ง/นาที")
            
            print(f"\n💡 คำแนะนำ: {result['advice']}")
            
        elif mode == "2":
            # แสดงข้อมูลตัวอย่าง 24 ชั่วโมง
            age = int(input("\n   อายุ (ปี): "))
            
            print("\n🔄 กำลังสร้างข้อมูลตัวอย่าง...")
            times, heart_rates = analyzer.generate_sample_data()
            
            # สถิติเบื้องต้น
            avg_hr = np.mean(heart_rates)
            min_hr = np.min(heart_rates)
            max_hr = np.max(heart_rates)
            
            print(f"\n📊 สถิติในช่วง 24 ชั่วโมง:")
            print(f"   ค่าเฉลี่ย: {avg_hr:.1f} ครั้ง/นาที")
            print(f"   ต่ำสุด: {min_hr} ครั้ง/นาที")
            print(f"   สูงสุด: {max_hr} ครั้ง/นาที")
            
            # แสดงกราฟ
            analyzer.plot_heart_rate_trend(times, heart_rates, age)
            
        elif mode == "3":
            # แสดงโซนการเต้นหัวใจ
            age = int(input("\n   อายุ (ปี): "))
            analyzer.create_heart_rate_zones_chart(age)
            
        else:
            print("❌ กรุณาเลือกโหมดที่ถูกต้อง (1-3)")
            return
        
        print("\n✨ ขอบคุณที่ใช้บริการ! การติดตามอัตราการเต้นหัวใจช่วยดูแลสุขภาพหัวใจของคุณ")
        
    except ValueError:
        print("❌ กรุณากรอกตัวเลขที่ถูกต้อง")
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")

if __name__ == "__main__":
    main()