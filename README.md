# BiteWise
ChatGPT said: BiteWise is your smart command-line sous-chef—fetching recipes, nutrition facts, and step-by-step guides straight to your terminal, complete with mouthwatering images.

This Hackaton version for the [BOOT.DEV Hackathon 2025](https://blog.boot.dev/news/hackathon-2025/) is currently reliant on an GEMINI API KEY follow the installation steps to set everything up correctly.

## Installation

1. Clone the repository to your environment an move into the directory
```bash
git clone https://github.com/LS-2ednar/BiteWise
```
```bash
cd BiteWise
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

5. Ensure you have an Gemini API Key this is a free plan option. You will need to create an account here: [https://aistudio.google.com](https://aistudio.google.com). When you finished createing your account you should be able to create a API Keye here: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey) then click the "Create API Key" button. Check out the [docs](https://ai.google.dev/gemini-api/docs/api-key?hl=en) if you struggle.

6. Create an ```.env``` file 
```bash
touch .env
```

and add the key as follows

```bash
GEMINI_API_KEY="your_api_key_here"
```

7. Checkout the demo
```bash
python BiteWise.py --demo
```
## How to use BiteWise?



## Future improvements
- Fetch Nutrion Data from an API e.g. [Edamam Food and Nutrion API](https://developer.edamam.com/edamam-docs-nutrition-api) , [Spoonacular API](https://spoonacular.com/food-api) or [USDA FoodData Central](https://fdc.nal.usda.gov/api-guide) rather then dealing with LLM hallucinations.
- Create a Mealplanner ?
- Optimize Foodchoices ?
- Optimize the prompts to be 100% hallucination free (We all wish that would be true)