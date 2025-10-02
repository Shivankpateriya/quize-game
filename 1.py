def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def calculate_bmr(weight, height, age, gender):
    height_cm = height * 100
    if gender.lower() == 'male':
        return 88.36 + (13.4 * weight) + (4.8 * height_cm) - (5.7 * age)
    else:
        return 447.6 + (9.2 * weight) + (3.1 * height_cm) - (4.3 * age)

def body_fat_percentage(bmi, age, gender):
    if gender.lower() == 'male':
        return (1.20 * bmi) + (0.23 * age) - 16.2
    else:
        return (1.20 * bmi) + (0.23 * age) - 5.4

def recommended_water_intake(weight):
    return weight * 35 / 1000  # in liters

def calories_burned(met, weight, duration):
    return (met * 3.5 * weight / 200) * duration

def bmi_category_health(bmi, age, gender):
    if bmi < 18.5:
        return "Underweight", "Unhealthy"
    elif 18.5 <= bmi <= 24.9:
        if (gender.lower() == "male" and 18 <= age <= 65) or (gender.lower() == "female" and 18 <= age <= 65):
            return "Normal weight", "Healthy"
        else:
            return "Normal weight", "Healthy"
    elif 25.0 <= bmi <= 29.9:
        return "Overweight", "Unhealthy"
    else:
        return "Obese", "Unhealthy"

import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def get_suggestions(category):
    suggestions = {
        "Underweight": "Consider increasing calorie intake and consult a healthcare provider.",
        "Normal weight": "Maintain your current lifestyle and stay active.",
        "Overweight": "Consider a balanced diet and regular exercise.",
        "Obese": "Consult a healthcare provider for a personalized plan. Focus on healthy eating and physical activity."
    }
    return suggestions.get(category, "No suggestion available.")

