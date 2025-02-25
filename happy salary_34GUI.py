import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันคำนวณโบนัส
def calculate_bonus():
    try:
        salary = float(entry_salary.get())
        years_worked = int(entry_years.get())

        if years_worked <= 5:
            bonus = salary * 0.05
        elif years_worked <= 10:
            bonus = salary * 0.10
        else:
            bonus = salary * 0.15

        bonus_formatted = f"{bonus:,.2f}"
        
        messagebox.showinfo("ผลลัพธ์", f"จำนวนเงินโบนัส: {bonus_formatted} บาท")
        
        clear_fields()

    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกตัวเลขที่ถูกต้อง")

# ฟังก์ชันเคลียร์ช่องกรอกข้อมูล
def clear_fields():
    entry_salary.delete(0, tk.END)
    entry_years.delete(0, tk.END)

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Happy Salary - โปรแกรมคำนวณโบนัส")
root.geometry("320x300")
root.configure(bg="#FFF176")  # สีเหลืองอ่อน

# ส่วนหัวของโปรแกรม
tk.Label(root, text="💰 Happy Salary 💰", font=("Arial", 16, "bold"), bg="#FFF176", fg="black").pack(pady=10)

# Label และ Entry สำหรับกรอกเงินเดือน
tk.Label(root, text="เงินเดือน:", font=("Arial", 12), bg="#FFF176").pack(pady=5)
entry_salary = tk.Entry(root, font=("Arial", 12))
entry_salary.pack(pady=5)

# Label และ Entry สำหรับกรอกจำนวนปีที่ทำงาน
tk.Label(root, text="จำนวนปีที่ทำงาน:", font=("Arial", 12), bg="#FFF176").pack(pady=5)
entry_years = tk.Entry(root, font=("Arial", 12))
entry_years.pack(pady=5)

# ปุ่มคำนวณโบนัส
btn_calculate = tk.Button(root, text="คำนวณโบนัส", font=("Arial", 12, "bold"), bg="#FFD700", fg="black", command=calculate_bonus)
btn_calculate.pack(pady=10)

# ปุ่มเคลียร์ค่า
btn_clear = tk.Button(root, text="เคลียร์", font=("Arial", 12, "bold"), bg="#FFEB3B", fg="black", command=clear_fields)
btn_clear.pack(pady=5)

# เริ่มต้นโปรแกรม
root.mainloop()
