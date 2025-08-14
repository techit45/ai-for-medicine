// AI for Medicine - Interactive JavaScript

// Smooth scrolling for navigation
function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Statistics counter animation
function animateCounter(element, target) {
    const increment = target / 100;
    let current = 0;
    
    const timer = setInterval(() => {
        current += increment;
        element.textContent = Math.floor(current);
        
        if (current >= target) {
            element.textContent = target;
            clearInterval(timer);
        }
    }, 20);
}

// Initialize statistics animation when in view
function initStatsAnimation() {
    const stats = document.querySelectorAll('.stat-number');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseInt(entry.target.dataset.target);
                animateCounter(entry.target, target);
                observer.unobserve(entry.target);
            }
        });
    });
    
    stats.forEach(stat => observer.observe(stat));
}

// Tab functionality for demos
function initDemoTabs() {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const demoContents = document.querySelectorAll('.demo-content');
    
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetTab = btn.dataset.tab;
            
            // Remove active class from all tabs and contents
            tabBtns.forEach(b => b.classList.remove('active'));
            demoContents.forEach(content => content.classList.remove('active'));
            
            // Add active class to clicked tab and corresponding content
            btn.classList.add('active');
            document.getElementById(targetTab).classList.add('active');
        });
    });
}

// Code tab functionality
function initCodeTabs() {
    const codeTabs = document.querySelectorAll('.code-tab-btn');
    const codeContents = document.querySelectorAll('.code-content');
    
    codeTabs.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetCode = btn.dataset.code;
            
            // Remove active class from all tabs and contents
            codeTabs.forEach(b => b.classList.remove('active'));
            codeContents.forEach(content => content.classList.remove('active'));
            
            // Add active class to clicked tab and corresponding content
            btn.classList.add('active');
            document.getElementById(targetCode + '-code').classList.add('active');
        });
    });
}

// Symptom Checker Demo
function checkSymptoms() {
    const checkboxes = document.querySelectorAll('.symptom-checkboxes input[type="checkbox"]:checked');
    const selectedSymptoms = Array.from(checkboxes).map(cb => cb.value);
    const resultDiv = document.getElementById('symptom-result');
    
    if (selectedSymptoms.length === 0) {
        resultDiv.innerHTML = '<p style="color: #e74c3c; text-align: center;">กรุณาเลือกอาการอย่างน้อย 1 อย่าง</p>';
        return;
    }
    
    // Show loading
    resultDiv.innerHTML = '<div style="text-align: center;"><div class="loading"></div> กำลังวิเคราะห์อาการ...</div>';
    
    // Simulate API call with timeout
    setTimeout(() => {
        const results = analyzeSymptoms(selectedSymptoms);
        displaySymptomResults(results);
    }, 2000);
}

function analyzeSymptoms(symptoms) {
    const diseases = {
        'ไข้หวัด': {
            symptoms: ['ไข้', 'ไอ', 'น้ำมูกไหล', 'เจ็บคอ', 'ปวดศีรษะ'],
            severity: 'เล็กน้อย',
            advice: 'พักผ่อน ดื่มน้ำมากๆ กินยาลดไข้'
        },
        'ไข้หวัดใหญ่': {
            symptoms: ['ไข้', 'ปวดกล้ามเนื้อ', 'ปวดศีรษะ', 'ไอ'],
            severity: 'ปานกลาง',
            advice: 'พักผ่อนมาก ดื่มน้ำ หากอาการรุนแรงควรพบแพทย์'
        },
        'ภูมิแพ้': {
            symptoms: ['น้ำมูกไหล', 'จาม'],
            severity: 'เล็กน้อย',
            advice: 'หลีกเลี่ยงสิ่งที่ทำให้แพ้ กินยาแก้แพ้'
        }
    };
    
    const results = [];
    
    Object.keys(diseases).forEach(disease => {
        const diseaseSymptoms = diseases[disease].symptoms;
        const matchingSymptoms = symptoms.filter(s => diseaseSymptoms.includes(s));
        
        if (matchingSymptoms.length > 0) {
            const percentage = Math.round((matchingSymptoms.length / diseaseSymptoms.length) * 100);
            results.push({
                disease,
                percentage,
                matchingSymptoms,
                severity: diseases[disease].severity,
                advice: diseases[disease].advice
            });
        }
    });
    
    return results.sort((a, b) => b.percentage - a.percentage);
}

