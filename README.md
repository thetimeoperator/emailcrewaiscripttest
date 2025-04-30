# CrewAI Email Newsletter Automation

## Project Overview
An automated email newsletter generator built with CrewAI that uses AI agents to research, summarize, and draft content for email newsletters.

## Technical Requirements
- Python 3.12
- Microsoft C++ Build Tools (for Windows)
- OpenAI API Key

## Environment Setup

### 1. Create and Activate Virtual Environment
```powershell
uv venv
.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies
```powershell
uv pip sync pyproject.toml
```

### 3. Configure Environment Variables
Create or modify `.env` file with your API keys:
```
OPENAI_API_KEY="your-api-key-here"
# Optional: Specify OpenAI model (e.g., gpt-4-turbo or gpt-3.5-turbo)
# OPENAI_MODEL_NAME='gpt-4-turbo'
```

## Project Structure
```
CrewAI - Email Newsletter/
├── .env                  # Environment variables
├── .venv/                # Virtual environment
├── pyproject.toml        # Project dependencies
├── README.md             # Project documentation
├── src/
│   ├── __init__.py
│   ├── main.py           # Entry point
│   ├── crew.py           # Agent definitions and crew assembly
│   ├── config/
│   │   ├── agents.yaml   # Agent role configurations
│   │   └── tasks.yaml    # Task definitions
│   └── tools/            # Custom tools directory
```

## Running the Application

**IMPORTANT:** Due to Windows encoding compatibility, the application must be run in UTF-8 mode:

```powershell
.\.venv\Scripts\python.exe -X utf8 src/main.py
```

Failure to use UTF-8 mode will result in `UnicodeDecodeError` exceptions when the application attempts to load JSON files with non-ASCII characters.

## Project Status
- ✅ Environment setup complete
- ✅ Project structure established
- ✅ Dependencies resolved
- ✅ Basic agent skeleton implemented
- 🔄 Agent implementation in progress
- 🔄 Task sequence implementation in progress

## Local Project Rules

### Coding Standards
1. Always run Python in UTF-8 mode (`-X utf8` flag) on Windows
2. Keep sensitive information in `.env` file, never hardcode API keys
3. Follow the agent-task pattern established in the CrewAI framework
4. Use descriptive names for agents and tasks that reflect their function
5. Store configuration in YAML files when possible for better maintainability

### Development Workflow
1. Test agent functionality individually before integration
2. Use sequential processing for the newsletter generation pipeline
3. Document any custom tools in code comments
4. Maintain clear separation between research, summarization, and writing phases

## Technical Notes
- The project uses a three-agent model: researcher, summarizer, and writer
- The workflow follows a sequential process: research → summarize → write
- Configuration is driven through YAML files for flexible agent and task definitions
- Dotenv is used for environment variable management
- CrewAI handles agent orchestration and communication
