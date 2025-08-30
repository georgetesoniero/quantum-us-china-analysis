#!/usr/bin/env python3
"""
Simple Patent Chart Generator - No GUI Display
Generates PNG charts without requiring display
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def main():
    """Generate patent comparison chart"""
    
    print("🚀 Generating Quantum Patent Trends Chart...")
    
    # Load data
    data_dir = Path(__file__).parent.parent / "data" / "patents"
    us_data = pd.read_csv(data_dir / "us-quantum-patents-2014-2024.csv")
    china_data = pd.read_csv(data_dir / "china-quantum-patents-2014-2024.csv")
    
    print(f"✓ Loaded data: {len(us_data)} years each for US and China")
    
    # Create chart
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle('US vs China Quantum Technology Patents (2014-2024)', fontsize=16, fontweight='bold')
    
    # Chart 1: Total Patents Over Time
    ax1.plot(us_data['Year'], us_data['Total_Patents'], 'b-o', 
             label='United States', linewidth=3, markersize=6)
    ax1.plot(china_data['Year'], china_data['Total_Patents'], 'r-s', 
             label='China', linewidth=3, markersize=6)
    
    ax1.set_title('Total Patent Applications by Year')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Number of Patents')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Chart 2: 2023 Technology Breakdown
    categories = ['Computing', 'Communications', 'Sensing']
    us_2023 = [530, 115, 75]  # 2023 data from our dataset
    china_2023 = [465, 755, 236]  # 2023 data from our dataset
    
    x = np.arange(len(categories))
    width = 0.35
    
    ax2.bar(x - width/2, us_2023, width, label='United States', color='steelblue', alpha=0.8)
    ax2.bar(x + width/2, china_2023, width, label='China', color='crimson', alpha=0.8)
    
    ax2.set_title('Patents by Technology Category (2023)')
    ax2.set_xlabel('Technology Category')
    ax2.set_ylabel('Number of Patents')
    ax2.set_xticks(x)
    ax2.set_xticklabels(categories)
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Add source citation
    fig.text(0.5, 0.02, 'Sources: PatentsView (USPTO), CNIPA, WIPO | Analysis: Quantum US-China Competition Study (2024)', 
             ha='center', fontsize=10, style='italic')
    
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.1)  # Make room for citation
    
    # Save chart
    output_dir = Path(__file__).parent / "visualizations"
    output_dir.mkdir(exist_ok=True)
    
    output_file = output_dir / "patent_trends_simple.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    
    print(f"✅ Chart saved successfully to: {output_file}")
    
    # Print key stats
    print("\n📊 KEY STATISTICS:")
    print(f"   2023 Total Patents - US: {us_data[us_data['Year']==2023]['Total_Patents'].iloc[0]:,}")
    print(f"   2023 Total Patents - China: {china_data[china_data['Year']==2023]['Total_Patents'].iloc[0]:,}")
    print(f"   China leads by {china_data[china_data['Year']==2023]['Total_Patents'].iloc[0]/us_data[us_data['Year']==2023]['Total_Patents'].iloc[0]:.1f}x")
    
    return output_file

if __name__ == "__main__":
    main()