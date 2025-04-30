print("Starting minimal test...")

try:
    print("Importing crewai...")
    import crewai
    print("✓ crewai imported successfully")
    
    print("\nEverything works!")
except Exception as e:
    import traceback
    print(f"❌ Error: {e}")
    traceback.print_exc()
