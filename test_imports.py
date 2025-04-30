# Simple test script to verify imports
print("Starting import test...")

try:
    print("Importing dotenv...")
    from dotenv import load_dotenv
    print("✓ dotenv imported successfully")
    
    print("Loading environment variables...")
    load_dotenv()
    print("✓ Environment loaded")
    
    print("Importing pydantic...")
    import pydantic
    print(f"✓ pydantic {pydantic.__version__} imported successfully")
    
    print("Importing langchain_openai...")
    import langchain_openai
    print("✓ langchain_openai imported successfully")
    
    print("Importing crewai...")
    from crewai import Agent, Crew, Task
    print("✓ crewai core classes imported successfully")
    
    print("Importing crewai_tools...")
    from crewai_tools import DuckDuckGoSearchRunTool
    print("✓ crewai_tools imported successfully")
    
    print("\nAll imports successful!")
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Other error: {e}")
