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

5. Create a .gitignore file to ensure you are not sharing your private keys with anyone!
```bash
touch .gitignore
```

then copy the following information into the file
```bash
venv
.env
```

6. Ensure you have an Gemini API Key this is a free plan option. You will need to create an account here: [https://aistudio.google.com](https://aistudio.google.com). When you finished createing your account you should be able to create a API Keye here: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey) then click the "Create API Key" button. Check out the [docs](https://ai.google.dev/gemini-api/docs/api-key?hl=en) if you struggle.

7. Create an ```.env``` file and add the key as follows.
```bash
GEMINI_API_KEY="your_api_key_here"
```

8. Checkout the demo
```bash
python BiteWise.py --demo
```
## How to use BiteWise?



## Future improvements
- Fetch Nutrion Data from another API e.g. [Edamam Food and Nutrion API](https://developer.edamam.com/edamam-docs-nutrition-api) , [Spoonacular API](https://spoonacular.com/food-api) or [USDA FoodData Central](https://fdc.nal.usda.gov/api-guide)