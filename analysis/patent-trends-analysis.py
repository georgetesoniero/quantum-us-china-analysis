#!/usr/bin/env python3
"""
Quantum Technology Patent Trends Analysis
Analyzes US vs China patent filing trends from 2014-2024
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

def load_patent_data():
    """Load patent data from CSV files"""
    data_dir = Path(__file__).parent.parent / "data" / "patents"
    
    us_data = pd.read_csv(data_dir / "us-quantum-patents-2014-2024.csv")
    china_data = pd.read_csv(data_dir / "china-quantum-patents-2014-2024.csv")
    
    return us_data, china_data

def create_comparison_plots(us_data, china_data):
    """Create comparative analysis plots"""
    
    # Set up the plotting style
    plt.style.use('seaborn-v0_8')
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('US vs China Quantum Technology Patents (2014-2024)', fontsize=16, fontweight='bold')
    
    # Plot 1: Total Patents Over Time
    axes[0, 0].plot(us_data['Year'], us_data['Total_Patents'], 'b-o', label='United States', linewidth=3)
    axes[0, 0].plot(china_data['Year'], china_data['Total_Patents'], 'r-s', label='China', linewidth=3)
    axes[0, 0].set_title('Total Patent Applications by Year')
    axes[0, 0].set_xlabel('Year')
    axes[0, 0].set_ylabel('Number of Patents')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # Plot 2: Technology Category Breakdown (2024)
    categories = ['Quantum_Computing', 'Quantum_Communications', 'Quantum_Sensing']
    us_2024 = us_data[us_data['Year'] == 2024][categories].iloc[0].values
    china_2024 = china_data[china_data['Year'] == 2024][categories].iloc[0].values
    
    x = np.arange(len(categories))
    width = 0.35
    
    axes[0, 1].bar(x - width/2, us_2024, width, label='United States', color='blue', alpha=0.7)
    axes[0, 1].bar(x + width/2, china_2024, width, label='China', color='red', alpha=0.7)
    axes[0, 1].set_title('Patents by Technology Category (2024)')
    axes[0, 1].set_xlabel('Technology Category')
    axes[0, 1].set_ylabel('Number of Patents')
    axes[0, 1].set_xticks(x)
    axes[0, 1].set_xticklabels(['Computing', 'Communications', 'Sensing'])
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # Plot 3: Quantum Computing Patents Trend
    axes[1, 0].plot(us_data['Year'], us_data['Quantum_Computing'], 'b-o', label='US Computing', linewidth=3)
    axes[1, 0].plot(china_data['Year'], china_data['Quantum_Computing'], 'r-s', label='China Computing', linewidth=3)
    axes[1, 0].set_title('Quantum Computing Patents')
    axes[1, 0].set_xlabel('Year')
    axes[1, 0].set_ylabel('Number of Patents')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # Plot 4: Quantum Communications Patents Trend
    axes[1, 1].plot(us_data['Year'], us_data['Quantum_Communications'], 'b-o', label='US Communications', linewidth=3)
    axes[1, 1].plot(china_data['Year'], china_data['Quantum_Communications'], 'r-s', label='China Communications', linewidth=3)
    axes[1, 1].set_title('Quantum Communications Patents')
    axes[1, 1].set_xlabel('Year')
    axes[1, 1].set_ylabel('Number of Patents')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save the plot
    output_dir = Path(__file__).parent / "visualizations"
    output_dir.mkdir(exist_ok=True)
    plt.savefig(output_dir / "patent_trends_comparison.png", dpi=300, bbox_inches='tight')
    plt.show()

def calculate_growth_rates(us_data, china_data):
    """Calculate and display growth rate statistics"""
    
    print("=== PATENT GROWTH ANALYSIS ===\n")
    
    # Calculate CAGR (Compound Annual Growth Rate)
    def cagr(start_value, end_value, years):
        return (end_value / start_value) ** (1/years) - 1
    
    # US Growth Rates
    us_start = us_data[us_data['Year'] == 2014]['Total_Patents'].iloc[0]
    us_end = us_data[us_data['Year'] == 2023]['Total_Patents'].iloc[0]  # Use 2023 due to 2024 publication delays
    us_cagr = cagr(us_start, us_end, 9)
    
    # China Growth Rates
    china_start = china_data[china_data['Year'] == 2014]['Total_Patents'].iloc[0]
    china_end = china_data[china_data['Year'] == 2023]['Total_Patents'].iloc[0]
    china_cagr = cagr(china_start, china_end, 9)
    
    print(f"United States CAGR (2014-2023): {us_cagr:.1%}")
    print(f"China CAGR (2014-2023): {china_cagr:.1%}")
    print(f"China growth rate is {china_cagr/us_cagr:.1f}x faster than US\n")
    
    # Technology-specific analysis for 2023
    us_2023 = us_data[us_data['Year'] == 2023].iloc[0]
    china_2023 = china_data[china_data['Year'] == 2023].iloc[0]
    
    print("=== 2023 TECHNOLOGY LEADERSHIP ===\n")
    print(f"Quantum Computing:")
    print(f"  US: {us_2023['Quantum_Computing']:,} patents")
    print(f"  China: {china_2023['Quantum_Computing']:,} patents")
    print(f"  China leads by {china_2023['Quantum_Computing']/us_2023['Quantum_Computing']:.1f}x\n")
    
    print(f"Quantum Communications:")
    print(f"  US: {us_2023['Quantum_Communications']:,} patents") 
    print(f"  China: {china_2023['Quantum_Communications']:,} patents")
    print(f"  China leads by {china_2023['Quantum_Communications']/us_2023['Quantum_Communications']:.1f}x\n")
    
    print(f"Quantum Sensing:")
    print(f"  US: {us_2023['Quantum_Sensing']:,} patents")
    print(f"  China: {china_2023['Quantum_Sensing']:,} patents") 
    print(f"  China leads by {china_2023['Quantum_Sensing']/us_2023['Quantum_Sensing']:.1f}x\n")

def main():
    """Main analysis function"""
    print("Loading patent data...")
    us_data, china_data = load_patent_data()
    
    print("Creating comparison plots...")
    create_comparison_plots(us_data, china_data)
    
    print("Calculating growth rates...")
    calculate_growth_rates(us_data, china_data)
    
    print("\nAnalysis complete! Check the visualizations folder for charts.")

if __name__ == "__main__":
    main()