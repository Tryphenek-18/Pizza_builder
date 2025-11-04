# Pizza Builder Pro 🍕

A comprehensive Python application for building custom pizzas with advanced nutritional analysis, secure user authentication, and interactive visualizations.

## Features

### 🔐 Secure Authentication
- User registration and login system
- SHA-256 password hashing with salt
- Persistent user data storage

### 🍕 Custom Pizza Building
- Interactive ingredient selection
- Real-time nutritional calculations
- Ingredient management with emojis

### 📊 Advanced Nutritional Analysis
- **NumPy-powered calculations**: Matrix operations, statistical analysis
- Macronutrient breakdown (protein, fat, carbs)
- Calorie tracking with daily goal comparison
- Standard deviation and mean calculations

### 📈 Interactive Visualizations
- **3-panel Matplotlib dashboard**:
  - Pie chart: Macronutrient distribution in grams
  - Bar chart: Macronutrient amounts with value labels
  - Bar chart: Calorie distribution percentages with goal lines
- Real-time chart updates
- Visual feedback on ingredient changes

### 💾 Data Export
- **Save recipes**: Export to JSON format
- **Export data**: Comprehensive CSV reports with nutritional analysis

### 🎨 Modern UI
- Responsive Tkinter interface
- Themed widgets with custom styles
- Emoji-enhanced ingredient display
- User-specific personalization

## Technical Stack

- **GUI Framework**: Tkinter with ttk themed widgets
- **Data Processing**: NumPy for advanced mathematical operations
- **Visualization**: Matplotlib with interactive features
- **Security**: hashlib for password encryption
- **Data Persistence**: JSON for user data and recipes
- **File Operations**: CSV export functionality

## Installation

1. Ensure you have Python 3.7+ installed
2. Install required dependencies:
   ```bash
   pip install numpy matplotlib
   ```

## Usage

1. Run the application:
   ```bash
   python pizza.py
   ```

2. **First-time users**: Register with a username and password
3. **Returning users**: Login with your credentials
4. Build your pizza by selecting ingredients from the list
5. View real-time nutritional analysis and visualizations
6. Save recipes or export data for further analysis

## File Structure

- `pizza.py` - Main application file with all functionality
- `README.md` - This documentation file

## Key Components

### User Management
- `UserManager` class handles authentication and user data
- Secure password storage with salt-based hashing
- JSON-based user data persistence

### Pizza Builder Application
- `PizzaBuilderApp` class manages the main interface
- Ingredient selection and nutritional calculations
- Real-time updates and visualizations

### Data Analysis
- Advanced NumPy operations for nutritional metrics
- Matrix calculations for ingredient combinations
- Statistical analysis (mean, standard deviation)

### Visualization Engine
- Interactive Matplotlib charts with tooltips
- Real-time updates on ingredient changes
- Professional styling and annotations

## Security Features

- **Password Security**: SHA-256 hashing with unique salt per user
- **Data Validation**: Input sanitization and error handling
- **Session Management**: User-specific application instances

## Nutritional Metrics Calculated

- Total calories
- Protein, fat, and carbohydrate content
- Macronutrient percentages
- Comparison to daily calorie goals
- Statistical analysis of nutritional values



### CSV Data Export
- Comprehensive nutritional breakdown
- Ingredient-specific data
- Statistical metrics
- Timestamp and user information

## Customization

The application supports:
- Custom ingredient lists
- Adjustable daily calorie goals
- Personalized user preferences
- Theme and style modifications

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request


## Support

For issues or questions, please check the code comments or create an issue in the repository.

---

**Built with ❤️ using Python, Tkinter, NumPy, and Matplotlib**
