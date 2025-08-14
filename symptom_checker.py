"""
ระบบตรวจสอบอาการเบื้องต้น (Simple Symptom Checker)
ตัวอย่าง AI ทางการแพทย์อย่างง่ายสำหรับนักเรียนมัธยม
"""

class SymptomChecker:
    def __init__(self):
        # ฐานข้อมูลโรคและอาการ (แบบง่าย)
        self.diseases = {
            "ไข้หวัด": {
                "symptoms": ["ไข้", "ไอ", "น้ำมูกไหล", "เจ็บคอ", "ปวดศีรษะ"],
                "severity": "เล็กน้อย",
                "advice": "พักผ่อน ดื่มน้ำมากๆ กินยาลดไข้ หากอาการไม่ดีขึ้นใน 3 วัน ควรพบแพทย์"
            },
            "ไข้เลือดออก": {
                "symptoms": ["ไข้สูง", "ปวดศีรษะ", "ปวดกล้ามเนื้อ", "ผื่นแดง", "เลือดออกง่าย"],
                "severity": "รุนแรง",
                "advice": "ควรพบแพทย์ทันที! ดื่มน้ำมากๆ ห้ามกินยาแอสไพริน"
            },
            "ภูมิแพ้": {
                "symptoms": ["จาม", "น้ำมูกไหล", "คันตา", "คันจมูก"],
                "severity": "เล็กน้อย",
                "advice": "หลีกเลี่ยงสิ่งที่ทำให้แพ้ กินยาแก้แพ้ ล้างหน้าและมือบ่อยๆ"
            },
            "ไข้หวัดใหญ่": {
                "symptoms": ["ไข้สูง", "หนาวสั่น", "ปวดกล้ามเนื้อ", "อ่อนเพลีย", "ไอแห้ง"],
                "severity": "ปานกลาง",
                "advice": "พักผ่อนมากๆ ดื่มน้ำ กินยาลดไข้ สวมหน้ากาก หากหายใจลำบากให้พบแพทย์"
            },
            "อาหารเป็นพิษ": {
                "symptoms": ["ท้องเสีย", "อาเจียน", "ปวดท้อง", "ไข้", "คลื่นไส้"],
                "severity": "ปานกลาง",
                "advice": "ดื่มน้ำเกลือแร่ งดอาหารหนักๆ หากอาเจียนมากหรือมีเลือดปนให้พบแพทย์"
            }
        }
    
    def check_symptoms(self, user_symptoms):
        """วิเคราะห์อาการและให้คำแนะนำ"""
        possible_diseases = []
        
        # ตรวจสอบอาการกับแต่ละโรค
        for disease, info in self.diseases.items():
            # นับจำนวนอาการที่ตรงกัน
            matching_symptoms = []
            for symptom in user_symptoms:
                if symptom in info["symptoms"]:
                    matching_symptoms.append(symptom)
            
            # คำนวณเปอร์เซ็นต์ความเป็นไปได้
            if matching_symptoms:
                match_percentage = (len(matching_symptoms) / len(info["symptoms"])) * 100
                possible_diseases.append({
                    "disease": disease,
                    "percentage": match_percentage,
                    "matching_symptoms": matching_symptoms,
                    "severity": info["severity"],
                    "advice": info["advice"]
                })
        
        # เรียงลำดับตามเปอร์เซ็นต์
        possible_diseases.sort(key=lambda x: x["percentage"], reverse=True)
        
        return possible_diseases
    
    def display_results(self, results):
        """แสดงผลการวิเคราะห์"""
        if not results:
            print("\n❌ ไม่พบโรคที่ตรงกับอาการของคุณในฐานข้อมูล")
            print("💡 แนะนำ: ควรปรึกษาแพทย์เพื่อการวินิจฉัยที่แม่นยำ")
            return
        
        print("\n" + "="*50)
        print("📊 ผลการวิเคราะห์อาการเบื้องต้น")
        print("="*50)
        
        for i, result in enumerate(results[:3], 1):  # แสดงแค่ 3 อันดับแรก
            print(f"\n🔍 ความเป็นไปได้ที่ {i}:")
            print(f"   โรค: {result['disease']}")
            print(f"   ความเป็นไปได้: {result['percentage']:.1f}%")
            print(f"   อาการที่ตรงกัน: {', '.join(result['matching_symptoms'])}")
            print(f"   ระดับความรุนแรง: {result['severity']}")
            print(f"   คำแนะนำ: {result['advice']}")
        
        print("\n" + "="*50)
        print("⚠️  คำเตือน: นี่เป็นเพียงการประเมินเบื้องต้น")
        print("    ควรพบแพทย์เพื่อการวินิจฉัยที่แม่นยำ")
        print("="*50)

def main():
    print("\n🏥 ยินดีต้อนรับสู่ระบบตรวจสอบอาการเบื้องต้น")
    print("    (AI for Medicine - ตัวอย่างสำหรับนักเรียน)")
    print("-" * 50)
    
    checker = SymptomChecker()
    
    # แสดงรายการอาการที่มีในระบบ
    all_symptoms = set()
    for info in checker.diseases.values():
        all_symptoms.update(info["symptoms"])
    
    print("\n📋 อาการที่ระบบรู้จัก:")
    for i, symptom in enumerate(sorted(all_symptoms), 1):
        print(f"   {i}. {symptom}")
    
    # รับข้อมูลอาการจากผู้ใช้
    print("\n📝 กรุณาระบุอาการของคุณ")
    print("   (พิมพ์อาการแต่ละอย่างแล้วกด Enter, พิมพ์ 'จบ' เมื่อเสร็จ)")
    
    user_symptoms = []
    while True:
        symptom = input("   อาการ: ").strip()
        if symptom.lower() == 'จบ':
            break
        if symptom and symptom in all_symptoms:
            user_symptoms.append(symptom)
            print(f"   ✅ เพิ่มอาการ: {symptom}")
        elif symptom:
            print(f"   ❓ ไม่พบอาการนี้ในระบบ: {symptom}")
    
    if user_symptoms:
        print(f"\n🔍 กำลังวิเคราะห์อาการ: {', '.join(user_symptoms)}")
        results = checker.check_symptoms(user_symptoms)
        checker.display_results(results)
    else:
        print("\n❌ คุณยังไม่ได้ระบุอาการใดๆ")

if __name__ == "__main__":
    main()