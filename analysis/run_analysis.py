#!/usr/bin/env python3
"""
Master script to run all quantum technology analyses
Executes patent trends and funding comparison scripts
"""

import sys
from pathlib import Path
import subprocess

def run_script(script_name):
    """Run a Python script and handle errors"""
    script_path = Path(__file__).parent / script_name
    
    print(f"\n{'='*60}")
    print(f"Running {script_name}")
    print('='*60)
    
    try:
        result = subprocess.run([sys.executable, str(script_path)], 
                              capture_output=True, text=True, check=True)
        print(result.stdout)
        if result.stderr:
            print("Warnings/Errors:", result.stderr)
        print(f"✅ {script_name} completed successfully")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running {script_name}:")
        print(f"Return code: {e.returncode}")
        print(f"Error output: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error running {script_name}: {e}")
        return False
    
    return True

def main():
    """Run all analysis scripts"""
    print("🚀 Starting Quantum Technology Analysis Suite")
    print("Analyzing US vs China patent and funding competition (2014-2024)")
    
    scripts = [
        "patent-trends-analysis.py",
        "funding-comparison.py"
    ]
    
    success_count = 0
    total_scripts = len(scripts)
    
    for script in scripts:
        if run_script(script):
            success_count += 1
    
    print(f"\n{'='*60}")
    print("ANALYSIS COMPLETE")
    print('='*60)
    print(f"✅ {success_count}/{total_scripts} scripts completed successfully")
    
    if success_count == total_scripts:
        print("🎉 All analyses completed! Check the visualizations folder for charts.")
        print("\n📊 Generated files:")
        print("  - patent_trends_comparison.png")
        print("  - funding_analysis_comprehensive.png") 
        print("  - investment_strategy_comparison.png")
        print("\n📖 View reports in the /reports folder:")
        print("  - executive-summary.md")
        print("  - detailed-findings.md")
        print("  - methodology.md")
    else:
        print("⚠️  Some analyses failed. Check error messages above.")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)