def get_diet_plan(category, health_status="Healthy", weight=70, age=30, gender="Male"):
    base_water = weight * 0.035
    if health_status == "Unhealthy" or category in ["Underweight", "Obese"]:
        water_intake = base_water + 0.5
    else:
        water_intake = base_water
    if age > 65:
        water_intake += 0.3
    elif age < 25:
        water_intake += 0.2
    if gender.lower() == "male":
        water_intake += 0.2
    diet_plans = {
        "Underweight": {
            "goal": "Healthy weight gain and muscle building",
            "daily_calories": "2500-3000 calories (500+ above maintenance)",
            "water_routine": f"{water_intake:.1f}L daily - Drink 250ml every 2 hours",
            "meal_plan": [
                "🌅 BREAKFAST (7-8 AM): Oatmeal with banana, nuts, honey + whole milk",
                "🥪 MID-MORNING (10 AM): Protein smoothie with peanut butter",
                "🍽️ LUNCH (12-1 PM): Grilled chicken, brown rice, avocado salad",
                "🍎 AFTERNOON (3 PM): Greek yogurt with granola and berries",
                "🍽️ DINNER (6-7 PM): Salmon, sweet potato, steamed broccoli",
                "🌙 EVENING (9 PM): Whole grain toast with almond butter"
            ],
            "water_schedule": [
                "💧 Wake up: 500ml warm water with lemon",
                "💧 Before meals: 250ml (30 min before eating)",
                "💧 Post-workout: 500ml with electrolytes",
                "💧 Before bed: 200ml (not too much to avoid sleep disruption)"
            ],
            "health_tips": [
                "🏋️ Combine with strength training for muscle gain",
                "😴 Get 8-9 hours sleep for recovery",
                "📱 Track calories to ensure adequate intake"
            ]
        },
        "Normal weight": {
            "goal": "Maintain healthy weight and optimize nutrition",
            "daily_calories": "2000-2500 calories (maintenance level)",
            "water_routine": f"{water_intake:.1f}L daily - Drink 200ml every 1.5 hours",
            "meal_plan": [
                "🌅 BREAKFAST (7-8 AM): Greek yogurt, berries, whole grain cereal",
                "🍎 MID-MORNING (10 AM): Apple with 10 almonds",
                "🍽️ LUNCH (12-1 PM): Quinoa bowl with vegetables and lean protein",
                "🥕 AFTERNOON (3 PM): Carrot sticks with hummus",
                "🍽️ DINNER (6-7 PM): Grilled fish, brown rice, mixed vegetables",
                "🌙 EVENING (8 PM): Herbal tea with 1 small fruit"
            ],
            "water_schedule": [
                "💧 Wake up: 400ml water with lemon",
                "💧 Before meals: 200ml",
                "💧 During exercise: 150ml every 15-20 minutes",
                "💧 Before bed: 150ml"
            ],
            "health_tips": [
                "🏃 Maintain regular exercise routine",
                "⚖️ Weigh yourself weekly at same time",
                "🥗 Follow 80/20 rule - healthy 80% of the time"
            ]
        },
        "Overweight": {
            "goal": "Gradual weight loss (1-2 lbs per week)",
            "daily_calories": "1500-1800 calories (300-500 below maintenance)",
            "water_routine": f"{water_intake:.1f}L daily - Drink 300ml before each meal",
            "meal_plan": [
                "🌅 BREAKFAST (7-8 AM): Egg white omelet with spinach, 1 slice whole grain toast",
                "🍎 MID-MORNING (10 AM): Green tea with 5 almonds",
                "🍽️ LUNCH (12-1 PM): Large salad with grilled chicken, olive oil dressing",
                "🥒 AFTERNOON (3 PM): Cucumber slices with low-fat yogurt dip",
                "🍽️ DINNER (6-7 PM): Baked fish, steamed vegetables, small sweet potato",
                "🌙 EVENING (8 PM): Herbal tea (no snacks after dinner)"
            ],
            "water_schedule": [
                "💧 Wake up: 500ml warm water with lemon (boosts metabolism)",
                "💧 Before meals: 300ml (30 min before - increases satiety)",
                "💧 Between meals: 200ml when hungry (often thirst mimics hunger)",
                "💧 Pre-workout: 250ml, Post-workout: 400ml"
            ],
            "health_tips": [
                "🚶 Walk 10,000+ steps daily",
                "📝 Keep a food diary",
                "🍽️ Use smaller plates to control portions",
                "⏰ Stop eating 3 hours before bedtime"
            ]
        },
        "Obese": {
            "goal": "Significant weight loss with medical supervision",
            "daily_calories": "1200-1500 calories (strict deficit with medical guidance)",
            "water_routine": f"{water_intake:.1f}L daily - Drink 400ml before each meal",
            "meal_plan": [
                "🌅 BREAKFAST (8 AM): Steel-cut oats with berries (no sugar)",
                "🥤 MID-MORNING (10 AM): Green tea or black coffee",
                "🍽️ LUNCH (12 PM): Large vegetable soup with lean protein",
                "🥬 AFTERNOON (3 PM): Raw vegetables with minimal hummus",
                "🍽️ DINNER (6 PM): Grilled lean protein, large portion steamed vegetables",
                "🌙 EVENING: Only herbal tea or water"
            ],
            "water_schedule": [
                "💧 Wake up: 600ml warm water with lemon and ginger",
                "💧 Before meals: 400ml (45 min before - maximum satiety)",
                "💧 When craving snacks: 300ml first, wait 10 minutes",
                "💧 Post-exercise: 500ml with electrolytes",
                "💧 Before bed: 200ml (2 hours before sleep)"
            ],
            "health_tips": [
                "👨‍⚕️ IMPORTANT: Consult doctor before starting any diet plan",
                "🏊 Start with low-impact exercises (swimming, walking)",
                "📱 Use apps to track food and water intake",
                "👥 Join support groups for motivation",
                "🎯 Set small, achievable weekly goals"
            ]
        }
    }
    plan = diet_plans.get(category, diet_plans["Normal weight"])
    if health_status == "Unhealthy":
        plan["health_warning"] = "⚠️ HEALTH ALERT: Consult healthcare provider before starting any new diet plan"
        plan["additional_water"] = "💧 EXTRA HYDRATION: Add 500ml daily for health recovery"
    return plan

class BMICalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator Pro")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        self.bmi_history = []
        self.create_interface()

    def create_interface(self):
        title_frame = tk.Frame(self.root, bg='#f0f0f0')
        title_frame.pack(fill=tk.X, pady=10)
        tk.Label(title_frame, text="🏥 BMI Calculator Pro", bg='#f0f0f0', fg='#2c3e50', font=('Arial', 24, 'bold')).pack()
        tk.Label(title_frame, text="Calculate your BMI and get personalized health recommendations", bg='#f0f0f0', fg='#7f8c8d', font=('Arial', 12)).pack()
        main_container = tk.Frame(self.root, bg='#f0f0f0')
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        left_panel = tk.Frame(main_container, bg='#f0f0f0')
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        right_panel = tk.Frame(main_container, bg='#f0f0f0')
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        self.create_input_section(left_panel)
        self.create_results_section(right_panel)

    def create_input_section(self, parent):
        input_frame = tk.LabelFrame(parent, text="📝 Personal Information", font=('Arial', 14, 'bold'), bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
        input_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        self.create_basic_inputs(input_frame)
        button_frame = tk.Frame(input_frame, bg='#f0f0f0')
        button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(button_frame, text="🧮 Calculate BMI", command=self.calculate_bmi_action, bg='#3498db', fg='white', font=('Arial', 12, 'bold'), relief='flat', padx=20, pady=8).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="🗑️ Clear", command=self.clear_fields, bg='#e74c3c', fg='white', font=('Arial', 12, 'bold'), relief='flat', padx=20, pady=8).pack(side=tk.LEFT, padx=5)
        progress_frame = tk.LabelFrame(parent, text="📈 BMI Progress", font=('Arial', 14, 'bold'), bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
        progress_frame.pack(fill=tk.BOTH, expand=True)
        self.fig_progress, self.ax_progress = plt.subplots(figsize=(8, 4), facecolor='#f0f0f0')
        self.canvas_progress = FigureCanvasTkAgg(self.fig_progress, master=progress_frame)
        self.canvas_progress.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def create_basic_inputs(self, parent):
        tk.Label(parent, text="⚖️ Weight:", bg='#f0f0f0', fg='#2c3e50', font=('Arial', 12, 'bold')).grid(row=0, column=0, sticky='w', pady=5, padx=5)
        weight_frame = tk.Frame(parent, bg='#f0f0f0')
        weight_frame.grid(row=0, column=1, sticky='w', pady=5, padx=5)
        self.weight_var = tk.StringVar()
        tk.Entry(weight_frame, textvariable=self.weight_var, width=10, font=('Arial', 12)).pack(side=tk.LEFT, padx=2)
        self.weight_unit_var = tk.StringVar(value="kg")
        tk.Radiobutton(weight_frame, text="kg", variable=self.weight_unit_var, value="kg", bg='#f0f0f0', font=('Arial', 10)).pack(side=tk.LEFT, padx=2)
        tk.Radiobutton(weight_frame, text="lbs", variable=self.weight_unit_var, value="lbs", bg='#f0f0f0', font=('Arial', 10)).pack(side=tk.LEFT, padx=2)
        tk.Label(parent, text="📏 Height:", bg='#f0f0f0', fg='#2c3e50', font=('Arial', 12, 'bold')).grid(row=1, column=0, sticky='w', pady=5, padx=5)
        height_frame = tk.Frame(parent, bg='#f0f0f0')
        height_frame.grid(row=1, column=1, sticky='w', pady=5, padx=5)
        self.height_var = tk.StringVar()
        tk.Entry(height_frame, textvariable=self.height_var, width=10, font=('Arial', 12)).pack(side=tk.LEFT, padx=2)
        self.height_unit_var = tk.StringVar(value="cm")
        tk.Radiobutton(height_frame, text="cm", variable=self.height_unit_var, value="cm", bg='#f0f0f0', font=('Arial', 10)).pack(side=tk.LEFT, padx=2)
        tk.Radiobutton(height_frame, text="ft", variable=self.height_unit_var, value="ft", bg='#f0f0f0', font=('Arial', 10)).pack(side=tk.LEFT, padx=2)
        tk.Label(parent, text="🎂 Age:", bg='#f0f0f0', fg='#2c3e50', font=('Arial', 12, 'bold')).grid(row=2, column=0, sticky='w', pady=5, padx=5)
        self.age_var = tk.StringVar()
        tk.Entry(parent, textvariable=self.age_var, width=10, font=('Arial', 12)).grid(row=2, column=1, sticky='w', pady=5, padx=5)
        tk.Label(parent, text="👤 Gender:", bg='#f0f0f0', fg='#2c3e50', font=('Arial', 12, 'bold')).grid(row=3, column=0, sticky='w', pady=5, padx=5)
        gender_frame = tk.Frame(parent, bg='#f0f0f0')
        gender_frame.grid(row=3, column=1, sticky='w', pady=5, padx=5)
        self.gender_var = tk.StringVar(value="Male")
        tk.Radiobutton(gender_frame, text="Male", variable=self.gender_var, value="Male", bg='#f0f0f0', font=('Arial', 12)).pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(gender_frame, text="Female", variable=self.gender_var, value="Female", bg='#f0f0f0', font=('Arial', 12)).pack(side=tk.LEFT, padx=5)

    def create_results_section(self, parent):
        result_frame = tk.LabelFrame(parent, text="📊 BMI Results", font=('Arial', 14, 'bold'), bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
        result_frame.pack(fill=tk.X, pady=(0, 10))
        self.result_label = tk.Label(result_frame, text="Calculate BMI to see results", bg='#f0f0f0', fg='#2c3e50', font=('Arial', 14, 'bold'))
        self.result_label.pack(pady=5)
        metrics_frame = tk.LabelFrame(parent, text="📈 Health Metrics", font=('Arial', 14, 'bold'), bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
        metrics_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        self.metrics_text = tk.Text(metrics_frame, height=6, bg='white', fg='#2c3e50', font=('Arial', 10), relief='flat', bd=1, padx=10, pady=10, wrap=tk.WORD)
        self.metrics_text.pack(fill=tk.BOTH, expand=True)
        suggestions_frame = tk.LabelFrame(parent, text="💡 Health Suggestions", font=('Arial', 14, 'bold'), bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
        suggestions_frame.pack(fill=tk.X, pady=(0, 10))
        self.suggestion_label = tk.Label(suggestions_frame, text="", bg='#f0f0f0', fg='#2c3e50', font=('Arial', 11), wraplength=400, justify='left')
        self.suggestion_label.pack(anchor='w', pady=5)
        diet_frame = tk.LabelFrame(parent, text="🍽️ Diet Plan", font=('Arial', 14, 'bold'), bg='#f0f0f0', fg='#2c3e50', padx=10, pady=10)
        diet_frame.pack(fill=tk.BOTH, expand=True)
        diet_scroll_frame = tk.Frame(diet_frame, bg='#f0f0f0')
        diet_scroll_frame.pack(fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(diet_scroll_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.diet_text = tk.Text(diet_scroll_frame, bg='white', fg='#2c3e50', font=('Arial', 10), relief='flat', bd=1, padx=10, pady=10, yscrollcommand=scrollbar.set, wrap=tk.WORD)
        self.diet_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.diet_text.yview)

    def calculate_bmi_action(self):
        try:
            weight = float(self.weight_var.get())
            height = float(self.height_var.get())
            age = int(self.age_var.get())
            gender = self.gender_var.get()
            weight_unit = self.weight_unit_var.get()
            height_unit = self.height_unit_var.get()
            if weight_unit == "lbs":
                weight_kg = weight * 0.453592
            else:
                weight_kg = weight
            if height_unit == "ft":
                height_m = height * 0.3048
            else:
                height_m = height / 100
            bmi = calculate_bmi(weight_kg, height_m)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")
            return
        category, health_status = bmi_category_health(bmi, age, gender)
        suggestion = get_suggestions(category)
        diet_plan = get_diet_plan(category, health_status, weight_kg, age, gender)
        self.result_label.config(text=f"Your BMI: {bmi:.1f} ({category}) - {health_status}")
        self.suggestion_label.config(text=suggestion)
        height_cm = height_m * 100
        min_weight = 18.5 * (height_m ** 2)
        max_weight = 25 * (height_m ** 2)
        goal_bmi = 25
        goal_weight = goal_bmi * (height_m ** 2)
        weight_loss = max(0, weight_kg - goal_weight)
        bmi_prime = bmi / 25
        ponderal_index = weight_kg / (height_m ** 3)
        metrics_text = (
            f"Healthy BMI Range: 18.5 - 25 kg/m²\n"
            f"Healthy Weight Range: {min_weight:.1f} - {max_weight:.1f} kg\n"
            f"Weight Goal (BMI 25): {weight_loss:.1f} kg to lose\n"
            f"BMI Prime: {bmi_prime:.2f}\n"
            f"Ponderal Index: {ponderal_index:.2f} kg/m³"
        )
        self.metrics_text.delete(1.0, tk.END)
        self.metrics_text.insert(tk.END, metrics_text)
        diet_text = f"🎯 GOAL: {diet_plan['goal']}\n"
        diet_text += f"🔥 CALORIES: {diet_plan['daily_calories']}\n"
        diet_text += f"💧 WATER: {diet_plan['water_routine']}\n\n"
        diet_text += "📅 DAILY MEAL PLAN:\n"
        for meal in diet_plan['meal_plan']:
            diet_text += f"{meal}\n"
        diet_text += f"\n💧 WATER SCHEDULE:\n"
        for water_tip in diet_plan['water_schedule']:
            diet_text += f"{water_tip}\n"
        diet_text += f"\n💡 HEALTH TIPS:\n"
        for tip in diet_plan['health_tips']:
            diet_text += f"{tip}\n"
        if 'health_warning' in diet_plan:
            diet_text += f"\n{diet_plan['health_warning']}\n"
        if 'additional_water' in diet_plan:
            diet_text += f"{diet_plan['additional_water']}\n"
        self.diet_text.delete(1.0, tk.END)
        self.diet_text.insert(tk.END, diet_text)
        self.bmi_history.append(bmi)
        self.update_progress()

    def clear_fields(self):
        self.weight_var.set("")
        self.height_var.set("")
        self.age_var.set("")
        self.gender_var.set("Male")
        self.weight_unit_var.set("kg")
        self.height_unit_var.set("cm")
        self.result_label.config(text="Calculate BMI to see results")
        self.suggestion_label.config(text="")
        self.metrics_text.delete(1.0, tk.END)
        self.diet_text.delete(1.0, tk.END)
        self.bmi_history.clear()
        self.update_progress()

    def update_progress(self):
        self.ax_progress.clear()
        if not self.bmi_history:
            self.ax_progress.text(0.5, 0.5, 'No BMI data to display\nCalculate BMI to see progress', ha='center', va='center', transform=self.ax_progress.transAxes, fontsize=12, color='gray')
            self.canvas_progress.draw()
            return
        categories = ["Underweight", "Normal", "Overweight", "Obese"]
        colors = ['#87CEEB', '#90EE90', '#FFD700', '#FF6B6B']
        bounds = [0, 18.5, 24.9, 29.9, 40]
        for i in range(len(categories)):
            self.ax_progress.axhspan(bounds[i], bounds[i+1], color=colors[i], alpha=0.3, label=categories[i])
        x = list(range(1, len(self.bmi_history)+1))
        self.ax_progress.plot(x, self.bmi_history, marker='o', color='blue', linewidth=2, markersize=8)
        if len(self.bmi_history) > 0:
            latest_bmi = self.bmi_history[-1]
            self.ax_progress.plot(x[-1], latest_bmi, marker='*', markersize=15, color='red', markeredgecolor='darkred', markeredgewidth=2)
        for line in [18.5, 24.9, 29.9]:
            self.ax_progress.axhline(y=line, color='black', linestyle='--', alpha=0.5)
        self.ax_progress.set_ylim(15, 35)
        self.ax_progress.set_xlim(0.5, max(len(self.bmi_history)+0.5, 2))
        self.ax_progress.set_title('BMI Progress Over Time', fontweight='bold', fontsize=12)
        self.ax_progress.set_xlabel('Measurement #')
        self.ax_progress.set_ylabel('BMI Value')
        self.ax_progress.grid(True, alpha=0.3)
        self.ax_progress.legend(loc='upper right', framealpha=0.8)
        self.ax_progress.set_facecolor('#f8f8f8')
        self.canvas_progress.draw()

def main():
    root = tk.Tk()
    app = BMICalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
