#!/usr/bin/env python3
"""
Simple Patent Trends Visualization Script
Reads patent data and generates comparison charts
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def load_data():
    """Load patent data from CSV files"""
    data_dir = Path(__file__).parent.parent / "data" / "patents"
    
    print("Loading patent data...")
    us_data = pd.read_csv(data_dir / "us-quantum-patents-2014-2024.csv")
    china_data = pd.read_csv(data_dir / "china-quantum-patents-2014-2024.csv")
    
    print(f"Loaded US data: {len(us_data)} years")
    print(f"Loaded China data: {len(china_data)} years")
    
    return us_data, china_data

def create_comparison_chart(us_data, china_data):
    """Create patent comparison visualization"""
    
    # Set up the plot
    plt.style.use('default')  # Use default style for compatibility
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle('US vs China Quantum Technology Patents (2014-2024)', fontsize=16, fontweight='bold')
    
    # Chart 1: Total Patents Over Time
    ax1.plot(us_data['Year'], us_data['Total_Patents'], 'b-o', 
             label='United States', linewidth=3, markersize=8)
    ax1.plot(china_data['Year'], china_data['Total_Patents'], 'r-s', 
             label='China', linewidth=3, markersize=8)
    
    ax1.set_title('Total Patent Applications by Year', fontsize=14)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Number of Patents')
    ax1.legend(fontsize=12)
    ax1.grid(True, alpha=0.3)
    
    # Add some styling
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Chart 2: 2023 Technology Breakdown (avoiding 2024 due to publication delays)
    categories = ['Quantum\nComputing', 'Quantum\nCommunications', 'Quantum\nSensing']
    us_2023 = [us_data[us_data['Year'] == 2023]['Quantum_Computing'].iloc[0],
               us_data[us_data['Year'] == 2023]['Quantum_Communications'].iloc[0],
               us_data[us_data['Year'] == 2023]['Quantum_Sensing'].iloc[0]]
    china_2023 = [china_data[china_data['Year'] == 2023]['Quantum_Computing'].iloc[0],
                  china_data[china_data['Year'] == 2023]['Quantum_Communications'].iloc[0],
                  china_data[china_data['Year'] == 2023]['Quantum_Sensing'].iloc[0]]
    
    x = np.arange(len(categories))
    width = 0.35
    
    bars1 = ax2.bar(x - width/2, us_2023, width, label='United States', 
                    color='steelblue', alpha=0.8)
    bars2 = ax2.bar(x + width/2, china_2023, width, label='China', 
                    color='crimson', alpha=0.8)
    
    ax2.set_title('Patents by Technology Category (2023)', fontsize=14)
    ax2.set_xlabel('Technology Category')
    ax2.set_ylabel('Number of Patents')
    ax2.set_xticks(x)
    ax2.set_xticklabels(categories)
    ax2.legend(fontsize=12)
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for bar in bars1:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 10,
                f'{int(height)}', ha='center', va='bottom', fontsize=10)
    
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 10,
                f'{int(height)}', ha='center', va='bottom', fontsize=10)
    
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    
    plt.tight_layout()
    
    # Save the chart
    output_dir = Path(__file__).parent / "visualizations"
    output_dir.mkdir(exist_ok=True)
    
    output_file = output_dir / "patent_trends_comparison.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    
    print(f"\n✅ Chart saved to: {output_file}")
    plt.show()
    
    return output_file

def print_key_statistics(us_data, china_data):
    """Print key statistics from the data"""
    
    print("\n" + "="*50)
    print("KEY PATENT STATISTICS (2014-2023)")
    print("="*50)
    
    # Use 2023 data to avoid publication delay issues
    us_2023 = us_data[us_data['Year'] == 2023].iloc[0]
    china_2023 = china_data[china_data['Year'] == 2023].iloc[0]
    
    us_2014 = us_data[us_data['Year'] == 2014].iloc[0]
    china_2014 = china_data[china_data['Year'] == 2014].iloc[0]
    
    print(f"\n📊 TOTAL PATENTS (2023):")
    print(f"   United States: {us_2023['Total_Patents']:,} patents")
    print(f"   China: {china_2023['Total_Patents']:,} patents")
    print(f"   China leads by: {china_2023['Total_Patents']/us_2023['Total_Patents']:.1f}x")
    
    print(f"\n🚀 GROWTH (2014-2023):")
    us_growth = (us_2023['Total_Patents'] / us_2014['Total_Patents'] - 1) * 100
    china_growth = (china_2023['Total_Patents'] / china_2014['Total_Patents'] - 1) * 100
    
    print(f"   US Growth: {us_growth:.0f}%")
    print(f"   China Growth: {china_growth:.0f}%")
    
    print(f"\n🔬 TECHNOLOGY BREAKDOWN (2023):")
    print(f"   Quantum Computing:")
    print(f"      US: {us_2023['Quantum_Computing']:,} | China: {china_2023['Quantum_Computing']:,}")
    print(f"   Quantum Communications:")  
    print(f"      US: {us_2023['Quantum_Communications']:,} | China: {china_2023['Quantum_Communications']:,}")
    print(f"   Quantum Sensing:")
    print(f"      US: {us_2023['Quantum_Sensing']:,} | China: {china_2023['Quantum_Sensing']:,}")

def main():
    """Main function to run the analysis"""
    
    print("🚀 Quantum Patent Trends Analysis")
    print("="*40)
    
    # Load data
    us_data, china_data = load_data()
    
    # Create visualization
    chart_file = create_comparison_chart(us_data, china_data)
    
    # Print statistics
    print_key_statistics(us_data, china_data)
    
    print(f"\n🎉 Analysis complete!")
    print(f"📈 Chart saved to: {chart_file}")
    print(f"\nThis script demonstrates:")
    print(f"✓ Reading CSV data with pandas")
    print(f"✓ Creating professional visualizations")
    print(f"✓ Statistical analysis and comparison")
    print(f"✓ Automated chart generation")

if __name__ == "__main__":
    main()