# BiteWise
ChatGPT said: BiteWise is your smart command-line sous-chef—fetching recipes, nutrition facts, and step-by-step guides straight to your terminal, complete with mouthwatering images.

This Hackaton version is currently reliant on an GEMINI API KEY.

## Installation

1. Clone the repository to your environment
```bash
git clone https://github.com/LS-2ednar/BiteWise
```

2. Create a new python environment for this project.
```bash
python -m venv venv
```

or

```bash
python3 -m venv venv
```

3. Set the environment as your new source
```bash
source venv/bin/activate
```

4. Install the requirements
```bash
pip install -r requirements.txt
```

5. Run the script for the first time.
```bash
python BiteWise.py --init
```

6. Checkout the demo
```bash
python BiteWise.py --demo
```

## Future improvements
- Fetch Nutrion Data from another API e.g. [Edamam Food and Nutrion API](https://developer.edamam.com/edamam-docs-nutrition-api) , [Spoonacular API](https://spoonacular.com/food-api) or [USDA FoodData Central](https://fdc.nal.usda.gov/api-guide)