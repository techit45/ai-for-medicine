"""
เครื่องคำนวณดัชนีมวลกาย (BMI Calculator) พร้อมคำแนะนำสุขภาพ
ตัวอย่าง AI ทางการแพทย์อย่างง่ายสำหรับนักเรียนมัธยม
"""

import matplotlib.pyplot as plt
import numpy as np

class BMICalculator:
    def __init__(self):
        # เกณฑ์ BMI ตามมาตรฐานองค์การอนามัยโลก (WHO)
        self.bmi_categories = {
            "น้ำหนักน้อยกว่าเกณฑ์": {"min": 0, "max": 18.5, "color": "#87CEEB"},
            "น้ำหนักปกติ": {"min": 18.5, "max": 25, "color": "#90EE90"},
            "น้ำหนักเกิน": {"min": 25, "max": 30, "color": "#FFD700"},
            "อ้วนระดับ 1": {"min": 30, "max": 35, "color": "#FFA500"},
            "อ้วนระดับ 2": {"min": 35, "max": 40, "color": "#FF6347"},
            "อ้วนระดับ 3": {"min": 40, "max": 50, "color": "#FF0000"}
        }
        
        # คำแนะนำสุขภาพ
        self.health_advice = {
            "น้ำหนักน้อยกว่าเกณฑ์": {
                "advice": "ควรเพิ่มน้ำหนักให้อยู่ในเกณฑ์ปกติ",
                "recommendations": [
                    "กินอาหารครบ 5 หมู่ เพิ่มปริมาณอาหารต่อมื้อ",
                    "เน้นโปรตีนคุณภาพดี เช่น ไข่ เนื้อ ปลา ถั่ว",
                    "ออกกำลังกายแบบสร้างกล้ามเนื้อ",
                    "นอนหับให้เพียงพอ 7-8 ชั่วโมงต่อวัน",
                    "หากน้ำหนักยังไม่เพิ่ม ควรปรึกษาแพทย์"
                ]
            },
            "น้ำหนักปกติ": {
                "advice": "ยอดเยี่ยม! น้ำหนักของคุณอยู่ในเกณฑ์ที่เหมาะสม",
                "recommendations": [
                    "รักษาน้ำหนักปัจจุบันด้วยการกินอาหารสมดุล",
                    "ออกกำลังกายสม่ำเสมอ อย่างน้อย 150 นาทีต่อสัปดาห์",
                    "ดื่มน้ำ 8-10 แก้วต่อวัน",
                    "หลีกเลี่ยงอาหารขยะและน้ำตาลมากเกินไป",
                    "ตรวจสุขภาพประจำปี"
                ]
            },
            "น้ำหนักเกิน": {
                "advice": "ควรลดน้ำหนักเล็กน้อยเพื่อสุขภาพที่ดี",
                "recommendations": [
                    "ลดแคลอรี่วันละ 300-500 แคลอรี่",
                    "เพิ่มการออกกำลังกาย 30-45 นาทีต่อวัน",
                    "กินผักผลไม้มากขึ้น ลดอาหารทอดและหวาน",
                    "ดื่มน้ำก่อนอาหาร เพิ่มความรู้สึกอิ่ม",
                    "ติดตามน้ำหนักสัปดาห์ละครั้ง"
                ]
            },
            "อ้วนระดับ 1": {
                "advice": "ควรลดน้ำหนักอย่างจริงจัง เสี่ยงต่อโรคเรื้อรัง",
                "recommendations": [
                    "วางเป้าลดน้ำหนัก 5-10% ของน้ำหนักปัจจุบัน",
                    "ออกกำลังกาย 45-60 นาทีต่อวัน",
                    "ควบคุมอาหาร เน้นผัก โปรตีน ลดแป้งและน้ำตาล",
                    "หาการสนับสนุนจากครอบครัวและเพื่อน",
                    "ปรึกษานักโภชนาการ"
                ]
            },
            "อ้วนระดับ 2": {
                "advice": "ควรลดน้ำหนักด่วน! เสี่ยงสูงต่อโรคร้ายแรง",
                "recommendations": [
                    "ปรึกษาแพทย์เพื่อวางแผนลดน้ำหนักอย่างปลอดภัย",
                    "อาจต้องการการรักษาทางการแพทย์ร่วมด้วย",
                    "ออกกำลังกายภายใต้การดูแลของผู้เชี่ยวชาญ",
                    "ปรับเปลี่ยนวิถีชีวิตอย่างเข้มข้น",
                    "ตรวจสุขภาพเป็นประจำ"
                ]
            },
            "อ้วนระดับ 3": {
                "advice": "อันตราย! ควรพบแพทย์ทันทีเพื่อการรักษา",
                "recommendations": [
                    "พบแพทย์ผู้เชี่ยวชาญด้านโรคอ้วนทันที",
                    "อาจต้องพิจารณาการผ่าตัดลดน้ำหนัก",
                    "รักษาภาวะแทรกซ้อนที่อาจเกิดขึ้น",
                    "ได้รับการดูแลจากทีมแพทย์หลายสาขา",
                    "ปรับเปลี่ยนชีวิตอย่างครอบคลุม"
                ]
            }
        }
    
    def calculate_bmi(self, weight, height):
        """คำนวณค่า BMI"""
        height_m = height / 100  # แปลงจาก cm เป็น m
        bmi = weight / (height_m ** 2)
        return round(bmi, 1)
    
    def get_bmi_category(self, bmi):
        """หาหมวดหมู่ BMI"""
        for category, range_data in self.bmi_categories.items():
            if range_data["min"] <= bmi < range_data["max"]:
                return category
        return "อ้วนระดับ 3"  # สำหรับกรณี BMI > 40
    
    def calculate_ideal_weight(self, height):
        """คำนวณน้ำหนักที่เหมาะสม"""
        height_m = height / 100
        # ใช้ BMI 22 เป็นค่ากลางของน้ำหนักปกติ
        ideal_weight = 22 * (height_m ** 2)
        return round(ideal_weight, 1)
    
    def analyze_health(self, weight, height, age, gender):
        """วิเคราะห์สุขภาพโดยรวม"""
        bmi = self.calculate_bmi(weight, height)
        category = self.get_bmi_category(bmi)
        ideal_weight = self.calculate_ideal_weight(height)
        weight_diff = weight - ideal_weight
        
        # ข้อมูลเพิ่มเติมตามเพศและอายุ
        health_risks = []
        if category in ["อ้วนระดับ 1", "อ้วนระดับ 2", "อ้วนระดับ 3"]:
            health_risks = [
                "โรคเบาหวานประเภท 2",
                "โรคหัวใจและหลอดเลือด",
                "ความดันโลหิตสูง",
                "โรคไขมันในเลือดสูง",
                "โรคข้อเข่าเสื่อม"
            ]
        elif category == "น้ำหนักน้อยกว่าเกณฑ์":
            health_risks = [
                "ภูมิต้านทานต่ำ",
                "โรคกระดูกพรุน",
                "ขาดสารอาหาร",
                "การเจริญเติบโตผิดปกติ"
            ]
        
        return {
            "bmi": bmi,
            "category": category,
            "ideal_weight": ideal_weight,
            "weight_diff": weight_diff,
            "health_risks": health_risks,
            "advice": self.health_advice[category]
        }
    
    def create_bmi_chart(self, bmi, category):
        """สร้างกราฟแสดงตำแหน่ง BMI"""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # สร้างแถบสี BMI
        categories = list(self.bmi_categories.keys())
        ranges = [self.bmi_categories[cat]["max"] for cat in categories[:-1]] + [45]
        colors = [self.bmi_categories[cat]["color"] for cat in categories]
        
        # วาดแถบสี
        prev_val = 0
        for i, (cat, next_val) in enumerate(zip(categories, ranges)):
            ax.barh(0, next_val - prev_val, left=prev_val, height=0.5, 
                   color=colors[i], alpha=0.7, label=cat)
            prev_val = next_val
        
        # ทำเครื่องหมายตำแหน่ง BMI ของผู้ใช้
        ax.plot(bmi, 0, 'ro', markersize=15, label=f'BMI ของคุณ: {bmi}')
        ax.annotate(f'BMI: {bmi}\n{category}', xy=(bmi, 0), xytext=(bmi, 0.3),
                   ha='center', va='bottom', fontsize=12, fontweight='bold',
                   arrowprops=dict(arrowstyle='->', color='red', lw=2))
        
        ax.set_xlim(15, 45)
        ax.set_ylim(-0.5, 0.8)
        ax.set_xlabel('ค่า BMI', fontsize=12)
        ax.set_title('ตำแหน่งค่า BMI ของคุณ', fontsize=14, fontweight='bold')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(True, alpha=0.3)
        
        # ซ่อนแกน Y
        ax.set_yticks([])
        
        plt.tight_layout()
        plt.show()