function displaySymptomResults(results) {
    const resultDiv = document.getElementById('symptom-result');
    
    if (results.length === 0) {
        resultDiv.innerHTML = '<p style="text-align: center; color: #7f8c8d;">ไม่พบโรคที่ตรงกับอาการในฐานข้อมูล</p>';
        return;
    }
    
    let html = '<h4 style="margin-bottom: 1rem; color: #2c5aa0;">ผลการวิเคราะห์:</h4>';
    
    results.slice(0, 3).forEach((result, index) => {
        html += `
            <div class="result-card">
                <div class="result-title">🔍 ความเป็นไปได้ที่ ${index + 1}: ${result.disease}</div>
                <div class="result-percentage">${result.percentage}% ความเป็นไปได้</div>
                <p><strong>อาการที่ตรงกัน:</strong> ${result.matchingSymptoms.join(', ')}</p>
                <p><strong>ระดับความรุนแรง:</strong> ${result.severity}</p>
                <p><strong>คำแนะนำ:</strong> ${result.advice}</p>
            </div>
        `;
    });
    
    html += '<div style="margin-top: 1rem; padding: 1rem; background: #fff3cd; border-radius: 8px; border-left: 4px solid #ffc107;"><strong>⚠️ คำเตือน:</strong> นี่เป็นเพียงการประเมินเบื้องต้น ควรปรึกษาแพทย์เพื่อการวินิจฉัยที่แม่นยำ</div>';
    
    resultDiv.innerHTML = html;
    resultDiv.classList.add('fade-in');
}

// BMI Calculator Demo
function calculateBMI() {
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value);
    const resultDiv = document.getElementById('bmi-result');
    
    if (!weight || !height || weight <= 0 || height <= 0) {
        resultDiv.innerHTML = '<p style="color: #e74c3c; text-align: center;">กรุณากรอกน้ำหนักและส่วนสูงที่ถูกต้อง</p>';
        return;
    }
    
    // Show loading
    resultDiv.innerHTML = '<div style="text-align: center;"><div class="loading"></div> กำลังคำนวณ BMI...</div>';
    
    setTimeout(() => {
        const bmi = weight / Math.pow(height / 100, 2);
        const category = getBMICategory(bmi);
        const advice = getBMIAdvice(category);
        
        displayBMIResult(bmi, category, advice, weight, height);
    }, 1500);
}

function getBMICategory(bmi) {
    if (bmi < 18.5) return 'น้ำหนักน้อยกว่าเกณฑ์';
    if (bmi < 25) return 'น้ำหนักปกติ';
    if (bmi < 30) return 'น้ำหนักเกิน';
    if (bmi < 35) return 'อ้วนระดับ 1';
    if (bmi < 40) return 'อ้วนระดับ 2';
    return 'อ้วนระดับ 3';
}

function getBMIAdvice(category) {
    const advice = {
        'น้ำหนักน้อยกว่าเกณฑ์': 'ควรเพิ่มน้ำหนักด้วยการกินอาหารครบ 5 หมู่',
        'น้ำหนักปกติ': 'ยอดเยี่ยม! รักษาน้ำหนักปัจจุบัน',
        'น้ำหนักเกิน': 'ควรลดน้ำหนักด้วยการออกกำลังกายและควบคุมอาหาร',
        'อ้วนระดับ 1': 'ควรลดน้ำหนักอย่างจริงจัง ปรึกษานักโภชนาการ',
        'อ้วนระดับ 2': 'ควรพบแพทย์เพื่อวางแผนลดน้ำหนัก',
        'อ้วนระดับ 3': 'ควรพบแพทย์ทันทีเพื่อการรักษา'
    };
    return advice[category] || 'ควรปรึกษาแพทย์';
}

