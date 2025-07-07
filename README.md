# AI Essay Generator

A simple Python project that helps you generate research essays or summaries using AI and Wikipedia. Built with LangChain and supports OpenAI/Anthropic APIs.

---

## Features

- Generate research essays or summaries on any topic
- Automatically pulls facts from Wikipedia and LLMs
- Easy to customize and extend with your own tools

---

## Setup

1. **(Optional but recommended) Create a virtual environment:**

    ```
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. **Install dependencies:**

    ```
    pip install -r requirements.txt
    ```

3. **Add your API keys:**

    - Create a file called `.env` in the project folder.
    - Add your API keys like this:
      ```
      OPENAI_API_KEY=your-openai-key
      ANTHROPIC_API_KEY=your-anthropic-key
      ```
    - Only add the keys you need.

4. **Run the project:**

    ```
    python main.py
    ```

---

## Example

After setup, run the project and follow any prompts to generate an essay or summary on your chosen topic.

---

## Notes

- **Keep your `.env` file private.**  
  Never upload your API keys or `.env` file to public repos.
- The `venv` folder is just for your local Python setup.

---

## Tech Stack

- Python 3.9+
- LangChain
- Wikipedia
- OpenAI or Anthropic (for LLMs)
- dotenv for API key management

---

## License

MIT

