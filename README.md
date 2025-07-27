# BiteWise
ChatGPT said: BiteWise is your smart command-line sous-chef—fetching recipes, nutrition facts, and step-by-step guides straight to your terminal, complete with mouthwatering images.

This Hackathon version for the [BOOT.DEV Hackathon 2025](https://blog.boot.dev/news/hackathon-2025/) currently relies on a GEMINI API key. Follow the installation steps to set everything up correctly.

## Installation

1. Clone the repository and move into the project directory:
```bash
git clone https://github.com/LS-2ednar/BiteWise
```
```bash
cd BiteWise
```

2. Create a new Python virtual environment for this project:
```bash
python -m venv venv
```

or

```bash
python3 -m venv venv
```

3. Activate the virtual environment:
```bash
source venv/bin/activate
```

4. Install the required dependencies:
```bash
pip install -r requirements.txt
```

5. Optain a Gemini API key (a free plan is available).
- First, create an account here: [https://aistudio.google.com](https://aistudio.google.com). 
- Once your account is set up, generate your API key here: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey) by clicking the "Create API Key" button. 
- If you encounter any issues, consult the [official docmentation](https://ai.google.dev/gemini-api/docs/api-key?hl=en) if you struggle.

6. Create an ```.env``` file: 
```bash
touch .env
```

Add the following line to your ```.env``` file: 

```bash
GEMINI_API_KEY="your_api_key_here"
```

7. Try out the demo
```bash
python BiteWise.py --demo
```
## How to use BiteWise?

- Fetch your favorit dish's recipe:
```bash
python BiteWise.py --recipie "YOUR DISH OF CHOICE"
```

- Fetch nutrition values for your favorit dish:
```bash
python BiteWise.py --nutrition "YOUR DISH OF CHOICE"
```

- Never heard of that dish before? Preview it right in your terminal:
```bash
python BiteWise.py --image "YOUR DISH OF CHOICE"
```

- Run the demo:
```bash
python BiteWise.py --demo
```

- Need help?
```bash
python BiteWise.py --help
```

## Future improvements
- Fetch Nutrion Data from an API suchg as [Edamam Food and Nutrion API](https://developer.edamam.com/edamam-docs-nutrition-api) , [Spoonacular API](https://spoonacular.com/food-api) or [USDA FoodData Central](https://fdc.nal.usda.gov/api-guide), instead of relying solely on LLMs.
- Build a meal planner.
- Optimize food choices and recommendations
- Improve prompts to further reduce LLM hallucinations (we all wish this could be 100% guaranteed!).
- Cleaning up the code more.
- Make outputs prettier. 