function displayBMIResult(bmi, category, advice, weight, height) {
    const resultDiv = document.getElementById('bmi-result');
    const idealWeight = 22 * Math.pow(height / 100, 2);
    const weightDiff = weight - idealWeight;
    
    let categoryColor = '#27ae60';
    if (category.includes('เกิน') || category.includes('อ้วน')) {
        categoryColor = '#e74c3c';
    } else if (category.includes('น้อย')) {
        categoryColor = '#f39c12';
    }
    
    const html = `
        <h4 style="margin-bottom: 1rem; color: #2c5aa0;">ผลการคำนวณ BMI:</h4>
        <div class="result-card">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
                <div>
                    <strong>ค่า BMI:</strong> ${bmi.toFixed(1)}
                </div>
                <div>
                    <strong>หมวดหมู่:</strong> <span style="color: ${categoryColor}; font-weight: bold;">${category}</span>
                </div>
            </div>
            <div style="margin-bottom: 1rem;">
                <strong>น้ำหนักที่เหมาะสม:</strong> ${idealWeight.toFixed(1)} กก.
                ${weightDiff > 0 ? 
                    `<br><span style="color: #e74c3c;">น้ำหนักเกิน: +${weightDiff.toFixed(1)} กก.</span>` : 
                    weightDiff < 0 ? 
                    `<br><span style="color: #f39c12;">น้ำหนักต่ำกว่าเกณฑ์: ${weightDiff.toFixed(1)} กก.</span>` :
                    `<br><span style="color: #27ae60;">น้ำหนักเหมาะสม ✅</span>`
                }
            </div>
            <div style="background: #f8f9fa; padding: 1rem; border-radius: 8px; border-left: 4px solid #2c5aa0;">
                <strong>💡 คำแนะนำ:</strong> ${advice}
            </div>
        </div>
    `;
    
    resultDiv.innerHTML = html;
    resultDiv.classList.add('fade-in');
}

// Heart Rate Analyzer Demo
function analyzeHeartRate() {
    const heartRate = parseInt(document.getElementById('heart-rate-input').value);
    const age = parseInt(document.getElementById('age-input').value);
    const resultDiv = document.getElementById('heart-rate-result');
    
    if (!heartRate || !age || heartRate <= 0 || age <= 0 || heartRate > 300 || age > 120) {
        resultDiv.innerHTML = '<p style="color: #e74c3c; text-align: center;">กรุณากรอกข้อมูลที่ถูกต้อง (อัตราการเต้นหัวใจ 1-300, อายุ 1-120)</p>';
        return;
    }
    
    // Show loading
    resultDiv.innerHTML = '<div style="text-align: center;"><div class="loading"></div> กำลังวิเคราะห์...</div>';
    
    setTimeout(() => {
        const analysis = analyzeHeartRateData(heartRate, age);
        displayHeartRateResult(analysis);
    }, 1500);
}

function analyzeHeartRateData(heartRate, age) {
    const maxHR = 220 - age;
    const targetLow = Math.round(maxHR * 0.5);
    const targetHigh = Math.round(maxHR * 0.85);
    
    let status, color, advice;
    
    if (heartRate < 50) {
        status = 'ช้ามาก';
        color = '#e74c3c';
        advice = 'อาจมีปัญหาระบบหัวใจ ควรพบแพทย์ทันที';
    } else if (heartRate < 60) {
        status = 'ช้า';
        color = '#f39c12';
        advice = 'ปกติสำหรับนักกีฬาหรือคนออกกำลังกายเป็นประจำ';
    } else if (heartRate <= 100) {
        status = 'ปกติ';
        color = '#27ae60';
        advice = 'อัตราการเต้นหัวใจปกติดี';
    } else if (heartRate <= 120) {
        status = 'เร็วเล็กน้อย';
        color = '#f39c12';
        advice = 'อาจเกิดจากความเครียด กาแฟ หรือการออกกำลังกาย';
    } else if (heartRate <= 150) {
        status = 'เร็ว';
        color = '#e74c3c';
        advice = 'ควรพักผ่อน หลีกเลี่ยงสิ่งกระตุ้น';
    } else {
        status = 'เร็วมาก';
        color = '#e74c3c';
        advice = 'ควรพบแพทย์ทันที อาจเป็นอันตราย';
    }
    
    return {
        heartRate,
        age,
        status,
        color,
        advice,
        maxHR,
        targetLow,
        targetHigh
    };
}

