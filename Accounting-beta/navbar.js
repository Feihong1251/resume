
// โค้ด HTML สำหรับแถบด้านข้างทั้งหมด
var navbaracc = `
<div class="navbar">
                <div style="width: 100%;height: 100%; padding: 24px;">
                    <div style=" width: 100%; height: 100%;display: flex;justify-content: space-between; ">
                        <div style="width: 15%; height: 100%; padding: 6.5px 0;">
                            <div class="nav-menu">
                                <div class="nav-menu-in">
                                    <div class="text-nav">หน้าหลัก</div>
                                    <img src="picture/arrow-right-nav.png" style="width: 12px;height: 12px;">
                                    <div class="text-nav">ขาย</div>
                                </div>
                                <div style="width: 50%;display: flex;justify-content: center;align-items: center;">
                                 <div class="nav-menu-in-right">ใบเสนอราคา</div>
                                </div>
                            </div>
                        </div>
                        <div style=" width: 30%; height: 100%; display: flex; justify-content: end; gap: 8px;">
                            <div class="nav-pic-right"><img src="picture/print.png"  class="nav-pic"></div>
                            <div class="nav-pic-right"><img src="picture/upload.png" class="nav-pic" ></div>
                        </div>
                    </div>
                    
                </div>
            </div>
`;

// *** สำคัญ: บรรทัดนี้ควรอยู่ก่อนโค้ด jQuery ที่จัดการการคลิก
// เพราะ jQuery ต้องเห็น HTML ที่ถูก inject เข้าไปก่อนจึงจะแนบ event listeners ได้
$("#navbaracc").html(navbaracc);

// ตัวแปรและฟังก์ชันสำหรับเมนูสไลด์อื่นๆ (ถ้ามี)


// โค้ด jQuery สำหรับเมนู Accordion และการเลือกรายการ
// ต้องแน่ใจว่าโค้ดส่วนนี้รันหลังจากที่ HTML ของ sidebar ถูกใส่ลงใน DOM แล้ว

