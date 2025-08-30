#!/usr/bin/env python3
"""
Quantum Technology Funding Comparison Analysis
Analyzes government and private sector funding patterns US vs China (2014-2024)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

def load_funding_data():
    """Load funding data from CSV files"""
    data_dir = Path(__file__).parent.parent / "data" / "funding"
    
    gov_data = pd.read_csv(data_dir / "government-investment-comparison.csv")
    private_data = pd.read_csv(data_dir / "private-sector-funding.csv")
    
    return gov_data, private_data

def create_funding_analysis_plots(gov_data, private_data):
    """Create comprehensive funding analysis visualizations"""
    
    plt.style.use('seaborn-v0_8')
    fig, axes = plt.subplots(2, 3, figsize=(20, 12))
    fig.suptitle('US vs China Quantum Technology Funding Analysis (2014-2024)', fontsize=16, fontweight='bold')
    
    # Plot 1: Annual Government Investment
    axes[0, 0].plot(gov_data['Year'], gov_data['US_Government_Millions'], 'b-o', label='US Government', linewidth=3)
    axes[0, 0].plot(gov_data['Year'], gov_data['China_Government_Millions'], 'r-s', label='China Government', linewidth=3)
    axes[0, 0].set_title('Annual Government Investment')
    axes[0, 0].set_xlabel('Year')
    axes[0, 0].set_ylabel('Investment (Millions USD)')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # Plot 2: Cumulative Government Investment
    axes[0, 1].plot(gov_data['Year'], gov_data['US_Cumulative_Millions'], 'b-o', label='US Cumulative', linewidth=3)
    axes[0, 1].plot(gov_data['Year'], gov_data['China_Cumulative_Millions'], 'r-s', label='China Cumulative', linewidth=3)
    axes[0, 1].set_title('Cumulative Government Investment')
    axes[0, 1].set_xlabel('Year')
    axes[0, 1].set_ylabel('Cumulative Investment (Millions USD)')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # Plot 3: Annual Private Investment
    axes[0, 2].plot(private_data['Year'], private_data['US_Private_Millions'], 'b-o', label='US Private', linewidth=3)
    axes[0, 2].plot(private_data['Year'], private_data['China_Private_Millions'], 'r-s', label='China Private', linewidth=3)
    axes[0, 2].set_title('Annual Private Sector Investment')
    axes[0, 2].set_xlabel('Year')
    axes[0, 2].set_ylabel('Investment (Millions USD)')
    axes[0, 2].legend()
    axes[0, 2].grid(True, alpha=0.3)
    
    # Plot 4: Total Investment Comparison (2024)
    categories = ['Government', 'Private', 'Total']
    us_final = [gov_data['US_Cumulative_Millions'].iloc[-1], 
               private_data['US_Private_Millions'].iloc[-1],
               gov_data['US_Cumulative_Millions'].iloc[-1] + private_data['US_Private_Millions'].iloc[-1]]
    china_final = [gov_data['China_Cumulative_Millions'].iloc[-1],
                  private_data['China_Private_Millions'].iloc[-1], 
                  gov_data['China_Cumulative_Millions'].iloc[-1] + private_data['China_Private_Millions'].iloc[-1]]
    
    x = np.arange(len(categories))
    width = 0.35
    
    axes[1, 0].bar(x - width/2, us_final, width, label='United States', color='blue', alpha=0.7)
    axes[1, 0].bar(x + width/2, china_final, width, label='China', color='red', alpha=0.7)
    axes[1, 0].set_title('Total Investment Comparison (2014-2024)')
    axes[1, 0].set_xlabel('Investment Type')
    axes[1, 0].set_ylabel('Investment (Millions USD)')
    axes[1, 0].set_xticks(x)
    axes[1, 0].set_xticklabels(categories)
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # Plot 5: Investment Growth Rate Comparison
    us_gov_growth = gov_data['US_Government_Millions'].pct_change() * 100
    china_gov_growth = gov_data['China_Government_Millions'].pct_change() * 100
    
    axes[1, 1].plot(gov_data['Year'][1:], us_gov_growth[1:], 'b-o', label='US Gov Growth %', linewidth=3)
    axes[1, 1].plot(gov_data['Year'][1:], china_gov_growth[1:], 'r-s', label='China Gov Growth %', linewidth=3)
    axes[1, 1].set_title('Government Investment Growth Rate')
    axes[1, 1].set_xlabel('Year')
    axes[1, 1].set_ylabel('Year-over-Year Growth (%)')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].axhline(y=0, color='black', linestyle='--', alpha=0.5)
    
    # Plot 6: Private Sector Share of Global Investment
    axes[1, 2].plot(private_data['Year'], private_data['US_Share_Percent'], 'b-o', label='US Share', linewidth=3)
    axes[1, 2].plot(private_data['Year'], private_data['China_Share_Percent'], 'r-s', label='China Share', linewidth=3)
    axes[1, 2].set_title('Share of Global Private Quantum Investment')
    axes[1, 2].set_xlabel('Year')
    axes[1, 2].set_ylabel('Share of Global Investment (%)')
    axes[1, 2].legend()
    axes[1, 2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save the plot
    output_dir = Path(__file__).parent / "visualizations"
    output_dir.mkdir(exist_ok=True)
    plt.savefig(output_dir / "funding_analysis_comprehensive.png", dpi=300, bbox_inches='tight')
    plt.show()

def calculate_funding_metrics(gov_data, private_data):
    """Calculate and display key funding metrics"""
    
    print("=== QUANTUM FUNDING ANALYSIS SUMMARY ===\n")
    
    # Total investments
    us_gov_total = gov_data['US_Cumulative_Millions'].iloc[-1]
    china_gov_total = gov_data['China_Cumulative_Millions'].iloc[-1]
    us_private_total = private_data['US_Private_Millions'].iloc[-1]
    china_private_total = private_data['China_Private_Millions'].iloc[-1]
    
    print("TOTAL INVESTMENT (2014-2024):")
    print(f"  US Government: ${us_gov_total:,.0f} million")
    print(f"  China Government: ${china_gov_total:,.0f} million") 
    print(f"  Government Ratio: China leads by {china_gov_total/us_gov_total:.1f}x\n")
    
    print(f"  US Private Sector: ${us_private_total:,.0f} million")
    print(f"  China Private Sector: ${china_private_total:,.0f} million")
    print(f"  Private Ratio: US leads by {us_private_total/china_private_total:.1f}x\n")
    
    # Combined totals
    us_total = us_gov_total + us_private_total
    china_total = china_gov_total + china_private_total
    
    print(f"COMBINED TOTAL INVESTMENT:")
    print(f"  United States: ${us_total:,.0f} million")
    print(f"  China: ${china_total:,.0f} million")
    print(f"  China leads overall by ${china_total - us_total:,.0f} million ({china_total/us_total:.1f}x)\n")
    
    # Investment strategy analysis
    us_gov_percent = us_gov_total / us_total * 100
    us_private_percent = us_private_total / us_total * 100
    china_gov_percent = china_gov_total / china_total * 100
    china_private_percent = china_private_total / china_total * 100
    
    print("INVESTMENT STRATEGY COMPARISON:")
    print(f"  US: {us_gov_percent:.1f}% government, {us_private_percent:.1f}% private")
    print(f"  China: {china_gov_percent:.1f}% government, {china_private_percent:.1f}% private\n")
    
    # Growth rate analysis
    us_gov_cagr = (gov_data['US_Government_Millions'].iloc[-1] / gov_data['US_Government_Millions'].iloc[0]) ** (1/10) - 1
    china_gov_cagr = (gov_data['China_Government_Millions'].iloc[-1] / gov_data['China_Government_Millions'].iloc[0]) ** (1/10) - 1
    
    print("GOVERNMENT INVESTMENT GROWTH (CAGR 2014-2024):")
    print(f"  US Government: {us_gov_cagr:.1%}")
    print(f"  China Government: {china_gov_cagr:.1%}")
    print(f"  China's growth rate is {china_gov_cagr/us_gov_cagr:.1f}x faster\n")
    
    # Recent trends (2022-2024)
    us_recent_growth = (gov_data['US_Government_Millions'].iloc[-1] / gov_data['US_Government_Millions'].iloc[-3]) - 1
    china_recent_growth = (gov_data['China_Government_Millions'].iloc[-1] / gov_data['China_Government_Millions'].iloc[-3]) - 1
    
    print("RECENT TRENDS (2022-2024):")
    print(f"  US Government Growth: {us_recent_growth:.1%}")
    print(f"  China Government Growth: {china_recent_growth:.1%}")
    if us_recent_growth < 0:
        print("  US showing decline in recent government investment")
    if china_recent_growth > 0:
        print("  China maintaining strong investment growth")

def create_investment_strategy_comparison(gov_data, private_data):
    """Create a pie chart comparison of investment strategies"""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle('Investment Strategy Comparison: Government vs Private (2014-2024)', fontsize=14, fontweight='bold')
    
    # US Investment Breakdown
    us_gov = gov_data['US_Cumulative_Millions'].iloc[-1]
    us_private = private_data['US_Private_Millions'].iloc[-1] 
    us_labels = ['Government\n$6.0B', 'Private Sector\n$3.3B']
    us_sizes = [us_gov, us_private]
    us_colors = ['lightblue', 'darkblue']
    
    ax1.pie(us_sizes, labels=us_labels, colors=us_colors, autopct='%1.1f%%', startangle=90)
    ax1.set_title('United States\nTotal: $9.3B')
    
    # China Investment Breakdown
    china_gov = gov_data['China_Cumulative_Millions'].iloc[-1]
    china_private = private_data['China_Private_Millions'].iloc[-1]
    china_labels = ['Government\n$15.6B', 'Private Sector\n$0.5B']
    china_sizes = [china_gov, china_private]
    china_colors = ['lightcoral', 'darkred']
    
    ax2.pie(china_sizes, labels=china_labels, colors=china_colors, autopct='%1.1f%%', startangle=90)
    ax2.set_title('China\nTotal: $16.1B')
    
    plt.tight_layout()
    
    # Save the plot
    output_dir = Path(__file__).parent / "visualizations"
    output_dir.mkdir(exist_ok=True)
    plt.savefig(output_dir / "investment_strategy_comparison.png", dpi=300, bbox_inches='tight')
    plt.show()

def main():
    """Main analysis function"""
    print("Loading funding data...")
    gov_data, private_data = load_funding_data()
    
    print("Creating funding analysis plots...")
    create_funding_analysis_plots(gov_data, private_data)
    
    print("Creating investment strategy comparison...")
    create_investment_strategy_comparison(gov_data, private_data)
    
    print("Calculating funding metrics...")
    calculate_funding_metrics(gov_data, private_data)
    
    print("\nFunding analysis complete! Check the visualizations folder for charts.")

if __name__ == "__main__":
    main()