function displayHeartRateResult(analysis) {
    const resultDiv = document.getElementById('heart-rate-result');
    
    const html = `
        <h4 style="margin-bottom: 1rem; color: #2c5aa0;">ผลการวิเคราะห์หัวใจ:</h4>
        <div class="result-card">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
                <div>
                    <strong>อัตราการเต้นหัวใจ:</strong> ${analysis.heartRate} ครั้ง/นาที
                </div>
                <div>
                    <strong>สถานะ:</strong> <span style="color: ${analysis.color}; font-weight: bold;">${analysis.status}</span>
                </div>
            </div>
            <div style="margin-bottom: 1rem;">
                <strong>อัตราการเต้นหัวใจสูงสุด:</strong> ${analysis.maxHR} ครั้ง/นาที<br>
                <strong>โซนเป้าหมายการออกกำลังกาย:</strong> ${analysis.targetLow}-${analysis.targetHigh} ครั้ง/นาที
            </div>
            <div style="background: #f8f9fa; padding: 1rem; border-radius: 8px; border-left: 4px solid ${analysis.color};">
                <strong>💡 คำแนะนำ:</strong> ${analysis.advice}
            </div>
        </div>
        <div style="margin-top: 1rem; padding: 1rem; background: #fff3cd; border-radius: 8px; border-left: 4px solid #ffc107;">
            <strong>📊 โซนการออกกำลังกาย:</strong><br>
            • โซนฟื้นฟู: ${Math.round(analysis.maxHR * 0.5)}-${Math.round(analysis.maxHR * 0.6)} ครั้ง/นาที<br>
            • โซนเผาผลาญไขมัน: ${Math.round(analysis.maxHR * 0.6)}-${Math.round(analysis.maxHR * 0.7)} ครั้ง/นาที<br>
            • โซนแอโรบิก: ${Math.round(analysis.maxHR * 0.7)}-${Math.round(analysis.maxHR * 0.8)} ครั้ง/นาที
        </div>
    `;
    
    resultDiv.innerHTML = html;
    resultDiv.classList.add('fade-in');
}

// Drug Information Demo (OpenFDA API simulation)
async function searchDrug() {
    const drugName = document.getElementById('drug-name').value.trim();
    const resultDiv = document.getElementById('drug-result');
    
    if (!drugName) {
        resultDiv.innerHTML = '<p style="color: #e74c3c; text-align: center;">กรุณากรอกชื่อยา</p>';
        return;
    }
    
    // Show loading
    resultDiv.innerHTML = '<div style="text-align: center;"><div class="loading"></div> กำลังค้นหาข้อมูลยา...</div>';
    
    try {
        // Simulate API call to OpenFDA
        setTimeout(() => {
            const drugInfo = simulateDrugSearch(drugName.toLowerCase());
            displayDrugResult(drugInfo, drugName);
        }, 2000);
        
    } catch (error) {
        resultDiv.innerHTML = '<p style="color: #e74c3c; text-align: center;">เกิดข้อผิดพลาดในการค้นหา กรุณาลองใหม่</p>';
    }
}

