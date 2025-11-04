"""
Pizza Builder Stats Application
Creates custom pizzas with nutritional statistics and visualizations.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class PizzaIngredient:
    """Represents a pizza ingredient with nutritional information."""
    
    def __init__(self, name, calories, protein, fat, carbs):
        """
        Initialize an ingredient.
        
        Args:
            name (str): Ingredient name
            calories (float): Calories per serving
            protein (float): Protein in grams
            fat (float): Fat in grams
            carbs (float): Carbohydrates in grams
        """
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
    
    def get_nutrition_array(self):
        """Returns nutritional values as a NumPy array."""
        return np.array([self.calories, self.protein, self.fat, self.carbs])


class PizzaBuilderApp:
    """Main application class for Pizza Builder."""
    
    def __init__(self, root):
        """Initialize the Pizza Builder application."""
        self.root = root
        self.root.title("Pizza Builder Stats")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        
        # Define available ingredients with nutritional data
        self.ingredients = {
            "Pizza Dough": PizzaIngredient("Pizza Dough", 266, 9, 1, 53),
            "Tomato Sauce": PizzaIngredient("Tomato Sauce", 29, 1.5, 0.5, 6),
            "Mozzarella": PizzaIngredient("Mozzarella", 280, 24, 21, 3),
            "Pepperoni": PizzaIngredient("Pepperoni", 494, 20, 44, 2),
            "Mushrooms": PizzaIngredient("Mushrooms", 22, 3, 0.3, 3.3),
            "Bell Peppers": PizzaIngredient("Bell Peppers", 31, 1, 0.3, 6),
            "Onions": PizzaIngredient("Onions", 40, 1.1, 0.1, 9.3),
            "Olives": PizzaIngredient("Olives", 115, 0.8, 11, 6),
            "Ham": PizzaIngredient("Ham", 145, 21, 6, 1.5),
            "Basil": PizzaIngredient("Basil", 23, 3, 0.6, 2.7),
            "Parmesan": PizzaIngredient("Parmesan", 431, 38, 29, 4),
            "Chicken": PizzaIngredient("Chicken", 165, 31, 3.6, 0)
        }
        
        # Checkbox variables
        self.checkbox_vars = {}
        
        # Create UI
        self._create_widgets()
        
    def _create_widgets(self):
        """Create and layout all UI widgets."""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text="🍕 Build Your Pizza", 
            font=("Arial", 20, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Ingredients section
        ingredients_frame = ttk.LabelFrame(
            main_frame, 
            text="Select Ingredients", 
            padding="10"
        )
        ingredients_frame.grid(row=1, column=0, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create checkboxes for each ingredient
        row_idx = 0
        col_idx = 0
        for ingredient_name in self.ingredients.keys():
            var = tk.BooleanVar()
            self.checkbox_vars[ingredient_name] = var
            
            checkbox = ttk.Checkbutton(
                ingredients_frame,
                text=ingredient_name,
                variable=var,
                command=self._update_stats
            )
            checkbox.grid(row=row_idx, column=col_idx, sticky=tk.W, padx=5, pady=3)
            
            row_idx += 1
            if row_idx >= 6:
                row_idx = 0
                col_idx += 1
        
        # Statistics section
        stats_frame = ttk.LabelFrame(
            main_frame, 
            text="Nutritional Stats", 
            padding="10"
        )
        stats_frame.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Stats labels
        self.calories_label = ttk.Label(
            stats_frame, 
            text="Total Calories: 0 kcal", 
            font=("Arial", 12)
        )
        self.calories_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        
        self.protein_label = ttk.Label(
            stats_frame, 
            text="Protein: 0 g", 
            font=("Arial", 12)
        )
        self.protein_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.fat_label = ttk.Label(
            stats_frame, 
            text="Fat: 0 g", 
            font=("Arial", 12)
        )
        self.fat_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        
        self.carbs_label = ttk.Label(
            stats_frame, 
            text="Carbohydrates: 0 g", 
            font=("Arial", 12)
        )
        self.carbs_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        
        # Chart frame
        chart_frame = ttk.LabelFrame(
            main_frame, 
            text="Macronutrient Distribution", 
            padding="10"
        )
        chart_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create matplotlib figure
        self.figure = Figure(figsize=(8, 4), dpi=80)
        self.canvas = FigureCanvasTkAgg(self.figure, chart_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        reset_button = ttk.Button(
            button_frame,
            text="Reset Pizza",
            command=self._reset_pizza
        )
        reset_button.pack(side=tk.LEFT, padx=5)
        
        quit_button = ttk.Button(
            button_frame,
            text="Quit",
            command=self.root.quit
        )
        quit_button.pack(side=tk.LEFT, padx=5)
        
    def _calculate_nutrition(self):
        """
        Calculate total nutritional values using NumPy.
        
        Returns:
            tuple: (calories, protein, fat, carbs) as floats
        """
        # Create a list to store nutrition arrays for selected ingredients
        selected_ingredients = []
        
        for ingredient_name, is_selected in self.checkbox_vars.items():
            if is_selected.get():
                ingredient = self.ingredients[ingredient_name]
                selected_ingredients.append(ingredient.get_nutrition_array())
        
        # If no ingredients selected, return zeros
        if not selected_ingredients:
            return 0.0, 0.0, 0.0, 0.0
        
        # Stack arrays and sum along axis 0 using NumPy
        nutrition_matrix = np.vstack(selected_ingredients)
        totals = np.sum(nutrition_matrix, axis=0)
        
        return totals[0], totals[1], totals[2], totals[3]
    
    def _update_stats(self):
        """Update nutritional statistics and chart."""
        calories, protein, fat, carbs = self._calculate_nutrition()
        
        # Update labels
        self.calories_label.config(text=f"Total Calories: {calories:.1f} kcal")
        self.protein_label.config(text=f"Protein: {protein:.1f} g")
        self.fat_label.config(text=f"Fat: {fat:.1f} g")
        self.carbs_label.config(text=f"Carbohydrates: {carbs:.1f} g")
        
        # Update chart
        self._update_chart(protein, fat, carbs)
    
    def _update_chart(self, protein, fat, carbs):
        """
        Update the macronutrient distribution chart.
        
        Args:
            protein (float): Protein in grams
            fat (float): Fat in grams
            carbs (float): Carbohydrates in grams
        """
        self.figure.clear()
        
        # Check if there's data to display
        total = protein + fat + carbs
        if total == 0:
            # Display empty chart with message
            ax = self.figure.add_subplot(111)
            ax.text(
                0.5, 0.5, 
                'Select ingredients to see distribution', 
                ha='center', 
                va='center',
                fontsize=12
            )
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
        else:
            # Create pie chart
            labels = ['Protein', 'Fat', 'Carbohydrates']
            sizes = np.array([protein, fat, carbs])
            colors = ['#FF6B6B', '#4ECDC4', '#FFE66D']
            explode = (0.05, 0.05, 0.05)
            
            ax = self.figure.add_subplot(121)
            ax.pie(
                sizes, 
                explode=explode, 
                labels=labels, 
                colors=colors,
                autopct='%1.1f%%',
                shadow=True, 
                startangle=90
            )
            ax.set_title('Pie Chart')
            
            # Create bar chart
            ax2 = self.figure.add_subplot(122)
            x_pos = np.arange(len(labels))
            ax2.bar(x_pos, sizes, color=colors, alpha=0.8)
            ax2.set_ylabel('Grams (g)', fontsize=10)
            ax2.set_title('Bar Chart')
            ax2.set_xticks(x_pos)
            ax2.set_xticklabels(labels, rotation=15, ha='right')
            ax2.grid(axis='y', alpha=0.3)
        
        self.figure.tight_layout()
        self.canvas.draw()
    
    def _reset_pizza(self):
        """Reset all ingredient selections."""
        for var in self.checkbox_vars.values():
            var.set(False)
        self._update_stats()


def main():
    """Main entry point for the application."""
    root = tk.Tk()
    app = PizzaBuilderApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
