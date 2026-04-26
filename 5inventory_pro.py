import csv
import os
import datetime

def start_inventory_app():
    # اسم الملف الاحترافي الذي سيجده المشتري
    file_name = "Smart_Inventory_Manager.csv"
    
    # التأكد من إنشاء الملف مع دعم اللغة العربية (utf-8-sig)
    if not os.path.exists(file_name):
        with open(file_name, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            # العناوين التي ستظهر في الإكسل
            writer.writerow(["التاريخ", "المنتج", "الكمية", "سعر التكلفة", "سعر البيع", "صافي الربح"])

    print("="*40)
    print("      🏪 نظام إدارة المخازن والمبيعات      ")
    print("          نسخة رقم 1.0 - باسم          ")
    print("="*40)
    
    while True:
        print("\n[1] إضافة بضاعة جديدة")
        print("[2] عرض سجل المخزن الحالي")
        print("[3] خروج وحفظ البيانات")
        
        choice = input("\n👉 اختر العملية المطلوبة: ")
        
        if choice == "1":
            try:
                name = input("📦 اسم المنتج: ")
                qty = int(input("🔢 الكمية المتوفرة: "))
                cost = float(input("💰 سعر التكلفة للقطعة: "))
                
                # حساب سعر البيع بزيادة 20% وحساب الربح الإجمالي للكمية
                sell_price = cost * 1.2
                total_profit = (sell_price - cost) * qty
                date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                
                # حفظ البيانات فوراً في الملف
                with open(file_name, 'a', newline='', encoding='utf-8-sig') as f:
                    writer = csv.writer(f)
                    writer.writerow([date_now, name, qty, cost, sell_price, total_profit])
                
                print(f"\n✅ تم الحفظ! سعر البيع المقترح لـ {name}: {sell_price:.2f}")
                print(f"📈 الربح المتوقع من هذه الكمية: {total_profit:.2f}")
                
            except ValueError:
                print("❌ خطأ: يرجى إدخال أرقام فقط في خانة السعر والكمية!")
                
        elif choice == "2":
            print("\n" + "-"*45)
            print(f"{'المنتج':<15} | {'الكمية':<8} | {'الربح المتوقع':<10}")
            print("-"*45)
            try:
                with open(file_name, 'r', encoding='utf-8-sig') as f:
                    reader = csv.reader(f)
                    next(reader)  # تخطي سطر العناوين
                    for row in reader:
                        print(f"{row[1]:<15} | {row[2]:<8} | {row[5]:<10}")
            except FileNotFoundError:
                print("السجل فارغ حالياً.")
            print("-"*45)
                
        elif choice == "3":
            print(f"\n🏁 تم حفظ جميع البيانات بنجاح في ملف: {file_name}")
            print("شكراً لاستخدامك نظامنا!")
            break
        else:
            print("⚠️ اختيار غير صحيح، جرب مرة أخرى.")

if __name__ == "__main__":
    start_inventory_app()