function simulateDrugSearch(drugName) {
    const drugs = {
        'aspirin': {
            brandName: 'Aspirin',
            genericName: 'Acetylsalicylic acid',
            manufacturer: 'Various',
            purpose: 'Pain reliever, fever reducer, anti-inflammatory',
            dosage: '325-650 mg every 4-6 hours',
            warnings: 'May cause stomach bleeding. Consult doctor if pregnant.',
            sideEffects: 'Stomach upset, heartburn, drowsiness'
        },
        'paracetamol': {
            brandName: 'Tylenol',
            genericName: 'Acetaminophen',
            manufacturer: 'Various',
            purpose: 'Pain reliever, fever reducer',
            dosage: '500-1000 mg every 4-6 hours',
            warnings: 'Do not exceed 4000mg per day. Liver damage risk.',
            sideEffects: 'Rare when used as directed'
        },
        'ibuprofen': {
            brandName: 'Advil, Motrin',
            genericName: 'Ibuprofen',
            manufacturer: 'Various',
            purpose: 'Pain reliever, fever reducer, anti-inflammatory',
            dosage: '200-400 mg every 4-6 hours',
            warnings: 'May increase risk of heart attack or stroke.',
            sideEffects: 'Stomach upset, heartburn, dizziness'
        }
    };
    
    return drugs[drugName] || null;
}

function displayDrugResult(drugInfo, searchTerm) {
    const resultDiv = document.getElementById('drug-result');
    
    if (!drugInfo) {
        resultDiv.innerHTML = `
            <div style="text-align: center; color: #7f8c8d;">
                <p>ไม่พบข้อมูลยา "${searchTerm}" ในฐานข้อมูลตัวอย่าง</p>
                <p style="font-size: 0.9rem; margin-top: 1rem;">ลองค้นหา: aspirin, paracetamol, ibuprofen</p>
            </div>
        `;
        return;
    }
    
    const html = `
        <h4 style="margin-bottom: 1rem; color: #2c5aa0;">ข้อมูลยา:</h4>
        <div class="result-card">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
                <div>
                    <strong>ชื่อการค้า:</strong> ${drugInfo.brandName}
                </div>
                <div>
                    <strong>ชื่อสามัญ:</strong> ${drugInfo.genericName}
                </div>
            </div>
            <div style="margin-bottom: 1rem;">
                <strong>ผู้ผลิต:</strong> ${drugInfo.manufacturer}<br>
                <strong>ประโยชน์:</strong> ${drugInfo.purpose}<br>
                <strong>ขนาดยา:</strong> ${drugInfo.dosage}
            </div>
            <div style="background: #fff3cd; padding: 1rem; border-radius: 8px; border-left: 4px solid #ffc107; margin-bottom: 1rem;">
                <strong>⚠️ คำเตือน:</strong> ${drugInfo.warnings}
            </div>
            <div style="background: #f8d7da; padding: 1rem; border-radius: 8px; border-left: 4px solid #e74c3c;">
                <strong>🔴 ผลข้างเคียง:</strong> ${drugInfo.sideEffects}
            </div>
        </div>
        <div style="margin-top: 1rem; padding: 1rem; background: #d4edda; border-radius: 8px; border-left: 4px solid #27ae60;">
            <strong>📝 หมายเหตุ:</strong> นี่เป็นข้อมูลตัวอย่างเพื่อการศึกษา ไม่ใช่คำแนะนำทางการแพทย์จริง
        </div>
    `;
    
    resultDiv.innerHTML = html;
    resultDiv.classList.add('fade-in');
}