def main():
    print("\n🏥 เครื่องคำนวณดัชนีมวลกาย (BMI Calculator)")
    print("    พร้อมระบบวิเคราะห์สุขภาพด้วย AI")
    print("-" * 60)
    
    calculator = BMICalculator()
    
    try:
        # รับข้อมูลจากผู้ใช้
        print("\n📝 กรุณากรอกข้อมูลของคุณ:")
        weight = float(input("   น้ำหนัก (กิโลกรัม): "))
        height = float(input("   ส่วนสูง (เซนติเมตร): "))
        age = int(input("   อายุ (ปี): "))
        gender = input("   เพศ (ชาย/หญิง): ").strip()
        
        # ตรวจสอบข้อมูล
        if weight <= 0 or height <= 0 or age <= 0:
            print("❌ ข้อมูลไม่ถูกต้อง กรุณากรอกตัวเลขที่มากกว่า 0")
            return
        
        # วิเคราะห์ผล
        result = calculator.analyze_health(weight, height, age, gender)
        
        # แสดงผล
        print("\n" + "="*60)
        print("📊 ผลการวิเคราะห์ BMI และสุขภาพ")
        print("="*60)
        
        print(f"\n👤 ข้อมูลส่วนตัว:")
        print(f"   น้ำหนัก: {weight} กก.")
        print(f"   ส่วนสูง: {height} ซม.")
        print(f"   อายุ: {age} ปี")
        print(f"   เพศ: {gender}")
        
        print(f"\n📈 ผลการคำนวณ:")
        print(f"   ค่า BMI: {result['bmi']}")
        print(f"   หมวดหมู่: {result['category']}")
        print(f"   น้ำหนักที่เหมาะสม: {result['ideal_weight']} กก.")
        
        if result['weight_diff'] > 0:
            print(f"   น้ำหนักเกิน: +{result['weight_diff']:.1f} กก.")
        elif result['weight_diff'] < 0:
            print(f"   น้ำหนักต่ำกว่าเกณฑ์: {result['weight_diff']:.1f} กก.")
        else:
            print(f"   น้ำหนักเหมาะสม ✅")
        
        print(f"\n💡 คำแนะนำ: {result['advice']['advice']}")
        
        print(f"\n📋 แนวทางปฏิบัติ:")
        for i, rec in enumerate(result['advice']['recommendations'], 1):
            print(f"   {i}. {rec}")
        
        if result['health_risks']:
            print(f"\n⚠️  ความเสี่ยงต่อโรค:")
            for risk in result['health_risks']:
                print(f"   • {risk}")
        
        print("\n" + "="*60)
        print("📊 ต้องการดูกราฟ BMI หรือไม่? (y/n)")
        show_chart = input("   คำตอบ: ").strip().lower()
        
        if show_chart in ['y', 'yes', 'ใช่']:
            calculator.create_bmi_chart(result['bmi'], result['category'])
        
        print("\n✨ ขอบคุณที่ใช้บริการ! จำไว้ว่าสุขภาพดีเริ่มต้นจากการดูแลตัวเอง")
        
    except ValueError:
        print("❌ กรุณากรอกตัวเลขที่ถูกต้อง")
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")

if __name__ == "__main__":
    main()