// Modal functionality
function openDemo(category) {
    const modal = document.getElementById('demo-modal');
    const modalBody = document.getElementById('modal-body');
    
    const demoContent = {
        'imaging': {
            title: 'การถ่ายภาพทางการแพทย์',
            content: `
                <h3>AI ในการถ่ายภาพทางการแพทย์</h3>
                <div style="margin: 2rem 0;">
                    <h4>การทำงานของ AI:</h4>
                    <ul style="margin-left: 2rem; margin-top: 1rem;">
                        <li>วิเคราะห์ภาพ X-ray เพื่อตรวจหาความผิดปกติ</li>
                        <li>ตรวจจับก้อนเนื้อในปอดจาก CT Scan</li>
                        <li>วิเคราะห์ MRI สำหรับการวินิจฉัยโรคสมอง</li>
                        <li>ตรวจหามะเร็งผิวหนังจากภาถ่าย</li>
                    </ul>
                </div>
                <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px;">
                    <h4>ประโยชน์:</h4>
                    <p>• ความแม่นยำสูงกว่า 95%</p>
                    <p>• ลดเวลาการวินิจฉัย 60%</p>
                    <p>• ตรวจพบโรคได้เร็วขึ้น</p>
                    <p>• ลดความผิดพลาดจากมนุษย์</p>
                </div>
            `
        },
        'drug': {
            title: 'การค้นพบยาใหม่',
            content: `
                <h3>AI ในการค้นพบและพัฒนายา</h3>
                <div style="margin: 2rem 0;">
                    <h4>กระบวนการ AI:</h4>
                    <ul style="margin-left: 2rem; margin-top: 1rem;">
                        <li>วิเคราะห์โครงสร้างโมเลกุลของยา</li>
                        <li>ทำนายปฏิกิริยาของยากับเซลล์</li>
                        <li>จำลองการทดลองก่อนทำจริง</li>
                        <li>ค้นหาเป้าหมายของยาใหม่</li>
                    </ul>
                </div>
                <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px;">
                    <h4>ผลลัพธ์:</h4>
                    <p>• ลดเวลาการพัฒนายาจาก 10-15 ปี เหลือ 3-5 ปี</p>
                    <p>• ลดต้นทุนการวิจัย 70%</p>
                    <p>• เพิ่มอัตราความสำเร็จ 40%</p>
                    <p>• ค้นพบยาสำหรับโรคหายากได้มากขึ้น</p>
                </div>
            `
        },
        'surgery': {
            title: 'การผ่าตัดด้วยหุ่นยนต์',
            content: `
                <h3>ระบบ AI ในการผ่าตัด</h3>
                <div style="margin: 2rem 0;">
                    <h4>เทคโนโลยี:</h4>
                    <ul style="margin-left: 2rem; margin-top: 1rem;">
                        <li>หุ่นยนต์ Da Vinci System</li>
                        <li>การนำทางด้วย AI</li>
                        <li>การถ่ายภาพแบบ Real-time</li>
                        <li>ระบบสั่นกรอง tremor</li>
                    </ul>
                </div>
                <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px;">
                    <h4>ข้อดี:</h4>
                    <p>• ความแม่นยำระดับมิลลิเมตร</p>
                    <p>• รอยแผลเล็ก (Minimally Invasive)</p>
                    <p>• ลดภาวะแทรกซ้อน 35%</p>
                    <p>• ระยะเวลาฟื้นตัวเร็วขึ้น 50%</p>
                </div>
            `
        },
        'personalized': {
            title: 'การแพทย์เฉพาะบุคคล',
            content: `
                <h3>Personalized Medicine ด้วย AI</h3>
                <div style="margin: 2rem 0;">
                    <h4>การวิเคราะห์:</h4>
                    <ul style="margin-left: 2rem; margin-top: 1rem;">
                        <li>ข้อมูลพันธุกรรม (Genomics)</li>
                        <li>ประวัติการรักษา</li>
                        <li>ปัจจัยสิ่งแวดล้อม</li>
                        <li>การตอบสนองต่อยา</li>
                    </ul>
                </div>
                <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px;">
                    <h4>การประยุกต์ใช้:</h4>
                    <p>• การรักษามะเร็งแบบเฉพาะเจาะจง</p>
                    <p>• การพยากรณ์ความเสี่ยงโรค</p>
                    <p>• การเลือกยาที่เหมาะสม</p>
                    <p>• แผนการป้องกันโรคส่วนบุคคล</p>
                </div>
            `
        },
        'telemedicine': {
            title: 'การแพทย์ทางไกล',
            content: `
                <h3>AI ในระบบ Telemedicine</h3>
                <div style="margin: 2rem 0;">
                    <h4>เทคโนโลยี AI:</h4>
                    <ul style="margin-left: 2rem; margin-top: 1rem;">
                        <li>Chatbots สำหรับปรึกษาเบื้องต้น</li>
                        <li>การติดตามสุขภาพแบบ Real-time</li>
                        <li>การวิเคราะห์อาการจากเสียง</li>
                        <li>การตรวจวินิจฉัยจากภาพถ่าย</li>
                    </ul>
                </div>
                <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px;">
                    <h4>ประโยชน์:</h4>
                    <p>• เข้าถึงการรักษาได้ 24/7</p>
                    <p>• ลดต้นทุนการรักษา 40%</p>
                    <p>• ลดการแพร่เชื้อโรค</p>
                    <p>• เหมาะสำหรับพื้นที่ห่างไกล</p>
                </div>
            `
        },
        'predictive': {
            title: 'การพยากรณ์โรค',
            content: `
                <h3>AI Predictive Analytics</h3>
                <div style="margin: 2rem 0;">
                    <h4>การทำงาน:</h4>
                    <ul style="margin-left: 2rem; margin-top: 1rem;">
                        <li>วิเคราะห์ข้อมูลสุขภาพในอดีต</li>
                        <li>ติดตามสัญญาณชีวิต</li>
                        <li>ประเมินปัจจัยเสี่ยง</li>
                        <li>พยากรณ์แนวโน้มการเกิดโรค</li>
                    </ul>
                </div>
                <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 8px;">
                    <h4>ตัวอย่างการใช้งาน:</h4>
                    <p>• พยากรณ์โรคหัวใจล่วงหน้า 5 ปี</p>
                    <p>• ตรวจหาความเสี่ยงเบาหวาน</p>
                    <p>• ประเมินโอกาสเกิดโรคซึมเศร้า</p>
                    <p>• แนะนำการป้องกันเฉพาะบุคคล</p>
                </div>
            `
        }
    };
    
    const demo = demoContent[category];
    if (demo) {
        modalBody.innerHTML = demo.content;
        modal.style.display = 'block';
    }
}

function closeModal() {
    document.getElementById('demo-modal').style.display = 'none';
}

// Mobile navigation toggle
function initMobileNav() {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (navToggle) {
        navToggle.addEventListener('click', () => {
            navMenu.style.display = navMenu.style.display === 'flex' ? 'none' : 'flex';
        });
    }
}

// Intersection Observer for animations
function initScrollAnimations() {
    const elements = document.querySelectorAll('.app-card, .demo-card, .api-card, .edu-card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    elements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
}

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initStatsAnimation();
    initDemoTabs();
    initCodeTabs();
    initMobileNav();
    initScrollAnimations();
    
    // Close modal when clicking outside
    window.addEventListener('click', function(event) {
        const modal = document.getElementById('demo-modal');
        if (event.target === modal) {
            closeModal();
        }
    });
    
    // Smooth scrolling for navigation links
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            scrollToSection(targetId);
        });
    });
    
    // Add loading states to demo buttons
    document.querySelectorAll('.demo-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const icon = this.querySelector('i');
            const originalClass = icon.className;
            icon.className = 'fas fa-spinner fa-spin';
            
            setTimeout(() => {
                icon.className = originalClass;
            }, 2000);
        });
    });
});

// Utility functions
function showLoading(elementId) {
    const element = document.getElementById(elementId);
    element.innerHTML = '<div style="text-align: center;"><div class="loading"></div> กำลังประมวลผล...</div>';
}

function hideLoading(elementId) {
    const element = document.getElementById(elementId);
    element.innerHTML = '';
}

// Export functions for potential external use
window.MedicalAI = {
    scrollToSection,
    checkSymptoms,
    calculateBMI,
    analyzeHeartRate,
    searchDrug,
    openDemo,
    closeModal
};